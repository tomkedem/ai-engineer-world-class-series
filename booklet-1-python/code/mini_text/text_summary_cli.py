import sys
from core import safe_write_json
from sentence_counter import summarize_my_text, summarize_file



if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"סיכום קובץ {file_path}:")
        file_summary = summarize_file(file_path)
        if file_summary:
            print(file_summary)
            safe_write_json(file_summary, "output/summary.json")
    else:
        sample = "שלום עולם! מה שלומך?"
        print("סיכום טקסט קשיח:")
        summary = summarize_my_text(sample)
        print(summary)
        safe_write_json(summary, "output/summary.json")