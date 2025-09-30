# mini_text/stats.py

from collections import Counter
from typing import Dict, List       

"""
כלי סטטיסטיקה לטקסט:
- word_count: סופר מילים
- unique_ratio: יחס מילים ייחודיות
"""

def word_count(text: str) -> int:
    """
    סופר את מספר המילים בטקסט.
    """
    return len(text.split())

def unique_ratio(text: str) -> float:
    """
    מחשב את יחס המילים הייחודיות בטקסט.
    """
    tokens = text.split()
    return len(set(tokens)) / max(1, len(tokens))

def word_frequencies(tokens: List[str]) -> Dict[str, int]:
    """
    מחשב את תדירות המילים ברשימת טוקנים.
    
    Args:
        tokens (List[str]): רשימת מילים (טוקנים).
        
    Returns:
        Dict[str, int]: מילון עם מילים כמפתחות ותדירותן כערכים.
    """
    return dict(Counter(tokens))
