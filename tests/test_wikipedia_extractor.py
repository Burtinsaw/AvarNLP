from src.scraping.wikipedia_extractor import extract_parallel_titles

def test_extract_parallel_titles():
    # Mock: Avar article with a Turkish interwiki link
    mock_data = [
        {"av_title": "Дагъистан", "tr_title": "Dagistan"},
        {"av_title": "Москва", "tr_title": "Moskova"},
    ]
    pairs = extract_parallel_titles(mock_data)
    assert len(pairs) == 2
    assert pairs[0].av == "Дагъистан"
    assert pairs[0].tr == "Dagistan"
    assert pairs[0].source == "wikipedia"
    assert pairs[0].quality == 0.7
