"""The Vacuum's Alibi — one-line entry printer.

Reads the alibi from entry.txt sitting next to this file and prints it.
"""

from pathlib import Path


def load_alibi():
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    alibi = text.strip()
    if not alibi:
        raise ValueError("entry.txt is empty — the vacuum has no alibi")
    return alibi


def main():
    print(load_alibi())


if __name__ == "__main__":
    main()
