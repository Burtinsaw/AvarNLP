"""Orchestrate all data collection sources into one pipeline."""

from src.data_types import SentencePair, save_pairs
from src.scraping.magarulaw_seed import extract_seed_pairs


def deduplicate_pairs(pairs: list[SentencePair]) -> list[SentencePair]:
    """Remove duplicates, keeping highest quality version."""
    seen: dict[tuple[str, str], SentencePair] = {}
    for pair in pairs:
        key = (pair.av.strip(), pair.tr.strip())
        if key not in seen or pair.quality > seen[key].quality:
            seen[key] = pair
    return list(seen.values())


def collect_all_seed_data(skip_network: bool = False) -> list[SentencePair]:
    """Collect data from all sources and merge."""
    all_pairs: list[SentencePair] = []

    # Always available: MagaruLaw seed
    print("[1/3] Extracting MagaruLaw seed data...")
    all_pairs.extend(extract_seed_pairs())
    print(f"  -> {len(all_pairs)} pairs")

    if not skip_network:
        # Glosbe
        try:
            from src.scraping.glosbe_scraper import scrape_glosbe
            print("[2/3] Scraping Glosbe...")
            glosbe_pairs = scrape_glosbe(max_pages=30)
            all_pairs.extend(glosbe_pairs)
            print(f"  -> {len(glosbe_pairs)} pairs from Glosbe")
        except Exception as e:
            print(f"  -> Glosbe failed: {e}")

        # Wikipedia
        try:
            from src.scraping.wikipedia_extractor import fetch_avar_wikipedia_titles, extract_parallel_titles
            print("[3/3] Extracting Wikipedia parallels...")
            titles = fetch_avar_wikipedia_titles(limit=500)
            wiki_pairs = extract_parallel_titles(titles)
            all_pairs.extend(wiki_pairs)
            print(f"  -> {len(wiki_pairs)} pairs from Wikipedia")
        except Exception as e:
            print(f"  -> Wikipedia failed: {e}")

    # Deduplicate
    deduped = deduplicate_pairs(all_pairs)
    print(f"\nTotal: {len(deduped)} unique pairs (from {len(all_pairs)} raw)")
    return deduped


if __name__ == "__main__":
    pairs = collect_all_seed_data()
    save_pairs(pairs, "data/processed/seed_corpus.jsonl")
    print(f"Saved to data/processed/seed_corpus.jsonl")
