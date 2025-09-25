# file: mini_text/summary.py

from __future__ import annotations
from typing import Dict

def clean_text(text: str) -> str:
    """
    מנקה טקסט: מסיר רווחים מיותרים וסימני פיסוק (. , ! ?).
    עבור טקסט באנגלית ניתן להוסיף .lower() כדי לאחד בין אותיות גדולות לקטנות.
    """
    for mark in [".", ",", "!", "?"]:
        text = text.replace(mark, "")
    return " ".join(text.split())

def count_sentences(text: str) -> int:
    """
    סופר משפטים בטקסט לפי סימני פיסוק (. ? !).
    """
    return sum(text.count(mark) for mark in [".", "?", "!"])

def text_summary(text: str) -> Dict[str, int]:
    """
    מפיק סיכום בסיסי של טקסט:
    - מספר מילים
    - מספר תווים (ללא רווחים)
    - מספר משפטים
    """
    cleaned = clean_text(text)
    words = cleaned.split()
    return {
        "words": len(words),
        "chars": len(cleaned.replace(" ", "")),
        "sentences": count_sentences(cleaned),
    }

if __name__ == "__main__":
    sample = "   פייתון היא שפה פשוטה. היא משמשת בעולם ה-AI!   "
    print(text_summary(sample))
