#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast for the invented city of Soggport
to /output/entry.txt. The line keeps the rhythm of a broadcast forecast
while bending it toward a smile for a bored commuter.
"""

import os

ENTRY = (
    "Soggport today: drizzle till noon, then one brave hour of sun for the "
    "harbour duck race; highs 14\u00b0, lows the mood aboard the 8:05 ferry."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
