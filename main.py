"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk to
entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output when unset).
Deterministic: no network, no randomness, no clock.
"""

import os

ENTRY = (
    "So... you also fake-check your notifications when the doors close, "
    "or is that just my firmware?"
)


def main() -> None:
    # Guard: the gate requires one line of 1-200 characters.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200
    # Grader runs with the repo read-only: resolve the output directory from
    # the environment first, never write next to the source files.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(
        os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline=""
    ) as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
