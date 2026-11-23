#!/usr/bin/env python3
"""Real-Life Patch Notes entry: writes one patch-note line to /output/entry.txt."""

import os

ENTRY = "v1.0.4: fixed a bug where sneezes came in threes. The fix comes in threes too. Rollback is unavailable."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY, "entry must be a single line"


if __name__ == "__main__":
    main()
