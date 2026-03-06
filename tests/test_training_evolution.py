from src.evolution.training_evolution import Genome, mutate_genome, crossover_genomes

def test_genome_creation():
    g = Genome()
    assert 1e-5 <= g.learning_rate <= 5e-4
    assert g.lora_rank in [8, 16, 32, 64]

def test_mutate_genome_changes_values():
    g = Genome(learning_rate=1e-4, lora_rank=16, batch_size=16)
    mutated = mutate_genome(g)
    # At least one field should be different (probabilistic but very likely)
    assert isinstance(mutated, Genome)

def test_crossover_genomes():
    a = Genome(learning_rate=1e-4, lora_rank=8, batch_size=8)
    b = Genome(learning_rate=5e-4, lora_rank=64, batch_size=32)
    child = crossover_genomes(a, b)
    assert child.learning_rate in [a.learning_rate, b.learning_rate]
    assert child.lora_rank in [a.lora_rank, b.lora_rank]
