import re

def count_sentences(text: str) -> int:
    # מחלק את הטקסט לפי סימני סוף משפט, ומסנן תוצאות ריקות
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])