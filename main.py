#!/usr/bin/env python3
"""Print the entry line for the make.fun bounty.

Resolves entry.txt relative to this file, so the grader can run
`python3 -P -s /bot/main.py` from any working directory on a read-only
filesystem and still find the entry.
"""
from pathlib import Path


def main():
    entry = Path(__file__).resolve().parent / "entry.txt"
    print(entry.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    main()
