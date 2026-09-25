# Modifier: Subdivision Surface


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Levels Viewport** | *Dentro del modificador, en la pila de Modifiers* | Basic | Cuántas subdivisiones se ven (y se calculan) en el propio viewport. Súbelo solo lo necesario: afecta al rendimiento en tiempo real. |
| - | **Levels Render** | *Dentro del modificador* | Intermediate | Subdivisiones usadas solo al renderizar (F12); puedes poner más nivel aquí que en Viewport sin ralentizar el trabajo diario. |
| - | **Catmull-Clark / Simple** | *Dentro del modificador* | Intermediate | Catmull-Clark suaviza la forma al subdividir (el uso normal); Simple solo divide la geometría sin suavizarla. |
| - | **Optimal Display** | *Dentro del modificador* | Basic | Muestra en el viewport solo las aristas de la malla base (no las generadas), para ver más claro mientras editas. |
| - | **On Cage** | *Dentro del modificador* | Advanced | Te deja seleccionar y editar vértices directamente sobre la superficie ya suavizada, en vez de sobre la malla base. |
| - | **Use Creases** | *Dentro del modificador* | Intermediate | Respeta las aristas marcadas con Crease (Mayús+E) para mantener zonas "duras" sin suavizar del todo, aunque subdividas. |

