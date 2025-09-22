import re
from core import safe_write_json


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

def summarize_my_text(text: str) -> dict:
    """
    מחזירה סיכום טקסט: מספר מילים, משפטים ותווים.
    """
    num_words = len([w for w in text.split() if w.strip()])
    num_sentences = count_sentences(text)
    num_chars = len(text)
    return {
        "num_words": num_words,
        "num_sentences": num_sentences,
        "num_chars": num_chars
    }
def summarize_file(file_path: str) -> dict:
    """
    קורא טקסט מקובץ ומחזיר סיכום.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            text = f.read()
        return summarize_my_text(text)
    except FileNotFoundError:
        print(f"שגיאה: הקובץ '{file_path}' לא נמצא.")
        return None
    except Exception as e:
        print(f"שגיאה בקריאת הקובץ: {e}")
        return None
    
if __name__ == "__main__":
    sample = (
    "היום יום יפה! מחר נצא לטיול. האם תבוא איתנו? "
    "הטיול יתחיל בשעה שמונה. נא להביא מים ואוכל. "
    "בסוף היום נחזור הביתה."
)

    sum_sentences =count_sentences(sample)
    print(f"מספר המשפטים בטקסט: {sum_sentences}")
    # sentences = [s.strip() for s in re.split(r'[.!?]', sample) if s.strip()]
    # num_sentences = len(sentences)
    # print(f"מספר המשפטים בטקסט: {num_sentences}")
    # print("המשפטים בטקסט:")
    # for i, sentence in enumerate(sentences, 1):
    #     print(f"{i}. {sentence}")

    # summarize_text(sample)    

    #   # תרגיל 3: קריאה מקובץ חיצוני
    # print("\nסיכום קובץ input.txt:")
    # file_summary = summarize_file("input.txt")
    # if file_summary:
       
    #     # תרגיל 4: שמירת סיכום ל-JSON באמצעות safe_write_json מהקובץ core.py
    #     safe_write_json(file_summary, "output/summary.json")