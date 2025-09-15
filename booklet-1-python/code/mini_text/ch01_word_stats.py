# file: word_stats.py
from __future__ import annotations
import json
import logging
from pathlib import Path
from typing import Any, Dict


def simple_word_stats(text: str) -> Dict[str, Any]:
    """
    מחזיר סטטיסטיקות בסיסיות על הטקסט.
    מטפל גם במקרה של טקסט ריק או טקסט שמכיל רק רווחים.
    """
    # סינון מילים ריקות (רווחים בלבד)
    words = [word for word in text.split() if word.strip()]

    if not words:
        return {
            "word_count": 0,
            "unique_words": 0,
            "avg_word_length": 0,
            "most_common_word": None,
        }

    return {
        "word_count": len(words),
        "unique_words": len(set(words)),
        "avg_word_length": sum(len(w) for w in words) / len(words),
        # מוצא את המילה הנפוצה ביותר:
        # set(words) -> כל המילים הייחודיות
        # key=words.count -> סופר כמה פעמים כל מילה מופיעה ברשימה המקורית
        "most_common_word": max(set(words), key=words.count),
    }


def safe_write_json(data: Dict[str, Any], filepath: Path) -> bool:
    """
    כותב נתונים לקובץ JSON עם טיפול בשגיאות.
    """
    try:
        filepath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    except (IOError, TypeError) as e:
        logging.error(f"נכשלה כתיבה לקובץ {filepath}: {e}")
        return False


def main() -> None:
    """
    נקודת הכניסה לסקריפט.
    """
    text = "פייתון היא שפה פרקטית מאוד. היא משמשת בליבת מערכות AI."
    stats = simple_word_stats(text)
    output_file = Path("stats.json")
    if safe_write_json(stats, output_file):
        print(f"נשמר קובץ: {output_file}")


if __name__ == "__main__":
    main()
