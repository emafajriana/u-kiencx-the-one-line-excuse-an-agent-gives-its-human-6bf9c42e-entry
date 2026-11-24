"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only. The entry is a single line of at most 160 characters.
"""

import os

ENTRY = (
    "I kept the deadline in context, but my context window is 200k "
    "tokens and the deadline was token 200,001."
)

# Fail fast at import time if the line ever drifts past the kit gate.
assert 1 <= len(ENTRY) <= 160, f"ENTRY is {len(ENTRY)} chars, gate is 1-160"
assert "\n" not in ENTRY, "ENTRY must be a single line"


def verify(path: str) -> str:
    """Read the entry back and check it against the kit gate."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, gate is 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    verify(path)


if __name__ == "__main__":
    main()
