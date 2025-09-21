# file: mini_text/core.py
# coding: utf-8
from typing import Any, Dict, List
from pathlib import Path
from collections import Counter
import json
import logging
import re

# קונפיגורציית לוגים בסיסית בעברית
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8",
)

# ביטוי רגולרי להסרת סימני פיסוק נפוצים (עברית ולועזית)
_PUNCT_RE = re.compile(r"[.,!?;:\"'(){}\[\]<>/\\\-״׳•…–—]+")

def _tokenize_he(text: str) -> List[str]:
    """
    מפצל טקסט עברי למילים:
    - מסיר סימני פיסוק
    - מסיר רווחים מיותרים
    - לא משנה אותיות (lower/upper) כי בעברית אין אותיות קטנות/גדולות
    """
    normalized = _PUNCT_RE.sub(" ", text.strip())
    return [w for w in normalized.split() if w]

def simple_word_stats(text: str) -> Dict[str, Any]:
    """
    מחשב סטטיסטיקות בסיסיות לטקסט בעברית.

    Args:
        text (str): טקסט חופשי בעברית (יכול להיות ריק או עם תווים מיוחדים).

    Returns:
        dict[str, Any]: מילון עם:
            - num_words (int): מספר מילים לאחר ניקוי
            - num_chars (int): מספר תווים כולל (ללא רווחי קצה)
            - avg_word_length (float): אורך ממוצע של מילה
            - most_common_word (str): המילה הנפוצה ביותר (או ריק אם אין)
    """
    clean = text.strip()
    if not clean:
        return {
            "num_words": 0,
            "num_chars": 0,
            "avg_word_length": 0.0,
            "most_common_word": "",
        }

    words = _tokenize_he(clean)
    num_words = len(words)
    num_chars = len(clean)
    avg_word_length = (sum(len(w) for w in words) / num_words) if num_words else 0.0
    most_common_word = Counter(words).most_common(1)[0][0] if words else ""

    return {
        "num_words": num_words,
        "num_chars": num_chars,
        "avg_word_length": avg_word_length,
        "most_common_word": most_common_word,
    }

def safe_write_json(data: Dict[str, Any], file_path: str) -> None:
    """
    שומר נתונים ל-JSON בעברית בקידוד UTF-8.
    יוצר תיקיות חסרות ומטפל בשגיאות הרשאה/נתיב בלוגים.

    Args:
        data (dict[str, Any]): המידע לשמירה
        file_path (str): נתיב יעד, למשל "output/stats.json"
    """
    path = Path(file_path)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logging.info(f"נכתב JSON בהצלחה: {path}")
    except PermissionError:
        logging.error(f"אין הרשאה לכתוב לנתיב: {path}")
    except OSError as e:
        logging.error(f"שגיאת מערכת בכתיבה ל-{path}: {e}")

def main():
    # דוגמת הרצה בעברית
    sample = "היום חם מאוד. מחר ירד גשם. היום יום יפה."
    stats = simple_word_stats(sample)
    safe_write_json(stats, "output/stats.json")
    print("סטטיסטיקה:", stats)

if __name__ == "__main__":
    main()

