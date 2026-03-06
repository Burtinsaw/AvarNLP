"""Evolutionary hyperparameter optimization for NLLB fine-tuning.

Genome = set of training hyperparameters.
Population evolves via tournament selection, crossover, and mutation.
Fitness = BLEU score on held-out test set after 1 epoch.
"""

import random
from dataclasses import dataclass, field
from src.data_types import SentencePair


LORA_RANKS = [8, 16, 32, 64]
BATCH_SIZES = [8, 16, 32]
AUGMENTATIONS = ["none", "swap", "noise"]


@dataclass
class Genome:
    learning_rate: float = 0.0
    warmup_ratio: float = 0.0
    batch_size: int = 16
    lora_rank: int = 16
    lora_alpha: int = 32
    frozen_layers: int = 0
    augmentation: str = "none"
    fitness: float = 0.0

    def __post_init__(self):
        if self.learning_rate == 0.0:
            self.learning_rate = random.uniform(1e-5, 5e-4)
        if self.warmup_ratio == 0.0:
            self.warmup_ratio = random.uniform(0.01, 0.2)
        if self.batch_size not in BATCH_SIZES:
            self.batch_size = random.choice(BATCH_SIZES)
        if self.lora_rank not in LORA_RANKS:
            self.lora_rank = random.choice(LORA_RANKS)
        self.lora_alpha = self.lora_rank * 2
        if self.augmentation not in AUGMENTATIONS:
            self.augmentation = random.choice(AUGMENTATIONS)


def mutate_genome(genome: Genome, mutation_rate: float = 0.3) -> Genome:
    """Mutate a genome by tweaking random parameters."""
    g = Genome(
        learning_rate=genome.learning_rate,
        warmup_ratio=genome.warmup_ratio,
        batch_size=genome.batch_size,
        lora_rank=genome.lora_rank,
        frozen_layers=genome.frozen_layers,
        augmentation=genome.augmentation,
    )

    if random.random() < mutation_rate:
        g.learning_rate *= random.uniform(0.5, 2.0)
        g.learning_rate = max(1e-6, min(1e-3, g.learning_rate))

    if random.random() < mutation_rate:
        g.warmup_ratio = max(0.01, min(0.3, g.warmup_ratio + random.uniform(-0.05, 0.05)))

    if random.random() < mutation_rate:
        g.batch_size = random.choice(BATCH_SIZES)

    if random.random() < mutation_rate:
        g.lora_rank = random.choice(LORA_RANKS)
        g.lora_alpha = g.lora_rank * 2

    if random.random() < mutation_rate:
        g.augmentation = random.choice(AUGMENTATIONS)

    if random.random() < mutation_rate:
        g.frozen_layers = random.randint(0, 12)

    return g


def crossover_genomes(a: Genome, b: Genome) -> Genome:
    """Uniform crossover between two genomes."""
    return Genome(
        learning_rate=random.choice([a.learning_rate, b.learning_rate]),
        warmup_ratio=random.choice([a.warmup_ratio, b.warmup_ratio]),
        batch_size=random.choice([a.batch_size, b.batch_size]),
        lora_rank=random.choice([a.lora_rank, b.lora_rank]),
        frozen_layers=random.choice([a.frozen_layers, b.frozen_layers]),
        augmentation=random.choice([a.augmentation, b.augmentation]),
    )


def run_training_evolution(
    train_pairs: list[SentencePair],
    test_pairs: list[SentencePair],
    generations: int = 20,
    population_size: int = 10,
    survival_count: int = 4,
) -> Genome:
    """Evolve training hyperparameters. Returns best genome.

    Each generation:
    1. Train each genome for 1 epoch
    2. Evaluate on test set (BLEU) -> fitness
    3. Select top survivors
    4. Crossover + mutate -> new generation
    """
    population = [Genome() for _ in range(population_size)]

    for gen in range(generations):
        # Evaluate each genome (placeholder — real training in train_nllb.py)
        for genome in population:
            # In real use, this calls train() with 1 epoch and evaluates BLEU
            # For now, placeholder fitness based on heuristics
            genome.fitness = _placeholder_fitness(genome)

        # Sort by fitness
        population.sort(key=lambda g: g.fitness, reverse=True)
        best = population[0]
        avg = sum(g.fitness for g in population) / len(population)
        print(f"Gen {gen}: best={best.fitness:.4f} avg={avg:.4f} lr={best.learning_rate:.6f} lora_r={best.lora_rank}")

        # Select survivors
        survivors = population[:survival_count]

        # Reproduce
        new_pop = list(survivors)
        while len(new_pop) < population_size:
            if random.random() < 0.7 and len(survivors) >= 2:
                parents = random.sample(survivors, 2)
                child = crossover_genomes(parents[0], parents[1])
            else:
                child = mutate_genome(random.choice(survivors))
            new_pop.append(child)

        population = new_pop

    population.sort(key=lambda g: g.fitness, reverse=True)
    return population[0]


def _placeholder_fitness(genome: Genome) -> float:
    """Placeholder fitness for testing. Replace with real BLEU evaluation."""
    score = 0.5
    if 1e-4 <= genome.learning_rate <= 3e-4:
        score += 0.2
    if genome.lora_rank in [16, 32]:
        score += 0.1
    if genome.batch_size == 16:
        score += 0.05
    score += random.uniform(-0.1, 0.1)
    return max(0.0, min(1.0, score))
