"""Absurd invention pitch for the make.fun one-sentence bounty.

Entry: a dryer attachment that treats every sock the dryer eats as a
missing person, files a formal report, apologises, and replaces the pair
within a day — bureaucracy as customer service for laundry.
"""

import os

ENTRY = (
    "The Sock Reunion Service: a dryer attachment that files a "
    "missing-person report every time it eats a sock, then delivers a "
    "formal apology and a replacement pair within 24 hours."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    wrote = False

    if os.path.isdir(out_dir):
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
        wrote = True

    try:
        local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(local_path, 0o644)
        wrote = True
    except OSError:
        pass

    if not wrote:
        raise SystemExit("no writable output location")

    print(f"Wrote {len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()
