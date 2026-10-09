#!/usr/bin/env python3
"""Check catalog consistency and local documentation links."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "catalog/resources.json").read_text())["resources"]
assert len({r["repository"] for r in rows}) == len(rows), "Duplicate resource"
readme = (ROOT / "README.md").read_text()
for row in rows:
    assert re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", row["repository"])
    assert re.fullmatch(r"[0-9a-f]{40}", row["commit"])
    assert row["url"] == "https://github.com/" + row["repository"]
    assert row["repository"] in readme
    assert row["build_state"] == "NOT_RUN"
json.loads((ROOT / "metadata/schema.jsonld").read_text())
count = 0
for path in ROOT.rglob("*.md"):
    if "workspace" in path.relative_to(ROOT).parts:
        continue
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if "://" in link or link.startswith("#"):
            continue
        target = (path.parent / link.split("#")[0]).resolve()
        assert target.is_relative_to(ROOT), f"Escaping link: {path} {link}"
        assert target.exists(), f"Broken link: {path} {link}"
        count += 1
print(f"PASS: {len(rows)} catalog records, JSON metadata and {count} local links")
