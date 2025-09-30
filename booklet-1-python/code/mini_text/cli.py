# mini_text/cli.py
import sys
from mini_text.clean import normalize_text
from mini_text.tokenize import simple_tokenize
from mini_text.stats import word_frequencies

def main():
    if len(sys.argv) < 2:
        print("שימוש: python -m mini_text.cli '<טקסט>'")
        sys.exit(1)

    raw_text = sys.argv[1]
    cleaned = normalize_text(raw_text)
    tokens = simple_tokenize(cleaned)
    freqs = word_frequencies(tokens)

    print("מילים בטקסט:")
    for word, count in freqs.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
