# Workflows


## Tool > Geometry > DynaMesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧊 | **DynaMesh: para qué es y cuándo usarlo** | *Tool > Geometry > DynaMesh* | Intermediate | Recalcula la malla entera con densidad uniforme, uniendo lo que se solape y arreglando polígonos estirados. Es para la fase de BLOQUEO: cuando estás explorando la forma, estirando y pegando trozos, y no te importa la topología. La densidad se controla con Resolution. No conserva niveles de subdivisión ni UVs, así que se usa al principio y se abandona cuando la silueta está decidida. |


## Tool > Geometry > ZRemesher


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔷 | **ZRemesher: para qué es y cuándo usarlo** | *Tool > Geometry > ZRemesher* | Intermediate | Genera automáticamente una topología LIMPIA y ordenada (cuadrados bien repartidos) a partir de tu escultura. Es el paso siguiente a DynaMesh: cuando la forma ya te gusta pero la malla es un caos, ZRemesher la reconstruye para poder subdividir y detallar bien. Se le puede guiar con PolyGroups (Keep Groups) o dibujando curvas con el pincel ZRemesherGuides. |


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📉 | **Decimation Master: para qué es y cuándo usarlo** | *Zplugin > Decimation Master* | Intermediate | Reduce drásticamente el número de polígonos CONSERVANDO el detalle visual, pero dejando triángulos irregulares. No sirve para seguir esculpiendo ni para animar: es para EXPORTAR — llevar el modelo a otro programa, imprimirlo en 3D o mandarlo a un cliente. Resumen de los tres: DynaMesh para explorar, ZRemesher para trabajar, Decimation para entregar. |
| 🔦 | **Spotlight** | *Textura cargada + Mayús+Z (encender) / Z (editar)* | Advanced | Sistema para proyectar imágenes sobre el modelo: coloca la imagen en un disco de controles con el que se mueve, escala, ajusta contraste, etc., y luego se pinta o esculpe a través de ella. Se usa para texturizar a partir de fotos y para proyectar detalle de referencia. SON DOS TECLAS DISTINTAS, confirmado con las notas emergentes: MAYÚS+Z es 'Turn On Spotlight' y enciende o apaga la herramienta, y Z sola es 'Edit Spotlight', que entra y sale del modo de edición de la imagen. Recuerda además que Spotlight tiene su propio historial de deshacer, en la paleta Edit, separado del general. |


## Barra superior > Live Boolean + Tool > SubTool


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✂️ | **Live Boolean** | *Barra superior > Live Boolean + Tool > SubTool* | Advanced | Permite ver en tiempo real el resultado de sumar, restar e intersecar SubTools entre sí, marcando cada uno con su operación en la lista de SubTools. Se ve el resultado antes de aplicarlo, y al confirmarlo se genera la malla real. Es la forma habitual de hacer formas duras y mecánicas en ZBrush. |


## Tool > SubTool > Project All


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎯 | **Project All (proyectar detalle)** | *Tool > SubTool > Project All* | Advanced | Transfiere el detalle esculpido de un SubTool a otro. El uso típico: has remallado con ZRemesher y quieres recuperar el detalle que tenías en la versión antigua — se ponen las dos mallas como SubTools, se subdivide la nueva y se proyecta la vieja sobre ella. |


## Zplugin


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔌 | **Zplugin: los plugins que ya vienen incluidos** | *Menú superior > Zplugin* | Intermediate | ZBrush trae plugins de fábrica que son parte del flujo normal de trabajo: Decimation Master (reducir polígonos), UV Master (desplegar UVs de forma automática y sencilla), Multi Map Exporter (exportar de golpe normal, displacement y demás mapas), SubTool Master (operaciones en masa sobre muchos SubTools) y GoZ (mandar el modelo a Maya, Blender o Photoshop y traerlo de vuelta con un botón). |

