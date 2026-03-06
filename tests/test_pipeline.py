from src.scraping.pipeline import collect_all_seed_data, deduplicate_pairs
from src.data_types import SentencePair

def test_deduplicate_pairs():
    pairs = [
        SentencePair(av="Салам", tr="Merhaba", source="seed", quality=1.0),
        SentencePair(av="Салам", tr="Merhaba", source="glosbe", quality=0.8),
        SentencePair(av="Баркала", tr="Tesekkurler", source="seed", quality=1.0),
    ]
    deduped = deduplicate_pairs(pairs)
    assert len(deduped) == 2
    # Should keep highest quality
    salam = [p for p in deduped if p.av == "Салам"][0]
    assert salam.quality == 1.0

def test_collect_all_seed_data_returns_pairs():
    # Only test that MagaruLaw seed works (no network)
    pairs = collect_all_seed_data(skip_network=True)
    assert len(pairs) >= 10
    assert all(isinstance(p, SentencePair) for p in pairs)
