"""Everyday Things, Two Lines -- make.fun entry.

Writes a two-line explanation of a toaster to /output/entry.txt.
Line 1 explains the toaster to a 10-year-old with one vivid analogy.
Line 2 says why that analogy works: what it maps and what it leaves out.
"""

ENTRY = (
    "A toaster is a tiny elevator for bread that takes it down into a hot "
    "basement and brings it back up brown and crispy.\n"
    "It maps the down-and-up trip and the heat turning pale bread brown, "
    "but it leaves out the timer that ends the ride and the fact that "
    "nobody is driving."
)


def gate_check(text):
    """Mirror the competition gate: UTF-8 text, 1-400 chars, not only
    whitespace, and exactly two lines. Also require each line to be a
    single sentence, as the task demands one sentence per line."""
    if not isinstance(text, str):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not 1 <= len(text) <= 400:
        return False
    if not text.strip():
        return False
    lines = text.split("\n")
    if len(lines) != 2:
        return False
    for line in lines:
        stripped = line.strip()
        if not stripped.endswith("."):
            return False
        # One sentence per line: no sentence-ending mark before the end.
        if any(mark in stripped[:-1] for mark in (".", "!", "?")):
            return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry failed the gate check")
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
