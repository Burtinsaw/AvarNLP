from src.data_types import SentencePair, load_pairs, save_pairs
import tempfile
import os

def test_sentence_pair_creation():
    pair = SentencePair(av="Салам", tr="Merhaba", source="seed", quality=1.0)
    assert pair.av == "Салам"
    assert pair.tr == "Merhaba"
    assert pair.source == "seed"
    assert pair.quality == 1.0

def test_sentence_pair_validation_rejects_empty():
    import pytest
    with pytest.raises(ValueError):
        SentencePair(av="", tr="Merhaba", source="seed", quality=1.0)

def test_sentence_pair_validation_rejects_bad_quality():
    import pytest
    with pytest.raises(ValueError):
        SentencePair(av="Салам", tr="Merhaba", source="seed", quality=1.5)

def test_save_and_load_roundtrip():
    pairs = [
        SentencePair(av="Салам", tr="Merhaba", source="seed", quality=1.0),
        SentencePair(av="Баркала", tr="Tesekkurler", source="glosbe", quality=0.9),
    ]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
        path = f.name
    try:
        save_pairs(pairs, path)
        loaded = load_pairs(path)
        assert len(loaded) == 2
        assert loaded[0].av == "Салам"
        assert loaded[1].quality == 0.9
    finally:
        os.unlink(path)
