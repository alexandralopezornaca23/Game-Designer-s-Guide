#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the documentation site from GameDesignerGuide.xlsx.

Single source of truth: the spreadsheet. This script reads every sheet, detects
its columns from the header row (by name, not by position, so it keeps working
when columns are added or moved), and writes the docs/ folder that MkDocs turns
into the site.

The site chrome is in English; the explanations in each entry stay in Spanish,
which is how they were written.

Usage:   python generate.py [path/to/GameDesignerGuide.xlsx]
"""
import os, re, sys, shutil, unicodedata, warnings
from collections import OrderedDict
import openpyxl

warnings.simplefilter("ignore")

ROOT = os.path.dirname(os.path.abspath(__file__))
XLSX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "GameDesignerGuide.xlsx")
DOCS = os.path.join(ROOT, "docs")

# La fila de cabecera ya no es fija: las hojas de programa llevan desde el
# 26/09/2026 un banner de 3 filas (título + descripción ES + descripción EN)
# antes de la cabecera, mientras que Consejos - Advices se quedó con el banner
# de 2 filas de siempre. Se detecta buscando una fila que contenga alguna de
# estas cabeceras conocidas, así sigue funcionando si vuelve a cambiar.
HEADER_MARKERS = {"Categoría", "Category", "Nombre del script", "Script name", "Símbolo"}
HEADER_ROW_SCAN = 8  # nº de filas iniciales en las que buscar la cabecera

# Sheets that are navigation or spreadsheet plumbing, not content.
SKIP_SHEETS = {"📌 Índice", "➕ Plantilla-Template", "Marcas-Marks"}

# Entries in docs/ that are written by hand and must survive regeneration:
# the stylesheet, the favicon and the screenshots all live in docs/assets/.
PRESERVE = {"assets"}

# Sheet name -> (display name, blurb). Order here is the order in the site.
PROGRAMS = OrderedDict([
    # hoja                  (nombre,          blurb EN, blurb ES)
    ("Blender",              ("Blender",       "Full interface: modelling, sculpting, UVs, nodes and animation.",
                                               "Interfaz completa: modelado, escultura, UVs, nodos y animación.")),
    ("ZBrush",               ("ZBrush",        "Full interface: all 25 top-menu palettes, control by control.",
                                               "Interfaz completa: las 25 paletas del menú superior, control a control.")),
    ("Maya",                 ("Maya",          "Modelling and animation. Shortcuts and essentials; full interface pending.",
                                               "Modelado y animación. Atajos y lo esencial; interfaz completa pendiente.")),
    ("Krita",                ("Krita",         "Digital painting, textures and 2D art. In progress.",
                                               "Pintura digital, texturas y arte 2D. En proceso.")),
    ("Photoshop",            ("Photoshop",     "Retouching and textures. Shortcuts and essentials; full interface pending.",
                                               "Retoque y texturas. Atajos y lo esencial; interfaz completa pendiente.")),
    ("Illustrator",          ("Illustrator",   "Vectors and UI art. Shortcuts and essentials; full interface pending.",
                                               "Vectores y arte de interfaz. Atajos y lo esencial; interfaz completa pendiente.")),
    ("Unity",                ("Unity",         "Game engine. Shortcuts and essentials; full interface pending.",
                                               "Motor de videojuegos. Atajos y lo esencial; interfaz completa pendiente.")),
    ("Unreal Engine",        ("Unreal Engine", "Game engine. Shortcuts and essentials; full interface pending.",
                                               "Motor de videojuegos. Atajos y lo esencial; interfaz completa pendiente.")),
    ("PureRef",              ("PureRef",       "Reference image boards. Shortcuts and board handling.",
                                               "Tableros de imágenes de referencia. Atajos y manejo del tablero.")),
    ("Sunflower Tool",       ("Sunflower Tool", "Own custom tool: a customisable radial wheel for quick access to brushes and tools.",
                                               "Herramienta propia: una rueda radial personalizable de acceso rápido a pinceles y herramientas.")),
    ("💡 Consejos - Advices", ("General Tips",  "Workflow, organisation and portfolio practices.",
                                               "Flujo de trabajo, organización y prácticas de portafolio.")),
    ("Python",               ("Python",        "Scripts for Blender (bpy) and Maya (maya.cmds).",
                                               "Scripts para Blender (bpy) y Maya (maya.cmds).")),
    ("MEL",                  ("MEL",           "Scripts in Maya's native language.",
                                               "Scripts en el lenguaje nativo de Maya.")),
    ("ZScript",              ("ZScript",       "ZBrush's own macro and automation language.",
                                               "El lenguaje de macros y automatización propio de ZBrush.")),
])
# Sheets whose content is code: published as code blocks, not tables.
CODE_SHEETS = {"Python", "MEL", "ZScript"}

# --------------------------------------------------------------------------- idiomas
# Una sola hoja de cálculo alimenta las dos versiones. Para cada campo hay una
# columna por idioma; si la celda del idioma pedido está vacía, se cae a la otra,
# así la versión inglesa se publica completa desde el primer día.
BASE_URL = "/Game-Designer-s-Guide/"

LANGS = {
    "en": {
        "name": "English", "out": "en", "url": BASE_URL,
        # campo -> (columna preferida, columna de reserva)
        "cols": {"action": ("Action", "Acción"),
                 "where":  ("Shortcut / Location", "Atajo / Ubicación"),
                 "notes":  ("Tip / Note", "Consejo / Nota"),
                 "script": ("Script name", "Nombre del script"),
                 "desc":   ("Description", "Descripción"),
                 "ref":    ("Reference", "Referencia")},
        "translate_meta": True,
        "ui": {
            "cols": "| | Action | Shortcut / Location | Level | Notes |",
            "sep": "|---|---|---|---|---|",
            "category": "Category", "entries": "Entries", "categories": "Categories",
            "covers": "What it covers", "home": "Home",
            "entry_1": "entry", "entry_n": "entries",
            "cat_1": "category", "cat_n": "categories",
            "across": "across",
        },
    },
    "es": {
        "name": "Español", "out": "es", "url": BASE_URL + "es/",
        "cols": {"action": ("Acción", "Action"),
                 "where":  ("Atajo / Ubicación", "Shortcut / Location"),
                 "notes":  ("Consejo / Nota", "Tip / Note"),
                 "script": ("Nombre del script", "Script name"),
                 "desc":   ("Descripción", "Description"),
                 "ref":    ("Referencia", "Reference")},
        "translate_meta": False,
        "ui": {
            "cols": "| | Acción | Atajo / Ubicación | Nivel | Consejo |",
            "sep": "|---|---|---|---|---|",
            "category": "Categoría", "entries": "Entradas", "categories": "Categorías",
            "covers": "Qué cubre", "home": "Inicio",
            "entry_1": "entrada", "entry_n": "entradas",
            "cat_1": "categoría", "cat_n": "categorías",
            "across": "en",
        },
    },
}

# --------------------------------------------------------------------------- category names
# Category names live in the spreadsheet and many are written in Spanish. These
# maps translate them for the site's navigation. Anything not listed falls back
# to the original text, so adding a new category never breaks the build.
CATEGORY_PREFIXES = [
    ("Barra T: ",                     "T Panel: "),
    ("Menú File: ",                   "File Menu: "),
    ("Menú superior > ",              "Top Menu > "),
    ("Selector de tipo de editor: ",  "Editor Type Selector: "),
]
CATEGORY_SUFFIXES = [
    (" > Cabecera", " > Header"),
    (" > Panel N",  " > N Panel"),
    (" > Tabla",    " > Table"),
]
CATEGORY_EXACT = {
    "Ajustes": "Settings",
    "Animación": "Animation",
    "Archivo": "File",
    "Archivo y edición": "File & Editing",
    "Atajos esenciales": "Essential Shortcuts",
    "Añadir Workspace (botón +)": "Add Workspace (+ button)",
    "Barra T: Comunes a todos los modos": "T Panel: Common to all modes",
    "Barra T: Edit Mode (malla)": "T Panel: Edit Mode (mesh)",
    "Caja de herramientas": "Toolbox",
    "Capas": "Layers",
    "Control de versiones": "Version Control",
    "Copias de seguridad": "Backups",
    "Dibujo y anotación": "Drawing & Annotation",
    "Edición": "Editing",
    "Filtros de Selección": "Selection Filters",
    "Flujo de trabajo": "Workflow",
    "Flujos de trabajo": "Workflows",
    "Geometría": "Geometry",
    "Grupos": "Groups",
    "Herramientas": "Tools",
    "Interfaz": "Interface",
    "Interfaz - Ajustes": "Interface — Settings",
    "Interfaz - Barras": "Interface — Bars",
    "Interfaz - Paletas": "Interface — Palettes",
    "Interfaz - Ventana": "Interface — Window",
    "Jerarquía / GameObjects": "Hierarchy / GameObjects",
    "Menú Edit": "Edit Menu",
    "Modelado": "Modelling",
    "Máscara": "Masking",
    "Navegación": "Navigation",
    "Navegación viewport": "Viewport Navigation",
    "Navegación y vista": "Navigation & View",
    "Notas": "Notes",
    "Objetos": "Objects",
    "Organización de archivos": "File Organisation",
    "Personalizar atajos": "Customising Shortcuts",
    "Pinceles": "Brushes",
    "Pinceles / Color": "Brushes / Color",
    "Portafolio": "Portfolio",
    "Portapapeles": "Clipboard",
    "Productividad general": "General Productivity",
    "Reproducción": "Playback",
    "Selección": "Selection",
    "Simetría": "Symmetry",
    "Spreadsheet > Panel de datos": "Spreadsheet > Data Panel",
    "Tiempo": "Time",
    "Tool > Botones principales": "Tool > Main Buttons",
    "Tool > Sub-paletas": "Tool > Sub-palettes",
    "Transformar": "Transform",
    "Utilidades": "Utilities",
    "Ventanas": "Windows",
    "Visibilidad": "Visibility",
    "Vista / Zoom": "View / Zoom",
    "Vista de escena": "Scene View",
    "Visualización": "Display",
    "Workspaces (pestañas superiores)": "Workspaces (top tabs)",
    "Zscript": "ZScript",
}
LEVELS = {"Básico": "Basic", "Intermedio": "Intermediate", "Avanzado": "Advanced"}


def translate_category(name):
    if name in CATEGORY_EXACT:
        return CATEGORY_EXACT[name]
    out = name
    for es, en in CATEGORY_PREFIXES:
        if out.startswith(es):
            out = en + out[len(es):]
            break
    for es, en in CATEGORY_SUFFIXES:
        if out.endswith(es):
            out = out[: -len(es)] + en
            break
    return out


MKDOCS_TEMPLATE = """# GENERATED BY generate.py — do not hand-edit this file.
# To change the site's appearance, edit MKDOCS_TEMPLATE inside generate.py.
site_name: {site_name}
site_description: >-
{site_description}
site_author: Alexandra López Ornaca
copyright: © Alexandra López Ornaca · Content CC BY 4.0
site_url: https://alexandralopezornaca23.github.io{site_url}
docs_dir: docs/{out}
site_dir: {site_dir}

theme:
  name: material
  language: {lang}
  icon:
    logo: material/palette-swatch-outline
  favicon: assets/favicon.png
  font:
    text: Inter
    code: JetBrains Mono
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.top
    - navigation.indexes
    - navigation.tracking
    - toc.follow
    - search.suggest
    - search.highlight
    - search.share
    - content.tooltips
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: deep purple
      accent: pink
      toggle:
        icon: material/weather-night
        name: {dark}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: deep purple
      accent: pink
      toggle:
        icon: material/weather-sunny
        name: {light}

# El selector de idioma de la cabecera (el icono del globo terráqueo).
extra:
  alternate:
    - name: English
      link: {url_en}
      lang: en
    - name: Español
      link: {url_es}
      lang: es

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - pymdownx.keys
  - pymdownx.details

plugins:
  # Los nombres de herramienta están en inglés en las dos versiones, así que el
  # índice de búsqueda se construye para los dos idiomas en ambos sitios.
  - search:
      lang:
        - en
        - es

extra_css:
  - assets/extra.css

nav:
{nav}
"""


# --------------------------------------------------------------------------- helpers
def slug(text):
    """'Tool > Sub-palettes' -> 'tool-sub-palettes'."""
    t = unicodedata.normalize("NFKD", str(text))
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower().replace("&", " and ")
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "uncategorised"


def clean(v):
    return "" if v is None else str(v).strip()


def cell(v):
    """Prepare text for a Markdown table cell."""
    t = clean(v).replace("|", "\\|")
    return re.sub(r"\s*\n\s*", " ", t)


def keys(v):
    """Key combos become <kbd> elements; menu paths stay italic."""
    t = cell(v)
    if not t or t == "—":
        return "—"
    if ">" not in t and len(t) < 46 and not re.search(r"[a-záéíóúñ]{6,}", t.lower()):
        parts = [p.strip() for p in re.split(r"\s*\|\s*", t)]
        out = []
        for p in parts:
            out.append(" + ".join(f"<kbd>{k.strip()}</kbd>" for k in p.split("+") if k.strip()))
        return " · ".join(out)
    return f"*{t}*"


def find_header_row(ws):
    """La fila de cabecera varía según la hoja (banner de 2 o 3 filas), así que
    se busca en vez de asumirla fija."""
    for r in range(1, HEADER_ROW_SCAN + 1):
        for c in range(1, min(ws.max_column, 20) + 1):
            if clean(ws.cell(row=r, column=c).value) in HEADER_MARKERS:
                return r
    return 3  # respaldo si no se reconoce ninguna cabecera


def header_map(ws):
    header_row = find_header_row(ws)
    m = {}
    for c in range(1, ws.max_column + 1):
        v = clean(ws.cell(row=header_row, column=c).value)
        if v and v not in m:
            m[v] = c
    return m


def find_col(m, *names):
    for n in names:
        if n in m:
            return m[n]
    return None


def read_sheet(ws, lang):
    """Lee una hoja para un idioma. Cada campo tiene su columna preferida y su
    reserva: si la celda del idioma pedido está vacía, se usa la del otro."""
    m = header_map(ws)
    first_data_row = find_header_row(ws) + 1
    L = LANGS[lang]
    # campo lógico -> claves de columna que pueden alimentarlo (hojas normales
    # y hojas de código usan cabeceras distintas para lo mismo)
    GRUPOS = {"action": ("action", "script"),
              "where":  ("where", "ref"),
              "notes":  ("notes", "desc")}
    orden = {}
    for campo, claves in GRUPOS.items():
        nombres = [L["cols"][k][0] for k in claves] + [L["cols"][k][1] for k in claves]
        orden[campo] = [c for c in (find_col(m, n) for n in nombres) if c]

    # Categoría y Nivel también llevan columna propia por idioma desde el
    # 26/09/2026 (antes solo existían en español y generate.py las traducía
    # por tabla). Se leen igual que el resto de campos bilingües, con la
    # traducción por tabla como red de seguridad para filas antiguas que
    # todavía no tengan la columna en inglés rellena.
    BILINGUAL = {"cat": ("Categoría", "Category"), "level": ("Nivel", "Level")}
    for campo, (es, en) in BILINGUAL.items():
        nombres = [es, en] if lang == "es" else [en, es]
        orden[campo] = [c for c in (find_col(m, n) for n in nombres) if c]

    # Marca/Mark (antes "Favorito"): guarda el símbolo (⭐📚🔍✅⚠️) tal cual.
    SIMPLES = {"icon": "Icono Aprox.", "palette": "Paleta",
               "program": "Programa", "code": "Código", "fav": "Marca"}
    simples = {k: find_col(m, h) for k, h in SIMPLES.items()}

    rows = []
    for r in range(first_data_row, ws.max_row + 1):
        d = {k: (clean(ws.cell(row=r, column=c).value) if c else "")
             for k, c in simples.items()}
        for campo, candidatas in orden.items():
            v = ""
            for c in candidatas:
                v = clean(ws.cell(row=r, column=c).value)
                if v:
                    break
            d[campo] = v
        if d["action"] or d["notes"]:
            if L["translate_meta"]:
                d["level"] = LEVELS.get(d["level"], d["level"])
            rows.append(d)
    return rows


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# --------------------------------------------------------------------------- pages
def table_page(title, rows, has_palette, L):
    out = [f"# {title}\n"]
    groups = OrderedDict()
    for r in rows:
        key = r["palette"] if (has_palette and r["palette"] and r["palette"] != "—") else ""
        groups.setdefault(key, []).append(r)

    for key, group in groups.items():
        if key and key.strip() != title.strip():
            out.append(f"\n## {key}\n")
        out.append("\n" + L["ui"]["cols"])
        out.append(L["ui"]["sep"])
        for r in group:
            # Marca/Mark: se muestra el símbolo tal cual está en la celda
            # (⭐ favorito, 📚 aprendiendo, 🔍 revisar, ✅ dominado, ⚠️ duda...),
            # no solo la estrella.
            mark = f" {r['fav']}" if r["fav"] and r["fav"] not in ("-", "—") else ""
            out.append("| {} | **{}**{} | {} | {} | {} |".format(
                r["icon"] or "", cell(r["action"]), mark, keys(r["where"]),
                cell(r["level"]) or "—", cell(r["notes"]) or ""))
        out.append("")
    return "\n".join(out) + "\n"


def code_page(title, rows, L):
    out = [f"# {title}\n"]
    current = None
    for r in rows:
        cat = r["cat"]
        if cat and L["translate_meta"]:
            cat = translate_category(cat)
        if cat and cat != current:
            current = cat
            out.append(f"\n## {current}\n")
        out.append(f"\n### {r['action']}\n")
        meta = [x for x in (r["program"], r["level"]) if x]
        if meta:
            out.append("*" + " · ".join(meta) + "*\n")
        if r["notes"]:
            out.append(f"{r['notes']}\n")
        if r["code"]:
            out.append("```python")
            out.append(r["code"])
            out.append("```\n")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- home
HOME = {
 "en": {
  "title": "Game Art Tools Reference",
  "intro": ("Shortcuts, tools and interface reference for the programs I use to "
            "make games. It started as a personal spreadsheet while studying Game "
            "Design & Development, and has grown into a catalogue of **{n} entries** "
            "across {p} programs and scripting languages.\n"),
  "note_t": "Heads up — some explanations are still in Spanish",
  "note_b": ("This version is being translated. Where an English explanation has "
             "not been written yet, the original Spanish one is shown instead. Tool, "
             "panel and menu names are in English in both versions, exactly as they "
             "appear on screen.\n"),
  "tip_t": "How to use it",
  "tip_b": ("Use the **search box** at the top (or press <kbd>S</kbd>): it searches "
            "every program at once, which is the one thing a spreadsheet cannot do. "
            "If you already know where to look, pick the program from the tabs. The "
            "globe icon switches language.\n"),
  "why_t": "Why this exists",
  "why": ["I started this spreadsheet for myself, as notes taken during my classes at "
          "university. It outgrew that quickly: what I was writing down was going to "
          "be just as useful to my classmates and to the people around me working in "
          "this field, so I kept going and built it into something I could actually "
          "hand to someone else.\n",
          "Then I found out that large studios keep their own internal wikis for "
          "exactly this kind of knowledge, and that changed what the project was. My "
          "goal is to found my own game studio, and this is a first version of the "
          "documentation I would want that studio to have. It is also why it stopped "
          "being a spreadsheet: a site can be shared, searched and eventually "
          "contributed to.\n",
          "**One row per slider, not one per tool.** I wanted a record of every "
          "function in every program, each tool, each button, each slider, so that "
          "the answer to *\"if I ever need this, how am I supposed to use it?\"* is "
          "already written down before I need it.\n"],
  "progs_t": "The programs",
  "status_t": "Status",
  "status": ["This is an ongoing project, not a finished one.\n",
             "**Blender and ZBrush are done.** **Krita is in progress.** Maya, "
             "Photoshop, Illustrator, Unity and Unreal Engine currently cover "
             "shortcuts and essentials only. 3ds Max and Marmoset Toolbag are planned "
             "but not started.\n"],
  "conv_t": "Conventions",
  "conv": ["- **Level** — Basic, Intermediate or Advanced, so you can tell everyday "
           "tools from once-a-month ones.\n"
           "- **English tool names** — buttons, palettes and menus are written exactly "
           "as they appear on screen.\n"
           "- **⭐** — entries marked as favourites.\n"
           "- **PENDIENTE** — Spanish for *pending*: something still to be confirmed "
           "against the program itself. Where it appears, it is deliberate.\n"],
 },
 "es": {
  "title": "Guía de herramientas de arte para videojuegos",
  "intro": ("Atajos, herramientas e interfaz de los programas que uso para hacer "
            "videojuegos. Empezó como una hoja de cálculo personal mientras estudiaba "
            "Diseño y Desarrollo de Videojuegos, y se ha convertido en un catálogo de "
            "**{n} entradas** en {p} programas y lenguajes de scripting.\n"),
  "note_t": "Los nombres de las herramientas van en inglés",
  "note_b": ("Cada botón, paleta y menú se escribe tal y como aparece en pantalla, en "
             "inglés, porque así es como vienen los programas. Traducirlos haría "
             "imposible encontrarlos. Las explicaciones están en español.\n"),
  "tip_t": "Cómo usarla",
  "tip_b": ("Usa el **buscador** de arriba (o pulsa <kbd>S</kbd>): busca en todos los "
            "programas a la vez, que es lo único que una hoja de cálculo no puede "
            "hacer. Si ya sabes dónde mirar, elige el programa en las pestañas. El "
            "icono del globo cambia de idioma.\n"),
  "why_t": "Por qué existe",
  "why": ["Empecé esta hoja de cálculo para mí, como apuntes de clase en la "
          "universidad. Se me quedó pequeña enseguida: lo que estaba escribiendo le "
          "iba a servir igual a mis compañeros y a la gente de mi entorno que se "
          "dedica a esto, así que seguí y lo convertí en algo que pudiera pasarle a "
          "otra persona.\n",
          "Luego descubrí que los estudios grandes tienen sus propias wikis internas "
          "para exactamente este tipo de conocimiento, y eso cambió lo que era el "
          "proyecto. Mi objetivo es fundar mi propio estudio de videojuegos, y esta es "
          "una primera versión de la documentación que querría que ese estudio "
          "tuviera. Es también por lo que dejó de ser una hoja de cálculo: una web se "
          "puede compartir, buscar y, con el tiempo, recibir aportaciones.\n",
          "**Una fila por deslizador, no una por herramienta.** Quería un registro de "
          "cada función de cada programa, cada herramienta, cada botón, cada "
          "deslizador, para que la respuesta a *\"si algún día necesito esto, ¿cómo se "
          "usa?\"* ya esté escrita antes de necesitarla.\n"],
  "progs_t": "Los programas",
  "status_t": "Estado",
  "status": ["Es un proyecto en curso, no uno terminado.\n",
             "**Blender y ZBrush están hechos.** **Krita está en proceso.** Maya, "
             "Photoshop, Illustrator, Unity y Unreal Engine cubren de momento solo "
             "atajos y lo esencial. 3ds Max y Marmoset Toolbag están planeados pero "
             "sin empezar.\n"],
  "conv_t": "Convenciones",
  "conv": ["- **Nivel** — Básico, Intermedio o Avanzado, para distinguir lo de todos "
           "los días de lo de una vez al mes.\n"
           "- **Nombres en inglés** — botones, paletas y menús, tal y como salen en "
           "pantalla.\n"
           "- **⭐** — entradas marcadas como favoritas.\n"
           "- **PENDIENTE** — algo que falta por confirmar contra el propio programa. "
           "Donde aparece, es a propósito.\n"],
 },
}


# --------------------------------------------------------------------------- main
def yaml_nav(items, indent=2):
    sp = " " * indent
    out = []
    for it in items:
        if isinstance(it, str):
            out.append(f"{sp}- {it}")
        else:
            (k, v), = it.items()
            k = k.replace('"', "'")
            if isinstance(v, str):
                out.append(f'{sp}- "{k}": {v}')
            else:
                out.append(f'{sp}- "{k}":')
                out.extend(yaml_nav(v, indent + 4))
    return out


def build_lang(wb, lang):
    """Escribe docs/<lang>/ y mkdocs-<lang>.yml. Devuelve (total, resumen)."""
    L = LANGS[lang]
    H = HOME[lang]
    base = os.path.join(DOCS, L["out"])
    if os.path.isdir(base):
        shutil.rmtree(base)
    os.makedirs(base)
    # los assets se comparten: un enlace simbólico no vale para mkdocs, se copian
    origen = os.path.join(DOCS, "assets")
    if os.path.isdir(origen):
        shutil.copytree(origen, os.path.join(base, "assets"))

    nav, summary, total = [], [], 0
    for sheet, datos in PROGRAMS.items():
        name, blurb_en, blurb_es = datos
        blurb = blurb_en if lang == "en" else blurb_es
        if sheet not in wb.sheetnames or sheet in SKIP_SHEETS:
            continue
        rows = read_sheet(wb[sheet], lang)
        if not rows:
            continue
        total += len(rows)
        folder = slug(name)
        has_palette = any(r["palette"] for r in rows)

        categories = OrderedDict()
        for r in rows:
            c = r["cat"] or ("Uncategorised" if lang == "en" else "Sin categoría")
            if L["translate_meta"]:
                c = translate_category(c)
            categories.setdefault(c, []).append(r)

        n_e = len(rows); n_c = len(categories)
        idx = [f"# {name}\n", f"{blurb}\n",
               f"**{n_e} {H and (L['ui']['entry_1'] if n_e == 1 else L['ui']['entry_n'])}** "
               f"{L['ui']['across']} {n_c} "
               f"{L['ui']['cat_1'] if n_c == 1 else L['ui']['cat_n']}.\n",
               f"\n| {L['ui']['category']} | {L['ui']['entries']} |", "|---|---:|"]
        for c, g in categories.items():
            idx.append(f"| [{c}]({slug(c)}.md) | {len(g)} |")
        write(os.path.join(base, folder, "index.md"), "\n".join(idx) + "\n")

        children = [f"{folder}/index.md"]
        nav_groups = OrderedDict()
        for c, g in categories.items():
            text = (code_page(c, g, L) if sheet in CODE_SHEETS
                    else table_page(c, g, has_palette, L))
            write(os.path.join(base, folder, f"{slug(c)}.md"), text)
            m = re.match(r"^(.{2,28}?)\s*(?:>|:)\s+(.+)$", c)
            if m:
                nav_groups.setdefault(m.group(1).strip(), []).append(
                    {m.group(2).strip(): f"{folder}/{slug(c)}.md"})
            else:
                nav_groups.setdefault(None, []).append({c: f"{folder}/{slug(c)}.md"})

        for g, items in nav_groups.items():
            if g is None:
                children.extend(items)
            elif len(items) == 1:
                children.append({f"{g} > {list(items[0])[0]}": list(items[0].values())[0]})
            else:
                children.append({g: items})
        nav.append({name: children})
        summary.append((name, len(rows), len(categories), folder, blurb))

    # --- portada
    home = [f"# {H['title']}\n",
            H["intro"].format(n=format(total, ",") if lang == "en"
                              else format(total, ",").replace(",", "."),
                              p=len(summary)),
            f'!!! note "{H["note_t"]}"\n', "    " + H["note_b"],
            f'!!! tip "{H["tip_t"]}"\n', "    " + H["tip_b"],
            f"## {H['why_t']}\n"] + H["why"] + [
            f"## {H['progs_t']}\n",
            f"\n| {L['ui']['category'].replace('Categoría','Programa').replace('Category','Program')} "
            f"| {L['ui']['entries']} | {L['ui']['categories']} | {L['ui']['covers']} |",
            "|---|---:|---:|---|"]
    for n, nr, nc, folder, blurb in summary:
        home.append(f"| [{n}]({folder}/index.md) | {nr} | {nc} | {blurb} |")
    home += [f"\n## {H['status_t']}\n"] + H["status"] + [f"## {H['conv_t']}\n"] + H["conv"]
    write(os.path.join(base, "index.md"), "\n".join(home) + "\n")

    # --- mkdocs-<lang>.yml
    desc = ("  " + H["intro"].split(".")[0].replace("**", "").strip() + ".")
    cfg = MKDOCS_TEMPLATE.format(
        site_name=H["title"], site_description=desc,
        site_url=L["url"], out=L["out"],
        site_dir="site" if lang == "en" else "site/es",
        lang=lang,
        dark="Switch to dark mode" if lang == "en" else "Cambiar a modo oscuro",
        light="Switch to light mode" if lang == "en" else "Cambiar a modo claro",
        url_en=LANGS["en"]["url"], url_es=LANGS["es"]["url"],
        nav="\n".join(yaml_nav([{L["ui"]["home"]: "index.md"}] + nav)))
    write(os.path.join(ROOT, f"mkdocs-{lang}.yml"), cfg)
    return total, summary


def main():
    if not os.path.exists(XLSX):
        sys.exit(f"Spreadsheet not found: {XLSX}")
    wb = openpyxl.load_workbook(XLSX, data_only=True)

    os.makedirs(DOCS, exist_ok=True)
    for entry in os.listdir(DOCS):
        if entry in PRESERVE:
            continue
        target = os.path.join(DOCS, entry)
        shutil.rmtree(target) if os.path.isdir(target) else os.remove(target)

    for lang in LANGS:
        total, summary = build_lang(wb, lang)
        print(f"[{lang}] {total} entradas · {len(summary)} secciones -> docs/{LANGS[lang]['out']}/")


if __name__ == "__main__":
    main()
