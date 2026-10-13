#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create the directory structure for a new DPI submission.")
    parser.add_argument("number", type=int, help="Submission number, for example 4")
    args = parser.parse_args()
    if args.number < 1:
        raise SystemExit("Submission number must be positive.")

    directory = ROOT / "submissions" / f"submission_{args.number}"
    if directory.exists():
        raise SystemExit(f"Directory already exists: {directory.relative_to(ROOT)}")

    (directory / "source").mkdir(parents=True)
    (directory / "revisions").mkdir()
    readme = f"""# Submission N{args.number}

## Workflow

1. Add the assignment prompt and original working files under `source/`.
2. Add reusable sources to `hub_manifest.json` and run `make hub-update`.
3. Read `AI_GUIDE.md` and the entry file for the selected agent.
4. Prepare the deliverable without overwriting source files.
5. Save instructor feedback as `feedback.md`.
6. Save corrected versions under `revisions/revision_1/`, `revision_2/`, and so on.
7. Document each correction in the revision's `revision_notes.md`.
8. Update `DECISIONS.md`, `INDEX.md`, and this README.
9. Run `make hub-check`.

## Contents

- `source/`: prompt and original working files.
- `revisions/`: corrected versions created after review or instructor feedback.
- `feedback.md`: instructor feedback when available.
"""
    (directory / "README.md").write_text(readme, encoding="utf-8")
    (directory / "source" / ".gitkeep").touch()
    (directory / "revisions" / ".gitkeep").touch()
    print(f"created {directory.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
