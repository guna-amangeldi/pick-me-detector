import sys
import re
import nltk
from nltk.tokenize import sent_tokenize

# Download tokenizer once (safe if already installed)
nltk.download("punkt", quiet=True)


# Patterns that represent self-negation
SELF_NEGATION_PATTERNS = [
    r"i('?m| am) not (pretty|interesting)",
    r"other girls are.*more",
    r"you don'?t have to worry about me",
    r"i('?m| am) fine being invisible",
    r"i don'?t belong (anywhere|here)",
    r"i don'?t fit in with girls",
    r"i don'?t like (shopping|makeup)",
    r"i('?m| am) clumsy",
    r"i('?m| am) boring",
    r"you wouldn'?t like me",
    r"you('?re| are) my entire world",
    r"if i have to die.*for you",
    r"my life doesn'?t matter",
    r"i('?ll| will) do whatever you want",
    r"just don'?t leave",
]


def analyze_text(text: str) -> list[str]:
    """
    Analyze text and return sentences that match self-negation patterns.
    """
    sentences = sent_tokenize(text.lower())
    hits = []

    for sentence in sentences:
        for pattern in SELF_NEGATION_PATTERNS:
            if re.search(pattern, sentence):
                hits.append(sentence.strip())
                break

    return hits


def main():
    # Expect a file path argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <phrases.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

    hits = analyze_text(text)

    print("Pick Me Detector")
    print("----------------------------")

    if not hits:
        print("No major Bella Swan energy")
        print("Either emotional growth happened, or this scene was cut")
        return

    print(f"Found {len(hits)} Bella-coded self-erasing lines:\n")

    for line in hits:
        print(f'- "{line}"')

    print("\nVibe check:")
    print("-----------")

    if len(hits) >= 5:
        print(
            "This script is DEEP in Bella Swan territory.\n"
            "Identity? Gone. Hobbies? Gone.\n"
            "Entire personality successfully replaced by one man."
        )
    elif len(hits) >= 2:
        print(
            "Some mild Bella energy detected.\n"
            "Nothing catastrophic yet, but the red flags are whispering."
        )
    else:
        print(
            "Low Bella Swan levels.\n"
            "Either character development exists, or the love interest hasn’t shown up yet."
        )



if __name__ == "__main__":
    main()
