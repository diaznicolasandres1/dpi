# DPI Repository Instructions

## Purpose

Use this repository as the source of truth for DPI coursework. Preserve original files and use Markdown conversions as the searchable knowledge layer.

## Language

- Respond and write deliverable content in Spanish unless the user requests another language.
- Keep folder and Markdown filenames in English.
- Preserve the original filenames of submitted PDF, DOCX, XLSX, Draw.io, and image files for traceability.

## Required context before preparing a submission

1. Read `README.md` and `INDEX.md`.
2. Read the assignment prompt when it is available.
3. Read the relevant files under `theory/`.
4. Read `SUBMISSION_CRITERIA.md` and `DECISIONS.md`.
5. Read every prior `submissions/submission_*/feedback.md` file.
6. Inspect prior submissions only when needed for continuity or traceability.
7. Verify critical tables, figures, formulas, and diagrams against their original source files.

## Source priority

Resolve conflicts in this order:

1. Current assignment prompt and explicit instructor requirements.
2. Instructor feedback in `feedback.md` files.
3. Original course material and original submission files.
4. Markdown conversions and repository summaries.
5. General project-management knowledge.

Never silently resolve a material contradiction. Record it in `DECISIONS.md` or flag it to the user.

## Submission workflow

- Work in the corresponding `submissions/submission_N/` directory.
- Keep the deliverable focused on the current assignment. Do not reproduce previous submissions unless the prompt requires it.
- Maintain traceability among objectives, scope, WBS/EDT, activities, network, schedule, resources, costs, risks, and acceptance criteria.
- Reconcile totals across narrative documents, diagrams, schedules, and spreadsheets.
- Explain any duration reduction through resources, productivity, scope, or another explicit assumption.
- Distinguish contingency reserve, management reserve, cost baseline, and total project budget.
- Treat SV as a monetary variance unless schedule time analysis is performed separately.
- Check the critical path after applying calendars, resource constraints, and mandatory milestones.
- Before finalizing, run the checklist in `SUBMISSION_CRITERIA.md`.
- Preserve the exact submitted version. Place later corrections under `revisions/revision_N/`.
- For every corrected version, create `revision_notes.md` mapping each feedback item to the change, affected file, and verification.

## Editing rules

- Do not delete or overwrite original academic files.
- Do not modify a previously submitted artifact unless the user explicitly asks.
- Add or update Markdown context when a new class, submission, correction, or decision is added.
- Update `INDEX.md` when adding a new knowledge file or submission.
- Update `DECISIONS.md` when an instructor correction changes the working criteria.
- Use relative Markdown links inside repository documentation.
- After adding or replacing source material, update `hub_manifest.json`, run `make hub-update`, and run `make hub-check`.
- When instructor feedback arrives, preserve it verbatim in `feedback.md`; record only reusable conclusions in `DECISIONS.md`.

## Verification

- Report inconsistencies instead of inventing missing data.
- Preserve units, dates, currencies, and formula definitions.
- Cross-check document totals with workbook totals.
- Cross-check listed activity durations with the Gantt and network diagram.
- Cross-check WBS package counts with the task list.
- Confirm final filenames and required output formats before delivery.
