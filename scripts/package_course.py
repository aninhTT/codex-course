#!/usr/bin/env python3
"""Build a portable course ZIP without learner progress or generated outputs."""

from pathlib import Path
import argparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "README.md", "AGENTS.md", "START-HERE.md",
    "learner-assets/artifact-tracker.md", "learner-assets/progress-template.json",
    "learner-assets/run-card-template.md", "learner-assets/workflow-map-template.md",
    "learner-assets/use-case-shortlist.md", "learner-assets/skills/clean-draft-source.json",
    "practice-workspace/README.md", "practice-workspace/outputs/README.md",
    "playground/README.md", "scripts/verify_course.py", "scripts/package_course.py",
}
PREFIXES = (
    "curriculum/", "reference/", "learner-assets/skills/clean-draft/",
    "learner-assets/skills/use-case/", "practice-workspace/weekly-update/",
    "practice-workspace/starter-app/", "practice-workspace/notes/",
    "practice-workspace/templates/", "practice-workspace/inbox/",
    "practice-workspace/projects/", "practice-workspace/reference/",
)


def selected_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(ROOT).parts):
            continue
        if relative in FILES or relative.startswith(PREFIXES):
            yield path, relative


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist/everyday-work-course.zip")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, relative in selected_files():
            archive.write(path, "everyday-work-course/" + relative)
    with zipfile.ZipFile(args.output) as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        assert "everyday-work-course/START-HERE.md" in names
        assert not any(name.endswith("/progress.json") or "/.git/" in name for name in names)
    print(f"Built {args.output} ({len(names)} files; no saved learner progress or generated outputs).")


if __name__ == "__main__":
    main()
