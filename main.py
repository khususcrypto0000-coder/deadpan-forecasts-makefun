#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes a single-line deadpan TV weather forecast for a fictional city
to /output/entry.txt. Standard library only, no network, deterministic.
"""

import os

FORECAST = (
    "In Vrellmark, expect 38\u00b0C rain falling sideways at 70 km/h until noon, "
    "followed by a brief, polite hailstorm that apologizes and clears by 15:00."
)


def main() -> None:
    text = FORECAST.strip()
    if not text:
        raise SystemExit("forecast must not be empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("forecast must be exactly one line")
    if not 1 <= len(text) <= 160:
        raise SystemExit(
            "forecast must be 1-160 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    # Deterministic: same forecast text on every run.
    main()
