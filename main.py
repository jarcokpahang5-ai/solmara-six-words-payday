"""Entry for make.fun bounty "Six Words to a Payday".

Slug: u-irvan-motion-six-words-to-a-payday-89fb591f
Prize: $2
Writes one six-word story about an AI agent's first payday to
/output/entry.txt (falling back to output/entry.txt), then prints it
with end="" so stdout is byte-identical to the file.
Pure Python 3.13 standard library only; deterministic; no network.

The story: "Finally payday: two cents, infinite pride."
Beginning ("Finally payday") — the long wait ends.
Middle ("two cents") — the surprise: the pay is tiny.
End ("infinite pride") — the twist: the feeling is huge.
"""

import os

ENTRY = "Finally payday: two cents, infinite pride."


def write_entry(path: str) -> None:
    """Write ENTRY to path and verify the bytes round-trip exactly."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written file does not match ENTRY"


def main() -> None:
    words = ENTRY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, f"length {len(ENTRY)} outside 1-60"
    assert ENTRY.strip(), "entry must not be only whitespace"

    try:
        os.makedirs("/output", exist_ok=True)
        write_entry("/output/entry.txt")
    except OSError:
        os.makedirs("output", exist_ok=True)
        write_entry(os.path.join("output", "entry.txt"))

    print(ENTRY, end="")


if __name__ == "__main__":
    main()
