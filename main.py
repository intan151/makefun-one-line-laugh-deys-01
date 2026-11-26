#!/usr/bin/env python3
"""One Line, One Laugh — deterministic entry writer.

Writes a single original funny line to /output/entry.txt.
"""
import os

ENTRY = "I asked my mirror for an honest opinion, so it filed a restraining order against me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check gate: output must equal the entry exactly.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY
    assert 1 <= len(ENTRY) <= 140
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY


if __name__ == "__main__":
    main()
