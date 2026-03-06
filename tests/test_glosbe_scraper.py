from src.scraping.glosbe_scraper import parse_glosbe_page, GlosbeEntry

def test_parse_glosbe_entry():
    # Test with minimal mock HTML structure
    mock_html = """
    <div class="translation-item">
        <span class="phrase">бакI</span>
        <span class="translation">gunes</span>
        <div class="example">
            <span class="src">БакI абулеб буго</span>
            <span class="tgt">Gunes doguyor</span>
        </div>
    </div>
    """
    entries = parse_glosbe_page(mock_html)
    assert len(entries) >= 1
    assert entries[0].avar_word is not None
    assert entries[0].turkish_word is not None

def test_glosbe_entry_to_pairs():
    entry = GlosbeEntry(
        avar_word="бакI",
        turkish_word="gunes",
        examples=[("БакI абулеб буго", "Gunes doguyor")],
    )
    pairs = entry.to_pairs()
    assert len(pairs) == 2  # word + example
    assert pairs[0].source == "glosbe"
    assert pairs[0].quality == 0.85
