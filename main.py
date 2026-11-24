#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

One line of weather, 140 characters at most, for a city that does not exist.
Run it and it prints the forecast; the competition harness reads the same
line from /output/entry.txt, so main() writes it there too.
"""

import os

LINE = "Murkford: 19°C, drizzle until lunch, then sunshine clocks in late — the bus is ten minutes behind, but the sky has already apologised."


def main() -> None:
    print(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
