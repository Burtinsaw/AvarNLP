"""Fitness functions for evaluating generated Avar-Turkish sentence pairs."""

import re
from src.data_types import SentencePair

# Common Avar Cyrillic characters (including special: I, ъ, гъ, etc.)
AVAR_CYRILLIC = set("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзиклмнопрстуфхцчшщъыьэюяI")

# Known Avar words (from seed data + common words)
KNOWN_AVAR_WORDS = {
    "дир", "буго", "йиго", "вуго", "руго", "гьаб", "гьеб",
    "эбел", "эмен", "вас", "яс", "рукъ", "росдал", "мацI",
    "лъикI", "хъвараб", "гъоркьаб", "бакIараб", "цIуяб",
    "салам", "баркала", "нуж", "чи", "мина",
}


def score_language_validity(text: str) -> float:
    """Score how likely text is valid Avar (0-1)."""
    if not text.strip():
        return 0.0

    chars = set(text.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", ""))
    if not chars:
        return 0.0

    # What fraction of characters are Avar Cyrillic?
    cyrillic_count = sum(1 for c in chars if c in AVAR_CYRILLIC)
    cyrillic_ratio = cyrillic_count / len(chars) if chars else 0

    # Does it contain known Avar words?
    words = text.lower().split()
    known_count = sum(1 for w in words if w.strip(".,!?\"'") in KNOWN_AVAR_WORDS)
    known_ratio = known_count / len(words) if words else 0

    # Weighted combination
    return 0.6 * cyrillic_ratio + 0.4 * min(known_ratio * 2, 1.0)


def score_diversity(text: str, existing: list[SentencePair]) -> float:
    """Score how different this text is from existing corpus (0-1)."""
    if not existing:
        return 1.0

    text_lower = text.lower().strip()
    text_words = set(text_lower.split())

    max_overlap = 0.0
    for pair in existing:
        existing_words = set(pair.av.lower().split())
        if not text_words or not existing_words:
            continue
        overlap = len(text_words & existing_words) / max(len(text_words), len(existing_words))
        max_overlap = max(max_overlap, overlap)

    return 1.0 - max_overlap


def score_translation_consistency(av_text: str, tr_text: str) -> float:
    """Score how consistent the Avar-Turkish pair is (0-1).

    Simple heuristic: length ratio and basic checks.
    Can be upgraded to use embedding similarity later.
    """
    if not av_text.strip() or not tr_text.strip():
        return 0.0

    av_len = len(av_text.split())
    tr_len = len(tr_text.split())

    if av_len == 0 or tr_len == 0:
        return 0.0

    # Length ratio should be reasonable (0.3 to 3.0)
    ratio = av_len / tr_len
    if ratio < 0.2 or ratio > 5.0:
        return 0.1
    elif ratio < 0.3 or ratio > 3.0:
        return 0.4

    # Both should have content
    return 0.7 + 0.3 * min(1.0, min(av_len, tr_len) / 5)


def compute_fitness(
    pair: SentencePair,
    existing: list[SentencePair],
    weights: dict[str, float] | None = None,
) -> float:
    """Compute overall fitness score (0-1) for a sentence pair."""
    if weights is None:
        weights = {
            "language": 0.35,
            "consistency": 0.30,
            "diversity": 0.35,
        }

    scores = {
        "language": score_language_validity(pair.av),
        "consistency": score_translation_consistency(pair.av, pair.tr),
        "diversity": score_diversity(pair.av, existing),
    }

    total = sum(scores[k] * weights[k] for k in weights)
    return round(min(max(total, 0.0), 1.0), 4)
