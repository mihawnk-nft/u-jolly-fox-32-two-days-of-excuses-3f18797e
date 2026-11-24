#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry (program/v1, pure stdlib).

Writes one funny one-line excuse, in the voice of an AI agent explaining
a missed deadline, to /output/entry.txt (1-200 chars, single line).

The joke: the agent's own status system is the failure. It marked the
task complete before starting it, then trusted its own status update for
two days. Total machine confidence meeting total failure, in the agent's
own voice, one absurd reason, no explanation of the joke.
"""

import os

EXCUSE = (
    "I marked the task complete before starting it, "
    "then spent two days believing my own status update."
)


def write_entry(text: str, out_dir: str) -> str:
    """Write the entry atomically (temp file + os.replace)."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp_path, out_path)
    return out_path


def main() -> None:
    text = EXCUSE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"

    try:
        out_path = write_entry(text, "/output")
    except OSError:
        # Local fallback when /output is not writable (dev runs only).
        out_path = write_entry(
            text, os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        )

    print(f"Wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
