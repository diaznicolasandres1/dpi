# Hub Maintenance Scripts

## Initial setup

The scripts require Python 3 and the packages listed in `requirements-hub.txt`.

```bash
python3 -m pip install -r requirements-hub.txt
```

## Update converted material

When an original PDF, Word document, or Excel workbook changes:

```bash
make hub-update
```

To regenerate only outputs older than their source:

```bash
make hub-update-changed
```

## Create a new submission workspace

```bash
make new-submission N=4
```

This creates `submissions/submission_4/` with `source/`, `revisions/`, and a workflow README. It refuses to overwrite an existing submission.

## Add a new source

1. Place the original file in the appropriate English-named directory.
2. Add an entry to `hub_manifest.json` with an English Markdown output name.
3. Run `make hub-update`.
4. Add the new Markdown file to `INDEX.md` and the relevant directory `README.md`.
5. Run `make hub-check`.

Image-based material belongs under `manual_conversions` because its transcription requires visual verification.

## Validate the hub

```bash
make hub-check
```

The check detects:

- broken relative Markdown links;
- missing sources or conversions;
- empty Markdown outputs;
- conversions older than their source;
- generated documents missing from `INDEX.md`.

## Important limitation

Generated Markdown preserves extractable text and workbook formulas, but does not replace visual inspection of the original PDF, Word, Excel, Draw.io, or image file.
