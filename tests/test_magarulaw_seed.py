from src.scraping.magarulaw_seed import extract_seed_pairs

def test_extract_seed_pairs():
    pairs = extract_seed_pairs()
    assert len(pairs) >= 10
    # Check a known pair
    avar_words = [p.av for p in pairs]
    assert any("Салам" in w for w in avar_words)
    # All should be seed source
    assert all(p.source == "magarulaw_seed" for p in pairs)
    # All should have quality 1.0 (human-verified)
    assert all(p.quality == 1.0 for p in pairs)
