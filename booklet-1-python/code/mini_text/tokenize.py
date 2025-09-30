from __future__ import annotations

def simple_tokenize(text: str) -> list[str]:
    return [w for w in text.split() if w.strip()]
