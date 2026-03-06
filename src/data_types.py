from dataclasses import dataclass
import json
from pathlib import Path


@dataclass
class SentencePair:
    av: str
    tr: str
    source: str
    quality: float

    def __post_init__(self):
        if not self.av.strip():
            raise ValueError("Avar text cannot be empty")
        if not self.tr.strip():
            raise ValueError("Turkish text cannot be empty")
        if not 0.0 <= self.quality <= 1.0:
            raise ValueError(f"Quality must be 0-1, got {self.quality}")

    def to_dict(self) -> dict:
        return {"av": self.av, "tr": self.tr, "source": self.source, "quality": self.quality}

    @classmethod
    def from_dict(cls, d: dict) -> "SentencePair":
        return cls(av=d["av"], tr=d["tr"], source=d["source"], quality=d["quality"])


def save_pairs(pairs: list[SentencePair], path: str | Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for pair in pairs:
            f.write(json.dumps(pair.to_dict(), ensure_ascii=False) + "\n")


def load_pairs(path: str | Path) -> list[SentencePair]:
    pairs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                pairs.append(SentencePair.from_dict(json.loads(line)))
    return pairs
