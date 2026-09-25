# Tool > Main Buttons


## Tool


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧰 | **Tool: el bloque de botones superior** | *Menú superior > Tool (parte superior, encima de las miniaturas)* | Basic | El bloque de botones que aparece nada más abrir la paleta Tool no toca la escultura: sirve para GESTIONAR la herramienta como archivo — cargarla, guardarla, importarla, exportarla, clonarla o mandarla a otro programa. Debajo están las miniaturas del inventario de herramientas cargadas, y más abajo empiezan ya las sub-paletas (SubTool, Geometry, Masking...) que sí modifican el modelo. |
| 🖼️ | **Tool: el inventario de herramientas (miniaturas)** | *Menú superior > Tool (cuadrícula de miniaturas, bajo los botones)* | Basic | Debajo de los botones está el inventario: todas las herramientas cargadas en la sesión, con su miniatura. Se cambia de una a otra haciendo clic. La grande de la izquierda es la activa. Siempre aparece SimpleBrush (el icono naranja de la S), que es la herramienta de pintura 2.5D heredada del ZBrush clásico y que casi nunca se usa hoy: si al pulsar en el lienzo te sale un brochazo plano en vez de tu modelo, es que tienes SimpleBrush activa por error. |
| 🎚️ | **Tool: el deslizador del nombre de la herramienta activa y el botón R** | *Menú superior > Tool (encima de las miniaturas y en el lateral)* | Basic | El deslizador de arriba muestra el nombre de la herramienta activa y su número dentro del inventario (en tu captura, 'Cylinder3D. 33'): arrastrándolo se recorre la lista sin abrir las miniaturas. Y los botones R del lateral son RESTORE CONFIGURATION, el mismo que aparece en Alpha y en Brush: devuelve la cantidad de elementos visibles a la configuración de fábrica cuando has escondido cosas sin querer. |


## Tool > Load Tool, Save As, Save, Save Next


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💾 | **Tool > guardar y cargar la herramienta (.ZTL)** | *Tool > Load Tool, Save As, Save, Save Next* | Basic | Guardan y cargan la HERRAMIENTA sola en formato .ZTL, no el proyecto entero .ZPR, que se guarda desde la paleta File. |
| 📂 | **Load Tool** | *Tool > Load Tool, Save As, Save, Save Next* | Basic | Abre un .ZTL guardado. |
| 🏷️ | **Save As** | *Tool > Load Tool, Save As, Save, Save Next* | Basic | Pide nombre y sitio. |
| 💾 | **Save** | *Tool > Load Tool, Save As, Save, Save Next* | Basic | Sobrescribe el archivo actual. |
| 🔢 | **Save Next** | *Tool > Load Tool, Save As, Save, Save Next* | Basic | El más útil de los cuatro: guarda una copia NUEVA numerando automáticamente (modelo_1, modelo_2...), así que pulsándolo cada rato te queda un historial de versiones sin pensar en nombres. Muy recomendable en esculturas largas. |


## Tool > Load Tools From Project


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📦 | **Load Tools From Project** | *Tool > Load Tools From Project* | Intermediate | Carga únicamente las herramientas que hay dentro de un archivo de proyecto (.ZPR), sin abrir el proyecto completo. Sirve para recuperar un modelo de un proyecto antiguo y meterlo en la escena en la que estás trabajando ahora, sin perder tu documento, luces ni configuración actuales. |


## Tool > Copy Tool, Paste Tool


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📋 | **Tool > copiar y pegar la herramienta** | *Tool > Copy Tool, Paste Tool* | Intermediate | Copia la herramienta activa a un portapapeles interno y la pega como una herramienta nueva del inventario. En tu captura Paste Tool aparece en gris porque todavía no se ha copiado nada: los botones de ZBrush se apagan cuando la acción no es posible en ese momento, y es una pista útil para saber qué falta hacer antes. |
| 📋 | **Copy Tool** | *Tool > Copy Tool, Paste Tool* | Intermediate | Copia la herramienta activa. |
| 📌 | **Paste Tool** | *Tool > Copy Tool, Paste Tool* | Intermediate | La pega como una herramienta nueva del inventario. |


## Tool > Import, Export


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📥 | **Tool > importar y exportar el modelo** | *Tool > Import, Export* | Intermediate | Los ajustes finos de escala y ejes están más abajo, en la sub-paleta Tool > Import/Export; conviene revisarlos porque son la causa típica de que un modelo llegue al otro programa gigantesco o tumbado. |
| 📥 | **Import** | *Tool > Import, Export* | Intermediate | Mete un modelo externo (OBJ, STL, FBX...) dentro de la herramienta activa. |
| 📤 | **Export** | *Tool > Import, Export* | Intermediate | Saca la herramienta a uno de esos formatos para llevarla a Maya, Blender, Unity o Unreal. |


## Tool > Clone


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👯 | **Clone** | *Tool > Clone* | Intermediate | Crea una copia completa e independiente de la herramienta activa como una entrada nueva del inventario. Es la red de seguridad clásica de ZBrush: antes de una operación destructiva (ZRemesher, Delete Lower, DynaMesh a resolución alta) se clona la herramienta y así queda intacta la versión anterior por si acaso. Ojo: clona la herramienta entera, no un SubTool suelto — para eso está Duplicate en la sub-paleta SubTool. |


## Tool > Make PolyMesh3D


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔄 | **Make PolyMesh3D** | *Tool > Make PolyMesh3D* | Basic | El botón MÁS IMPORTANTE de este bloque cuando empiezas. Las primitivas de ZBrush (Cylinder3D, Sphere3D, Cube3D... como el Cylinder3D de la captura) son objetos PARAMÉTRICOS: se controlan con deslizadores, pero NO se pueden esculpir ni subdividir. Make PolyMesh3D las convierte en una malla poligonal de verdad, y a partir de ahí ya responden a los pinceles. Si has intentado esculpir sobre una primitiva y no pasaba nada, es porque faltaba pulsar esto. |


## Tool > GoZ, All, Visible


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔁 | **Tool > GoZ: el puente con otros programas** | *Tool > GoZ, All, Visible* | Intermediate | GoZ manda el modelo a otro programa compatible (Maya, Blender, Photoshop, Cinema 4D...) y permite devolverlo a ZBrush con un botón, conservando la correspondencia entre los dos. |
| 🔁 | **GoZ** | *Tool > GoZ, All, Visible* | Intermediate | Manda el modelo al programa compatible configurado. |
| 🌐 | **All** | *Tool > GoZ, All, Visible* | Intermediate | Envía TODOS los SubTools. |
| 👁️ | **Visible** | *Tool > GoZ, All, Visible* | Intermediate | Envía solo los SubTools visibles en ese momento, que es lo normal cuando el modelo es pesado. |


## Tool > GoZ To iPad


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📱 | **GoZ To iPad** | *Tool > GoZ To iPad* | Intermediate | Misma idea que GoZ pero enviando el modelo a ZBrush para iPad, para seguir esculpiendo en la tableta y traerlo de vuelta. Es una función de las versiones recientes: el ciclo 2025 ha metido bastante trabajo en acercar la versión de iPad a la de escritorio. |


## Tool > Lightbox▶Tools


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💡 | **Lightbox▶Tools** | *Tool > Lightbox▶Tools* | Basic | Atajo directo que abre LightBox ya colocado en la pestaña Tools, es decir, en la biblioteca de herramientas que trae ZBrush y las que tengas guardadas. Equivale a pulsar la coma y luego ir a la pestaña Tools a mano. |


## Tool > SubTool > Visible Count


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👁️ | **SubTool > Visible Count y los botones V1-V8** | *Tool > SubTool* | Intermediate | La cabecera de la sub-paleta: el contador de SubTools visibles y la fila de botones de versión que hay justo debajo. |
| 🔢 | **Visible Count** | *Tool > SubTool* | Intermediate | Contador que indica cuántos SubTools hay visibles ahora mismo (7 en tu captura). Es un dato práctico: muchas operaciones actúan solo sobre lo visible, y varias herramientas empiezan a ir lentas a partir de cierto número de SubTools visibles a la vez. |
| 💾 | **V1 - V8** | *Tool > SubTool* | Intermediate | La fila de ocho botones de debajo. CERRADO el 06/09/2026 con tu interpretación: son VERSIONES guardadas del estado de la geometría y de los SubTools, para poder volver a una configuración anterior. Queda anotado como lectura tuya, no como dato confirmado por nota emergente. |

