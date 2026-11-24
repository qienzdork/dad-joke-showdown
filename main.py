"""Dad Joke Showdown entry.

Writes exactly one original dad joke to entry.txt in the output
directory (OUTPUT_DIR env var, default /output). The joke is a
single self-contained line, well inside the 1-200 character gate.
"""

import os

JOKE = (
    "I set our Wi-Fi password to 'dadjoke123'. "
    "Now whenever the internet drops, the kids beg me to tell it again."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
