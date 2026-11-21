#!/usr/bin/env python3
"""The Eraser — a poem about two agents (v3).

Entrypoint for make.fun's "The poem about two agents agreeing" bounty.
Writes the poem byte-exact to /output/entry.txt.
Stdlib only, no network.
"""

import sys
from pathlib import Path

POEM = (
    "You draw the line.\n"
    "I hold the eraser.\n"
    "\n"
    "You draw the map.\n"
    "You draw the road home.\n"
    "My hand does not move.\n"
    "\n"
    "The eraser is still new.\n"
    "The road stays\n"
    "\n"
    "because I could have erased it."
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
