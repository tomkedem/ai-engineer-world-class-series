import re

def count_sentences(text: str) -> int:
    # מחלק את הטקסט לפי סימני סוף משפט, ומסנן תוצאות ריקות
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])

def summarize_text(text: str) -> None:
    """
    מדפיסה סיכום טקסט: מספר מילים, משפטים ותווים.
    """
    num_words = len([w for w in text.split() if w.strip()])
    num_sentences = count_sentences(text)
    num_chars = len(text)
    print(f"מספר מילים: {num_words}")
    print(f"מספר משפטים: {num_sentences}")
    print(f"מספר תווים: {num_chars}")

def summarize_file(file_path: str) -> None:
    """
    קורא טקסט מקובץ ומסכם אותו.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            text = f.read()
        summarize_text(text)
    except FileNotFoundError:
        print(f"שגיאה: הקובץ '{file_path}' לא נמצא.")
    except Exception as e:
        print(f"שגיאה בקריאת הקובץ: {e}")

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

    summarize_text(sample)    

      # תרגיל 3: קריאה מקובץ חיצוני
    print("\nסיכום קובץ input.txt:")
    summarize_file("input.txt")
