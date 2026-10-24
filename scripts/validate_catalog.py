#!/usr/bin/env python3
import csv
from pathlib import Path

for source, mandatory in [
    ("literature/papers.csv", ["Title", "URL", "Area"]),
    ("resources/datasets_and_code.csv", ["Resource", "URL", "Category"]),
]:
    path = Path(source)
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    assert rows, f"{source} is empty"
    for field in mandatory:
        assert field in rows[0], f"Missing column {field} in {source}"
    print(f"{source}: {len(rows)} records")
