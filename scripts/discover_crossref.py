#!/usr/bin/env python3
"""Find candidate dental robotics publications via Crossref, without auto-accepting them."""
import json
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

terms = [
    '"dental robotics"',
    '"robotic tooth preparation"',
    '"robot-assisted dental implant"',
    '"robotic dentistry"',
]
cutoff = (datetime.now(timezone.utc) - timedelta(days=21)).date().isoformat()
results = {}
for term in terms:
    query = urllib.parse.urlencode({
        "query.bibliographic": term,
        "filter": "from-pub-date:" + cutoff,
        "rows": 15,
        "select": "DOI,title,published,URL",
    })
    req = urllib.request.Request(
        "https://api.crossref.org/works?" + query,
        headers={"User-Agent": "DentalRoboticsResearchHub/1.0 (research discovery)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            items = json.load(response)["message"]["items"]
        for item in items:
            doi = item.get("DOI")
            if doi:
                results[doi] = item
    except Exception as error:
        print("Discovery warning:", term, error)

lines = ["# Candidate dental robotics papers", "", "Automatically found suggestions — verify relevance and citation metadata before adding to the catalog.", ""]
for doi, paper in sorted(results.items()):
    title = (paper.get("title") or ["Untitled"])[0]
    lines.append(f"- {title} — https://doi.org/{doi}")
if not results:
    lines.append("No candidates found in the queried window.")
Path("discovery.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Candidates:", len(results))
