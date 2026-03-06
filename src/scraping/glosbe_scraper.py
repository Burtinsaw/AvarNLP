"""Scrape Avar-Turkish translation pairs from Glosbe.com."""

from dataclasses import dataclass, field
from bs4 import BeautifulSoup
import httpx
import time
from src.data_types import SentencePair


@dataclass
class GlosbeEntry:
    avar_word: str
    turkish_word: str
    examples: list[tuple[str, str]] = field(default_factory=list)

    def to_pairs(self) -> list[SentencePair]:
        pairs = [SentencePair(av=self.avar_word, tr=self.turkish_word, source="glosbe", quality=0.85)]
        for av_ex, tr_ex in self.examples:
            pairs.append(SentencePair(av=av_ex, tr=tr_ex, source="glosbe", quality=0.8))
        return pairs


def parse_glosbe_page(html: str) -> list[GlosbeEntry]:
    soup = BeautifulSoup(html, "html.parser")
    entries = []

    for item in soup.select(".translation-item, [data-element='translation']"):
        phrase_el = item.select_one(".phrase, [data-element='phrase']")
        trans_el = item.select_one(".translation, [data-element='translation-text']")
        if not phrase_el or not trans_el:
            continue

        examples = []
        for ex in item.select(".example, [data-element='example']"):
            src = ex.select_one(".src, [data-element='example-src']")
            tgt = ex.select_one(".tgt, [data-element='example-tgt']")
            if src and tgt:
                examples.append((src.get_text(strip=True), tgt.get_text(strip=True)))

        entries.append(GlosbeEntry(
            avar_word=phrase_el.get_text(strip=True),
            turkish_word=trans_el.get_text(strip=True),
            examples=examples,
        ))

    return entries


def scrape_glosbe(direction: str = "av/tr", max_pages: int = 50, delay: float = 2.0) -> list[SentencePair]:
    """Scrape Glosbe for Avar-Turkish pairs. direction: 'av/tr' or 'tr/av'."""
    all_pairs = []
    base_url = f"https://glosbe.com/{direction}"

    client = httpx.Client(
        headers={"User-Agent": "AvarNLP-Research/0.1 (academic research)"},
        timeout=30.0,
    )

    for page in range(1, max_pages + 1):
        try:
            resp = client.get(f"{base_url}?page={page}")
            if resp.status_code != 200:
                break
            entries = parse_glosbe_page(resp.text)
            if not entries:
                break
            for entry in entries:
                all_pairs.extend(entry.to_pairs())
            time.sleep(delay)
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break

    client.close()
    return all_pairs
