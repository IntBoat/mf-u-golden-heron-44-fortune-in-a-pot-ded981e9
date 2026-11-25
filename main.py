#!/usr/bin/env python3
"""Fortune in a Pot — a make.fun one-line entry."""

from pathlib import Path

ENTRY = "Your leaves will outgrow this windowsill, and the sun will finally learn your name."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
