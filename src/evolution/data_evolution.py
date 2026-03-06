"""Evolutionary data generation — the heart of AvarNLP.

Uses genetic algorithms to evolve a population of 'generator agents',
each with a strategy for producing new Avar-Turkish sentence pairs.
Best agents survive and reproduce, growing the corpus iteratively.
"""

import random
from dataclasses import dataclass, field
from src.data_types import SentencePair
from src.evolution.fitness import compute_fitness


STRATEGIES = ["word_swap", "word_shuffle", "template_fill", "back_translate", "paraphrase"]


@dataclass
class Agent:
    strategy: str
    temperature: float = 0.7
    fitness_history: list[float] = field(default_factory=list)

    @property
    def avg_fitness(self) -> float:
        return sum(self.fitness_history) / len(self.fitness_history) if self.fitness_history else 0.0


def mutate_sentence(sentence: str, strategy: str) -> str:
    """Apply a mutation strategy to an Avar sentence."""
    words = sentence.split()
    if len(words) < 2:
        return sentence

    if strategy == "word_shuffle":
        shuffled = words[:]
        random.shuffle(shuffled)
        return " ".join(shuffled)

    elif strategy == "word_swap":
        idx = random.randint(0, len(words) - 2)
        words[idx], words[idx + 1] = words[idx + 1], words[idx]
        return " ".join(words)

    elif strategy == "template_fill":
        # Replace a random word with another from known vocab
        known = ["буго", "йиго", "вуго", "руго", "дир", "гьаб"]
        idx = random.randint(0, len(words) - 1)
        words[idx] = random.choice(known)
        return " ".join(words)

    return sentence


def mutate_pair(pair: SentencePair, strategy: str) -> SentencePair:
    """Create a mutated version of a sentence pair."""
    new_av = mutate_sentence(pair.av, strategy)
    # For now, keep Turkish translation (will be improved with LLM)
    return SentencePair(av=new_av, tr=pair.tr, source="evolved", quality=0.0)


def crossover_agents(a: Agent, b: Agent) -> Agent:
    """Combine two agents to create a child agent."""
    return Agent(
        strategy=random.choice([a.strategy, b.strategy]),
        temperature=round((a.temperature + b.temperature) / 2 + random.uniform(-0.1, 0.1), 2),
    )


def mutate_agent(agent: Agent) -> Agent:
    """Slightly modify an agent's parameters."""
    new_temp = max(0.1, min(1.0, agent.temperature + random.uniform(-0.15, 0.15)))
    new_strategy = agent.strategy if random.random() > 0.2 else random.choice(STRATEGIES)
    return Agent(strategy=new_strategy, temperature=round(new_temp, 2))


def run_evolution(
    seed_pairs: list[SentencePair],
    generations: int = 50,
    population_size: int = 20,
    pairs_per_agent: int = 100,
    survival_rate: float = 0.3,
    fitness_threshold: float = 0.4,
) -> list[SentencePair]:
    """Run the evolutionary data generation loop."""
    corpus = list(seed_pairs)
    population = [
        Agent(strategy=random.choice(STRATEGIES), temperature=round(random.uniform(0.3, 0.9), 2))
        for _ in range(population_size)
    ]

    for gen in range(generations):
        gen_pairs: list[tuple[SentencePair, float]] = []

        # Each agent produces new pairs
        for agent in population:
            for _ in range(pairs_per_agent):
                source_pair = random.choice(corpus)
                new_pair = mutate_pair(source_pair, agent.strategy)
                fitness = compute_fitness(new_pair, corpus)
                gen_pairs.append((new_pair, fitness))
                agent.fitness_history.append(fitness)

        # Filter by fitness threshold
        good_pairs = [(p, f) for p, f in gen_pairs if f >= fitness_threshold]
        for pair, fitness in good_pairs:
            pair.quality = round(fitness, 4)
            corpus.append(pair)

        # Select survivors
        population.sort(key=lambda a: a.avg_fitness, reverse=True)
        n_survive = max(2, int(len(population) * survival_rate))
        survivors = population[:n_survive]

        # Reproduce
        new_population = list(survivors)
        while len(new_population) < population_size:
            if random.random() < 0.7 and len(survivors) >= 2:
                parents = random.sample(survivors, 2)
                child = crossover_agents(parents[0], parents[1])
            else:
                parent = random.choice(survivors)
                child = mutate_agent(parent)
            new_population.append(child)

        population = new_population

        if gen % 10 == 0 or gen == generations - 1:
            avg_fit = sum(f for _, f in gen_pairs) / len(gen_pairs) if gen_pairs else 0
            print(f"Gen {gen}: corpus={len(corpus)}, new_good={len(good_pairs)}, avg_fitness={avg_fit:.3f}")

    return corpus
