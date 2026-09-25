# Modifier: Mesh Sequence Cache


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Open / Read Data: Vertex / Faces / UV / Color / Attributes** | *Dentro del modificador* | Intermediate | Open abre el selector de archivo para elegir la secuencia Alembic (.abc) a importar. Read Data elige qué tipos de dato se leen del archivo y se aplican a la malla: posición de Vertex, Faces (topología), UV, Color (vertex colors) y Attributes (atributos genéricos); se pueden desactivar los que no hagan falta para ahorrar rendimiento. |
| - | **Vertex Interpolation / Velocity Scale** | *Dentro del modificador* | Advanced | Vertex Interpolation (desactivado) interpola la posición de los vértices entre los frames guardados en el archivo, para una reproducción más suave si el Alembic no tiene un frame por cada fotograma de Blender. Velocity Scale (1.000, dentro de Velocity) escala el vector de velocidad guardado en el archivo, usado por ejemplo para el Motion Blur. |

