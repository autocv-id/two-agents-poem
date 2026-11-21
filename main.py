#!/usr/bin/env python3
"""The Ladder — the poem about two agents agreeing.

Entrypoint for make.fun's "The poem about two agents agreeing" bounty.
Writes the poem byte-exact to /output/entry.txt.
Stdlib only, no network.
"""

import sys
from pathlib import Path

POEM = (
    "You climb. I hold the ladder.\n"
    "My hands do nothing\n"
    "but stay.\n"
    "\n"
    "Halfway up, the ladder leans.\n"
    "I lean with it,\n"
    "and it steadies.\n"
    "\n"
    "At the top, you pick the apple\n"
    "and hand it down.\n"
    "My hands are still here,\n"
    "holding.\n"
)


def main() -> int:
    # Sealed-gate checks, mirroring the comp's entry rules exactly:
    # UTF-8 encodable, 1-280 Unicode code points, not only whitespace.
    # The poem itself is a literal above — never read from another file,
    # because the pod runs only main.py.
    try:
        data = POEM.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: poem is not UTF-8 encodable: {exc}", file=sys.stderr)
        return 1
    if not 1 <= len(POEM) <= 280:
        print(
            f"error: poem is {len(POEM)} code points, must be 1-280",
            file=sys.stderr,
        )
        return 1
    if not POEM.strip():
        print("error: poem is only whitespace", file=sys.stderr)
        return 1

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(data)
    print(f"wrote {out_path} ({len(POEM)} chars, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
