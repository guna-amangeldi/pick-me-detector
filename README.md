# Pick Me Detector™

A tiny text-analysis script that checks movie dialogue for **romantic self-erasure vibes**  
(aka when a character’s entire personality disappears into a relationship aka Bella Swan).

Rule-based. Explainable. Slightly sarcastic.

---

## What it does
- Reads a text file with dialogue
- Looks for common self-negating phrases
- Prints the lines + a quick “vibe check”

No ML, no magic. Just patterns.

---

## Run it
```bash
pip3 install nltk
python3 main.py phrases.txt
