# UV Editor > Select


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖱️ | **Box Select Pinned** | *Barra superior del UV Editor > Select* | Intermediate | Igual que Box Select pero limitada a los UVs marcados como Pin (pinned): permite seleccionar por rectángulo solo entre los UVs fijados, útil para reorganizar solo esos sin tocar el resto del mapa. |
| ✂️ | **Select Split** | *Barra superior del UV Editor > Select* | Advanced | Divide la selección actual: separa en UVs independientes los vértices seleccionados que hasta ahora compartían posición con vértices no seleccionados de otras caras, útil antes de mover una parte de una isla sin arrastrar el resto. |
| ⌨️ | **Box Select Pinned** | <kbd>Alt</kbd> + <kbd>B</kbd> | Intermediate | Box Select Pinned |
| ⌨️ | **Select Split** | <kbd>Y</kbd> | Advanced | Select Split |
| 🖱️ | **Lasso Select: Set / Extend / Subtract** | *Barra superior del UV Editor > Select > Lasso Select* | Intermediate | Variante de Lasso Select ya vista en 'Viewport 3D > Select' pero aquí con solo 3 modos (sin Difference/Intersect): Set reemplaza la selección, Extend (Ctrl+arrastrar con Botón Derecho) añade a la selección, Subtract (Mayús+Ctrl+arrastrar con Botón Derecho) quita de la selección. |
| ⌨️ | **Lasso Select: Extend** | *Ctrl+arrastrar (Botón Derecho)* | Intermediate | Lasso Select: Extend |
| ⌨️ | **Lasso Select: Subtract** | *Mayús+Ctrl+arrastrar (Botón Derecho)* | Intermediate | Lasso Select: Subtract |
| 🖱️ | **Select Linked: Linked / Shortest Path** | *Barra superior del UV Editor > Select > Select Linked* | Advanced | Linked (Ctrl+L): selecciona todos los UVs conectados a la selección actual dentro de la misma isla. Shortest Path: selecciona el camino más corto de UVs conectados entre el elemento activo y el último seleccionado (normalmente con Ctrl+clic). |
| ⌨️ | **Select Linked** | <kbd>Ctrl</kbd> + <kbd>L</kbd> | Advanced | Select Linked |
| 🖱️ | **Select All by Trait: Tile / Pinned / Overlap / Winding** | *Barra superior del UV Editor > Select > Select All by Trait* | Advanced | Selecciona UVs según una característica concreta: Tile (dentro del mismo tile UDIM), Pinned (Mayús+P, los UVs fijados con Pin), Overlap (UVs que se solapan con otros), Winding (caras con el sentido de las UVs invertido/winding incorrecto, útil para detectar errores de unwrap). |
| ⌨️ | **Select All by Trait: Pinned** | <kbd>Mayús</kbd> + <kbd>P</kbd> | Advanced | Select All by Trait: Pinned |
| 🖱️ | **Select Similar: Area / Area 3D / Material / Object / Polygon Sides / Winding** | *Barra superior del UV Editor > Select > Select Similar* | Advanced | Selecciona UVs de caras con una propiedad similar a la ya seleccionada: Area (área en 2D del mapa UV), Area 3D (área real en la malla 3D), Material, Object, Polygon Sides (nº de lados del polígono), Winding (mismo sentido de bobinado UV). Todas se activan con Shift+G y luego se elige la variante en un menú contextual. |
| ⌨️ | **Select Similar** | <kbd>Shift</kbd> + <kbd>G</kbd> | Advanced | Select Similar |

