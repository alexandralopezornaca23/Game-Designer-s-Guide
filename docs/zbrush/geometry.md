# Geometry


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔺 | **Subdividir malla (Divide)** | <kbd>Ctrl</kbd> + <kbd>D</kbd> | Basic | Ctrl+D SUBDIVIDE: crea un nivel de subdivisión nuevo con cuatro veces más polígonos, y es lo mismo que el botón Divide de Tool > Geometry. CORRECCIÓN (06/09/2026, con tu permiso): esta fila decía antes que con DynaMesh activo este atajo remallaba en vez de subdividir, y eso mezclaba dos cosas distintas. El remallado de DynaMesh NO es Ctrl+D: se hace con CTRL + ARRASTRAR sobre el fondo del lienzo, y tiene su propia fila en esta misma categoría. Lo que sí es cierto es que un SubTool con DynaMesh activo no tiene niveles de subdivisión, así que ahí Ctrl+D no te dará lo que esperas: primero se desactiva DynaMesh y luego se subdivide. |
| ✂️ | **Decimation Master** | *Zplugin > Decimation Master* | Advanced | Reduce drásticamente el número de polígonos manteniendo el detalle visual (útil para exportar a Unity/Unreal). |
| 🔼 | **Higher Res / Lower Res: subir y bajar de nivel de subdivisión** | <kbd>D / Mayús</kbd> + <kbd>D</kbd> | Basic | ZBrush trabaja por NIVELES de subdivisión: el mismo modelo existe a la vez en varias densidades de malla. D sube un nivel (más polígonos, más detalle fino) y Mayús+D baja uno (menos polígonos, para cambiar la forma general). Lo esculpido en un nivel se propaga a los demás, así que se bloquea la silueta en niveles bajos y se detalla en los altos, saltando entre ellos constantemente. |
| ⌨️ | **Higher Res (subir nivel de subdivisión)** | <kbd>D</kbd> | Basic | Higher Res (subir nivel de subdivisión) |
| ⌨️ | **Lower Res (bajar nivel de subdivisión)** | <kbd>Mayús</kbd> + <kbd>D</kbd> | Basic | Lower Res (bajar nivel de subdivisión) |
| 🧊 | **DynaMesh: remallar** | *Ctrl + arrastrar sobre el fondo del lienzo* | Intermediate | Con DynaMesh activo (Tool > Geometry > DynaMesh), este gesto RECALCULA la malla entera con una densidad uniforme, uniendo trozos que se solapen y arreglando geometría estirada. Es el gesto que se repite constantemente en la fase de bloqueo. Nota: es distinto de Ctrl+D, que subdivide; conviene tenerlos separados en la cabeza. |
| ⌨️ | **DynaMesh: remallar** | *Ctrl + arrastrar sobre el fondo* | Intermediate | DynaMesh: remallar |


## Tool > Geometry > DynaMesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕸️ | **Dynamesh** | *Tool > Geometry > Dynamesh* | Intermediate | Remalla el modelo de forma uniforme; ideal en las fases iniciales de bloqueo de formas. |


## Tool > Geometry > ZRemesher


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔺 | **ZRemesher** | *Tool > Geometry > ZRemesher* | Advanced | Genera automáticamente una topología limpia en quads a partir de la escultura. |


## Tool > Geometry


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗑️ | **Tool > Geometry: borrar niveles de subdivisión** | *Tool > Geometry* | Intermediate | Se usan para aligerar el archivo o antes de remallar. OJO: no se pueden deshacer una vez guardado, así que guarda una copia antes. |
| 🔽 | **Delete Lower** | *Tool > Geometry* | Intermediate | Borra todos los niveles por DEBAJO del actual, congelando la malla actual como base. |
| 🔼 | **Delete Higher** | *Tool > Geometry* | Intermediate | Borra los niveles de ARRIBA, perdiendo el detalle fino. |


## Tool > Geometry > Reconstruct Subdiv


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ♻️ | **Reconstruct Subdiv** | *Tool > Geometry > Reconstruct Subdiv* | Advanced | Intenta reconstruir niveles de subdivisión MÁS BAJOS a partir de una malla que no los tiene. Funciona si la topología es limpia y regular (típicamente una malla que venía de un programa externo o de ZRemesher); si la topología es caótica, no podrá. |


## Tool > Geometry > Crease


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📐 | **Crease / UnCrease** | *Tool > Geometry > Crease* | Intermediate | Marca aristas como 'creased' para que se mantengan afiladas al subdividir, en vez de redondearse. Es la forma de conservar bordes duros en un modelo que por lo demás quieres suave. UnCrease quita esas marcas. |

