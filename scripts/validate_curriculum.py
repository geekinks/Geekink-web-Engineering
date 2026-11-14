#!/usr/bin/env python3
"""Validate the active 12-week GeekInk curriculum."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
weeks = sorted((ROOT / "weeks").glob("week-*"))
required = ["monday.md", "tuesday.md", "wednesday.md", "thursday.md", "friday.md"]
lesson_sections = [
    "Learning objectives", "Concepts to understand", "Lesson content",
    "Practical coding activity", "Guided example", "Independent exercises",
    "Expected output", "Homework / assignment", "Recommended learning resources",
]
errors = []
if len(weeks) != 12:
    errors.append(f"Expected 12 weeks; found {len(weeks)}.")
for number, week in enumerate(weeks, 1):
    if not week.name.startswith(f"week-{number:02d}-"):
        errors.append(f"Unexpected week order: {week.name}")
    if not (week / "README.md").is_file(): errors.append(f"Missing README: {week}")
    for filename in required:
        path = week / filename
        if not path.is_file(): errors.append(f"Missing {filename}: {week}")
        else:
            text = path.read_text(encoding="utf-8")
            missing = [section for section in lesson_sections if f"## {section}" not in text]
            if missing: errors.append(f"Incomplete lesson: {path.relative_to(ROOT)} missing {', '.join(missing)}")
lesson_count = sum(1 for week in weeks for name in required if (week / name).is_file())
if lesson_count != 60: errors.append(f"Expected 60 weekday lessons; found {lesson_count}.")
for path in [ROOT / "README.md", ROOT / "ROADMAP.md", ROOT / "CURRICULUM.md"]:
    if not path.is_file(): errors.append(f"Missing required overview: {path.name}")
if errors:
    print("Curriculum validation failed:\n- " + "\n- ".join(errors)); sys.exit(1)
print("Curriculum validation passed: 12 weeks, 60 weekday lessons.")
