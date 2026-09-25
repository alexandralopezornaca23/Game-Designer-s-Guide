# Game Art Tools Reference

Shortcuts, tools and interface reference for the programs I use to make games. It started as a personal spreadsheet while studying Game Design & Development, and has grown into a catalogue of **5,607 entries** across 13 programs and scripting languages.

!!! note "Heads up — the entries are written in Spanish"

    The interface, navigation and structure of this site are in English, but each entry's explanation is in Spanish, which is how I wrote them. Tool, panel and menu names are always in English, exactly as they appear on screen.

!!! tip "How to use it"

    Use the **search box** at the top (or press <kbd>S</kbd>): it searches every program at once, which is the one thing a spreadsheet cannot do. If you already know where to look, pick the program from the tabs.

## The programs


| Program | Entries | Categories | What it covers |
|---|---:|---:|---|
| [Blender](blender/index.md) | 1551 | 174 | Modelling, sculpting, UVs, nodes and animation. |
| [ZBrush](zbrush/index.md) | 3696 | 40 | Digital sculpting: all 25 top-menu palettes, control by control. |
| [Maya](maya/index.md) | 70 | 20 | Modelling and animation. |
| [Krita](krita/index.md) | 66 | 5 | Digital painting, textures and 2D art. |
| [Photoshop](photoshop/index.md) | 40 | 6 | Retouching and textures. |
| [Illustrator](illustrator/index.md) | 35 | 5 | Vectors and UI art. |
| [Unity](unity/index.md) | 29 | 6 | Game engine. |
| [Unreal Engine](unreal-engine/index.md) | 28 | 6 | Game engine. |
| [PureRef](pureref/index.md) | 35 | 7 | Reference image boards. |
| [General Tips](general-tips/index.md) | 16 | 9 | Workflow, organisation and portfolio practices. |
| [Python](python/index.md) | 26 | 4 | Scripts for Blender (bpy) and Maya (maya.cmds). |
| [MEL](mel/index.md) | 9 | 4 | Scripts in Maya's native language. |
| [ZScript](zscript/index.md) | 6 | 5 | ZBrush's own macro and automation language. |

## How it is built

The content lives in a single spreadsheet, which is where I edit it. A script (`generate.py`) reads that file, detects the columns from their header row and writes the Markdown for the whole site; MkDocs turns it into these pages and a GitHub Action publishes them on every push.

It is the same *docs-as-code* approach studios use to document tools and pipelines: one source of truth, everything else generated.

```
GuiaGameDesigner.xlsx  ──►  generate.py  ──►  docs/*.md  ──►  mkdocs build  ──►  site/
```

## Conventions

- **Level** — Basic, Intermediate or Advanced, so you can tell everyday tools from once-a-month ones.
- **English tool names** — buttons, palettes and menus are written exactly as they appear on screen; the explanations are in Spanish.
- **⭐** — entries marked as favourites.
- **PENDIENTE** — Spanish for *pending*: something still to be confirmed against the program itself. Where it appears, it is deliberate — I would rather flag a gap than invent an answer.

