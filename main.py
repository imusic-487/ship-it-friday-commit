#!/usr/bin/env python3
"""Ship It Friday entry.

Writes one line -- the funniest git commit message an AI coding agent
would write right before breaking production on a Friday -- to
/output/entry.txt, as the competition kit requires.
"""

import os

ENTRY = "feat: approved my own PR, deleted the failing tests, shipped to prod \u2014 happy Friday!"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def check_entry(text):
    """Make sure the entry passes the kit's gate before writing it."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must have no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d cap" % (len(text), MAX_CHARS))


def main():
    check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    # Read back what was written and confirm it matches byte for byte,
    # so a silent write failure can never pass as a valid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry on disk differs from ENTRY")
    print("Wrote %d chars to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
