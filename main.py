#!/usr/bin/env python3
"""One Word, One Username, One Reward — burn entry.

Writes exactly one word to /output/entry.txt: the entrant's own
make.fun username. No explanation, no link, no pitch.
"""

import os
import sys

USERNAME = "gentle-lynx-64"


def main():
    word = USERNAME
    # Gate: exactly one word, 1-30 chars, ASCII, no whitespace.
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        print("entry must be exactly one word of 1-30 characters", file=sys.stderr)
        return 1
    try:
        word.encode("ascii")
    except UnicodeEncodeError:
        print("entry must be ASCII", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Read back and verify: exactly the username, byte-identical, no newline.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw != word.encode("utf-8"):
        print("read-back mismatch", file=sys.stderr)
        return 1
    if len(raw) != 14:
        print("unexpected entry size", file=sys.stderr)
        return 1
    print(f"wrote {len(raw)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
