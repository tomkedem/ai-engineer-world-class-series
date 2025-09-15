def clean_text(text: str) -> str:
    """
    מנקה טקסט: מסיר רווחים מיותרים ומחזיר lowercase.
    """
    return " ".join(text.split()).lower()

if __name__ == "__main__":
    sample = "   פייתון   היא   שפה  נהדרת   "
    print(clean_text(sample))
