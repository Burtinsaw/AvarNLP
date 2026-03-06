from src.evolution.fitness import (
    score_language_validity,
    score_diversity,
    score_translation_consistency,
    compute_fitness,
)
from src.data_types import SentencePair

def test_score_language_validity_valid_avar():
    score = score_language_validity("Дир эбел цIуяб нуж йиго")
    assert score > 0.5

def test_score_language_validity_invalid():
    score = score_language_validity("This is English text")
    assert score < 0.3

def test_score_diversity_unique():
    existing = [SentencePair(av="Салам", tr="Merhaba", source="seed", quality=1.0)]
    score = score_diversity("Баркала дуе", existing)
    assert score > 0.5

def test_score_diversity_duplicate():
    existing = [SentencePair(av="Салам", tr="Merhaba", source="seed", quality=1.0)]
    score = score_diversity("Салам", existing)
    assert score < 0.3

def test_compute_fitness_returns_0_to_1():
    pair = SentencePair(av="Дир эбел", tr="Annem", source="evolved", quality=0.0)
    existing = []
    fitness = compute_fitness(pair, existing)
    assert 0.0 <= fitness <= 1.0
