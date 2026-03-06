"""Main entry point for AvarNLP pipeline."""

import argparse
import json
from pathlib import Path

from src.data_types import save_pairs, load_pairs


def cmd_collect(args):
    """Faz 1: Collect seed data."""
    from src.scraping.pipeline import collect_all_seed_data
    pairs = collect_all_seed_data(skip_network=args.offline)
    save_pairs(pairs, args.output)
    print(f"Saved {len(pairs)} pairs to {args.output}")


def cmd_evolve_data(args):
    """Faz 2: Evolve corpus using genetic algorithms."""
    from src.evolution.data_evolution import run_evolution
    seed_pairs = load_pairs(args.input)
    config = json.loads(Path(args.config).read_text()) if args.config else {}
    evolved = run_evolution(
        seed_pairs=seed_pairs,
        generations=config.get("generations", 50),
        population_size=config.get("population_size", 20),
        pairs_per_agent=config.get("pairs_per_agent", 100),
    )
    save_pairs(evolved, args.output)
    print(f"Evolved corpus: {len(evolved)} pairs saved to {args.output}")


def cmd_train(args):
    """Faz 3: Train or evolve training."""
    pairs = load_pairs(args.input)
    if args.evolve:
        from src.evolution.training_evolution import run_training_evolution
        best = run_training_evolution(
            train_pairs=pairs[:int(len(pairs)*0.9)],
            test_pairs=pairs[int(len(pairs)*0.9):],
        )
        print(f"Best genome: lr={best.learning_rate:.6f} lora_r={best.lora_rank} batch={best.batch_size}")
    else:
        from src.training.train_nllb import train
        train(pairs, output_dir=args.output)


def cmd_serve(args):
    """Start API server."""
    import uvicorn
    uvicorn.run("src.api.server:app", host="0.0.0.0", port=args.port, reload=args.reload)


def cmd_demo(args):
    """Start Gradio demo."""
    from src.api.demo import demo
    demo.launch(server_port=args.port, share=args.share)


def main():
    parser = argparse.ArgumentParser(description="AvarNLP Pipeline")
    sub = parser.add_subparsers(dest="command")

    # collect
    p = sub.add_parser("collect", help="Collect seed data (Faz 1)")
    p.add_argument("--output", default="data/processed/seed_corpus.jsonl")
    p.add_argument("--offline", action="store_true")

    # evolve
    p = sub.add_parser("evolve", help="Evolve data corpus (Faz 2)")
    p.add_argument("--input", default="data/processed/seed_corpus.jsonl")
    p.add_argument("--output", default="data/evolved/evolved_corpus.jsonl")
    p.add_argument("--config", default="configs/data_evolution.json")

    # train
    p = sub.add_parser("train", help="Train model (Faz 3)")
    p.add_argument("--input", default="data/evolved/evolved_corpus.jsonl")
    p.add_argument("--output", default="checkpoints/nllb-avar")
    p.add_argument("--evolve", action="store_true", help="Use evolutionary hyperparameter search")

    # serve
    p = sub.add_parser("serve", help="Start API server")
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--reload", action="store_true")

    # demo
    p = sub.add_parser("demo", help="Start Gradio demo")
    p.add_argument("--port", type=int, default=7860)
    p.add_argument("--share", action="store_true")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    {"collect": cmd_collect, "evolve": cmd_evolve_data, "train": cmd_train, "serve": cmd_serve, "demo": cmd_demo}[args.command](args)


if __name__ == "__main__":
    main()
