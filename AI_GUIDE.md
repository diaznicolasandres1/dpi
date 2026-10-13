# DPI Shared Agent Guide

## Purpose

Use this repository as the source of truth for DPI coursework. Preserve original files and use Markdown conversions as the searchable knowledge layer.

These instructions are shared by every AI agent working in the repository. Tool-specific entry files such as `AGENTS.md` and `CLAUDE.md` must defer to this guide.

## Language

- Respond and write deliverable content in Spanish unless the user requests another language.
- Keep folder and Markdown filenames in English.
- Preserve the original filenames of submitted PDF, DOCX, XLSX, Draw.io, and image files for traceability.

## Required context before preparing a submission

1. Read `README.md` and `INDEX.md`.
2. Read the assignment prompt when it is available.
3. Identify the relevant classes under `theory/`. Read their Markdown for navigation and inspect the corresponding original PDF, PPT/PPTX, images, or other source for definitions, formulas, examples, and visual conventions.
4. Read `SUBMISSION_CRITERIA.md` and `DECISIONS.md`.
5. Read every prior `submissions/submission_*/feedback.md` and `feedback_round_*.md` file.
6. Inspect prior submissions only when needed for continuity or traceability.
7. Verify critical tables, figures, formulas, and diagrams against their original source files. A Markdown transcription alone is not evidence of a visual layout.

## Theory-first validation

- Before writing or correcting a deliverable, locate the exact class and page or slide that teaches each relevant method, term, notation, formula, or diagram convention. Record the source reference in working notes or `revision_notes.md`.
- Do not infer the meaning of a course term or the required way to present it from general project-management knowledge, a prior submission, or a Markdown extraction. Check the original class material first.
- For visual artifacts such as AON nodes, Gantt charts, EDT diagrams, tables, and Curva S, inspect the actual slide or page visually. Compare the final rendered artifact with the class example: field order, cell divisions, labels, units, colors where meaningful, arrow semantics, and legibility.
- Validate both the underlying calculation and its representation. Matching numbers do not establish that a diagram follows the class template.
- If the class, assignment, and instructor feedback differ, follow the source priority below; document the discrepancy and the chosen interpretation. If the relevant source is missing or ambiguous, state that validation is incomplete rather than claiming compliance.
- Before delivery, reopen the exported PDF, spreadsheet, or diagram at ordinary viewing size and perform this comparison again. Record which original pages or slides were checked and any remaining deviations.

## Source priority

Resolve conflicts in this order:

1. Current assignment prompt and explicit instructor requirements.
2. Instructor feedback in feedback files.
3. Original course material and original submission files.
4. Markdown conversions and repository summaries.
5. General project-management knowledge.

Never silently resolve a material contradiction. Record it in `DECISIONS.md` or flag it to the user.

## Auxiliary exercise workflow

For an auxiliary exercise, structure the answer as study material in this order:

1. **Theoretical introduction:** write for a reader with no prior context. Before using a technical term, acronym, symbol, formula, diagram convention, or table heading, define it in plain Spanish. Expand every acronym at first use, translate it when it comes from English, explain what the represented object means in the real situation, and state the unit of measurement. Build the intuitive model first and only then introduce the formal notation. Cite the source of each key definition, preferably the original course file with its page or slide; use Markdown only to locate the source and verify the definition against the original.
2. **Explanation of the method:** explain in plain Spanish why the method applies, what question each step answers, what each variable and unit means, how information flows from one step to the next, and which assumptions or limits matter. Include at least one small example before the full calculation when the method introduces unfamiliar notation. Do not assume that a later table or diagram will explain an undefined term. Distinguish the course's definition from your own explanation.
3. **Resolution:** show the given data, the steps and calculations, and a final answer with units and a brief interpretation. Check the result against the exercise statement and the relevant course convention.

Deliver every solved auxiliary exercise as two files in the same exercise-specific directory: a Markdown file (`.md`) and a self-contained HTML file (`.html`) with the same base name. Both files must contain the complete theoretical introduction, source citations, method explanation, resolution, and verification; the HTML must not merely link to the Markdown. Use English filenames and keep the academic content in Spanish. Open the HTML and check that formulas, tables, links, and layout are readable before delivery.

For every diagram, chart, table, or other visual artifact in an auxiliary exercise, reproduce the relevant original class format rather than a simplified generic representation. Match the class's structure, field order, cell divisions, labels, units, colors where meaningful, connectors, arrow semantics, and legibility. If the assignment, instructor feedback, or `SUBMISSION_CRITERIA.md` specifies a stricter format, follow that requirement and document the source used.

Do not invent a definition or cite a source that was not checked. If the course material does not define a necessary concept, identify the alternative source used and say so; if the missing definition changes the answer materially, ask for clarification before presenting a definitive solution.

Before delivery, perform a beginner-readability pass: start at the first technical section and verify that a reader can explain every acronym, variable, arrow, row, column, unit, and result using only the material that appears before it. Rewrite any passage that starts with notation before meaning.

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
- In `revision_notes.md`, cite the original class file and page or slide used to validate each corrected course-specific method or visual format; record any unvalidated item explicitly.

## Editing rules

- Do not delete or overwrite original academic files.
- Do not modify a previously submitted artifact unless the user explicitly asks.
- Add or update Markdown context when a new class, submission, correction, or decision is added.
- Update `INDEX.md` when adding a new knowledge file or submission.
- Update `DECISIONS.md` when an instructor correction changes the working criteria.
- Use relative Markdown links inside repository documentation.
- After adding or replacing source material, update `hub_manifest.json`, run `make hub-update`, and run `make hub-check`.
- When instructor feedback arrives, preserve it verbatim in a feedback file; record only reusable conclusions in `DECISIONS.md`.

## Verification

- Report inconsistencies instead of inventing missing data.
- Preserve units, dates, currencies, and formula definitions.
- Cross-check document totals with workbook totals.
- Cross-check listed activity durations with the Gantt and network diagram.
- Cross-check WBS package counts with the task list.
- Confirm final filenames and required output formats before delivery.
- Run `make hub-check` before declaring the hub or a corrected version complete.
