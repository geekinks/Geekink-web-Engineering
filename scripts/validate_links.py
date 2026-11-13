#!/usr/bin/env python3
"""Check local Markdown links while deliberately ignoring external URLs and anchors."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]; errors=[]
for md in ROOT.rglob("*.md"):
    text=md.read_text(encoding="utf-8")
    for href in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if href.startswith(("http://", "https://", "#", "mailto:")): continue
        target=href.split("#",1)[0]
        if target and not (md.parent/target).resolve().exists(): errors.append(f"{md.relative_to(ROOT)} -> {href}")
if errors:
    print("Broken local links:\n- " + "\n- ".join(errors)); sys.exit(1)
print("Local Markdown link validation passed.")
