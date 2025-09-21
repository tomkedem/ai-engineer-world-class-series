import re

def count_sentences(text: str) -> int:
    # מחלק את הטקסט לפי סימני סוף משפט, ומסנן תוצאות ריקות
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])

if __name__ == "__main__":
    sample = (
    "היום יום יפה! מחר נצא לטיול. האם תבוא איתנו? "
    "הטיול יתחיל בשעה שמונה. נא להביא מים ואוכל. "
    "בסוף היום נחזור הביתה."
)


    sentences = [s.strip() for s in re.split(r'[.!?]', sample) if s.strip()]
    num_sentences = len(sentences)
    print(f"מספר המשפטים בטקסט: {num_sentences}")
    print("המשפטים בטקסט:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
