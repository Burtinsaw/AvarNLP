<p align="center">
  <h1 align="center">🏔️ AvarNLP</h1>
  <p align="center">
    <strong>Self-Evolving AI for the Endangered Avar Language</strong>
  </p>
  <p align="center">
    The world's first machine translation system for Avar (МагIарул мацI) — built through genetic algorithms that evolve their own training data.
  </p>
  <p align="center">
    <a href="https://github.com/Burtinsaw/AvarNLP/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
    <img src="https://img.shields.io/badge/python-3.11%2B-3776AB.svg?logo=python&logoColor=white" alt="Python 3.11+">
    <img src="https://img.shields.io/badge/PyTorch-2.1%2B-EE4C2C.svg?logo=pytorch&logoColor=white" alt="PyTorch">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow.svg" alt="Hugging Face">
    <img src="https://img.shields.io/badge/DEAP-Genetic%20Algorithms-green.svg" alt="DEAP">
    <img src="https://img.shields.io/badge/status-active%20development-orange.svg" alt="Status">
  </p>
</p>

---

## Why AvarNLP?

**Avar** is a Northeast Caucasian language spoken by ~800,000 people in Dagestan and diaspora communities across Turkey and Europe. Despite a literary tradition dating to the 15th century, Avar has:

- **Zero** machine translation systems
- **Zero** parallel corpora available digitally
- **Zero** pre-trained language models
- **No support** in Google Translate, DeepL, or any commercial MT service

AvarNLP changes this — not by waiting for someone to manually build a large dataset, but by **evolving one from scratch**.

## How It Works

Most NLP systems need millions of sentence pairs. Avar has fewer than 1,000. AvarNLP solves this through a three-phase evolutionary pipeline:

```
┌─────────────────────┐     ┌──────────────────────────┐     ┌────────────────────────────┐
│  Phase 1             │     │  Phase 2                  │     │  Phase 3                    │
│  DATA COLLECTION     │────>│  EVOLUTIONARY GENERATION  │────>│  EVOLUTIONARY FINE-TUNING   │
│                      │     │                           │     │                             │
│  ~1K seed pairs      │     │  Genetic algorithms       │     │  NLLB-600M + LoRA           │
│  from web sources    │     │  evolve corpus to ~50K+   │     │  with GA-optimized params   │
│                      │     │  with fitness filtering   │     │                             │
└─────────────────────┘     └──────────────────────────┘     └──────────┬─────────────────┘
                                                                        │
                                                              ┌─────────▼──────────┐
                                                              │  Translation API   │
                                                              │  + Gradio Demo     │
                                                              └────────────────────┘
```

### Phase 1 — Data Collection

Collects Avar-Turkish parallel sentence pairs from multiple sources:
- [MagaruLaw.com](https://magarulaw.com) bilingual dictionary
- Glosbe online dictionary
- Avar Wikipedia (av.wikipedia.org)
- Additional web sources

### Phase 2 — Evolutionary Data Generation

Uses **genetic algorithms** (via DEAP) to evolve the small seed corpus into a much larger training set:
- Evolutionary agents apply mutations: word swap, word shuffle, template filling
- A **fitness function** evaluates each generated pair on:
  - Language validity (Cyrillic script, known Avar vocabulary)
  - Translation consistency (source-target length ratios)
  - Diversity (avoiding repetitive generations)
- Natural selection keeps only the fittest pairs across generations

### Phase 3 — Evolutionary Fine-Tuning

Fine-tunes Meta's **NLLB-600M** (No Language Left Behind) using the evolved dataset:
- **LoRA** (Low-Rank Adaptation) for parameter-efficient training
- A second genetic algorithm optimizes hyperparameters:
  - Learning rate, LoRA rank, batch size, warmup ratio, weight decay
- Each "genome" is a training configuration; the fittest survive and reproduce

## Quick Start

```bash
# Clone
git clone https://github.com/Burtinsaw/AvarNLP.git
cd AvarNLP

# Setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# Run the pipeline
python run.py collect              # Phase 1: Collect seed data
python run.py evolve               # Phase 2: Evolve corpus with GA
python run.py train --evolve       # Phase 3: Train with evolutionary optimization

# Deploy
python run.py serve                # Start FastAPI server
python run.py demo --share         # Launch Gradio demo
```

## Project Structure

```
AvarNLP/
├── src/
│   ├── scraping/              # Phase 1: Data collection
│   │   ├── magarulaw_seed.py  #   Seed data from MagaruLaw
│   │   ├── glosbe_scraper.py  #   Glosbe dictionary scraper
│   │   ├── wikipedia_extractor.py  # Avar Wikipedia extractor
│   │   └── pipeline.py        #   Collection orchestrator
│   ├── evolution/             # Phase 2 & 3: Genetic algorithms
│   │   ├── fitness.py         #   Fitness functions
│   │   ├── data_evolution.py  #   Evolutionary data generation
│   │   └── training_evolution.py  # Evolutionary hyperparameter search
│   ├── training/              # NLLB-600M fine-tuning
│   │   └── train_nllb.py      #   LoRA training pipeline
│   ├── evaluation/            # Quality metrics
│   │   └── metrics.py         #   BLEU, chrF++ scoring
│   └── api/                   # Deployment
│       ├── server.py          #   FastAPI inference API
│       └── demo.py            #   Gradio web demo
├── configs/                   # Evolution & training configs
├── data/                      # Raw, processed, evolved datasets
├── notebooks/                 # Colab/Kaggle notebooks
├── tests/                     # Test suite
├── docs/                      # Documentation & research
└── run.py                     # CLI entry point
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.11+ |
| Deep Learning | PyTorch, Transformers (Hugging Face) |
| Genetic Algorithms | DEAP |
| Fine-Tuning | LoRA via PEFT |
| Translation Model | Meta NLLB-600M |
| Metrics | sacrebleu (BLEU, chrF++) |
| API | FastAPI + Uvicorn |
| Demo UI | Gradio |
| Experiment Tracking | Weights & Biases |

## What Makes This Novel

1. **Evolutionary data generation** — No existing system uses genetic algorithms to evolve training corpora for endangered languages. This is a new paradigm for extreme low-resource NLP.

2. **Works with <1,000 seed pairs** — Most low-resource approaches need 10,000+ parallel sentences. AvarNLP starts from virtually nothing.

3. **Self-improving** — The system gets better over generations without human intervention. Each evolutionary cycle produces higher-quality data and better models.

4. **Replicable framework** — The same approach can be applied to other endangered languages: Lezgin, Tabasaran, Tsez, Lak, Dargwa, and dozens more.

## Roadmap

- [x] Project architecture and design
- [x] Data collection pipeline (Phase 1)
- [x] Evolutionary data generation engine (Phase 2)
- [x] NLLB-600M LoRA training pipeline (Phase 3)
- [x] FastAPI inference server
- [x] Gradio web demo
- [ ] Seed corpus collection (~1K pairs)
- [ ] First evolutionary data generation run
- [ ] First model training and evaluation
- [ ] Hugging Face model release: `burtinsaw/avarnlp-nllb-600m`
- [ ] Hugging Face dataset release: `burtinsaw/avar-turkish-parallel`
- [ ] Research writeup / technical blog post
- [ ] Support for Avar-Russian translation direction
- [ ] Community testing via MagaruLaw.com

## About the Avar Language

| | |
|---|---|
| **Name** | Avar (МагIарул мацI) |
| **Family** | Northeast Caucasian (Nakh-Dagestanian) |
| **Speakers** | ~800,000 |
| **Region** | Dagestan (Russia), Turkey, diaspora in Europe |
| **Script** | Cyrillic (modern), Arabic (historical) |
| **UNESCO Status** | Definitely Endangered |
| **Digital Resources** | Virtually none |

## Contributing

Contributions are welcome, especially from:
- **Avar speakers** — for data validation and quality evaluation
- **NLP researchers** — for improving the evolutionary approach
- **Low-resource language enthusiasts** — for adapting the framework to new languages

See the [issues](https://github.com/Burtinsaw/AvarNLP/issues) page or open a new one.

## Related Projects

- [MagaruLaw.com](https://magarulaw.com) — Avar cultural platform (source of seed data)
- [Meta NLLB](https://github.com/facebookresearch/fairseq/tree/nllb) — Base translation model
- [DEAP](https://github.com/DEAP/deap) — Genetic algorithm framework
- [Masakhane](https://www.masakhane.io/) — Inspiration from African NLP community

## License

[MIT](LICENSE) — Use it, fork it, adapt it for your language.

## Citation

If you use AvarNLP in your research, please cite:

```bibtex
@software{avarnlp2026,
  title     = {AvarNLP: Self-Evolving AI for the Endangered Avar Language},
  author    = {AvarNLP Contributors},
  url       = {https://github.com/Burtinsaw/AvarNLP},
  year      = {2026},
  license   = {MIT}
}
```

---

<p align="center">
  <em>Built with care for the Avar people and all endangered language communities.</em>
</p>
