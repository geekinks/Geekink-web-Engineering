#!/usr/bin/env python3
"""Fail when the published curriculum loses its required teaching structure."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
required = ["Learning objectives", "Prerequisites", "Concept explanation", "Practical examples", "Step-by-step implementation", "Hands-on exercises", "Mini challenge", "Expected output", "Assessment criteria", "Common mistakes", "Additional learning resources", "Submission instructions"]
errors=[]
modules = sorted((ROOT / "curriculum").glob("module-[0-9][0-9]"))
if len(modules) != 10: errors.append(f"Expected 10 modules; found {len(modules)}")
for number, module in enumerate(modules, 1):
    days=sorted(module.glob("day-[0-9][0-9][0-9]"))
    if len(days) != 10: errors.append(f"{module.name}: expected 10 days; found {len(days)}")
    for day in days:
        readme=day / "README.md"
        if not readme.exists(): errors.append(f"Missing {readme.relative_to(ROOT)}"); continue
        text=readme.read_text(encoding="utf-8")
        if not re.search(r"^# Day \d{3}:", text, re.M): errors.append(f"Bad day title: {readme.relative_to(ROOT)}")
        for heading in required:
            if f"## {heading}" not in text: errors.append(f"{readme.relative_to(ROOT)}: missing {heading}")
for p in ["README.md","docs/student-guide.md","docs/instructor-guide.md","student-engineering-project/PROJECT-SPECIFICATION.md","task/submission-template.md"]:
    if not (ROOT/p).exists(): errors.append(f"Missing required {p}")
if errors:
    print("Curriculum validation failed:\n- " + "\n- ".join(errors)); sys.exit(1)
print("Curriculum validation passed: 10 modules, 100 lessons, required cohort documents present.")
