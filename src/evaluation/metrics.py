"""Translation quality metrics: BLEU and chrF++."""

import sacrebleu


def compute_bleu(hypotheses: list[str], references: list[str]) -> float:
    """Compute BLEU score. Returns 0-100."""
    bleu = sacrebleu.corpus_bleu(hypotheses, [references])
    return round(bleu.score, 2)


def compute_chrf(hypotheses: list[str], references: list[str]) -> float:
    """Compute chrF++ score. Returns 0-100."""
    chrf = sacrebleu.corpus_chrf(hypotheses, [references], word_order=2)
    return round(chrf.score, 2)


def evaluate_model_on_pairs(predictions: list[str], references: list[str]) -> dict:
    """Run all evaluation metrics and return a summary dict."""
    return {
        "bleu": compute_bleu(predictions, references),
        "chrf": compute_chrf(predictions, references),
        "num_samples": len(predictions),
    }
