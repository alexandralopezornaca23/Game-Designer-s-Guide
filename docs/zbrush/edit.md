# Edit


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ↩️ | **Edit: los TRES historiales de deshacer que tiene ZBrush** | *Menú superior > Edit* | Basic | Aquí viven Deshacer y Rehacer, con sus atajos de siempre: Ctrl+Z y Mayús+Ctrl+Z. Lo que no es obvio, y esta paleta lo enseña de un vistazo, es que ZBrush lleva TRES historiales separados, uno debajo de otro: el general de arriba, el de SPOTLIGHT (los retoques de la imagen proyectada) y el de TOOL (los cambios sobre tu escultura). Cada uno se deshace por su cuenta, y eso explica un despiste típico: si estás con Spotlight abierto y pulsas Ctrl+Z esperando quitar un trazo de escultura, lo que se deshace es lo de Spotlight. Los números que aparecen al lado de cada Undo y Redo indican cuántos pasos hay guardados en ese historial; salen a 0 o en gris cuando no hay nada que deshacer. |


## Edit > Tool


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔢 | **Edit > Tool: el historial de tu escultura** | *Menú superior > Edit > Tool* | Intermediate | El historial que de verdad importa. El deslizador UndoCounter es comodísimo para volver a un punto concreto de la sesión y ver cómo iba antes de una decisión. |
| ↩️ | **Undo** | *Menú superior > Edit > Tool* | Intermediate | Deshace sobre la herramienta activa. |
| ↪️ | **Redo** | *Menú superior > Edit > Tool* | Intermediate | Rehace sobre la herramienta activa. |
| ⏱️ | **UndoCounter** | *Menú superior > Edit > Tool* | Intermediate | El deslizador del historial: en vez de ir pulsando Ctrl+Z muchas veces, se arrastra y el modelo va retrocediendo o avanzando por todos los pasos guardados, como una línea de tiempo. |
| 🧹 | **DelOlderUH** | *Menú superior > Edit > Tool* | Intermediate | Borra la parte ANTIGUA del historial (UH = Undo History). El historial ocupa mucha memoria y engorda el archivo, así que en modelos pesados conviene vaciarlo de vez en cuando; eso sí, después ya no hay vuelta atrás. |
| 🗑️ | **DelUH** | *Menú superior > Edit > Tool* | Intermediate | Borra el historial ENTERO. |
| 📍 | **Edit > Tool: la colocación de la herramienta sobre el lienzo** | *Menú superior > Edit > Tool* | Advanced | Vienen del modo 2.5D clásico, donde importaba mucho recuperar el sitio exacto en el que estaba una pieza para volver a estamparla igual. Trabajando en 3D con Edit activo apenas se usan; no confundirlos con las cámaras guardadas de la paleta Draw, que hacen algo parecido pero con el punto de vista. |
| 📍 | **Restore Placement** | *Menú superior > Edit > Tool* | Advanced | Devuelve la posición, el tamaño y la orientación guardados. |
| 💾 | **Store** | *Menú superior > Edit > Tool* | Advanced | Guarda la posición, el tamaño y la orientación actuales. |


## Edit > SpotLight


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔦 | **Edit > SpotLight: el historial propio de Spotlight** | *Menú superior > Edit > SpotLight* | Intermediate | Todo lo que hagas dentro de Spotlight — mover, girar, escalar o retocar la imagen — se deshace desde aquí y NO desde el historial general. Sale en gris en tu captura porque no tienes Spotlight activo. Es la causa habitual de que un Ctrl+Z 'no haga nada' o deshaga algo que no esperabas. |
| ↩️ | **Undo** | *Menú superior > Edit > SpotLight* | Intermediate | Deshace el último cambio hecho dentro de Spotlight. |
| ↪️ | **Redo** | *Menú superior > Edit > SpotLight* | Intermediate | Lo rehace. |

