# AvarNLP

World's first self-evolving Avar language translation AI.

Avarca ↔ Turkce translation using genetic algorithms for data generation and model optimization.

## Overview

Avar (МагIарул мацI) is a severely under-resourced language with ~1 million speakers, zero NLP models, zero parallel corpora, and zero pre-trained models. AvarNLP creates all of it from scratch using evolutionary algorithms.

### Three-Phase Pipeline

```
Faz 1: Veri Toplama    →  Faz 2: Evrimsel Veri Uretimi  →  Faz 3: Evrimsel Fine-Tuning
(~5K paralel cift)        (~50K+ cift via GA)               (NLLB-600M + LoRA via GA)
                                                                      │
                                                                      ▼
                                                              HF Model + API
```

**Faz 1** — Collect ~5K Avar-Turkish parallel sentence pairs from MagaruLaw dictionary, Glosbe, Wikipedia, and other sources.

**Faz 2** — Evolve the corpus to ~50K+ pairs using genetic algorithms with fitness-based quality filtering (language validity, translation consistency, diversity).

**Faz 3** — Fine-tune Meta's NLLB-600M with LoRA using evolutionary hyperparameter optimization.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"
```

## Usage

```bash
# Faz 1: Collect seed data
python run.py collect

# Faz 2: Evolve corpus with genetic algorithms
python run.py evolve

# Faz 3: Train model (with evolutionary hyperparameter search)
python run.py train --evolve

# Serve API
python run.py serve

# Launch Gradio demo
python run.py demo --share
```

## Project Structure

- `src/scraping/` — Data collection from web sources
- `src/evolution/` — Genetic algorithm engines (data + training)
- `src/training/` — NLLB-600M fine-tuning with LoRA
- `src/evaluation/` — BLEU, chrF++ metrics
- `src/api/` — FastAPI inference server + Gradio demo
- `data/` — Raw, processed, and evolved datasets
- `configs/` — Evolution and training configurations
- `notebooks/` — Colab/Kaggle notebooks

## Tech Stack

- Python 3.11+
- PyTorch + Transformers (HuggingFace)
- DEAP (genetic algorithm framework)
- LoRA via PEFT
- FastAPI (inference API)
- Gradio (demo UI)
- Weights & Biases (training tracking)

## Uniqueness

1. World's first Avar language AI model
2. Evolutionary data generation — novel approach for low-resource languages
3. Evolutionary fine-tuning — automatic hyperparameter optimization via GA
4. Fully open source — template for other endangered languages

## License

MIT
