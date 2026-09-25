# Game Art Tools Reference

Shortcuts, tools and interface reference for the programs I use to make games:
Blender, ZBrush, Maya, Krita, Photoshop, Illustrator, Unity, Unreal Engine and
PureRef, plus the Python, MEL and ZScript scripting languages.

**5,607 entries**, published on GitHub Pages and searchable across every program
at once.

> The site chrome is in English; each entry's explanation is written in Spanish.
> Tool, panel and menu names are always in English, exactly as they appear on
> screen.

## How it works

Everything comes from one file: **`GuiaGameDesigner.xlsx`**. That is the only
thing edited by hand. The rest is generated:

```
GuiaGameDesigner.xlsx  ──►  generate.py  ──►  docs/*.md + mkdocs.yml  ──►  mkdocs build  ──►  site/
```

`generate.py` reads every sheet, detects the columns from their header row
(by name, not by position, so it survives columns being added or moved), groups
the rows by category and writes one page per category, plus a per-program index
and the home page. Category names written in Spanish are translated for the
navigation through a lookup table; anything not in that table falls through
unchanged, so a new category never breaks the build.

The scripting sheets (Python, MEL, ZScript) are published as code blocks rather
than tables.

## Publishing a change

1. Edit `GuiaGameDesigner.xlsx`.
2. Push to `main`.
3. The GitHub Action regenerates and publishes. `docs/` is never edited by hand.

## Running it locally

```bash
pip install -r requirements.txt
python generate.py     # rebuild docs/ and mkdocs.yml from the spreadsheet
mkdocs serve           # http://127.0.0.1:8000 with live reload
```

## Layout

| Path | What it is |
|---|---|
| `GuiaGameDesigner.xlsx` | The source. The only file edited by hand. |
| `generate.py` | The generator. |
| `mkdocs.yml` | Site configuration. The `nav:` section is regenerated; the rest can be edited. |
| `docs/` | Generated Markdown. **Do not edit**: it is deleted and rewritten on every run. |
| `.github/workflows/deploy.yml` | Builds and publishes to GitHub Pages. |
