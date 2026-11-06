#!/usr/bin/env python3
"""Check curriculum integrity without executing any learner activity."""

from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTATIONS = "https://thumbtack.haystack.so/resources/c8602dcc-0898-4f92-ae93-243ee7d696ba"
VIDEOS = {
    "1.01": "5eba8bbfee0e4480b1916ddbf81c0f52",
    "4.02": "1b8d4305c7514781ae863a8026441953",
    "5.01": "a577d0d389c84940adc1ef10ae835fd1",
    "8.01": "1cee2c493d364e9fa291de56bab91374",
    "10.01": "ddb675d9010e40469563edcac5adbba8",
}


def verify(root=ROOT):
    errors = []
    index = json.loads((root / "curriculum/course-index.json").read_text())
    template = json.loads((root / "learner-assets/progress-template.json").read_text())
    expected = {}
    links = 0
    for module in index:
        module_path = root / module["path"]
        body = module_path.read_text()
        lessons = module["lessons"]
        if f"lessons: {len(lessons)}" not in body:
            errors.append(f"Lesson count mismatch: {module_path}")
        if "**ChatGPT Work:**" not in body or "**Codex:**" not in body:
            errors.append(f"Missing surface route: {module_path}")
        actual_files = set((module_path.parent / "lessons").glob("*.md"))
        expected_files = {root / lesson["path"] for lesson in lessons}
        if actual_files != expected_files:
            errors.append(f"Unindexed or missing lesson: {module_path}")
        for number, lesson in enumerate(lessons, 1):
            key = lesson["number"]
            expected[key] = lesson["title"]
            if key != f"{module['module']}.{number:02d}":
                errors.append(f"Lesson sequence: {key}")
            path = root / lesson["path"]
            text = path.read_text()
            if f"# Lesson {key}: {lesson['title']}" not in text:
                errors.append(f"Title/index mismatch: {path}")
            sections = ["## Learn", "## See It", "## Practice", "## Challenge — Optional", "## Quick Check", "## Carry Forward"]
            positions = [text.find(section) for section in sections]
            if min(positions) < 0 or positions != sorted(positions):
                errors.append(f"Teaching sequence: {path}")
            if text.count("**Success criteria:**") != 2:
                errors.append(f"Missing activity criteria: {path}")
            practice = text.split("## Practice", 1)[-1].split("## Challenge", 1)[0]
            if len(re.findall(r"^\d+\. ", practice, flags=re.M)) < 3:
                errors.append(f"Missing guided practice steps: {path}")
            video_ids = set(re.findall(r"loom\.com/share/([a-f0-9]{32})", text))
            if video_ids != ({VIDEOS[key]} if key in VIDEOS else set()):
                errors.append(f"Unexpected or missing video: {path}")
            record = template["lessons"].get(key, {})
            if record.get("title") != lesson["title"]:
                errors.append(f"Progress title mismatch: {key}")
            if any(record.get(s) != "not_started" for s in ["learn", "practice", "challenge"]):
                errors.append(f"Template contains completed learner state: {key}")
    if set(expected) != set(template["lessons"]):
        errors.append("Progress template and lesson index differ")
    for path in root.rglob("*.md"):
        if "skills" in path.relative_to(root).parts:
            continue  # Preserve imported source packages rather than editing their links.
        text = path.read_text()
        if text.count("```") % 2:
            errors.append(f"Unclosed code block: {path}")
        if re.search(r"AI Operating Guardrails|1eKbp89j9o7q|1zxApnzVuSZ", text, flags=re.I):
            errors.append(f"Retired company reference: {path}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-z]+://|mailto:|#", target):
                continue
            clean = unquote(target.strip("<>").split("#")[0])
            if clean:
                links += 1
                if not (path.parent / clean).exists():
                    errors.append(f"Broken local link: {path}: {target}")
    for location in ["README.md", "AGENTS.md", "curriculum/modules/module-00-welcome/welcome.md"]:
        if EXPECTATIONS not in (root / location).read_text():
            errors.append(f"Missing current expectations link: {location}")
    source = json.loads((root / "learner-assets/skills/clean-draft-source.json").read_text())
    for file in source["files"]:
        content = (root / "learner-assets/skills/clean-draft" / file["path"]).read_bytes()
        if hashlib.sha256(content).hexdigest() != file["sha256"]:
            errors.append(f"Changed Clean Draft source: {file['path']}")
    totals = collections.defaultdict(lambda: [0, 0])
    with (root / "practice-workspace/weekly-update/sample-metrics.csv").open() as source_file:
        for row in csv.DictReader(source_file):
            totals[row["week"]][0] += int(row["requests_received"])
            totals[row["week"]][1] += int(row["requests_completed"])
    if dict(totals) != {"2026-10-19": [20, 16], "2026-10-26": [20, 17]}:
        errors.append("Sample data no longer supports the spreadsheet lesson")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Verified {len(index)} modules, {len(expected)} lessons, {links} local links, progress template, five video placements, Clean Draft integrity, and sample calculations.")
    return 0


if __name__ == "__main__":
    sys.exit(verify())
