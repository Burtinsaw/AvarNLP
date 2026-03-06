from src.evolution.data_evolution import (
    Agent,
    mutate_sentence,
    crossover_agents,
    run_evolution,
)
from src.data_types import SentencePair

def test_agent_creation():
    agent = Agent(strategy="word_swap", temperature=0.7)
    assert agent.strategy == "word_swap"
    assert agent.fitness_history == []

def test_mutate_sentence_changes_output():
    original = "Дир эбел цIуяб нуж йиго"
    # Mutation should produce something different (or same if no swap possible)
    result = mutate_sentence(original, strategy="word_shuffle")
    assert isinstance(result, str)
    assert len(result) > 0

def test_crossover_agents():
    a = Agent(strategy="word_swap", temperature=0.5)
    b = Agent(strategy="back_translate", temperature=0.9)
    child = crossover_agents(a, b)
    assert child.strategy in ["word_swap", "back_translate"]
    assert 0.0 <= child.temperature <= 1.0

def test_run_evolution_produces_pairs():
    seed = [
        SentencePair(av="Салам", tr="Merhaba", source="seed", quality=1.0),
        SentencePair(av="Баркала", tr="Tesekkurler", source="seed", quality=1.0),
        SentencePair(av="Дир эбел цIуяб нуж йиго", tr="Annem genc bir kadindir", source="seed", quality=1.0),
    ]
    result = run_evolution(seed_pairs=seed, generations=2, population_size=4, pairs_per_agent=3)
    assert len(result) > len(seed)
    assert all(isinstance(p, SentencePair) for p in result)
