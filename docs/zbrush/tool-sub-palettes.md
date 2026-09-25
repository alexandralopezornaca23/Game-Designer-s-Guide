# Tool > Sub-palettes


## Tool


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧰 | **Tool: la paleta donde vive tu modelo** | *Menú superior > Tool* | Basic | Tool es el centro de ZBrush: contiene la herramienta activa (tu escultura) y TODAS las sub-paletas que la modifican. Es el equivalente al panel Properties de Blender, y donde vas a pasar la mayor parte del tiempo. Las sub-paletas se pliegan y despliegan haciendo clic en su nombre, y se pueden arrastrar a la bandeja lateral para tener a mano las que más uses. |
| ⚠️ | **IMPORTANTE: la paleta Tool con una PRIMITIVA activa (14 sub-paletas + Initialize)** | *Menú superior > Tool* | Basic | Confirmado con capturas de los dos estados y conviene tenerlo muy claro: la lista de sub-paletas NO es siempre la misma. Con una PRIMITIVA paramétrica activa (un Cylinder3D, una esfera...) aparecen solo 14: SubTool, Geometry muy reducida, Preview, Deformation, Masking, Visibility, Contact, Morph Target, Polypaint, UV Map, Texture Map, Display Properties, Unified Skin, Initialize y Export. Está INITIALIZE, que es donde se ajustan los parámetros de la primitiva, y NO están DynaMesh, ZRemesher ni los niveles de subdivisión, porque una primitiva no es todavía una malla editable. |
| 🔓 | **IMPORTANTE: lo que aparece al pulsar Make PolyMesh3D** | *Menú superior > Tool* | Basic | Al pulsar MAKE POLYMESH3D la primitiva se convierte en malla editable: INITIALIZE desaparece y aparecen de golpe la Geometry completa (DynaMesh, ZRemesher, SDiv, Crease, EdgeLoop, ClayPolish, ShadowBox, Dynamic Subdiv, Proxy Pose, Tessimate, Modify Topology, Stager, MeshIntegrity...), muchos bloques nuevos dentro de SubTool (Merge, Split, Boolean, Bevel Pro, Align, Distribute, Remesh, Project, Project BasRelief, Extract) y cinco sub-paletas nuevas: ArrayMesh, NanoMesh, Slime Bridge, Thick Skin y Layers. REGLA PRÁCTICA que resuelve la mitad de los apuros: si buscas una opción y no la encuentras, lo primero es comprobar si el objeto sigue siendo una primitiva. |
| 🆕 | **Sub-paletas que solo existen con PolyMesh3D (índice)** | *Menú superior > Tool* | Intermediate | Al convertir el objeto aparecen en la lista sub-paletas que con una primitiva no existen, y cada una tiene su fila propia más abajo: ArrayMesh (repetir el objeto en matrices), NanoMesh (sembrar una malla pequeña sobre cada polígono), Slime Bridge (puentes orgánicos entre superficies), Thick Skin (dar grosor), Layers (capas de escultura), FiberMesh (generar pelo y fibras) y Geometry HD (detalle a resolución altísima). |


## Tool > Geometry


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔺 | **Tool > Geometry** | *Tool > Geometry* | Basic | La sub-paleta más importante: niveles de subdivisión (Divide, SDiv, Delete Lower/Higher, Reconstruct Subdiv), DynaMesh, ZRemesher, Crease, EdgeLoop, Modify Topology, Position y Size. Todo lo que cambia la MALLA en sí está aquí. |
| 🔺 | **Tool > Geometry: contenido con una primitiva activa** | *Tool > Geometry* | Intermediate | Con una primitiva paramétrica, Geometry se queda en lo mínimo: Divide (subdividir), Smt (suavizado al subdividir, activo en naranja), Spin Edge y Align Edge (en gris), un deslizador Optimize, y Position y Size. Sirve como comparación: todo lo potente aparece solo tras Make PolyMesh3D, y está documentado en las filas 'Geometry (PolyMesh3D)' de más abajo. |
| 🔢 | **Geometry > niveles de subdivisión** | *Tool > Geometry (bloque superior)* | Basic | El bloque más importante del programa. La idea de fondo: la malla puede tener varios NIVELES de detalle guardados a la vez; bajas de nivel para corregir el volumen general y subes para detallar, y los cambios que haces abajo se propagan hacia arriba. Debajo va cada botón y deslizador del bloque. |
| ⬆️ | **Divide** | *Tool > Geometry (bloque superior)* | Basic | Subdivide la malla creando un nivel nuevo con cuatro veces más polígonos. ATAJO Ctrl+D. Es el botón con el que se pasa de la forma general al detalle fino sin perder ninguna de las dos. |
| 🎚️ | **SDiv** | *Tool > Geometry (bloque superior)* | Basic | El deslizador que indica en qué nivel de subdivisión estás y permite saltar entre ellos. Hace lo mismo que las teclas D (subir) y Mayús+D (bajar). |
| 🔽 | **Lower Res** | *Tool > Geometry (bloque superior)* | Basic | Baja un nivel de subdivisión, igual que Mayús+D o que arrastrar SDiv hacia abajo. Se usa para corregir el volumen general sin que estorbe el detalle. |
| 🔼 | **Higher Res** | *Tool > Geometry (bloque superior)* | Basic | Sube un nivel de subdivisión, igual que D. Se usa para volver al detalle después de haber retocado la forma en un nivel bajo. |
| 🗑️ | **Del Lower** | *Tool > Geometry (bloque superior)* | Intermediate | Borra todos los niveles INFERIORES al actual, dejando el modelo solo con el detalle. Sin marcha atrás: guarda antes de tocarlo, porque pierdes la posibilidad de corregir el volumen general. |
| 🗑️ | **Del Higher** | *Tool > Geometry (bloque superior)* | Intermediate | Borra todos los niveles SUPERIORES al actual, o sea el detalle. Sin marcha atrás. Se usa a propósito cuando quieres quedarte con la forma limpia y volver a detallar de cero. |
| 🧊 | **Geometry > modificadores de la subdivisión** | *Tool > Geometry (bloque superior)* | Intermediate | Los tres interruptores que deciden CÓMO se subdivide: si la forma se suaviza o se mantiene angulosa, y qué pasa con las UV al hacerlo. |
| 🫧 | **Smt** | *Tool > Geometry (bloque superior)* | Intermediate | Decide si al subdividir se SUAVIZA la forma o se mantiene angulosa (activo en naranja en tu captura). Desactivarlo antes de dividir es el truco para conservar bordes duros en una pieza mecánica. |
| 🗺️ | **Suv** | *Tool > Geometry (bloque superior)* | Advanced | Conserva las UV al subdividir, para no perder el desplegado que ya tenías hecho. |
| ♻️ | **ReUV** | *Tool > Geometry (bloque superior)* | Advanced | Rehace las UV al subdividir, para que el desplegado siga cuadrando con la malla nueva. |
| ❄️ | **Geometry > gestión avanzada de niveles** | *Tool > Geometry (bloque superior)* | Advanced | Las herramientas para salvar, reconstruir o convertir los niveles de subdivisión cuando una operación normalmente los destruiría. |
| ❄️ | **Freeze SubDivision Levels** | *Tool > Geometry (bloque superior)* | Advanced | Congela los niveles altos mientras trabajas en los bajos, lo que permite usar operaciones que normalmente los destruirían (como un ZRemesher) y luego recuperar el detalle intacto. |
| 🏗️ | **Reconstruct Subdiv** | *Tool > Geometry (bloque superior)* | Advanced | Intenta reconstruir niveles más BAJOS que no existían, deduciéndolos de la malla actual. Útil en mallas importadas de fuera, que llegan con un solo nivel. |
| 📦 | **Cage** | *Tool > Geometry (bloque superior)* | Advanced | Opción de la jaula de subdivisión: la malla de control de baja resolución que envuelve la forma suave. |
| 🔄 | **Rstr** | *Tool > Geometry (bloque superior)* | Advanced | La otra opción de la jaula de subdivisión, que restaura su estado. |
| 🧱 | **Convert BPR To Geo** | *Tool > Geometry (bloque superior)* | Advanced | Convierte en geometría REAL lo que hasta ese momento solo era una previsualización del render BPR, por ejemplo el resultado de Dynamic Subdiv o de un FiberMesh en modo preview. |
| 📋 | **Geometry: los 6 bloques del final (índice)** | *Tool > Geometry (parte inferior)* | Intermediate | Cierran la sub-paleta Geometry y cada uno tiene su fila propia a continuación: Modify Topology (operaciones de topología), Repeat To Similar Parts (repetir un cambio en piezas parecidas), Stager (guardar estados del modelo), Position y Size (colocar y dimensionar con deslizadores numéricos) y MeshIntegrity (comprobar y arreglar errores de malla). |


## Tool > SubTool


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📚 | **Tool > SubTool** | *Tool > SubTool* | Basic | La lista de SubTools: cada objeto independiente de tu escena (cabeza, ojos, ropa...) es un SubTool dentro de la misma herramienta. Permite añadir, duplicar, borrar, fusionar (Merge), dividir (Split), reordenar y ocultar. También están Extract (crear geometría nueva a partir de una máscara), Project All y las operaciones booleanas de Live Boolean. |
| 📚 | **Tool > SubTool: la lista y sus controles de arriba** | *Tool > SubTool (parte superior)* | Basic | Cada objeto independiente de la escena es un SubTool dentro de la misma herramienta (cabeza, ojos, ropa...) y aquí está la lista, con miniatura y nombre de cada uno (en tu captura solo 'Cylinder3D_1'). Arriba, Visible Count indica cuántos hay visibles. A la derecha de cada SubTool hay una fila de iconos pequeños para activar/desactivar cosas por SubTool, siendo el ojo el de visibilidad. Debajo de la lista están las flechas para mover el SubTool seleccionado arriba y abajo en el orden. CERRADO (06/09/2026): los botones V1 a V8 son, según tu interpretación, versiones guardadas del estado de la geometría y los SubTools (ver la fila de Visible Count). Los iconos pequeños de cada fila de SubTool quedan como están: el ojo es visibilidad y el resto se identifican por su posición. |
| 🗂️ | **SubTool > organizar la lista** | *Tool > SubTool* | Intermediate | Los cuatro botones que sirven para tener la lista de SubTools ordenada y con nombres que se entiendan. En un personaje con muchas piezas, esto es la diferencia entre encontrar algo y perder el rato. |
| 📋 | **List All** | *Tool > SubTool* | Intermediate | Despliega la lista completa de SubTools, cómodo cuando hay muchos y la ventana se queda corta. |
| 📁 | **New Folder** | *Tool > SubTool* | Intermediate | Crea una carpeta para agrupar SubTools. Es la forma moderna de organizar personajes con muchas piezas, y además permite operar sobre la carpeta entera de una vez. |
| ✏️ | **Rename** | *Tool > SubTool* | Basic | Cambia el nombre del SubTool activo. Merece la pena nombrarlos bien desde el principio: 'Cylinder3D_14' no te dice nada dentro de seis meses. |
| 🔀 | **AutoReorder** | *Tool > SubTool* | Intermediate | Reordena la lista automáticamente. Aparece en gris cuando no hay suficientes SubTools para que tenga sentido. |
| 🔽 | **SubTool > operaciones sobre todos a la vez** | *Tool > SubTool* | Intermediate | Cuatro botones que actúan sobre TODOS los SubTools de golpe. El primero es uno de los trucos de rendimiento más importantes del programa. |
| 🔽 | **All Low** | *Tool > SubTool* | Intermediate | Pone TODOS los SubTools en su nivel de subdivisión más bajo. Truco de rendimiento importantísimo: antes de guardar, de girar la cámara en una escena pesada o de hacer operaciones globales, se bajan todos y el programa vuela. |
| 🔼 | **All High** | *Tool > SubTool* | Intermediate | Pone todos los SubTools en su nivel de subdivisión más alto, para volver al detalle. |
| 🏠 | **All To Home** | *Tool > SubTool* | Intermediate | Mueve todos los SubTools a la posición de origen. |
| 🎯 | **All To Target** | *Tool > SubTool* | Intermediate | Mueve todos los SubTools a la posición del objetivo. |
| ➕ | **SubTool > añadir, copiar y borrar** | *Tool > SubTool* | Basic | El bloque del día a día: meter piezas nuevas en la escena, duplicarlas y quitarlas. Los que salen en gris es porque con un solo SubTool no tienen sentido. Ojo con los tres de borrar: no tienen marcha atrás. |
| ⧉ | **Duplicate** | *Tool > SubTool* | Basic | Copia el SubTool activo dejándolo justo encima en la lista. Es el gesto más habitual antes de probar algo arriesgado: duplicas, pruebas, y si sale mal borras la copia. |
| 📎 | **Append** | *Tool > SubTool* | Basic | Añade una herramienta nueva como SubTool al FINAL de la lista. Así se meten ojos, dientes o una esfera para empezar otra pieza. |
| 📌 | **Insert** | *Tool > SubTool* | Basic | Añade una herramienta como SubTool justo DEBAJO del activo, en vez de al final. |
| 📋 | **Copy** | *Tool > SubTool* | Intermediate | Copia el SubTool activo al portapapeles, para poder llevarlo a otra herramienta distinta. |
| 📥 | **Paste** | *Tool > SubTool* | Intermediate | Pega el SubTool copiado dentro de la herramienta actual. |
| 🗑️ | **Delete** | *Tool > SubTool* | Basic | Borra el SubTool activo. Sin marcha atrás. |
| 🗑️ | **Del Other** | *Tool > SubTool* | Intermediate | Borra todos los SubTools MENOS el activo. Sin marcha atrás. |
| 🗑️ | **Del All** | *Tool > SubTool* | Intermediate | Borra TODOS los SubTools. Sin marcha atrás, y es fácil pulsarlo por error al lado de Delete. |
| 🔁 | **SubTool > Apply Last Action To All Subtools** | *Tool > SubTool* | Advanced | Repite la última acción que hiciste sobre TODOS los SubTools de golpe, en vez de ir uno a uno. Ahorra muchísimo tiempo en modelos con muchas piezas (por ejemplo aplicar la misma deformación o el mismo nivel de subdivisión a todo). En tu captura está en gris porque solo hay un SubTool. |
| 🧩 | **Tool > SubTool: el bloque inferior de operaciones** | *Tool > SubTool (bloque inferior)* | Advanced | Las operaciones del final de la sub-paleta SubTool. Extract tiene además su propia fila detallada más arriba, con Paleta 'Tool > SubTool > Extract'. |


## Tool > Masking


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🛡️ | **Tool > Masking** | *Tool > Masking* | Intermediate | Sub-paleta con todo lo relacionado con máscaras que no es pintarlas a mano con Ctrl: verlas, invertirlas, borrarlas, generarlas a partir del color o de un alpha, y convertirlas en otras cosas. El contenido exacto botón a botón está en la fila 'Tool > Masking: contenido real de la sub-paleta', tomada de tu captura. |
| 🛡️ | **Tool > Masking: versión REDUCIDA (con una primitiva activa)** | *Tool > Masking* | Intermediate | Con una PRIMITIVA paramétrica, Masking se queda en lo básico: ViewMask (muestra/oculta la máscara sin borrarla), Inverse, Clear, MaskAll, Create Alpha (convierte la máscara en un alpha reutilizable), Go To Unmasked Center, Mask By Color, Mask By Alpha y Apply. Al convertir a PolyMesh3D la sub-paleta se multiplica: ver las filas 'Masking (PolyMesh3D)' de más abajo, que es la versión completa y la que vas a usar de verdad. |
| 🛡️ | **Masking > los controles básicos de la máscara** | *Tool > Masking* | Intermediate | Los controles de siempre, ya con malla real: ver la máscara, invertirla, borrarla, y ajustar tanto su EXTENSIÓN (hasta dónde llega) como su FUERZA (cuánto protege). Esa distinción es la que más confunde al principio. |
| 👁️ | **ViewMask** | *Tool > Masking* | Intermediate | Muestra u oculta la máscara sin borrarla, para ver la escultura limpia sin perder el trabajo hecho. |
| 🔄 | **Inverse** | *Tool > Masking* | Basic | Invierte la máscara: lo protegido pasa a estar libre y al revés. |
| 🧹 | **Clear** | *Tool > Masking* | Basic | Borra la máscara por completo. |
| 🛡️ | **MaskAll** | *Tool > Masking* | Basic | Enmascara el modelo entero de golpe. |
| 🫧 | **BlurMask** | *Tool > Masking* | Intermediate | Difumina los bordes de la máscara. Es lo mismo que Ctrl+clic sobre el modelo, pero por botón y con control exacto de cuántas veces se aplica. |
| 🔪 | **SharpenMask** | *Tool > Masking* | Intermediate | Endurece los bordes de la máscara, lo mismo que Ctrl+Alt+clic sobre el modelo. |
| ➕ | **GrowMask** | *Tool > Masking* | Intermediate | Agranda la zona enmascarada un poco cada vez que se pulsa. |
| ➖ | **ShrinkMask** | *Tool > Masking* | Intermediate | Encoge la zona enmascarada un poco cada vez que se pulsa. |
| ⏫ | **Grow All** | *Tool > Masking* | Intermediate | Agranda la zona enmascarada de golpe, sin ir poco a poco. |
| ⏬ | **Shrink All** | *Tool > Masking* | Intermediate | Encoge la zona enmascarada de golpe. |
| 💪 | **BoostMask** | *Tool > Masking* | Intermediate | Intensifica la máscara: la hace más opaca, o sea que protege más. Ajusta la FUERZA, no la extensión. |
| 💧 | **DiluteMask** | *Tool > Masking* | Intermediate | Suaviza la máscara: la hace más transparente, de modo que deja pasar parte del pincel. También es fuerza, no extensión. |
| 🔄 | **Masking > funciones especiales** | *Tool > Masking* | Intermediate | Cuatro funciones que no generan la máscara por criterio geométrico, sino a partir del trabajo que ya has hecho o de la simetría del modelo. |
| 🆕 | **Mask Changed Points** | *Tool > Masking* | Intermediate | Enmascara automáticamente todo lo que has modificado desde el último Morph Target. Es una forma muy directa de aislar el trabajo reciente sin pintar nada. |
| 🪞 | **Flip By Posable Symmetry** | *Tool > Masking* | Advanced | Voltea la máscara usando la simetría POSABLE, o sea la que sigue funcionando aunque el modelo esté posado y ya no sea simétrico en el espacio. |
| 🪞 | **Mirror By Posable Symmetry** | *Tool > Masking* | Advanced | Refleja la máscara al otro lado con esa misma simetría posable. Es lo que salva la papeleta cuando la simetría normal ha dejado de funcionar por la pose. |
| 🏷️ | **Create Alpha** | *Tool > Masking* | Intermediate | Convierte la máscara en un alpha reutilizable como pincel o como textura. Es el camino para convertir algo que has enmascarado en un sello que puedas estampar donde quieras. |
| 🎯 | **Go To Unmasked Center** | *Tool > Masking* | Intermediate | Lleva la vista al centro de lo NO enmascarado, cómodo para saltar directamente a la zona en la que vas a trabajar. |
| 🧩 | **Masking > MaskByFeature y MaskByDraft** | *Tool > Masking* | Advanced | Dos generadores de máscara a partir de la ESTRUCTURA del modelo: uno mira los elementos de la malla (bordes, grupos, aristas duras) y el otro el ángulo de desmoldeo. |
| 🧩 | **MaskByFeature** | *Tool > Masking* | Advanced | Enmascara automáticamente según elementos estructurales del modelo. Los tres botones de debajo eligen cuáles (los tres activos en naranja en tu captura). Es la forma rápida de proteger o aislar justo las zonas de transición sin pintar nada a mano. |
| ➖ | **Border** | *Tool > Masking* | Advanced | Toma como criterio los BORDES ABIERTOS de la malla. |
| 🎨 | **Groups** | *Tool > Masking* | Advanced | Toma como criterio los límites entre PolyGroups. |
| 📏 | **Crease** | *Tool > Masking* | Advanced | Toma como criterio las aristas marcadas como duras en la sub-paleta Crease. |
| 📐 | **MaskByDraft** | *Tool > Masking* | Advanced | Enmascara según el ÁNGULO DE DESMOLDEO respecto a una dirección. Se usa sobre todo pensando en impresión 3D y en moldes, para detectar las zonas que quedarían en contrasalida. |
| 📐 | **DraftAngle** | *Tool > Masking* | Advanced | El ángulo de desmoldeo que se toma como límite (2 en tu captura). |
| 🧭 | **SetDir** | *Tool > Masking* | Advanced | Fija la dirección de desmoldeo tomando la vista actual de la cámara. |
| 🔃 | **InvDir** | *Tool > Masking* | Advanced | Invierte esa dirección, para mirar el molde por el otro lado. |
| 🎯 | **Masking > Mask Region y Mask Adjust** | *Tool > Masking* | Advanced | Dos bloques que van seguidos: el primero reconoce regiones del modelo por su forma, y el segundo retoca una máscara que ya existe. |
| 🔍 | **Analyze Region** | *Tool > Masking* | Advanced | Estudia la geometría buscando zonas diferenciadas dentro del modelo. |
| 🤖 | **Auto Region** | *Tool > Masking* | Advanced | Enmascara automáticamente esas regiones reconocidas. Ahorra trabajo en modelos con partes bien definidas. |
| 🪣 | **Fill Region** | *Tool > Masking* | Advanced | Rellena por completo la región que elijas. |
| ✅ | **Apply** | *Tool > Masking* | Advanced | Aplica el ajuste a la máscara existente. |
| 🫧 | **Blur** | *Tool > Masking* | Advanced | El difuminado con el que se aplica ese ajuste (2 en tu captura). |
| 📈 | **Mask Adjust Profile** | *Tool > Masking* | Advanced | Curva editable con la que se controla con precisión cómo CAE el borde de la máscara. Más útil de lo que parece: ese borde decide si una deformación queda con escalón o con transición suave. |
| 💡 | **Masking > Mask By AO y Mask By Cavity** | *Tool > Masking* | Advanced | Las dos máscaras que se generan a partir de la FORMA de la superficie, y son de lo más útil para texturizar: una detecta los recovecos donde no llega la luz y la otra las grietas esculpidas. |
| 📐 | **Masking > máscaras por criterio geométrico** | *Tool > Masking* | Advanced | Cinco generadores más de máscara automática, cada uno con un criterio geométrico distinto. Cada bloque tiene su propio valor en la columna Paleta, porque varios repiten nombres de deslizador entre sí. |
| 🎨 | **Masking > Mask By Color, Mask By Alpha y Apply** | *Tool > Masking* | Advanced | El último bloque: generar la máscara a partir de algo que ya has pintado, o a partir de un alpha o una textura. Convertir lo pintado en máscara es lo que permite esculpir exactamente sobre lo pintado. |


## Tool > Polygroups


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎨 | **Tool > Polygroups** | *Tool > Polygroups* | Intermediate | Los PolyGroups son grupos de polígonos con un color asignado, y son la forma de organizar un modelo por partes (visibles con Mayús+F). Se generan desde máscaras, por ángulo (Auto Groups), por UVs o por trozos sueltos. Sirven para aislar zonas al instante, controlar ZRemesher y trabajar con ZModeler. |
| 🟩 | **Polygroups > los generadores automáticos** | *Tool > Polygroups* | Intermediate | La versión COMPLETA de la sub-paleta, la que aparece con un PolyMesh3D (con una primitiva casi todo sale en gris). Este primer bloque crea los grupos solo, sin que tengas que enmascarar ni ocultar nada. |
| 🤖 | **Auto Groups** | *Tool > Polygroups* | Intermediate | Crea PolyGroups automáticamente separando las partes SUELTAS de la malla: si tu modelo son tres trozos independientes, salen tres grupos de tres colores. |
| 🗺️ | **Uv Groups** | *Tool > Polygroups* | Advanced | Crea los grupos a partir de las islas de UV del desplegado. |
| 🔗 | **Auto Groups With UV** | *Tool > Polygroups* | Advanced | Combina las dos cosas: partes sueltas e islas de UV. |
| 🧲 | **Merge Similar Groups** | *Tool > Polygroups* | Intermediate | Fusiona en uno solo los grupos que se parecen entre sí. |
| 🧹 | **Merge Stray Groups** | *Tool > Polygroups* | Intermediate | Se come los grupos diminutos y sueltos que quedan tras una operación automática. Es el botón de limpieza cuando un Auto Groups ha salido demasiado troceado. |
| 📐 | **Polygroups > generadores por geometría** | *Tool > Polygroups* | Advanced | Los dos generadores que se basan en la forma de la malla: uno mira las aristas y el otro hacia dónde miran las caras. |
| ➖ | **Regroup By Edges** | *Tool > Polygroups* | Advanced | Rehace los grupos siguiendo las aristas de la malla. |
| 🎚️ | **Edge Sensitivity** | *Tool > Polygroups* | Advanced | Cuánto de marcada tiene que estar una arista para que cuente como corte. En pantalla aparece abreviado como EDGE SENS. |
| 🧭 | **Groups By Normals** | *Tool > Polygroups* | Advanced | Crea grupos según la ORIENTACIÓN de las caras. Es la forma rápida de separar las caras planas de una pieza de modelado duro: un cubo biselado queda dividido en sus seis caras de un clic. |
| 📐 | **Maximum Angle Tolerance** | *Tool > Polygroups* | Advanced | A partir de cuántos grados se considera que ya es otra cara. En pantalla aparece abreviado como MAXANGLE. |
| 👁️ | **Polygroups > agrupar lo visible** | *Tool > Polygroups* | Advanced | El método manual más usado de todos: ocultas lo que no te interesa y conviertes lo que queda en un grupo. Se combina con Ctrl+Mayús+arrastrar para ocultar y Ctrl+Mayús+clic en el fondo para volver a mostrar todo. |
| 👁️ | **GroupVisible** | *Tool > Polygroups* | Intermediate | Convierte TODO lo que esté visible en un único PolyGroup nuevo. Es el gesto que vas a repetir mil veces: ocultas todo menos la manga, pulsas GroupVisible, y ya tienes la manga como grupo propio. |
| 📏 | **Coverage** | *Tool > Polygroups* | Advanced | El otro deslizador del par, que regula cuánto abarca la operación. De este no capturaste la nota emergente, así que el matiz exacto queda sin confirmar. |
| 🧩 | **Regroup Clusters** | *Tool > Polygroups* | Advanced | Rehace los grupos por racimos de polígonos conectados. En pantalla aparece abreviado como CLSTR. |
| ♻️ | **ReGroupVisible** | *Tool > Polygroups* | Advanced | Rehace el grupo de lo visible respetando los grupos que ya existían. |
| 🎯 | **Polygroups > Group Front** | *Tool > Polygroups* | Intermediate | Agrupa por lo que está de cara a la cámara, así que basta con girar el modelo hasta encuadrar la zona que quieres y pulsar. |
| 🎯 | **Group Front** | *Tool > Polygroups* | Intermediate | Agrupa todo lo que está de cara a la cámara en ese momento. |
| 📐 | **Angle** | *Tool > Polygroups* | Intermediate | Hasta qué inclinación cuenta como 'de frente': con un ángulo pequeño solo coge lo que mira justo a cámara, con uno grande coge también los laterales. |
| ➕ | **Group Front Additive Grouping** | *Tool > Polygroups* | Intermediate | Suma el grupo nuevo al que ya había en vez de reemplazarlo, lo que permite ir construyendo un grupo en varias pasadas desde ángulos distintos. En pantalla aparece como ADDITIVE. |
| 🎭 | **Polygroups > agrupar por máscara** | *Tool > Polygroups* | Intermediate | El atajo mental es sencillo: si sabes enmascarar, ya sabes hacer PolyGroups. |
| 🎭 | **Group Masked** | *Tool > Polygroups* | Intermediate | Convierte lo ENMASCARADO en un PolyGroup. |
| ✨ | **Polish Grouped Polygons** | *Tool > Polygroups* | Intermediate | Pule los polígonos del grupo recién creado para que el borde entre grupos no quede con dientes de sierra. En pantalla aparece cortado como 'PolishG...'. |
| 🧹 | **Group Masked Clear Mask** | *Tool > Polygroups* | Intermediate | Hace lo mismo que Group Masked y además borra la máscara, que es lo que casi siempre quieres. Usa este y te ahorras un paso. |
| 🕳️ | **Group As Dynamesh Sub** | *Tool > Polygroups* | Advanced | Marca el grupo como SUSTRACCIÓN para DynaMesh: al remallar resta en vez de sumar y abre un hueco. Así se perforan agujeros limpios. |
| 🖌️ | **Polygroups > agrupar por color, máscara o cambios** | *Tool > Polygroups* | Advanced | Tres generadores más, y los dos primeros comparten un detalle que conviene tener claro: en sus deslizadores de tolerancia, NÚMERO MÁS GRANDE = MÁS GRUPOS. |
| 🎨 | **From Polypaint** | *Tool > Polygroups* | Advanced | Crea un PolyGroup por cada color pintado sobre el modelo. Es una forma muy cómoda de 'dibujar' los grupos: pintas las zonas con colores planos y las conviertes de golpe. |
| 🎚️ | **PTolerance** | *Tool > Polygroups* | Advanced | Es 'GROUP FROM POLYPAINT TOLERANCE', y su nota emergente añade el dato que importa: número más grande, más grupos. Subiéndolo el programa se vuelve más quisquilloso y separa colores parecidos en grupos distintos; bajándolo, los mete todos juntos. |
| 🎭 | **From Masking** | *Tool > Polygroups* | Advanced | Crea los grupos a partir de la máscara en vez de del color. |
| 🎚️ | **MTolerance** | *Tool > Polygroups* | Advanced | Es 'GROUP FROM MASKING TOLERANCE' y funciona igual que PTolerance: más número, más grupos. |
| 🆕 | **Groups Changed Points** | *Tool > Polygroups* | Advanced | Agrupa los puntos que han cambiado respecto al Morph Target guardado, o sea exactamente la zona que has tocado desde que lo guardaste. |


## Tool > Deformation


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔧 | **Tool > Deformation** | *Tool > Deformation* | Intermediate | Deformaciones aplicadas a todo el SubTool (o a lo no enmascarado): Inflate, Smooth, Taper, Twist, Bend, Flatten, Spherize, Offset, Rotate, Size... Cada una con un deslizador por eje. Es la manera de hacer cambios globales controlados sin tocar el pincel, y respeta las máscaras. |
| 🔧 | **Tool > Deformation: cómo funciona y los ejes XYZ** | *Tool > Deformation* | Intermediate | Deformaciones que se aplican a TODO el SubTool de golpe (o solo a lo no enmascarado, porque respetan la máscara). Cada fila es un deslizador que se arrastra desde el centro hacia un lado u otro, y a la derecha tiene las letras X Y Z: pulsándolas se elige sobre qué ejes actúa, y ese detalle cambia por completo el resultado. El deslizador vuelve solo al centro tras aplicarse, así que se puede repetir el gesto varias veces para acumular efecto. Es la forma de hacer cambios globales controlados sin tocar un pincel. |
| ✨ | **Deformation > el grupo de pulido** | *Tool > Deformation* | Intermediate | Los cuatro botones de PULIDO, para dar acabado a la superficie. La diferencia entre usar Polish a secas y usar una de las variantes es la que separa una pieza mecánica creíble de una que parece de plastilina. |
| ✨ | **Polish** | *Tool > Deformation* | Intermediate | Suaviza y aplana dando un acabado pulido, tipo metal o cerámica. Aplicado sin más, redondea también las aristas que querías marcadas. |
| 🔷 | **Polish By Features** | *Tool > Deformation* | Intermediate | Pule respetando los bordes de las FORMAS: alisa la cara plana de una pieza sin comerse sus aristas. |
| 🎨 | **Polish By Groups** | *Tool > Deformation* | Intermediate | Pule respetando los bordes de los POLYGROUPS. Es la variante clave en modelado duro, porque los grupos marcan dónde acaba cada placa. |
| 🔪 | **Polish Crisp Edges** | *Tool > Deformation* | Intermediate | Pule la superficie manteniendo los filos afilados. |
| 📐 | **Deformation > ordenar la malla y recuperar la simetría** | *Tool > Deformation* | Intermediate | El grupo de poner orden: repartir los polígonos de forma uniforme y devolver la simetría a un modelo que se ha ido deformando por un lado. |
| 🧘 | **Relax** | *Tool > Deformation* | Intermediate | Reparte los polígonos de forma más uniforme SIN cambiar la silueta. Ideal para arreglar una malla estirada por haber movido mucho una zona. |
| ▦ | **Relax Plane Grid** | *Tool > Deformation* | Advanced | Lleva la malla hacia una rejilla plana y regular. |
| ▦ | **Morph to Grid** | *Tool > Deformation* | Advanced | Transforma la malla hasta encajarla en una rejilla. |
| 📏 | **Unify** | *Tool > Deformation* | Intermediate | Normaliza el tamaño y la posición de la herramienta, dejándola centrada y a escala estándar. |
| 🪞 | **Mirror** | *Tool > Deformation* | Intermediate | Refleja la herramienta entera en el eje elegido. |
| 🔁 | **ReSym** | *Tool > Deformation* | Intermediate | Vuelve a hacer simétrico un modelo que se ha deformado a un lado. |
| 🧠 | **Smart ReSym** | *Tool > Deformation* | Intermediate | Recupera la simetría RESPETANDO el detalle ya esculpido en vez de aplastarlo. Cuando ya hay trabajo fino encima, usa siempre esta y no ReSym. |
| 📐 | **Deformation > las transformaciones geométricas** | *Tool > Deformation* | Intermediate | El bloque de deformaciones de forma. Combinadas sobre una primitiva sacan formas complejas muy rápido y sin esculpir nada. Recuerda que cada deslizador vuelve solo al centro tras aplicarse, así que puedes repetir el gesto para acumular efecto. |
| ↔️ | **Offset** | *Tool > Deformation* | Intermediate | Desplaza la malla en el eje elegido. |
| 🔄 | **Rotate** | *Tool > Deformation* | Intermediate | Gira la malla sobre el eje elegido. |
| 🔍 | **Size** | *Tool > Deformation* | Intermediate | Escala la malla en el eje elegido. |
| 🪝 | **Bend** | *Tool > Deformation* | Intermediate | Dobla el objeto sobre un eje, como doblar un tubo. |
| 〰️ | **SBend** | *Tool > Deformation* | Intermediate | Dobla el objeto en forma de S, con dos curvas opuestas. |
| 📐 | **Skew** | *Tool > Deformation* | Intermediate | Inclina el objeto, desplazando un extremo respecto al otro. |
| 📐 | **SSkew** | *Tool > Deformation* | Intermediate | Inclina el objeto en S, con la inclinación cambiando de sentido a mitad. |
| 🌀 | **Twist** | *Tool > Deformation* | Intermediate | Retuerce el objeto sobre un eje. Perfecto para cuernos, conchas y columnas salomónicas. |
| 🔻 | **Taper** | *Tool > Deformation* | Intermediate | Estrecha el objeto hacia uno de sus extremos. |
| 🤏 | **Squeeze** | *Tool > Deformation* | Intermediate | Aplasta el objeto por el centro o por los extremos. |
| ▬ | **Flatten** | *Tool > Deformation* | Intermediate | Aplana la malla contra un plano. |
| ▬ | **RFlatten** | *Tool > Deformation* | Intermediate | Variante radial del aplanado. |
| ▬ | **SFlatten** | *Tool > Deformation* | Intermediate | Variante suave del aplanado. |
| 🌊 | **Deformation > superficie y volumen** | *Tool > Deformation* | Intermediate | Deformaciones que actúan sobre el acabado de la superficie o sobre el volumen general, en vez de sobre la forma geométrica. |
| 🌾 | **Noise** | *Tool > Deformation* | Intermediate | Añade ruido a la superficie para romper lo perfecto: piedra, piel, metal picado. Un poco de esto quita el aspecto de render de escuela. |
| 🫧 | **Smooth** | *Tool > Deformation* | Intermediate | Suaviza todo el SubTool de una vez, sin tener que pasar el pincel. |
| 🌗 | **Contrast** | *Tool > Deformation* | Intermediate | Exagera las diferencias de relieve, haciendo el detalle más marcado. |
| 🎈 | **Inflate** | *Tool > Deformation* | Intermediate | Hincha la malla siguiendo sus normales, engordándola de forma uniforme. |
| 🎈 | **Inflate Balloon** | *Tool > Deformation* | Intermediate | La hincha como un globo, redondeándola hacia una forma más esférica en vez de seguir las normales. |
| ⚪ | **Spherize** | *Tool > Deformation* | Intermediate | Acerca la forma a una esfera. |
| 🌍 | **Gravity** | *Tool > Deformation* | Intermediate | Deja caer la malla hacia abajo. Muy útil para dar peso realista a telas y carnes sin simular nada. |
| 👁️ | **Perspective** | *Tool > Deformation* | Advanced | Aplica una deformación de perspectiva a la malla. |
| 🔂 | **Deformation > repetir en otros SubTools** | *Tool > Deformation (parte inferior)* | Advanced | Repiten la última deformación aplicada sobre otros SubTools, en vez de tener que repetirla a mano. En tu captura salen en gris porque solo hay un SubTool y aún no habías aplicado ninguna deformación. |
| 🎯 | **Repeat To Active** | *Tool > Deformation (parte inferior)* | Advanced | Repite la última deformación sobre el SubTool activo. |
| 🧩 | **Repeat To Other** | *Tool > Deformation (parte inferior)* | Advanced | Repite la última deformación sobre los DEMÁS SubTools. |
| 📁 | **Repeat To Folder** | *Tool > Deformation (parte inferior)* | Advanced | Repite la última deformación sobre todos los SubTools de una carpeta. |
| 🛡️ | **Mask** | *Tool > Deformation (parte inferior)* | Advanced | Decide si esa repetición respeta las máscaras de cada SubTool. |


## Tool > Layers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📄 | **Tool > Layers** | *Tool > Layers* | Intermediate | Capas de escultura: permiten esculpir sobre una capa y luego subir o bajar su intensidad, o desactivarla, sin perder lo de debajo. Imprescindible para detalles reversibles (arrugas, poros, expresiones faciales) y la base de las blend shapes para animación. |
| 📄 | **Tool > Layers: la lista y sus botones** | *Tool > Layers* | Intermediate | Las CAPAS DE ESCULTURA, una de las funciones más útiles del programa: cada capa guarda un conjunto de cambios por separado, con un deslizador de intensidad que va de 0 a 1 (e incluso a valores negativos para invertir el efecto). Así puedes esculpir las arrugas en una capa, los poros en otra, y luego subir, bajar o apagar cada una sin perder nada. Es también la base de las blend shapes para animación facial. |
| ✏️ | **Name** | *Tool > Layers* | Intermediate | Pone nombre a la capa seleccionada. |
| 🔥 | **Bake All** | *Tool > Layers* | Intermediate | Fusiona todas las capas en la malla de forma DEFINITIVA. A partir de ahí ya no se pueden regular por separado. |
| 📥 | **Import MDD** | *Tool > Layers* | Advanced | Carga una animación externa en formato MDD. |
| ⏩ | **MDD Speed** | *Tool > Layers* | Advanced | La velocidad de reproducción de esa animación importada. |
| ⏺️ | **Record Deformation Animation** | *Tool > Layers* | Advanced | Graba la deformación del modelo como animación. |


## Tool > Morph Target


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👥 | **Tool > Morph Target** | *Tool > Morph Target* | Advanced | Guarda un estado del modelo (StoreMT) al que puedes volver total o parcialmente. Combinado con el pincel Morph permite 'repintar' hacia el estado guardado solo en la zona que pintes: la mejor forma de deshacer un detalle concreto sin perder el resto. |
| 👥 | **Tool > Morph Target: los controles** | *Tool > Morph Target* | Advanced | Guarda un estado del modelo al que puedes volver total o parcialmente. Combinado con el pincel Morph permite 'deshacer' pintando solo en una zona concreta, que es la mejor forma de quitar un detalle sin perder el resto. Casi todo sale en gris hasta que hay un estado guardado. |
| 💾 | **StoreMT** | *Tool > Morph Target* | Advanced | Guarda el estado actual del modelo como objetivo de morph. Es lo único disponible hasta que hay uno guardado. |
| 🔄 | **Switch** | *Tool > Morph Target* | Advanced | Intercambia el modelo actual con el guardado. |
| 🗑️ | **DelMT** | *Tool > Morph Target* | Advanced | Borra el estado guardado. |
| ➖ | **CreateDiff Mesh** | *Tool > Morph Target* | Advanced | Crea una malla con la DIFERENCIA entre el estado actual y el guardado. |
| 🎚️ | **Morph** | *Tool > Morph Target* | Advanced | Cuánto se vuelve hacia el estado guardado, de 0 a 1. |
| ↔️ | **Morph Width** | *Tool > Morph Target* | Advanced | La anchura de la zona afectada al aplicar el morph. |
| ↕️ | **Morph Height** | *Tool > Morph Target* | Advanced | La altura de la zona afectada al aplicar el morph. |
| 📏 | **MorphDist** | *Tool > Morph Target* | Advanced | La distancia máxima que se tiene en cuenta al calcular el morph. |
| 🎯 | **Project Morph** | *Tool > Morph Target* | Advanced | Proyecta el estado guardado sobre el actual en vez de interpolarlo. |


## Tool > Surface


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌐 | **Tool > Surface** | *Tool > Surface* | Advanced | Aplica RUIDO procedural sobre la superficie sin esculpirlo a mano: piel, roca, metal picado, corteza. OJO CON LO IMPORTANTE: mientras no pulses Apply To Mesh el ruido es solo una PREVISUALIZACIÓN — se ve, pero no existe como geometría, no se puede esculpir encima y no se exporta. |
| 🌾 | **Noise** | *Tool > Surface* | Advanced | Activa el ruido y abre su editor, con una curva para controlar cómo se reparte. |
| ✏️ | **Edit** | *Tool > Surface* | Advanced | Vuelve a abrir el editor del ruido para retocarlo. |
| 🗑️ | **Del** | *Tool > Surface* | Advanced | Borra el ruido aplicado al SubTool. |
| 📚 | **Lightbox ▶ NoiseMakers** | *Tool > Surface* | Advanced | Abre la biblioteca de ruidos ya preparados que trae ZBrush, que es por donde conviene empezar. |
| 🧭 | **SNorm** | *Tool > Surface* | Advanced | Ajusta la intensidad del ruido respecto a las normales de la superficie. |
| 🗺️ | **Suv** | *Tool > Surface* | Advanced | Hace que el ruido siga las UV en vez de la geometría. |
| 🧱 | **Apply To Mesh** | *Tool > Surface* | Advanced | Convierte el ruido en GEOMETRÍA real. Hasta pulsarlo no es más que una vista previa. |
| 🎭 | **MaskByNoise** | *Tool > Surface* | Advanced | Convierte ese ruido en una máscara, truco muy útil para pintar o deformar solo en las zonas rugosas. |
| 🎭 | **UnmaskByNoise** | *Tool > Surface* | Advanced | Lo contrario: desenmascara según el ruido. |
| 🌾 | **Apply Noise To NanoMesh** | *Tool > Surface* | Advanced | Aplica el ruido a las copias sembradas con NanoMesh. |


## Tool > Visibility / Display Properties


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👁️ | **Tool > Visibility y Tool > Display Properties** | *Tool > Visibility / Display Properties* | Intermediate | Visibility gestiona qué partes están ocultas (ver la categoría Visibilidad). Display Properties controla cómo se DIBUJA el modelo: Double (ver las caras por ambos lados, útil en ropa y planos sueltos), Flip (invertir normales) y el grosor del PolyFrame. |


## Tool > UV Map


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗺️ | **Tool > UV Map** | *Tool > UV Map* | Advanced | Gestión de las coordenadas UV del modelo: resolución del mapa, comprobación de si hay UVs, y proyecciones automáticas simples. Para desplegar UVs de verdad se usa el plugin UV Master (en Zplugin), no esta sub-paleta. |
| 🗺️ | **Tool > UV Map: contenido con una primitiva activa** | *Tool > UV Map* | Advanced | Con una primitiva la sub-paleta se reduce a Hrepeat y Vrepeat, que repiten la textura horizontal y verticalmente sobre el objeto. Las opciones de verdad (tamaño del mapa, comprobación de UVs, proyecciones) aparecen al convertir a PolyMesh3D. Para desplegar UVs en serio se usa UV Master, en Zplugin. |
| 🗺️ | **UV Map > ver y borrar el desplegado** | *Tool > UV Map* | Advanced | Al convertir a PolyMesh3D la sub-paleta se abre entera. Este bloque sirve para COMPROBAR cómo han quedado las UVs sin salir de ZBrush. |
| 🦋 | **Morph UV** | *Tool > UV Map* | Advanced | Despliega el modelo en pantalla con una animación para enseñarte cómo quedan sus UVs sobre el plano. Es la forma de comprobar el desplegado sin salir de ZBrush, y se vuelve pulsándolo otra vez. |
| 🏔️ | **Bump** | *Tool > UV Map* | Advanced | Es 'MORPH UV VISUAL BUMP' según su nota emergente: controla cuánto relieve visual conserva el modelo mientras está desplegado en plano, para que puedas seguir viendo el detalle esculpido sobre el desplegado en vez de una plancha lisa. Es puramente visual: no cambia ni la malla ni las UVs. |
| 🗑️ | **Delete UV** | *Tool > UV Map* | Advanced | Borra las UVs del modelo. |
| 📏 | **UV Map > tamaño y margen del mapa** | *Tool > UV Map* | Advanced | Las dos decisiones que más afectan a cómo se va a ver tu textura en el motor: cuánta resolución tiene y cuánto margen se deja entre islas. |
| 📐 | **UV Map Size** | *Tool > UV Map* | Advanced | La resolución del mapa (2048 en tu captura). 2048 es lo normal para un personaje de videojuego, y 4096 solo si la pieza es protagonista y se va a ver de cerca: subirlo sin necesidad solo hace que el juego cargue más lento. |
| 🔢 | **512** | *Tool > UV Map* | Advanced | Acceso directo que fija el mapa en 512 píxeles, para piezas pequeñas o de fondo. |
| 🔢 | **1024** | *Tool > UV Map* | Advanced | Acceso directo que fija el mapa en 1024 píxeles. |
| 🔢 | **2048** | *Tool > UV Map* | Advanced | Acceso directo que fija el mapa en 2048 píxeles, el tamaño habitual de un personaje. |
| 🔢 | **4096** | *Tool > UV Map* | Advanced | Acceso directo que fija el mapa en 4096 píxeles, solo para piezas protagonistas. |
| ⬜ | **UV Map Border** | *Tool > UV Map* | Advanced | El margen en píxeles que se deja alrededor de cada isla para que los colores no se derramen de una a otra (4 en tu captura). Si al aplicar la textura en Unity aparecen costuras raras o líneas de color que no deberían estar, este valor es uno de los primeros sospechosos. Nunca lo pongas a 0. |


## Tool > Texture Map / Polypaint


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖼️ | **Tool > Texture Map y Tool > Polypaint** | *Tool > Texture Map / Polypaint* | Advanced | Polypaint permite pintar color directamente sobre los vértices del modelo, sin necesitar UVs — muy cómodo para pintar mientras esculpes. Texture Map gestiona la textura como imagen; para pasar de uno a otro se usa 'New From Polypaint' (Polypaint → textura, requiere UVs) o 'Polypaint from Texture' (al revés). |


## Tool > Import / Export


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📤 | **Tool > Import / Export** | *Tool > Import / Export* | Intermediate | Importa y exporta la herramienta en formatos externos (OBJ, FBX, STL...). Aquí están las escalas y los ejes de exportación, que hay que revisar al llevar el modelo a Maya, Unity o Unreal para que no llegue gigantesco o tumbado. |


## Tool > SubTool > bloque inferior


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✂️ | **Split** | *Tool > SubTool (bloque inferior)* | Advanced | Parte un SubTool en varios según distintos criterios: por trozos sueltos, por PolyGroups, por máscara... |
| 📐 | **Align** | *Tool > SubTool (bloque inferior)* | Advanced | Coloca los SubTools alineados en el espacio. |
| ↔️ | **Distribute** | *Tool > SubTool (bloque inferior)* | Advanced | Los reparte en el espacio. |
| 🕸️ | **Remesh** | *Tool > SubTool (bloque inferior)* | Advanced | Genera una malla nueva que envuelve varios SubTools combinados. Útil para unificar un montaje de piezas sueltas. |
| 📽️ | **Project** | *Tool > SubTool (bloque inferior)* | Advanced | Es el Project All: transfiere el detalle de un SubTool a otro. |
| 🗿 | **Project BasRelief** | *Tool > SubTool (bloque inferior)* | Advanced | Proyecta como bajorrelieve. |
| 🎬 | **Redshift Properties** | *Tool > SubTool (bloque inferior)* | Advanced | Los ajustes del motor de render Redshift para ese SubTool. |


## Tool > Preview


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👀 | **Tool > Preview** | *Tool > Preview* | Intermediate | Ventanita con una vista en miniatura de la herramienta, que se puede girar arrastrando dentro de ella para mirar el modelo desde otro ángulo sin mover la cámara del lienzo. Cómoda para tener una segunda vista de referencia mientras esculpes. |
| 💾 | **Store** | *Tool > Preview* | Intermediate | Guarda el ángulo actual de esa previsualización. |
| ↩️ | **Restore** | *Tool > Preview* | Intermediate | Vuelve al ángulo guardado. |


## Tool > Visibility


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👁️ | **Tool > Visibility** | *Tool > Visibility* | Intermediate | Gestiona qué partes del modelo están ocultas. Se combina con los gestos de ratón: Ctrl+Mayús+arrastrar para ocultar y Ctrl+Mayús+clic en el fondo para volver a mostrar todo. Varios botones salen en gris cuando no hay nada oculto. |
| 🙈 | **HidePt** | *Tool > Visibility* | Intermediate | Oculta los puntos seleccionados. |
| 👁️ | **ShowPt** | *Tool > Visibility* | Intermediate | Muestra los puntos ocultos. |
| ➕ | **Grow** | *Tool > Visibility* | Intermediate | Amplía la zona visible poco a poco, un polígono cada vez. Muy cómodo para ajustar con precisión hasta dónde llega lo que estás aislando. |
| ➖ | **Shrink** | *Tool > Visibility* | Intermediate | Reduce la zona visible poco a poco, un polígono cada vez. |
| ⏫ | **Grow All** | *Tool > Visibility* | Intermediate | Muestra todo el modelo de golpe. |
| ⭕ | **Outer Ring** | *Tool > Visibility* | Intermediate | Deja visible solo el anillo exterior de lo que estaba visible. |
| 🎨 | **Grow To Polygroups** | *Tool > Visibility* | Intermediate | Amplía la zona visible hasta completar los PolyGroups enteros. |
| 🕳️ | **Group As Dynamesh Sub** | *Tool > Visibility* | Advanced | Marca lo visible como sustracción para DynaMesh, para abrir huecos al remallar. |


## Tool > Contact


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔗 | **Tool > Contact** | *Tool > Contact* | Advanced | RESUELTA ENTERA con tus notas emergentes. Guarda hasta tres 'contactos' del SubTool en tres huecos y permite volver a aplicarlos sobre la geometría. En tu captura están todos en gris porque todavía no habías guardado ninguno. Es una sub-paleta muy poco usada; no te preocupes por ella. |
| 1️⃣ | **C1** | *Tool > Contact* | Advanced | Es 'Stores 1st Contact': guarda el primer contacto. |
| 2️⃣ | **C2** | *Tool > Contact* | Advanced | Es 'Stores 2nd Contact': guarda el segundo contacto. |
| 3️⃣ | **C3** | *Tool > Contact* | Advanced | Es 'Stores 3rd Contact': guarda el tercer contacto. |
| 🗑️ | **Del** | *Tool > Contact* | Advanced | Es 'Delete Contact': borra el contacto guardado. |
| ✅ | **Apply** | *Tool > Contact* | Advanced | Es 'Apply Contacts To Mesh': aplica a la malla los contactos almacenados. |


## Tool > Polypaint


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎨 | **Polypaint > los controles básicos** | *Tool > Polypaint* | Intermediate | El color por VÉRTICE: se pinta directamente sobre la malla, sin necesidad de UVs ni de textura. Es la forma cómoda de pintar en ZBrush; convertirlo en textura de verdad viene después, en Texture Map. |
| 👁️ | **Colorize** | *Tool > Polypaint* | Intermediate | Activa la visualización del color pintado sobre el modelo. Si pintas y no ves nada, casi siempre es que este botón está apagado. |
| 🌈 | **Grd** | *Tool > Polypaint* | Intermediate | Aplica el color como degradado (activo en naranja en tu captura). |
| 🪣 | **FillColor** | *Tool > Polypaint* | Intermediate | Rellena todo el SubTool con el color activo de golpe. |
| 🌈 | **FillGrad** | *Tool > Polypaint* | Intermediate | Rellena todo el SubTool con un degradado entre los dos colores activos. |
| 🖼️ | **Polypaint From Texture** | *Tool > Polypaint* | Advanced | Pasa una textura existente a color por vértice, o sea el camino inverso al habitual. Sale en gris cuando no hay textura cargada. |
| 🎨 | **Polypaint > lo que se añade con un PolyMesh3D** | *Tool > Polypaint* | Intermediate | Con un PolyMesh3D la sub-paleta crece respecto a la versión reducida. En tu captura estos salen en gris porque todavía no había color pintado. |
| 🟩 | **Polypaint From Polygroups** | *Tool > Polypaint* | Intermediate | Pinta cada PolyGroup de su color. Es la forma más rápida de convertir los grupos en color de verdad o de preparar máscaras por zonas. |
| 🎛️ | **Adjust Colors** | *Tool > Polypaint* | Intermediate | Abre controles para retocar el color ya pintado —tono, saturación, brillo— sin volver a pintar nada. |
| 🪞 | **Flip By Posable Symmetry** | *Tool > Polypaint* | Advanced | Voltea el color usando la simetría 'posable', la que sigue funcionando aunque el modelo esté en una pose asimétrica. |
| 🪞 | **Mirror By Posable Symmetry** | *Tool > Polypaint* | Advanced | Refleja el color al otro lado con esa misma simetría posable. |
| 🌗 | **Polypaint > From Draft y From Thickness** | *Tool > Polypaint* | Advanced | Dos generadores de color automáticos que en realidad son herramientas de DIAGNÓSTICO, muy útiles antes de exportar o de imprimir en 3D. |


## Tool > Texture Map


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖼️ | **Tool > Texture Map: contenido real de la sub-paleta** | *Tool > Texture Map* | Advanced | Según tu captura: una miniatura para elegir la textura y, a su lado, Texture On (activarla), Clone Txtr (clonarla a la paleta Texture), Transparent (transparencia) y Antialiased (suavizado de bordes), todos en gris porque no hay textura asignada. Abajo, Fill rellena la textura con el color activo y Create la genera nueva. Necesita UVs para funcionar bien. |
| 🖼️ | **Texture Map > la textura del SubTool** | *Tool > Texture Map* | Advanced | La miniatura de la izquierda es la textura asignada al SubTool y se pulsa para elegir otra. Este bloque la gestiona. Necesita UVs para funcionar bien. |
| 🔘 | **Texture On** | *Tool > Texture Map* | Advanced | Activa o desactiva la textura sobre el modelo. |
| 📋 | **Clone Txtr** | *Tool > Texture Map* | Advanced | Copia la textura a la paleta Texture del menú superior, que es desde donde se exporta. |
| 🆕 | **New Txtr** | *Tool > Texture Map* | Advanced | Crea una textura nueva y vacía del tamaño indicado en UV Map Size. Es el paso previo obligatorio antes de pintar sobre textura. |
| 🩹 | **Fix Seam** | *Tool > Texture Map* | Advanced | Intenta arreglar las costuras visibles rellenando los bordes de las islas. |
| 👻 | **Transparent** | *Tool > Texture Map* | Advanced | Hace que la textura use transparencia. |
| 🫧 | **Antialiased** | *Tool > Texture Map* | Advanced | Suaviza los bordes de la textura. |
| 🪣 | **Fill Mat** | *Tool > Texture Map* | Advanced | Rellena la textura con el material activo. |
| 🪣 | **FillColor** | *Tool > Texture Map* | Advanced | Rellena la textura con el color activo. |
| 🌈 | **FillGrad** | *Tool > Texture Map* | Advanced | Rellena la textura con un degradado entre los dos colores de la barra izquierda. |


## Tool > Display Properties


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💡 | **Tool > Display Properties: contenido real de la sub-paleta** | *Tool > Display Properties* | Intermediate | Según tu captura: Sh y Sv (activos en naranja) junto a Bh y Bv controlan cómo se dibuja la superficie. DRes ajusta la resolución de dibujado. Double hace que se vean las caras por AMBOS lados, imprescindible en ropa, hojas o cualquier superficie de un solo grosor que de otro modo desaparece al mirarla por detrás. Flip invierte las normales, que es la solución cuando un modelo se ve 'del revés' o con manchas negras. BPR Settings abre los ajustes de render de este SubTool. |
| 🖥️ | **Tool > Display Properties** | *Tool > Display Properties* | Intermediate | Controla cómo se DIBUJA el modelo en pantalla. Nada de esto cambia la malla: solo su aspecto en el visor. Dos de sus botones resuelven problemas muy típicos. |
| 🫧 | **DSmooth** | *Tool > Display Properties* | Intermediate | El suavizado con el que se dibuja la superficie. No cambia la malla, solo cómo se ve en pantalla. |
| 🔢 | **DRes** | *Tool > Display Properties* | Intermediate | La resolución de ese dibujado. |
| ❓ | **Es** | *Tool > Display Properties* | Intermediate | Aparece en gris en tu captura, sin nota emergente que lo identifique. |
| ⧉ | **Double** | *Tool > Display Properties* | Intermediate | Hace que las caras se vean por AMBOS lados. Imprescindible en ropa, hojas, capas o cualquier superficie de un solo grosor, que sin él desaparece al mirarla por detrás. |
| 🔃 | **Flip** | *Tool > Display Properties* | Intermediate | Invierte las normales. Es la solución cuando un modelo se ve del revés o con manchas negras. |
| 📏 | **Polygons Draw Size** | *Tool > Display Properties* | Intermediate | El grosor con el que se pintan las líneas del PolyFrame (Mayús+F), 1 en tu captura. Súbelo si te cuesta ver la malla sobre el modelo. |


## Tool > Unified Skin


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧴 | **Tool > Unified Skin** | *Tool > Unified Skin* | Advanced | Genera una malla nueva que envuelve la herramienta como una piel unificada. Es un método antiguo de unificar volúmenes: hoy para eso se suele usar DynaMesh o el Remesh de SubTool, pero sigue siendo útil para conseguir una envoltura suave. |
| 🔢 | **Resolution** | *Tool > Unified Skin* | Advanced | La densidad de la malla generada (128 por defecto). |
| 🫧 | **Smooth** | *Tool > Unified Skin* | Advanced | Cuánto se suaviza el resultado (10 por defecto). |
| 🎚️ | **Sdns** | *Tool > Unified Skin* | Advanced | El otro ajuste de densidad del cálculo. |
| ✅ | **Make Unified Skin** | *Tool > Unified Skin* | Advanced | Crea la piel unificada como herramienta aparte, sin destruir la original. |


## Tool > Initialize


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎚️ | **Tool > Initialize: los parámetros de la primitiva** | *Tool > Initialize* | Intermediate | Los deslizadores PARAMÉTRICOS de la primitiva activa: cambian su forma sin esculpir nada, y desaparecen en cuanto conviertes a PolyMesh3D. Conviene dejar la primitiva con la forma y la densidad que quieres ANTES de pulsar Make PolyMesh3D. Los de tu captura son los de un Cylinder3D. |
| ↔️ | **Align X** | *Tool > Initialize* | Intermediate | Genera la primitiva orientada sobre el eje X. |
| ↕️ | **Align Y** | *Tool > Initialize* | Intermediate | Genera la primitiva orientada sobre el eje Y (el que tienes activo). |
| 🔃 | **Align Z** | *Tool > Initialize* | Intermediate | Genera la primitiva orientada sobre el eje Z. |
| ↔️ | **X Size** | *Tool > Initialize* | Intermediate | La dimensión de la primitiva en el eje X. |
| ↕️ | **Y Size** | *Tool > Initialize* | Intermediate | La dimensión de la primitiva en el eje Y. |
| 🔃 | **Z Size** | *Tool > Initialize* | Intermediate | La dimensión de la primitiva en el eje Z. |
| 🕳️ | **Inner Radius** | *Tool > Initialize* | Intermediate | El radio interior, con el que un cilindro se convierte en un tubo hueco. |
| ▦ | **HDivide** | *Tool > Initialize* | Intermediate | El número de divisiones horizontales (32 en tu captura). Junto con VDivide decide la densidad de la malla que obtendrás al convertir. |
| ▦ | **VDivide** | *Tool > Initialize* | Intermediate | El número de divisiones verticales (17 en tu captura). |
| 🔻 | **TaperTop** | *Tool > Initialize* | Intermediate | Estrecha la parte de arriba, para hacer un cono truncado. |
| ⚪ | **CapSubRatio** | *Tool > Initialize* | Intermediate | La subdivisión de las tapas del cilindro. |
| 🧊 | **Tool > Initialize: el generador de mallas base** | *Tool > Initialize* | Intermediate | Con un PolyMesh3D la sub-paleta cambia POR COMPLETO: ya no son deslizadores paramétricos, sino un generador de mallas base de topología cuadrada. Es la forma rápida de empezar una pieza de modelado duro con una topología limpia y ordenada, lista para trabajar con ZModeler. |
| 🧊 | **QCube** | *Tool > Initialize* | Intermediate | Crea un cubo de topología cuadrada limpia. |
| ⚪ | **QSphere** | *Tool > Initialize* | Intermediate | Crea una esfera de topología cuadrada limpia. |
| ▦ | **QGrid** | *Tool > Initialize* | Intermediate | Crea una rejilla plana. |
| 🛢️ | **QCyl X** | *Tool > Initialize* | Intermediate | Crea un cilindro orientado en el eje X. |
| 🛢️ | **QCyl Y** | *Tool > Initialize* | Intermediate | Crea un cilindro orientado en el eje Y. |
| 🛢️ | **QCyl Z** | *Tool > Initialize* | Intermediate | Crea un cilindro orientado en el eje Z. |
| 🔢 | **X Res** | *Tool > Initialize* | Intermediate | Cuántas divisiones tendrá la malla resultante en el eje X (2 por defecto). |
| 🔢 | **Y Res** | *Tool > Initialize* | Intermediate | Cuántas divisiones tendrá la malla resultante en el eje Y (2 por defecto). |
| 🔢 | **Z Res** | *Tool > Initialize* | Intermediate | Cuántas divisiones tendrá la malla resultante en el eje Z (2 por defecto). |


## Tool > Import


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📥 | **Tool > Import: cómo entra la malla** | *Tool > Import* | Intermediate | Los ajustes que se aplican al IMPORTAR una malla externa (OBJ, FBX, STL...). Conviene revisarlos ANTES de importar, porque después ya no se pueden aplicar sin volver a cargar el archivo. |
| 📂 | **Import** | *Tool > Import* | Intermediate | El botón que abre el archivo y carga la malla. |
| 🔗 | **Mrg** | *Tool > Import* | Intermediate | Fusiona lo que entra en una sola malla en lugar de dejar cada trozo suelto. |
| ➕ | **Add** | *Tool > Import* | Intermediate | Añade lo importado a la herramienta actual en vez de sustituirla, que es lo que permite ir metiendo piezas dentro del mismo objeto en lugar de empezar de cero cada vez. |
| 🔗 | **Tool > Import: arreglar una malla que llega mal** | *Tool > Import* | Intermediate | Los dos deslizadores que hay que mirar cuando importas algo de Maya o de Blender y al subdividirlo salen facetas o costuras raras. |
| 🔲 | **Tri2Quad** | *Tool > Import* | Intermediate | Convierte triángulos en cuadrados al entrar (0 en tu captura): subiéndolo, ZBrush intenta emparejar triángulos vecinos para darte una malla de quads, que es la que se subdivide y se esculpe bien. A 0 no toca nada. |
| 🔗 | **Weld** | *Tool > Import* | Intermediate | Suelda entre sí los vértices que estén más cerca de esa distancia (0 en tu captura). Es el arreglo cuando una malla llega con los vértices partidos y por eso no se puede suavizar ni subdividir sin que aparezcan grietas. |


## Tool > Export


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📤 | **Tool > Export** | *Tool > Export* | Intermediate | Los ajustes que se aplican al exportar. Son exactamente los valores que hay que revisar cuando un modelo llega a Unity, Unreal o Maya gigantesco, minúsculo o descolocado respecto al origen. TRUCO: si necesitas que la pieza salga con medidas reales (centímetros, milímetros), es más fiable usar el plugin Scale Master, en la paleta Zplugin, que pelearse con estos deslizadores. |
| 💾 | **Export** | *Tool > Export* | Intermediate | El botón que guarda la herramienta en un archivo externo. |
| 🔍 | **Scale** | *Tool > Export* | Intermediate | Multiplica el tamaño del modelo al exportar (0 en tu captura). |
| ↔️ | **X Offset** | *Tool > Export* | Intermediate | Desplaza el modelo en el eje X respecto al origen al exportar. |
| ↕️ | **Y Offset** | *Tool > Export* | Intermediate | Desplaza el modelo en el eje Y respecto al origen al exportar. |
| 🔃 | **Z Offset** | *Tool > Export* | Intermediate | Desplaza el modelo en el eje Z respecto al origen al exportar. |


## Tool > SubTool > Merge


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔗 | **SubTool > Merge** | *Tool > SubTool > Merge* | Intermediate | Fusiona SubTools en uno solo. Los que salen en gris es porque con un solo SubTool no hay nada que fusionar. |
| ⬇️ | **MergeDown** | *Tool > SubTool > Merge* | Intermediate | Une el SubTool activo con el que tiene JUSTO DEBAJO en la lista. Es el que más se usa, y por eso para juntar dos piezas hay que colocarlas seguidas primero. |
| 🔍 | **MergeSimilar** | *Tool > SubTool > Merge* | Intermediate | Une los SubTools que compartan características entre sí. |
| 👁️ | **MergeVisible** | *Tool > SubTool > Merge* | Intermediate | Funde todos los SubTools VISIBLES en una herramienta nueva. Ojo: crea una herramienta aparte y deja intactos los originales. |
| 🔗 | **Weld** | *Tool > SubTool > Merge* | Intermediate | Suelda los vértices que coincidan en el punto de unión en vez de dejarlos sueltos, para que el resultado sea una malla continua y no dos pegadas. |
| 🗺️ | **Uv** | *Tool > SubTool > Merge* | Intermediate | Conserva las coordenadas UV al fusionar (activa en naranja en tu captura). |


## Tool > SubTool > Split


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✂️ | **SubTool > Split** | *Tool > SubTool > Split* | Intermediate | Lo contrario de Merge: parte un SubTool en varios, y cada opción usa un criterio distinto para decidir por dónde cortar. |
| 🙈 | **Split Hidden** | *Tool > SubTool > Split* | Intermediate | Separa lo OCULTO de lo visible, dejando cada parte como un SubTool. |
| 🎨 | **Groups Split** | *Tool > SubTool > Split* | Intermediate | Crea un SubTool por cada PolyGroup. Es la forma más limpia de trocear un modelo que ya has organizado por grupos de color. |
| 🔍 | **Split To Similar Parts** | *Tool > SubTool > Split* | Intermediate | Agrupa en SubTools las partes que se parezcan entre sí. |
| 🧩 | **Split To Parts** | *Tool > SubTool > Split* | Intermediate | Separa los trozos que no estén conectados entre sí. Útil cuando has hecho DynaMesh de varias piezas sueltas y quieres recuperarlas por separado. |
| 🎭 | **Split Unmasked Points** | *Tool > SubTool > Split* | Intermediate | Separa a un SubTool nuevo todo lo que NO esté enmascarado. |
| 🎭 | **Split Masked Points** | *Tool > SubTool > Split* | Intermediate | Separa a un SubTool nuevo lo que SÍ está enmascarado. Es la forma de sacar una zona concreta pintándola primero con la máscara. |


## Tool > SubTool > Boolean


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚫ | **SubTool > Boolean** | *Tool > SubTool > Boolean* | Advanced | Aquí se CONFIRMAN las operaciones booleanas que hayas montado con Live Boolean (sumar, restar o intersecar SubTools). Sale en gris hasta que hay operaciones booleanas definidas. |
| ✅ | **Make Boolean Mesh** | *Tool > SubTool > Boolean* | Advanced | Calcula el resultado de verdad y genera una herramienta nueva con la malla resultante, dejando intactos los SubTools originales. Hasta pulsarlo, el boolean es solo una previsualización. |
| 🔢 | **DSDiv** | *Tool > SubTool > Boolean* | Advanced | La densidad con la que se resuelve la operación: más alto da un resultado más fino en los bordes del corte, pero más pesado. |


## Tool > SubTool > Bevel Pro


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📐 | **SubTool > Bevel Pro** | *Tool > SubTool > Bevel Pro* | Advanced | Sistema de biselado avanzado que crea chaflanes controlados en los bordes del modelo, con perfiles y ajustes propios, pensado sobre todo para modelado de superficies duras (mecánico, armaduras, props). Es bastante más completo que el Bevel suelto que hay dentro de Crease en la sub-paleta Geometry. |


## Tool > SubTool > Align


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ↔️ | **SubTool > Align (los 6 botones de iconos)** | *Tool > SubTool > Align* | Intermediate | Seis botones con iconos que ALINEAN unos SubTools respecto a otros en el espacio: alineación por el centro y por los extremos, en los distintos ejes (los tres de arriba trabajan en un sentido y los tres de abajo en el otro). Es la forma de dejar piezas perfectamente colocadas — ojos a la misma altura, botones de una chaqueta en línea — sin moverlas a ojo con el Gizmo. |


## Tool > SubTool > Distribute


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ↕️ | **SubTool > Distribute (los 6 botones de iconos)** | *Tool > SubTool > Distribute* | Intermediate | Otros seis botones de iconos que REPARTEN los SubTools a distancias iguales entre sí, en horizontal o en vertical según el que elijas. Se usa junto con Align: primero alineas y luego distribuyes, y te quedan las piezas ordenadas de forma regular sin colocarlas una a una. |


## Tool > SubTool > Remesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔄 | **SubTool > Remesh** | *Tool > SubTool > Remesh* | Advanced | Genera UNA malla nueva que envuelve varios SubTools a la vez, unificándolos. Se usa para convertir un montaje de piezas sueltas en una sola superficie continua sobre la que seguir esculpiendo. |
| ▶️ | **ReMesh All** | *Tool > SubTool > Remesh* | Advanced | Lanza la operación sobre los SubTools visibles. |
| 🔢 | **Res** | *Tool > SubTool > Remesh* | Advanced | La resolución de la malla nueva (128 por defecto): más alto conserva mejor la forma de las piezas originales, pero pesa más. |
| ✨ | **Polish** | *Tool > SubTool > Remesh* | Advanced | Suaviza el resultado (10 por defecto). |
| 🎨 | **PolyGrp** | *Tool > SubTool > Remesh* | Advanced | Asigna PolyGroups distintos a cada trozo de origen, para poder volver a separarlos después con Groups Split. |


## Tool > SubTool > Project


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎯 | **SubTool > Project** | *Tool > SubTool > Project* | Advanced | Transfiere detalle de un SubTool a otro. El uso típico: has remallado con ZRemesher y quieres recuperar el detalle que tenías en la versión antigua. |
| ▶️ | **ProjectAll** | *Tool > SubTool > Project* | Advanced | Ejecuta la proyección del SubTool de origen sobre el de destino. |
| 📏 | **Dist** | *Tool > SubTool > Project* | Advanced | La distancia máxima que busca (0.02 en tu captura). Si es muy pequeña no encuentra la superficie de origen; si es muy grande coge detalle equivocado de otras zonas. Es el deslizador que hay que tocar cuando la proyección sale llena de picos. |
| 📊 | **Mean** | *Tool > SubTool > Project* | Advanced | Promedia el resultado para suavizar la transferencia (25 en tu captura). |
| 🔺 | **Geometry** | *Tool > SubTool > Project* | Advanced | Transfiere la FORMA (activo en naranja en tu captura). |
| 🎨 | **Color** | *Tool > SubTool > Project* | Advanced | Transfiere el COLOR pintado (activo en naranja en tu captura). |
| 🫧 | **PA Blur** | *Tool > SubTool > Project* | Advanced | Difumina la proyección para evitar artefactos (10 en tu captura). |
| ↔️ | **Farthest** | *Tool > SubTool > Project* | Advanced | Usa el punto más LEJANO de la superficie de origen en vez del más cercano. |
| 🥚 | **ProjectionShell** | *Tool > SubTool > Project* | Advanced | Define un grosor de búsqueda alrededor de la superficie, con sus ejes XYZ. |
| ⬆️ | **Outer** | *Tool > SubTool > Project* | Advanced | Limita la proyección a la parte EXTERIOR de la superficie. |
| ⬇️ | **Inner** | *Tool > SubTool > Project* | Advanced | Limita la proyección a la parte INTERIOR de la superficie. |


## Tool > SubTool > Project BasRelief


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗿 | **SubTool > Project BasRelief** | *Tool > SubTool > Project BasRelief* | Advanced | Proyecta un SubTool sobre otro aplastándolo como un BAJORRELIEVE, en vez de transferir el detalle tal cual: el resultado queda como una talla en relieve sobre la superficie receptora — monedas, placas grabadas, ornamentos en una pared. |
| 🔢 | **Relief Repeat Count** | *Tool > SubTool > Project BasRelief* | Advanced | El número de pasadas del cálculo (1000 en tu captura): más pasadas, resultado más fino y más lento. |
| 📐 | **Relief Step Tolerance** | *Tool > SubTool > Project BasRelief* | Advanced | La tolerancia de cada paso del cálculo (0.2 en tu captura). |
| 🌗 | **Relief Contrast** | *Tool > SubTool > Project BasRelief* | Advanced | Exagera o suaviza las diferencias de profundidad del relieve (0 en tu captura). |
| 🫧 | **Relief Blur Radius** | *Tool > SubTool > Project BasRelief* | Advanced | Difumina el resultado para que no queden escalones (4 en tu captura). |


## Tool > SubTool > Extract


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👕 | **SubTool > Extract** | *Tool > SubTool > Extract* | Intermediate | Uno de los botones más útiles de ZBrush: crea geometría NUEVA a partir de la zona que hayas enmascarado. Es como recortar un trozo de la superficie y darle grosor, y es la forma clásica de sacar ropa, placas de armadura, costras o parches directamente del cuerpo. |
| ✂️ | **Extract** | *Tool > SubTool > Extract* | Intermediate | Genera la previsualización de la pieza a partir de la máscara pintada. |
| 🫧 | **S Smt** | *Tool > SubTool > Extract* | Intermediate | Cuánto se suaviza el resultado (5 en tu captura). |
| 📐 | **Thick** | *Tool > SubTool > Extract* | Intermediate | El GROSOR de la pieza resultante (0.02 en tu captura). Es el deslizador que decide si sale una tela fina o una placa de armadura. |
| ✅ | **Accept** | *Tool > SubTool > Extract* | Intermediate | Convierte la previsualización en un SubTool nuevo de verdad. Sale en gris hasta que hay algo extraído. |
| ⧉ | **Double** | *Tool > SubTool > Extract* | Intermediate | Genera la pieza con doble superficie, o sea con volumen cerrado por los dos lados (activo en naranja en tu captura). |
| 📐 | **TCorner** | *Tool > SubTool > Extract* | Advanced | Controla cómo se resuelven las ESQUINAS del recorte. |
| ➖ | **TBorder** | *Tool > SubTool > Extract* | Advanced | Controla cómo se resuelve el BORDE del recorte. |


## Tool > SubTool > Redshift Properties


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎥 | **SubTool > Redshift Properties: Smooth surface** | *Tool > SubTool > Redshift Properties* | Advanced | Ajustes específicos del motor de render Redshift para ESTE SubTool. En tu captura solo aparece Smooth surface (activo en naranja), que le dice a Redshift que suavice la superficie al renderizar aunque la malla tenga pocos polígonos. Solo importa si vas a renderizar con Redshift; para trabajar esculpiendo se puede ignorar. |


## Tool > Geometry > Proxy Pose


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧍 | **Geometry > Proxy Pose** | *Tool > Geometry > Proxy Pose* | Advanced | Crea temporalmente una versión LIGERA del modelo para poder posarlo con fluidez, y luego devuelve la pose al modelo original con todo su detalle. Es la solución cuando posar un personaje de varios millones de polígonos va a tirones. |
| 🎚️ | **Reduction Amount** | *Tool > Geometry > Proxy Pose* | Advanced | Cuánto se reduce la malla para generar el proxy (0.5 en tu captura): más reducción, más fluido pero menos preciso al posar. |
| ❄️ | **Freeze Border** | *Tool > Geometry > Proxy Pose* | Advanced | Congela los bordes de la malla para que no se deformen mientras se posa el proxy. |
| ✨ | **Polish** | *Tool > Geometry > Proxy Pose* | Advanced | Suaviza el resultado al devolver la pose al modelo original (0 en tu captura). |
| 💎 | **Keep Details** | *Tool > Geometry > Proxy Pose* | Advanced | Conserva parte del detalle en el proxy (0 en tu captura). Subirlo hace el proxy más fiel y más pesado. |
| 🎨 | **ProxyGroups** | *Tool > Geometry > Proxy Pose* | Advanced | Respeta los PolyGroups al generar el proxy, para que las piezas no se mezclen entre sí. |


## Tool > Geometry > Dynamic Subdiv


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚡ | **Geometry > Dynamic Subdiv** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Subdivisión VISUAL: muestra el modelo suavizado y biselado sin añadir polígonos de verdad, igual que el modificador Subdivision Surface de Blender. Sirve para ver cómo quedaría la pieza acabada mientras trabajas con la malla ligera. |
| 🔘 | **Dynamic** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Activa el modo de subdivisión dinámica sobre el SubTool actual. |
| ✅ | **Apply** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Convierte esa previsualización en geometría real y permanente. Hasta pulsarlo, lo que ves no existe como polígonos. |
| ▦ | **QGrid** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Trata los bordes con una REJILLA de subdivisión, repartiendo el suavizado en cuadrícula. |
| ◗ | **Bevel** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Trata los bordes con un bisel redondeado (activo en naranja en tu captura). Es el modo que da ese brillo fino en la arista que hace que una pieza dura se lea bien. |
| ◣ | **Chamfer** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Trata los bordes con un chaflán recto, un corte plano en vez de redondeado. |
| 📏 | **Coverage** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Cuánta superficie abarca el tratamiento del borde desde la arista hacia dentro. |
| 🔒 | **Constant** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Mantiene el bisel del mismo tamaño en todo el modelo, en vez de escalarlo según el tamaño de cada polígono. Es lo que hace que los cantos se vean uniformes. |
| ▬ | **FlatSubdiv** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Subdivide sin suavizar: añade malla pero respeta la forma angulosa. |
| 🫧 | **SmoothSubdiv** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Subdivide suavizando, que es el comportamiento clásico de la subdivisión. |
| 📐 | **Thickness** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Da GROSOR a una superficie abierta, convirtiendo un plano en una placa con dos caras. Es como se saca una chapa o una tela con canto a partir de una superficie plana. |
| ⏭️ | **Post SubDiv** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Aplica el efecto DESPUÉS de la subdivisión normal en vez de antes, lo que cambia cómo se combinan los dos. |
| 🧶 | **MicroPoly** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Repite una malla pequeña por cada polígono del modelo: es como se hacen tejidos, escamas o mallas metálicas de una sola vez. Sus ajustes van justo debajo. |
| ↔️ | **Fit** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Ajusta la malla de MicroPoly al tamaño del polígono que la aloja. |
| 🔗 | **Weld** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Suelda entre sí las copias vecinas de MicroPoly, para que formen una superficie continua. |
| 🔍 | **Scale** | *Tool > Geometry > Dynamic Subdiv* | Advanced | El tamaño de cada copia de MicroPoly respecto a su polígono. |
| 📐 | **Align** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Cómo se orientan las copias de MicroPoly respecto a la superficie. |
| 🔄 | **Rot Z** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Gira cada copia de MicroPoly sobre su eje Z. |
| 🔄 | **Rot X** | *Tool > Geometry > Dynamic Subdiv* | Advanced | Gira cada copia de MicroPoly sobre su eje X. |


## Tool > Geometry > EdgeLoop


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ➰ | **Geometry > EdgeLoop** | *Tool > Geometry > EdgeLoop* | Advanced | Crea anillos de aristas a partir de bordes, máscaras o PolyGroups. Sirve para meter geometría de control justo donde hace falta que un borde se mantenga duro al subdividir. |
| 🎭 | **Edgeloop Masked Border** | *Tool > Geometry > EdgeLoop* | Advanced | Genera un anillo de aristas siguiendo el BORDE de la máscara que tengas pintada. |
| ➰ | **Edge Loop** | *Tool > Geometry > EdgeLoop* | Advanced | Crea el anillo de aristas a partir del borde abierto de la malla. |
| 🔪 | **Crisp** | *Tool > Geometry > EdgeLoop* | Advanced | Deja ese anillo marcado y afilado, en vez de suavizado. |
| 🎨 | **GroupsLoops** | *Tool > Geometry > EdgeLoop* | Advanced | Añade anillos en los bordes de los PolyGroups, que es la forma de blindar la separación entre piezas. |
| 🔢 | **Loops** | *Tool > Geometry > EdgeLoop* | Advanced | Cuántos anillos se añaden (4 en tu captura). |
| ✨ | **GPolish** | *Tool > Geometry > EdgeLoop* | Advanced | Cuánto se pule el resultado de GroupsLoops (50 en tu captura). |
| 🔺 | **Triangle** | *Tool > Geometry > EdgeLoop* | Advanced | Resuelve los triángulos que queden al generar los anillos. |
| 🗑️ | **Delete Loops** | *Tool > Geometry > EdgeLoop* | Advanced | Borra anillos de aristas sobrantes, según los dos criterios que van debajo. |
| 📐 | **Angle** | *Tool > Geometry > EdgeLoop* | Advanced | El ángulo por debajo del cual un anillo se considera prescindible (45 en tu captura). |
| 📏 | **Aspect Ratio** | *Tool > Geometry > EdgeLoop* | Advanced | Lo alargados que tienen que ser los polígonos para borrar su anillo (25 en tu captura). |
| 📐 | **Align Loops** | *Tool > Geometry > EdgeLoop* | Advanced | Realinea los anillos existentes para que queden regulares. |
| 🛡️ | **Geometry > EdgeLoop > Panel Loops** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | La estrella del bloque: convierte cada PolyGroup en un PANEL independiente con grosor. Así es como se hacen placas de armadura y paneles mecánicos a partir de una superficie lisa — divides con PolyGroups, pulsas Panel Loops, y cada grupo se separa como una pieza con canto. |
| 📐 | **Thickness** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | El grosor de la placa resultante (0.01 en tu captura). |
| ✨ | **Polish** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | Cuánto se pule el resultado (5 en tu captura). |
| ◗ | **Bevel** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | El bisel del canto de la placa (50 en tu captura). |
| ⬆️ | **Elevation** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | Cuánto sobresale el panel respecto a la superficie original (100 en tu captura). |
| ⧉ | **Double** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | Genera el panel por AMBAS caras de la superficie, no solo por una. |
| ⬇️ | **Inner** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | Saca el panel hacia DENTRO en vez de hacia fuera. |
| 🚫 | **Ignore Groups** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | Genera los paneles ignorando los PolyGroups, tratando la malla como una sola pieza. |
| 🎨 | **RegroupPanels** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | Reasigna PolyGroups nuevos a los paneles creados, para poder seleccionarlos por separado. |
| 🎨 | **RegroupLoops** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | Reasigna PolyGroups nuevos a los anillos creados en los cantos. |
| 📈 | **Bevel Profile** | *Tool > Geometry > EdgeLoop > Panel Loops* | Advanced | La curva que define el PERFIL del canto. Ahí se decide si el borde queda recto, redondeado o con moldura, y es lo que diferencia una placa de plástico de una de metal trabajado. |


## Tool > Geometry > Crease


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📏 | **Geometry > Crease** | *Tool > Geometry > Crease* | Intermediate | Marca aristas como 'creased' para que se mantengan AFILADAS al subdividir en vez de redondearse. Es la forma de conservar bordes duros en un modelo por lo demás suave. |
| 📏 | **Crease** | *Tool > Geometry > Crease* | Intermediate | Marca como afiladas las aristas que cumplan el criterio de ángulo de CTolerance. |
| 📏 | **CreaseAll** | *Tool > Geometry > Crease* | Intermediate | Marca como afiladas TODAS las aristas de la malla, sin mirar el ángulo. |
| 📐 | **CTolerance** | *Tool > Geometry > Crease* | Intermediate | El ángulo a partir del cual se considera que una arista es un borde duro (45 en tu captura). Bajarlo marca más aristas; subirlo, solo las esquinas más pronunciadas. |
| 🔢 | **CreaseLvl** | *Tool > Geometry > Crease* | Intermediate | Hasta qué nivel de subdivisión aguanta la marca (15 en tu captura). Pasado ese nivel, la arista se redondea como cualquier otra. |
| 🧹 | **UnCrease** | *Tool > Geometry > Crease* | Intermediate | Quita la marca de afilado de las aristas que cumplan el criterio. |
| 🧹 | **UnCreaseAll** | *Tool > Geometry > Crease* | Intermediate | Quita la marca de afilado de TODAS las aristas del modelo de golpe. |
| 🎨 | **Crease PG** | *Tool > Geometry > Crease* | Advanced | Marca como afiladas las aristas que forman el borde de los PolyGroups. |
| 🎨 | **UnCrease PG** | *Tool > Geometry > Crease* | Advanced | Quita la marca de afilado de los bordes de los PolyGroups. |
| 🎭 | **Crease UM** | *Tool > Geometry > Crease* | Advanced | Marca como afiladas las aristas del borde de lo NO enmascarado. |
| 🎭 | **UnCrease UM** | *Tool > Geometry > Crease* | Advanced | Quita la marca de afilado del borde de lo no enmascarado. |
| ◗ | **Bevel** | *Tool > Geometry > Crease* | Advanced | Convierte las aristas marcadas en un BISEL real de geometría, en vez de dejarlas como una marca virtual. |
| 📏 | **PropWidth** | *Tool > Geometry > Crease* | Advanced | Hace que la anchura del bisel sea proporcional al tamaño de cada arista. |
| 🔢 | **Resolution** | *Tool > Geometry > Crease* | Advanced | Cuántos tramos de malla tiene el bisel generado (0 en tu captura). |
| 📐 | **Bevel Width** | *Tool > Geometry > Crease* | Advanced | La anchura de ese bisel (0.05 en tu captura). |


## Tool > Geometry > ShadowBox


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📦 | **Geometry > ShadowBox** | *Tool > Geometry > ShadowBox* | Advanced | Modo de modelado por SILUETAS: aparece una caja con tres planos (frontal, lateral y superior) y lo que pintas con máscara en cada plano se convierte en volumen 3D, como una intersección de sombras. Es una forma rápida y muy visual de bloquear una forma base a partir de dibujos planos. |
| 📦 | **ShadowBox** | *Tool > Geometry > ShadowBox* | Advanced | Enciende y apaga el modo ShadowBox sobre el SubTool actual. |
| 🔢 | **Res** | *Tool > Geometry > ShadowBox* | Advanced | La resolución del volumen generado (128 en tu captura): más resolución, más fiel al dibujo de la máscara y más pesado. |
| ✨ | **Polish** | *Tool > Geometry > ShadowBox* | Advanced | Cuánto se pulen los bordes del volumen resultante (10 en tu captura). |


## Tool > Geometry > ClayPolish


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✨ | **Geometry > ClayPolish** | *Tool > Geometry > ClayPolish* | Advanced | Pule toda la malla de golpe, marcando los bordes y aplanando las superficies, con un acabado 'de barro trabajado'. Se usa mucho justo después de DynaMesh para quitarle el aspecto blando. Conviene ir poco a poco: pasado de rosca deja el modelo con aspecto de plástico. |
| 📐 | **Max** | *Tool > Geometry > ClayPolish* | Advanced | El ángulo máximo entre los que actúa el pulido (25 en tu captura). |
| 📐 | **Min** | *Tool > Geometry > ClayPolish* | Advanced | El ángulo mínimo entre los que actúa el pulido (0 en tu captura). |
| 🔪 | **Sharp** | *Tool > Geometry > ClayPolish* | Advanced | Cuánto AFILA los bordes que entran en ese rango de ángulo (0 en tu captura). |
| 🫧 | **Soft** | *Tool > Geometry > ClayPolish* | Advanced | Cuánto SUAVIZA esas mismas zonas (0 en tu captura). |
| 🔪 | **RSharp** | *Tool > Geometry > ClayPolish* | Advanced | La versión inversa de Sharp: afila donde Sharp no llega. |
| 🫧 | **RSoft** | *Tool > Geometry > ClayPolish* | Advanced | La versión inversa de Soft: suaviza donde Soft no llega. |
| ➖ | **Edge** | *Tool > Geometry > ClayPolish* | Advanced | El tratamiento que reciben los bordes de la malla (0 en tu captura). |
| ▭ | **Surface** | *Tool > Geometry > ClayPolish* | Advanced | El tratamiento que reciben las superficies planas (0 en tu captura). |


## Tool > Geometry > DynaMesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧊 | **Geometry > DynaMesh** | *Tool > Geometry > DynaMesh* | Intermediate | El remallado sobre la marcha: rehace la malla entera de forma uniforme cada vez que la estiras demasiado, de modo que puedes esculpir como con plastilina sin quedarte sin polígonos. Se activa con el botón DynaMesh y a partir de ahí se remalla con Ctrl+arrastrar sobre el fondo. |
| 🔘 | **DynaMesh** | *Tool > Geometry > DynaMesh* | Intermediate | Activa el modo DynaMesh sobre el SubTool actual y hace el primer remallado. |
| 🎚️ | **Resolution** | *Tool > Geometry > DynaMesh* | Intermediate | La densidad de la malla resultante (128 en tu captura). Es EL deslizador a vigilar, porque de él depende cuánto detalle aguanta el modelo y cuánto pesa. |
| 🫧 | **Blur** | *Tool > Geometry > DynaMesh* | Intermediate | Difumina un poco el resultado del remallado (2 en tu captura). |
| 📐 | **SubProjection** | *Tool > Geometry > DynaMesh* | Advanced | Afina la proyección del detalle antiguo sobre la malla nueva (0.6 en tu captura). |
| 🎨 | **Groups** | *Tool > Geometry > DynaMesh* | Intermediate | Mantiene los PolyGroups al remallar, en vez de fundirlo todo en uno. |
| ✨ | **Polish** | *Tool > Geometry > DynaMesh* | Intermediate | Pule la malla resultante para quitarle el aspecto granulado. |
| 💎 | **Project** | *Tool > Geometry > DynaMesh* | Intermediate | Conserva el detalle que ya tenías al remallar (activo en tu captura). Casi siempre conviene tenerlo encendido: sin él, cada remallado te borra el trabajo fino. |
| 🎯 | **Picker** | *Tool > Geometry > DynaMesh* | Advanced | Toma la resolución directamente de una zona concreta del modelo, en vez de acertarla a ojo. |
| ➕ | **Add** | *Tool > Geometry > DynaMesh* | Advanced | Al remallar, los SubTools marcados con esta operación se SUMAN al volumen. |
| ➖ | **Sub** | *Tool > Geometry > DynaMesh* | Advanced | Al remallar, los SubTools marcados se RESTAN, agujereando el volumen. |
| ∩ | **And** | *Tool > Geometry > DynaMesh* | Advanced | Al remallar, se queda solo con la INTERSECCIÓN de los volúmenes. |
| 🥚 | **Create Shell** | *Tool > Geometry > DynaMesh* | Advanced | Convierte el volumen macizo en una cáscara HUECA, útil para impresión 3D y para ahorrar material. |
| 📐 | **Thickness** | *Tool > Geometry > DynaMesh* | Advanced | El grosor de pared de esa cáscara. |


## Tool > Geometry > Tessimate


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔺 | **Geometry > Tessimate** | *Tool > Geometry > Tessimate* | Advanced | Ajusta la densidad de la malla de forma LOCAL y adaptativa. Sirve para meter más malla justo donde vas a esculpir detalle y aligerar donde no hace falta, sin subdividir el modelo entero. |
| ➕ | **Tesselate** | *Tool > Geometry > Tessimate* | Advanced | AÑADE polígonos en la zona indicada (activo en naranja en tu captura), siguiendo los ejes marcados y lo que tengas enmascarado. |
| ➖ | **Decimate** | *Tool > Geometry > Tessimate* | Advanced | QUITA polígonos en la zona indicada, con los mismos criterios. |
| 📏 | **Polygons Size** | *Tool > Geometry > Tessimate* | Advanced | El tamaño de polígono objetivo al que tiende el resultado (1 en tu captura). |


## Tool > Geometry > ZRemesher


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔷 | **Geometry > ZRemesher: la cuenta de polígonos** | *Tool > Geometry > ZRemesher* | Intermediate | ZRemesher reconstruye automáticamente la topología en cuadrados limpios y bien repartidos: es lo que se usa cuando la malla se ha estirado de tanto esculpir, o antes de detallar en serio sobre un DynaMesh. Este primer bloque decide CUÁNTOS polígonos tendrá el resultado. |
| 🔢 | **Target Polygons Count** | *Tool > Geometry > ZRemesher* | Intermediate | El objetivo en MILES de polígonos (5 en tu captura, o sea unos 5.000). Es el número que decide si la malla sirve para animar en un motor o solo para esculpir. |
| ½ | **Half** | *Tool > Geometry > ZRemesher* | Intermediate | Fija el objetivo en la MITAD de los polígonos que tiene ahora la malla. |
| 🟰 | **Same** | *Tool > Geometry > ZRemesher* | Intermediate | Fija el objetivo en el MISMO número de polígonos que tiene ahora. |
| ×2 | **Double** | *Tool > Geometry > ZRemesher* | Intermediate | Fija el objetivo en el DOBLE de los polígonos actuales. |
| 🌊 | **Adapt** | *Tool > Geometry > ZRemesher* | Intermediate | Reparte la densidad de forma adaptativa según la forma (activo en tu captura): más malla donde hay curvatura y menos en las zonas lisas, en vez de repartirla uniforme. |
| 🎚️ | **AdaptiveSize** | *Tool > Geometry > ZRemesher* | Intermediate | Cuánto varía esa densidad entre las zonas curvas y las lisas (50 en tu captura). |
| 🎲 | **Retry** | *Tool > Geometry > ZRemesher* | Intermediate | Vuelve a intentar el remallado con otra semilla. A veces es lo único que hace falta cuando el resultado sale con el flujo de aristas torcido. |
| 🧭 | **Geometry > ZRemesher: cómo guiar el remallado** | *Tool > Geometry > ZRemesher* | Intermediate | Aquí está la diferencia entre un ZRemesher aprovechable y uno que hay que repetir: estos interruptores le dicen al programa qué debe respetar y por dónde quieres que pasen las líneas de la malla. |
| 📏 | **KeepCreases** | *Tool > Geometry > ZRemesher* | Intermediate | Conserva las aristas marcadas como duras en la sub-paleta Crease. |
| 🎨 | **KeepGroups** | *Tool > Geometry > ZRemesher* | Intermediate | Respeta los PolyGroups como límites. Es la mejor forma de decirle a ZRemesher por dónde quieres que pasen las líneas: pintas los grupos y él se ajusta a ellos. |
| ❄️ | **FreezeGroups** | *Tool > Geometry > ZRemesher* | Advanced | Congela los PolyGroups para que el remallado no los toque en absoluto. |
| ❄️ | **FreezeBorder** | *Tool > Geometry > ZRemesher* | Advanced | Congela los bordes abiertos de la malla para que no se muevan al remallar. |
| 🔍 | **DetectEdges** | *Tool > Geometry > ZRemesher* | Intermediate | Busca automáticamente los bordes duros del modelo y los respeta. |
| 🎨 | **KeepPolypaint** | *Tool > Geometry > ZRemesher* | Intermediate | Conserva el color pintado, que si no se pierde al remallar. Acuérdate de activarlo si has pintado. |
| 🖌️ | **Use Polypaint** | *Tool > Geometry > ZRemesher* | Advanced | Permite pintar de color las zonas donde quieres MÁS densidad de malla: pintas la cara de rojo y sale con más polígonos que la espalda. |
| 🎚️ | **ColorDensity** | *Tool > Geometry > ZRemesher* | Advanced | Cuánto influye ese color pintado en la densidad final. |
| 〰️ | **Curves Strength** | *Tool > Geometry > ZRemesher* | Advanced | Cuánto obedece el remallado a las guías que hayas dibujado con el pincel ZRemesherGuides (50 en tu captura). |


## Tool > Geometry > Modify Topology


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🪞 | **Geometry > Modify Topology: las operaciones grandes** | *Tool > Geometry > Modify Topology* | Advanced | Las cuatro operaciones que cambian la ESTRUCTURA de la malla y no su forma. Son las de mayor consecuencia de toda la sub-paleta: dos de ellas no tienen vuelta atrás. |
| 🪞 | **Mirror And Weld** | *Tool > Geometry > Modify Topology* | Advanced | Refleja el modelo en el eje marcado (XYZ) y suelda la unión. Es la forma habitual de hacer simétrico algo que solo has esculpido en un lado. |
| 🗑️ | **Del Hidden** | *Tool > Geometry > Modify Topology* | Advanced | BORRA de verdad lo que tengas oculto — sin vuelta atrás. Es como se recorta un modelo: ocultas lo que sobra con Ctrl+Mayús+arrastrar y lo eliminas. |
| 🕳️ | **Close Holes** | *Tool > Geometry > Modify Topology* | Advanced | Tapa los agujeros de la malla. Imprescindible antes de imprimir en 3D, porque una malla abierta no es un sólido y la impresora no sabe qué hacer con ella. |
| ✂️ | **Delete By Symmetry** | *Tool > Geometry > Modify Topology* | Advanced | Borra la mitad simétrica del modelo. Es el paso previo a rehacerla limpia con Mirror And Weld cuando los dos lados se han desincronizado. |
| 🔧 | **Geometry > Modify Topology: soldar e insertar** | *Tool > Geometry > Modify Topology* | Advanced | Las operaciones de limpieza y de meter una malla dentro de otra. |
| 🔗 | **WeldPoints** | *Tool > Geometry > Modify Topology* | Advanced | Suelda los vértices que estén muy cerca unos de otros. Es el arreglo de las mallas que llegan partidas de otro programa. |
| 📏 | **WeldDist** | *Tool > Geometry > Modify Topology* | Advanced | La distancia máxima a la que dos vértices se sueldan (1 en tu captura). |
| 📥 | **Insert Mesh** | *Tool > Geometry > Modify Topology* | Advanced | Mete otra malla dentro de la actual, pasando a formar parte del mismo SubTool. |
| 🧶 | **Micro Mesh** | *Tool > Geometry > Modify Topology* | Advanced | Sustituye cada polígono del modelo por una malla en miniatura: es la forma de convertir una superficie lisa en una tejida, escamada o remachada de una sola vez. Es hermano de NanoMesh, con la diferencia de que aquí el resultado es geometría real desde el principio. |
| ✂️ | **Geometry > Modify Topology: retoque de aristas y puntos** | *Tool > Geometry > Modify Topology* | Advanced | El retoque fino de la topología: arreglar un polo feo, limpiar sobras o despegar piezas sin rehacer la malla entera. |
| ▦ | **Grid Divide** | *Tool > Geometry > Modify Topology* | Advanced | Subdivide en rejilla en vez de por subdivisión normal. |
| 🔢 | **GD Segments** | *Tool > Geometry > Modify Topology* | Advanced | Cuántas divisiones hace Grid Divide. |
| 🔄 | **Spin Edge** | *Tool > Geometry > Modify Topology* | Advanced | Gira una arista suelta, para arreglar un polo feo sin rehacer la topología entera. |
| 📐 | **Align Edge** | *Tool > Geometry > Modify Topology* | Advanced | Realinea una arista suelta con las de su alrededor. |
| 🧹 | **Optimize Point** | *Tool > Geometry > Modify Topology* | Advanced | Limpia los puntos sobrantes que no aportan nada a la forma. |
| 🔺 | **MergeTris** | *Tool > Geometry > Modify Topology* | Advanced | Fusiona triángulos sobrantes para convertirlos en cuadrados. |
| 💥 | **Unweld All** | *Tool > Geometry > Modify Topology* | Advanced | Separa la malla del todo, dejando cada polígono suelto. |
| 🎨 | **Unweld Groups Border** | *Tool > Geometry > Modify Topology* | Advanced | Separa la malla solo por los bordes de los PolyGroups: es como se despega una pieza de armadura del cuerpo sin cortarla a mano. |
| 📋 | **Geometry > Modify Topology: copiar topología e igualar** | *Tool > Geometry > Modify Topology* | Advanced | Dos grupos que van juntos en el panel: llevarse la topología de un SubTool a otro, y repartir los polígonos para que tengan un tamaño uniforme. |
| 📋 | **Copy** | *Tool > Geometry > Modify Topology* | Advanced | Copia la topología del SubTool actual al portapapeles interno. |
| 📥 | **Paste Append** | *Tool > Geometry > Modify Topology* | Advanced | Pega esa topología AÑADIÉNDOLA a la que ya hay en el SubTool de destino. |
| ♻️ | **Paste Replace** | *Tool > Geometry > Modify Topology* | Advanced | Pega esa topología SUSTITUYENDO por completo la que había. |
| 🖌️ | **MeshFromBrush** | *Tool > Geometry > Modify Topology* | Advanced | Genera geometría a partir de la malla que lleve dentro el pincel activo (los de tipo Insert), sin tener que estamparla primero sobre el modelo. Muy cómodo para sacar una pieza suelta de un pincel IMM. |
| ▭ | **Equalize Surface Area** | *Tool > Geometry > Modify Topology* | Advanced | Reparte los polígonos igualando el ÁREA de cada cara. Ayuda cuando una zona ha quedado con la malla muy estirada. |
| 📏 | **Equalize Edge Length** | *Tool > Geometry > Modify Topology* | Advanced | Reparte los polígonos igualando la LONGITUD de las aristas. |


## Tool > Geometry > Repeat To Similar Parts


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔁 | **Geometry > Repeat To Similar Parts** | *Tool > Geometry > Repeat To Similar Parts* | Advanced | Repite el último cambio que hayas hecho en TODAS las piezas parecidas del modelo, en vez de repetirlo a mano una a una: si haces un remache y tienes veinte iguales, se aplica a los veinte. |
| ✅ | **Apply to Similar** | *Tool > Geometry > Repeat To Similar Parts* | Advanced | Ejecuta la repetición: aplica el último cambio a todas las piezas que cumplan el criterio. |
| 🎨 | **Groups** | *Tool > Geometry > Repeat To Similar Parts* | Advanced | Cuenta como 'parecida' toda pieza del mismo PolyGroup (activo en naranja en tu captura). |
| 🌈 | **Colors** | *Tool > Geometry > Repeat To Similar Parts* | Advanced | Cuenta como 'parecida' toda pieza del mismo color (activo en naranja en tu captura). |
| 🎭 | **Masking** | *Tool > Geometry > Repeat To Similar Parts* | Advanced | Cuenta como 'parecida' toda pieza con la misma máscara (activo en naranja en tu captura). |
| 🔺 | **Topology Only** | *Tool > Geometry > Repeat To Similar Parts* | Advanced | Compara únicamente la topología, ignorando el tamaño y la posición de cada pieza. |
| 🎚️ | **Precision** | *Tool > Geometry > Repeat To Similar Parts* | Advanced | Cuánto se tienen que parecer para contar (0.1 en tu captura): bajarlo acepta piezas más distintas, subirlo exige que sean casi idénticas. |


## Tool > Geometry > Stager


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎬 | **Geometry > Stager** | *Tool > Geometry > Stager* | Advanced | Guarda distintos ESTADOS del modelo y permite pasar de uno a otro. Sirve para comparar versiones de una escultura, hacer transiciones y montar presentaciones del proceso. Casi todo sale en gris hasta que hay más de un estado guardado. |
| 🏠 | **Home Stage** | *Tool > Geometry > Stager* | Advanced | El estado de partida, al que se vuelve siempre. |
| 🎯 | **Target Stage** | *Tool > Geometry > Stager* | Advanced | El estado de destino hacia el que se transforma el modelo. |
| 🔄 | **Switch Stage** | *Tool > Geometry > Stager* | Advanced | Cambia entre el estado de partida y el de destino. |
| 〰️ | **Interpolate** | *Tool > Geometry > Stager* | Advanced | Genera los pasos intermedios entre los dos estados, para ver la transformación. |
| 🔢 | **Stages Count** | *Tool > Geometry > Stager* | Advanced | Cuántos pasos intermedios se generan. |
| 📋 | **Copy** | *Tool > Geometry > Stager* | Advanced | Copia un estado guardado. |
| 📥 | **Paste** | *Tool > Geometry > Stager* | Advanced | Pega el estado copiado en otra ranura. |


## Tool > Geometry > Position


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📍 | **Geometry > Position** | *Tool > Geometry > Position* | Basic | Tres deslizadores numéricos que colocan el SubTool en el espacio (los tres a 0 en tu captura, o sea en el origen). A diferencia de mover con el Gizmo, aquí se escriben valores exactos, que es lo que hace falta para dejar una pieza justo en el centro o a una distancia concreta. |
| ↔️ | **X Position** | *Tool > Geometry > Position* | Basic | La posición del SubTool en el eje X, en unidades de ZBrush. |
| ↕️ | **Y Position** | *Tool > Geometry > Position* | Basic | La posición del SubTool en el eje Y, en unidades de ZBrush. |
| 🔃 | **Z Position** | *Tool > Geometry > Position* | Basic | La posición del SubTool en el eje Z, en unidades de ZBrush. |


## Tool > Geometry > Size


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📐 | **Geometry > Size** | *Tool > Geometry > Size* | Basic | Las dimensiones del SubTool en unidades de ZBrush (2.00002 en los cuatro en tu captura, porque el cilindro es simétrico). Igual que Position, es la forma de trabajar con números exactos en vez de a ojo — importante si el modelo tiene que encajar con medidas reales o llegar a un motor con la escala correcta. |
| 🔍 | **XYZ Size** | *Tool > Geometry > Size* | Basic | Escala los tres ejes a la vez manteniendo la proporción del objeto. |
| ↔️ | **X Size** | *Tool > Geometry > Size* | Basic | La dimensión en el eje X. Cambiarlo solo a él deforma el objeto. |
| ↕️ | **Y Size** | *Tool > Geometry > Size* | Basic | La dimensión en el eje Y. Cambiarlo solo a él deforma el objeto. |
| 🔃 | **Z Size** | *Tool > Geometry > Size* | Basic | La dimensión en el eje Z. Cambiarlo solo a él deforma el objeto. |


## Tool > Geometry > MeshIntegrity


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🩺 | **Geometry > MeshIntegrity** | *Tool > Geometry > MeshIntegrity* | Intermediate | El botiquín de la malla. Merece la pena pasarlo cuando ZBrush empieza a comportarse raro con un modelo, cuando falla una operación que debería funcionar, o antes de exportar a otro programa. |
| 🔍 | **Check Mesh Integrity** | *Tool > Geometry > MeshIntegrity* | Intermediate | Analiza el modelo buscando errores de estructura —polígonos degenerados, puntos sueltos, caras mal formadas— e informa de lo que encuentra. |
| 🔧 | **Fix Mesh** | *Tool > Geometry > MeshIntegrity* | Intermediate | Intenta reparar automáticamente los errores que ha encontrado el análisis. |


## Tool > ArrayMesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔢 | **ArrayMesh > el patrón de repetición** | *Tool > ArrayMesh* | Advanced | Repite el objeto muchas veces siguiendo un patrón, y todo se actualiza en vivo: cadenas, escaleras, columnas, vértebras, engranajes. Este bloque decide cuántas copias hay y qué cambia entre una y otra. |
| 🔢 | **Repeat** | *Tool > ArrayMesh* | Advanced | El número de copias del array. |
| ⛓️ | **Chain** | *Tool > ArrayMesh* | Advanced | Encadena las copias una tras otra, en vez de dejarlas sueltas. |
| ↔️ | **Offset** | *Tool > ArrayMesh* | Advanced | Modo en el que lo que cambia entre copia y copia es el DESPLAZAMIENTO (activo en naranja en tu captura). |
| 🔍 | **Scale** | *Tool > ArrayMesh* | Advanced | Modo en el que lo que cambia entre copia y copia es el TAMAÑO. |
| 🔄 | **Rotate** | *Tool > ArrayMesh* | Advanced | Modo en el que lo que cambia entre copia y copia es el GIRO. |
| 📍 | **Pivot** | *Tool > ArrayMesh* | Advanced | Modo en el que lo que cambia entre copia y copia es el PUNTO DE GIRO. |
| ↔️ | **X Amount** | *Tool > ArrayMesh* | Advanced | Cuánto cambia en el eje X entre copia y copia, según el modo elegido. |
| ↕️ | **Y Amount** | *Tool > ArrayMesh* | Advanced | Cuánto cambia en el eje Y entre copia y copia. |
| 🔃 | **Z Amount** | *Tool > ArrayMesh* | Advanced | Cuánto cambia en el eje Z entre copia y copia. |
| 📈 | **X Profile** | *Tool > ArrayMesh* | Advanced | Curva para que ese cambio en X no sea uniforme, sino que crezca, se afile o vaya y vuelva a lo largo de la cadena. |
| 📈 | **Y Profile** | *Tool > ArrayMesh* | Advanced | La misma curva para el eje Y. |
| 📈 | **Z Profile** | *Tool > ArrayMesh* | Advanced | La misma curva para el eje Z. |
| 🫧 | **Smooth** | *Tool > ArrayMesh* | Advanced | Suaviza la transición entre copias. |
| 🛤️ | **ArrayMesh > orientación, patrones con huecos y cierre** | *Tool > ArrayMesh* | Advanced | La orientación de la matriz, los patrones con huecos y cómo se convierte en geometría real. Hasta que pulses Make Mesh, el array es solo una vista previa. |
| 🛤️ | **AlignToPath** | *Tool > ArrayMesh* | Advanced | Hace que la matriz siga un recorrido en vez de crecer recta. |
| 🧭 | **AlignToAxis** | *Tool > ArrayMesh* | Advanced | Hace que la matriz siga un eje. |
| ▶️ | **PatternStart** | *Tool > ArrayMesh* | Advanced | Dónde empieza el patrón de huecos. Con este grupo se hacen vallas, escaleras con peldaños alternos o cadenas con eslabones intercalados. |
| 📏 | **PatternLength** | *Tool > ArrayMesh* | Advanced | Cada cuántas copias se repite el patrón. |
| 👁️ | **PatternOn** | *Tool > ArrayMesh* | Advanced | Cuántas copias se VEN dentro de cada repetición del patrón. |
| 🙈 | **PatternOff** | *Tool > ArrayMesh* | Advanced | Cuántas copias se SALTAN dentro de cada repetición del patrón. |
| 🧱 | **Make Mesh** | *Tool > ArrayMesh* | Advanced | Convierte todo el array en geometría REAL. |
| ⬆️ | **Extrude** | *Tool > ArrayMesh* | Advanced | Opción de Make Mesh: extruye al convertir. |
| 🔒 | **Close** | *Tool > ArrayMesh* | Advanced | Opción de Make Mesh: cierra los extremos al convertir. |
| 📐 | **Angle** | *Tool > ArrayMesh* | Advanced | Opción de Make Mesh: el ángulo con el que se resuelve ese cierre. |
| 🌾 | **Convert To NanoMesh** | *Tool > ArrayMesh* | Advanced | Pasa el array al sistema NanoMesh. |
| 📚 | **Lightbox ▶ Arrays Presets** | *Tool > ArrayMesh* | Advanced | Abre ejemplos ya montados, que es la mejor forma de entender qué puede hacer esta sub-paleta. |
| 🔗 | **ArrayMesh > interruptor y colocación** | *Tool > ArrayMesh* | Advanced | El botón que enciende el array y todo lo que sirve para colocarlo bien en el espacio. |
| 🔘 | **Array Mesh** | *Tool > ArrayMesh* | Advanced | El botón que activa el array sobre el SubTool. |
| 📐 | **Transpose** | *Tool > ArrayMesh* | Advanced | Deja colocar la cadena de copias con la Transpose Line, arrastrándola por el espacio. |
| 🔒 | **Lock Pos** | *Tool > ArrayMesh* | Advanced | Congela la posición para que al mover el original no se descoloque todo lo demás. |
| 🔒 | **Lock Size** | *Tool > ArrayMesh* | Advanced | Congela el tamaño por el mismo motivo. |
| 🔀 | **SwitchXY** | *Tool > ArrayMesh* | Advanced | Intercambia los ejes X e Y de golpe. Es el arreglo rápido cuando el array crece en la dirección equivocada, mucho más cómodo que ir corrigiendo los Amount uno a uno. |
| 🔀 | **SwitchXZ** | *Tool > ArrayMesh* | Advanced | Intercambia los ejes X y Z de golpe. |
| 🔀 | **SwitchYZ** | *Tool > ArrayMesh* | Advanced | Intercambia los ejes Y y Z de golpe. |
| 🪞 | **X Mirror** | *Tool > ArrayMesh* | Advanced | Refleja el patrón en el eje X. |
| 🪞 | **Y Mirror** | *Tool > ArrayMesh* | Advanced | Refleja el patrón en el eje Y. |
| 🪞 | **Z Mirror** | *Tool > ArrayMesh* | Advanced | Refleja el patrón en el eje Z. |
| 📐 | **X Align** | *Tool > ArrayMesh* | Advanced | Alinea el patrón en el eje X. |
| 📐 | **Y Align** | *Tool > ArrayMesh* | Advanced | Alinea el patrón en el eje Y. |
| 📐 | **Z Align** | *Tool > ArrayMesh* | Advanced | Alinea el patrón en el eje Z. |


## Tool > ArrayMesh > Transform Stage


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🪜 | **ArrayMesh > Transform Stage** | *Tool > ArrayMesh > Transform Stage* | Advanced | Lo más potente de la sub-paleta: permite encadenar VARIAS etapas de transformación, de modo que el array se puede curvar, escalar y girar en fases distintas. Así es como se hace una escalera de caracol (una etapa que sube y otra que gira) o una columna vertebral que se estrecha mientras se curva. Cada etapa tiene sus propios Amount y Profile por eje. |
| ➕ | **Append New** | *Tool > ArrayMesh > Transform Stage* | Advanced | Añade una etapa de transformación al final de la cadena. |
| 📌 | **Insert New** | *Tool > ArrayMesh > Transform Stage* | Advanced | Mete una etapa nueva en medio de las que ya hay. |
| ↩️ | **Reset** | *Tool > ArrayMesh > Transform Stage* | Advanced | Devuelve una etapa a sus valores de partida. |
| 🗑️ | **Delete** | *Tool > ArrayMesh > Transform Stage* | Advanced | Borra una etapa de la cadena. |
| 📋 | **Copy** | *Tool > ArrayMesh > Transform Stage* | Advanced | Copia los valores de una etapa. |
| 📥 | **Paste** | *Tool > ArrayMesh > Transform Stage* | Advanced | Pega esos valores en otra etapa, para reutilizarlos. |
| ↔️ | **X Amount** | *Tool > ArrayMesh > Transform Stage* | Advanced | Cuánto se transforma en el eje X en ESTA etapa, según el modo elegido. |
| ↕️ | **Y Amount** | *Tool > ArrayMesh > Transform Stage* | Advanced | Cuánto se transforma en el eje Y en esta etapa. |
| 🔃 | **Z Amount** | *Tool > ArrayMesh > Transform Stage* | Advanced | Cuánto se transforma en el eje Z en esta etapa. |
| 📈 | **X Profile** | *Tool > ArrayMesh > Transform Stage* | Advanced | La curva que hace que ese cambio en X no sea uniforme a lo largo de la cadena. |
| 📈 | **Y Profile** | *Tool > ArrayMesh > Transform Stage* | Advanced | La misma curva para el eje Y de esta etapa. |
| 📈 | **Z Profile** | *Tool > ArrayMesh > Transform Stage* | Advanced | La misma curva para el eje Z de esta etapa. |


## Tool > NanoMesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌾 | **NanoMesh > activar y ajustar la pieza sembrada** | *Tool > NanoMesh* | Advanced | Siembra una malla pequeña sobre CADA polígono del modelo: remaches, escamas, púas, hojas, eslabones. LA CLAVE de esta sub-paleta es que los deslizadores van SIEMPRE EN PAREJA valor + variación: sin las variaciones las copias salen calcadas y se nota a la legua. |
| 🔘 | **NanoMesh On** | *Tool > NanoMesh* | Advanced | Activa el sistema NanoMesh sobre el SubTool. |
| ✏️ | **Edit Mesh** | *Tool > NanoMesh* | Advanced | Entra a editar la pieza que se repite. |
| 🙈 | **Hide Others** | *Tool > NanoMesh* | Advanced | Oculta todo lo demás para ver solo las copias sembradas mientras las ajustas. |
| 🪟 | **Split Screen** | *Tool > NanoMesh* | Advanced | Parte la pantalla para enseñar a la vez el modelo y la pieza que se siembra. |
| 🔢 | **Index** | *Tool > NanoMesh* | Advanced | Selecciona cuál de las piezas del inventario se usa. |
| ↔️ | **Width** | *Tool > NanoMesh* | Advanced | La anchura de cada copia. |
| 🎲 | **WVar** | *Tool > NanoMesh* | Advanced | Cuánta variación aleatoria tiene la anchura entre copias. |
| 📏 | **Length** | *Tool > NanoMesh* | Advanced | La longitud de cada copia. |
| 🎲 | **LVar** | *Tool > NanoMesh* | Advanced | Cuánta variación aleatoria tiene la longitud entre copias. |
| ↕️ | **Height** | *Tool > NanoMesh* | Advanced | La altura de cada copia. |
| 🎲 | **HVar** | *Tool > NanoMesh* | Advanced | Cuánta variación aleatoria tiene la altura entre copias. |
| ↔️ | **XOffset** | *Tool > NanoMesh* | Advanced | Desplaza cada copia en el eje X respecto a su polígono. |
| 🎲 | **XOVar** | *Tool > NanoMesh* | Advanced | La variación aleatoria de ese desplazamiento en X. |
| ↕️ | **YOffset** | *Tool > NanoMesh* | Advanced | Desplaza cada copia en el eje Y. |
| 🎲 | **YOVar** | *Tool > NanoMesh* | Advanced | La variación aleatoria de ese desplazamiento en Y. |
| 🔃 | **ZOffset** | *Tool > NanoMesh* | Advanced | Desplaza cada copia en el eje Z, o sea la hunde o la levanta respecto a la superficie. |
| 🎲 | **ZOVar** | *Tool > NanoMesh* | Advanced | La variación aleatoria de ese desplazamiento en Z. |
| 🔄 | **XRotation** | *Tool > NanoMesh* | Advanced | Gira cada copia sobre el eje X. |
| 🎲 | **XRVar** | *Tool > NanoMesh* | Advanced | La variación aleatoria de ese giro en X. |
| 🔄 | **YRotation** | *Tool > NanoMesh* | Advanced | Gira cada copia sobre el eje Y. |
| 🎲 | **YRVar** | *Tool > NanoMesh* | Advanced | La variación aleatoria de ese giro en Y. |
| 🔄 | **ZRotation** | *Tool > NanoMesh* | Advanced | Gira cada copia sobre el eje Z. |
| 🎲 | **ZRVar** | *Tool > NanoMesh* | Advanced | La variación aleatoria de ese giro en Z. |
| 🎲 | **NanoMesh > cómo se adapta cada copia al polígono** | *Tool > NanoMesh* | Advanced | Cómo se adapta y se repite cada copia DENTRO del polígono que la aloja. |
| 📐 | **Prop** | *Tool > NanoMesh* | Advanced | Ajusta la pieza de forma PROPORCIONAL al polígono. |
| 📐 | **Fit** | *Tool > NanoMesh* | Advanced | AJUSTA la pieza al polígono, deformándola si hace falta. |
| 🪣 | **Fill** | *Tool > NanoMesh* | Advanced | RELLENA el polígono con la pieza. |
| 🔒 | **Cons** | *Tool > NanoMesh* | Advanced | RESTRINGE la pieza a los límites del polígono. |
| ✂️ | **Clip** | *Tool > NanoMesh* | Advanced | RECORTA lo que sobresalga del polígono. |
| ↔️ | **H Tile** | *Tool > NanoMesh* | Advanced | Repite la pieza en horizontal dentro de cada polígono. |
| ↕️ | **V Tile** | *Tool > NanoMesh* | Advanced | Repite la pieza en vertical dentro de cada polígono. |
| 🔄 | **Flip H** | *Tool > NanoMesh* | Advanced | Voltea la pieza en horizontal. |
| 🔄 | **Flip V** | *Tool > NanoMesh* | Advanced | Voltea la pieza en vertical. |
| 🎰 | **NanoMesh > cómo se reparten las copias** | *Tool > NanoMesh* | Advanced | Cómo se distribuyen las copias por la superficie. Pulsar la semilla hasta que salga un reparto que te guste es parte del flujo normal de trabajo, no una chapuza. |
| ▦ | **Pattern** | *Tool > NanoMesh* | Advanced | La distribución general de las copias (Grid en tu captura). |
| 🎲 | **Random Distribution** | *Tool > NanoMesh* | Advanced | Aleatoriza esa distribución. |
| 🌱 | **Random Seed** | *Tool > NanoMesh* | Advanced | La semilla del azar: cambiarla da un reparto distinto sin tocar nada más. |
| 🎲 | **RandArray** | *Tool > NanoMesh* | Advanced | Otra fuente de azar para variar el resultado. |
| 👁️ | **Show Instances** | *Tool > NanoMesh* | Advanced | Muestra las copias mientras trabajas. |
| 📍 | **ShowPlacement** | *Tool > NanoMesh* | Advanced | Muestra dónde se van a colocar las copias. |
| ❄️ | **FreezePlacement** | *Tool > NanoMesh* | Advanced | Congela la colocación para que deje de recalcularse. |
| 🎨 | **Modulate By Color** | *Tool > NanoMesh* | Advanced | Hace que el color pintado module el resultado: pintas de blanco donde quieres las piezas grandes y de negro donde no quieres ninguna. |


## Tool > NanoMesh > Alignment


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧭 | **NanoMesh > Alignment** | *Tool > NanoMesh > Alignment* | Advanced | Decide hacia dónde MIRA cada copia sembrada. Es lo que separa unas escamas bien puestas de un montón de piezas giradas al azar. |
| 🧭 | **Align To Normal** | *Tool > NanoMesh > Alignment* | Advanced | Orienta la copia perpendicular a la superficie, que es lo normal para escamas o púas. |
| ➖ | **Align To Short Edge** | *Tool > NanoMesh > Alignment* | Advanced | La alinea con la arista CORTA del polígono. |
| ➖ | **Align To Long Edge** | *Tool > NanoMesh > Alignment* | Advanced | La alinea con la arista LARGA. Es lo que se usa cuando la pieza debe seguir la dirección de la malla, como en eslabones o tejidos. |
| ➖ | **Align To Near Edge** | *Tool > NanoMesh > Alignment* | Advanced | La alinea con la arista más CERCANA. |
| 🔢 | **Align By Point Order** | *Tool > NanoMesh > Alignment* | Advanced | La orienta siguiendo el orden de los puntos del polígono. |
| 🎲 | **Align To Random Edge** | *Tool > NanoMesh > Alignment* | Advanced | Aleatoriza la orientación entre las aristas disponibles. |
| 🚫 | **No Alignment** | *Tool > NanoMesh > Alignment* | Advanced | Deja las copias sin orientar. |


## Tool > NanoMesh > Colorize


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎨 | **NanoMesh > Colorize** | *Tool > NanoMesh > Colorize* | Advanced | Controla el color y el material de las copias sembradas: si heredan los de la malla original o usan los que tengas activos en la interfaz. |
| 🎨 | **Mesh MRGB** | *Tool > NanoMesh > Colorize* | Advanced | Usa el color y el material de la malla original. |
| 🎨 | **Mesh Color** | *Tool > NanoMesh > Colorize* | Advanced | Usa solo el color de la malla original. |
| 🧱 | **Mesh Material** | *Tool > NanoMesh > Colorize* | Advanced | Usa solo el material de la malla original. |
| 🖌️ | **UI MRGB** | *Tool > NanoMesh > Colorize* | Advanced | Usa el color y el material que tengas activos en la interfaz. |
| 🖌️ | **UI Color** | *Tool > NanoMesh > Colorize* | Advanced | Usa solo el color activo en la interfaz. |
| 🖌️ | **UI Material** | *Tool > NanoMesh > Colorize* | Advanced | Usa solo el material activo en la interfaz. |
| 🌈 | **Adjust Hue** | *Tool > NanoMesh > Colorize* | Advanced | Retoca el tono de todas las copias a la vez. |
| 💧 | **Adjust Saturation** | *Tool > NanoMesh > Colorize* | Advanced | Retoca la saturación de todas las copias a la vez. |
| 🌗 | **Adjust Intensity** | *Tool > NanoMesh > Colorize* | Advanced | Retoca la intensidad de todas las copias a la vez. |
| 🎲 | **Adjust Variations** | *Tool > NanoMesh > Colorize* | Advanced | Introduce diferencias aleatorias entre copias para que no queden todas del mismo color exacto. |
| ↩️ | **Restore NanoMesh MRGB** | *Tool > NanoMesh > Colorize* | Advanced | Devuelve el color original a las copias. |


## Tool > NanoMesh > Uv, Inventory


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗺️ | **NanoMesh > Uv e Inventory** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Dos bloques que van juntos: de dónde salen las UV y la textura de las copias, y cómo se gestionan las piezas cargadas en el inventario. |
| 🗺️ | **Use Base Mesh UVs** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Las copias heredan las UV del modelo de base en vez de las suyas propias. |
| 🖼️ | **Use Base Mesh Texture** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Las copias heredan la textura del modelo de base. |
| 🧱 | **One To Mesh** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Convierte UNA pieza del inventario en geometría real. |
| 🖌️ | **All To Brush** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Pasa TODAS las piezas a un pincel reutilizable. |
| ♻️ | **Replace NanoMesh From Brush** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Cambia la pieza sembrada por la que lleve dentro un pincel. |
| 🗑️ | **Delete One** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Borra una pieza del inventario. |
| 🗑️ | **Delete All** | *Tool > NanoMesh > Uv, Inventory* | Advanced | Borra todas las piezas del inventario. |


## Tool > Slime Bridge


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕸️ | **Tool > Slime Bridge** | *Tool > Slime Bridge* | Advanced | Genera puentes ORGÁNICOS entre superficies cercanas: hilos de baba, telarañas, mucosidad, raíces o tejido conectivo. Muy útil en criaturas y en terror. |
| 🪢 | **Tension** | *Tool > Slime Bridge* | Advanced | La tirantez de los hilos (0 en tu captura): valores altos los dejan tensos y rectos, bajos los dejan colgando. |
| 🔢 | **Bridges** | *Tool > Slime Bridge* | Advanced | El número de puentes principales (20 en tu captura). |
| 🌿 | **Branches** | *Tool > Slime Bridge* | Advanced | Cuántas ramificaciones salen de esos puentes (10 en tu captura). |
| 🧵 | **Capillaries** | *Tool > Slime Bridge* | Advanced | Los hilos finos secundarios que dan el aspecto viscoso (20 en tu captura). |


## Tool > Thick Skin


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧥 | **Tool > Thick Skin** | *Tool > Thick Skin* | Advanced | Da GROSOR a una superficie que no lo tiene, generando una segunda capa por debajo — la misma idea que el modificador Solidify de Blender. Útil para ropa, hojas, placas o cualquier malla abierta que necesite volumen real para renderizar o imprimir. Sale en gris hasta que se activa. |
| 🔘 | **Thick Skin** | *Tool > Thick Skin* | Advanced | Activa el grosor sobre el SubTool. |
| 📐 | **Thickness** | *Tool > Thick Skin* | Advanced | Cuánto grosor se genera. |


## Tool > FiberMesh > Modifiers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💇 | **FiberMesh > el flujo de trabajo** | *Tool > FiberMesh > Modifiers* | Advanced | Genera pelo, hierba, plumas o fibras a partir de la zona que tengas ENMASCARADA. El flujo es siempre el mismo: enmascarar, Preview, ajustar y Accept. Empezar desde un preset de LightBox y retocar es mucho más rápido que partir de cero. |
| 📚 | **Lightbox ▶ Fibers** | *Tool > FiberMesh > Modifiers* | Advanced | Abre la biblioteca de ajustes que trae ZBrush ya preparados: pelo corto, hierba, plumas... |
| 📂 | **Open** | *Tool > FiberMesh > Modifiers* | Advanced | Carga unos ajustes de fibras guardados por ti. |
| 💾 | **Save** | *Tool > FiberMesh > Modifiers* | Advanced | Guarda los ajustes de fibras actuales. |
| 👀 | **Preview** | *Tool > FiberMesh > Modifiers* | Advanced | Muestra el resultado en vivo sobre el modelo, sin crearlo todavía. |
| ✅ | **Accept** | *Tool > FiberMesh > Modifiers* | Advanced | Crea las fibras de verdad, como un SubTool nuevo. |
| 🎚️ | **FiberMesh > los pares valor y variación** | *Tool > FiberMesh > Modifiers* | Advanced | Los deslizadores van casi todos en pareja valor + variación (la V del final): el valor pone la medida general y la variación cuánto se aparta cada fibra de ella, que es lo que evita que todas salgan clavadas. |
| 🔢 | **MaxFibers** | *Tool > FiberMesh > Modifiers* | Advanced | La cantidad de fibras que se generan. |
| 🎲 | **DeV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de esa cantidad. |
| 📏 | **Length** | *Tool > FiberMesh > Modifiers* | Advanced | La longitud de las fibras. |
| 🎲 | **LeV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de la longitud. |
| 🧶 | **Coverage** | *Tool > FiberMesh > Modifiers* | Advanced | El grosor de cada mechón. |
| 🎲 | **CoV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de ese grosor. |
| 🔻 | **Slim** | *Tool > FiberMesh > Modifiers* | Advanced | Cuánto se afinan las fibras hacia la punta. |
| 🎲 | **SlV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de ese afinado. |
| 🌍 | **Gravity** | *Tool > FiberMesh > Modifiers* | Advanced | Cuánto caen las fibras por su peso. |
| 🎲 | **NoV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de esa caída. |
| 🌀 | **Twist** | *Tool > FiberMesh > Modifiers* | Advanced | Cuánto se retuercen las fibras. |
| 🎲 | **TwV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de ese retorcido. |
| 🪢 | **Clumps** | *Tool > FiberMesh > Modifiers* | Advanced | Cuánto se agrupan las fibras en mechones. |
| 🎲 | **ClV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de ese agrupamiento. |
| 🌾 | **FiberMesh > la forma de las fibras** | *Tool > FiberMesh > Modifiers* | Advanced | Qué controla la máscara, cómo se enrollan y en qué dirección crecen, más las curvas de perfil que hacen que el cambio no sea lineal de la raíz a la punta. |
| 🎭 | **ByMask** | *Tool > FiberMesh > Modifiers* | Advanced | Hace que la máscara controle la DENSIDAD de las fibras. |
| 🎭 | **ByArea** | *Tool > FiberMesh > Modifiers* | Advanced | Hace que la máscara controle la LONGITUD. Pintar la máscara con degradado y usar ByArea es como se consigue que el pelo sea más largo en la coronilla. |
| 🌀 | **Revolve Radius** | *Tool > FiberMesh > Modifiers* | Advanced | El radio con el que se enrollan las fibras. Es como se hacen los rizos. |
| 🌀 | **Revolve Rate** | *Tool > FiberMesh > Modifiers* | Advanced | Cada cuánto dan una vuelta al enrollarse. |
| ↔️ | **HTangent** | *Tool > FiberMesh > Modifiers* | Advanced | Inclina la dirección general de las fibras en horizontal. |
| ↕️ | **VTangent** | *Tool > FiberMesh > Modifiers* | Advanced | Inclina la dirección general de las fibras en vertical. |
| 📈 | **Length Profile** | *Tool > FiberMesh > Modifiers* | Advanced | Curva que define cómo varía el LARGO desde la raíz hasta la punta. |
| 📈 | **Width Profile** | *Tool > FiberMesh > Modifiers* | Advanced | Curva que define cómo varía el GROSOR de la raíz a la punta. Es la que hace que un mechón parezca pelo de verdad y no cerdas de escoba. |
| 📈 | **Gravity Profile** | *Tool > FiberMesh > Modifiers* | Advanced | Curva que define cómo CAE la fibra a lo largo de su longitud. |
| 🎨 | **FiberMesh > el color y el dibujado** | *Tool > FiberMesh > Modifiers* | Advanced | El color de la raíz y el de la punta con sus variaciones, más los ajustes de dibujado. Un degradado de raíz oscura a punta clara es lo que hace que el pelo no parezca de plástico. |
| 🎨 | **Base** | *Tool > FiberMesh > Modifiers* | Advanced | El bloque de color de la RAÍZ de la fibra. |
| 🎨 | **BColor** | *Tool > FiberMesh > Modifiers* | Advanced | El color concreto de la raíz. |
| 🎲 | **BCVar** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria del color de la raíz entre fibras. |
| 🎨 | **Tip** | *Tool > FiberMesh > Modifiers* | Advanced | El bloque de color de la PUNTA de la fibra. |
| 🎨 | **TColor** | *Tool > FiberMesh > Modifiers* | Advanced | El color concreto de la punta. |
| 🎲 | **TCVar** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria del color de la punta entre fibras. |
| 👻 | **Transparent** | *Tool > FiberMesh > Modifiers* | Advanced | Dibuja las fibras con transparencia. |
| 🫧 | **Antialiased** | *Tool > FiberMesh > Modifiers* | Advanced | Suaviza los bordes de las fibras al dibujarlas. |
| 🔢 | **Segments** | *Tool > FiberMesh > Modifiers* | Advanced | La resolución de cada fibra: pocos segmentos dan pelo rígido, muchos dan pelo que se curva bien y pesa más. |
| 🧬 | **FiberMesh > Imbed** | *Tool > FiberMesh > Modifiers* | Advanced | Un solo control, pero de los que más se notan. |
| 🧬 | **Imbed** | *Tool > FiberMesh > Modifiers* | Advanced | Decide cuánto se HUNDE la raíz de la fibra dentro del modelo. Si lo dejas corto se ven los agujeros por donde salen los pelos, y ese es el fallo más típico al empezar con FiberMesh. |
| 📏 | **FiberMesh > escalado, variaciones y guiado** | *Tool > FiberMesh > Modifiers* | Advanced | El resto de controles del bloque, que es enorme. Aquí están las variaciones de dirección, sin las cuales el resultado parece césped artificial. |
| 🔻 | **ScaleRoot** | *Tool > FiberMesh > Modifiers* | Advanced | Escala la fibra en la RAÍZ. Es la forma directa de afilarla sin tocar los perfiles. |
| 🔺 | **ScaleTip** | *Tool > FiberMesh > Modifiers* | Advanced | Escala la fibra en la PUNTA. |
| 🎲 | **HtV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de HTangent: cuánto se desvía cada fibra de la inclinación horizontal general. |
| 🎲 | **VtV** | *Tool > FiberMesh > Modifiers* | Advanced | La variación aleatoria de VTangent, lo mismo en vertical. |
| 🌗 | **TColorI** | *Tool > FiberMesh > Modifiers* | Advanced | La intensidad del color de la punta, que acompaña a TColor y TCVar. |
| 📐 | **Max Size** | *Tool > FiberMesh > Modifiers* | Advanced | Limita el tamaño máximo de las fibras. |
| ↕️ | **Ht** | *Tool > FiberMesh > Modifiers* | Advanced | El alto dentro de ese límite de tamaño máximo. |
| ↔️ | **Vt** | *Tool > FiberMesh > Modifiers* | Advanced | El ancho dentro de ese límite de tamaño máximo. |
| 🧭 | **MorphTarget Guided** | *Tool > FiberMesh > Modifiers* | Advanced | Hace que las fibras sigan un Morph Target guardado en vez de crecer libres. Es como se consiguen peinados controlados en lugar de una melena al viento. |


## Tool > FiberMesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚙️ | **FiberMesh > Preview Settings, Export Curves, BPR Settings y Export Displacement** | *Tool > FiberMesh* | Advanced | Los cuatro bloques finales de FiberMesh: aligerar la vista previa, sacar las fibras a otro programa, controlar cómo se renderizan y exportar mapas. |


## Tool > FiberMesh > Preview Settings


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚡ | **FastPreview** | *Tool > FiberMesh* | Advanced | Aligera la previsualización para que no se atasque con muchas fibras. |
| 👀 | **PRE Vis** | *Tool > FiberMesh* | Advanced | El otro ajuste de la vista previa rápida. |


## Tool > FiberMesh > Export Curves


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📤 | **Export Curves** | *Tool > FiberMesh* | Advanced | Exporta las fibras como CURVAS para llevarlas a otro programa (Maya, Blender) y peinarlas o animarlas allí. |


## Tool > FiberMesh > BPR Settings


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✨ | **RootAniso** | *Tool > FiberMesh* | Advanced | El brillo anisotrópico en la RAÍZ, que es lo que hace que el pelo brille como pelo y no como plástico. |
| ✨ | **TipAniso** | *Tool > FiberMesh* | Advanced | El brillo anisotrópico en la PUNTA. |
| 🔢 | **Subdiv** | *Tool > FiberMesh* | Advanced | La subdivisión de cada fibra al renderizar. |
| 🔷 | **Sides** | *Tool > FiberMesh* | Advanced | Cuántos lados tiene la sección de cada fibra al renderizar. |
| 📐 | **Radius** | *Tool > FiberMesh* | Advanced | El radio de cada fibra al renderizar. |


## Tool > FiberMesh > Export Displacement


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗺️ | **Export Displacement** | *Tool > FiberMesh* | Advanced | Saca mapas de desplazamiento de las fibras. |
| 🧭 | **Tangent** | *Tool > FiberMesh* | Advanced | Calcula ese mapa en espacio tangente. |
| 💎 | **32Bits** | *Tool > FiberMesh* | Advanced | Lo calcula en 32 bits, para no perder precisión. |
| 🧭 | **Export Vectors Disp** | *Tool > FiberMesh* | Advanced | Exporta el mapa como desplazamiento VECTORIAL, que admite detalle que se dobla sobre sí mismo. |


## Tool > Geometry HD


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔬 | **Tool > Geometry HD: el detalle extremo** | *Tool > Geometry HD* | Advanced | Permite llegar a densidades de malla que no caben en memoria de forma normal — cientos de millones de polígonos — para detalle extremo tipo poros, escamas finas o grano de piedra. Es de las últimas cosas que se tocan en un modelo, ya en fase de acabado. |
| ➗ | **DivideHD** | *Tool > Geometry HD* | Advanced | Añade niveles HD. |
| 🔢 | **SculptHD Subdiv** | *Tool > Geometry HD* | Advanced | Indica en qué nivel HD trabajar. |
| 🖌️ | **Sculpt HD** | *Tool > Geometry HD* | Advanced | Entra en el modo de escultura HD, donde solo se carga en memoria la REGIÓN que estás tocando. Por eso puede con tanta densidad. |
| ⭕ | **RadialRgn** | *Tool > Geometry HD* | Advanced | Define esa región de trabajo. |


## Tool > Masking > Mask By Fibers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💇 | **Masking > Mask By Fibers** | *Tool > Masking > Mask By Fibers* | Advanced | Máscaras generadas a partir de las FIBRAS de un FiberMesh. Todo el bloque sale en gris si el SubTool activo no es un FiberMesh. |
| 🛡️ | **FiberMask** | *Tool > Masking > Mask By Fibers* | Advanced | Enmascara según las fibras del FiberMesh. |
| 🔄 | **FiberUnmask** | *Tool > Masking > Mask By Fibers* | Advanced | Hace lo contrario: desenmascara según las fibras. |
| 📈 | **FiberMask Profile** | *Tool > Masking > Mask By Fibers* | Advanced | Curva con la que se afina cómo se reparte la máscara de la RAÍZ a la PUNTA de la fibra. Permite, por ejemplo, proteger solo las puntas para trabajar el color de la raíz. |


## Tool > Masking > Mask By AO


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💡 | **Mask Ambient Occlusion** | *Tool > Masking* | Advanced | Enmascara las zonas donde no llega la luz, es decir los recovecos y las uniones. Perfecto para meter suciedad o desgaste solo donde tocaría. |
| 🎚️ | **Occlusion Intensity** | *Tool > Masking* | Advanced | La fuerza de esa máscara de oclusión (1 en tu captura). |
| 📏 | **AO ScanDist** | *Tool > Masking* | Advanced | Hasta qué distancia mira el cálculo de oclusión (0.1 en tu captura). |
| 📐 | **AO Aperture** | *Tool > Masking* | Advanced | El ángulo del barrido con el que se busca la oclusión (90 en tu captura). |


## Tool > Masking > Mask By Cavity


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕳️ | **Mask By Cavity** | *Tool > Masking* | Advanced | Enmascara las CAVIDADES, o sea las grietas y los surcos que has esculpido. Es la técnica clásica para pintar el fondo de los poros y las arrugas de otro color: enmascaras por cavidad, inviertes y pintas. |
| 🫧 | **Blur** | *Tool > Masking* | Advanced | Suaviza el borde de la máscara de cavidad (2 en tu captura). |
| 🎚️ | **Intensity** | *Tool > Masking* | Advanced | La fuerza de la máscara de cavidad (100 en tu captura). |
| 📈 | **Cavity Profile** | *Tool > Masking* | Advanced | Curva de control de cómo se reparte esa máscara según la profundidad del surco. |


## Tool > Masking > Mask By Depth


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌫️ | **Mask By Depth** | *Tool > Masking* | Advanced | Enmascara según la PROFUNDIDAD respecto a la cámara. |
| 🫧 | **Blur** | *Tool > Masking* | Advanced | Suaviza el borde de la máscara por profundidad. |
| 📈 | **Depth Profile** | *Tool > Masking* | Advanced | Curva de control del reparto de esa máscara. |


## Tool > Masking > Mask By Normals


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧭 | **Mask By Normals** | *Tool > Masking* | Advanced | Enmascara según hacia dónde MIRA cada zona: por ejemplo, solo lo que apunta hacia arriba. |
| 📈 | **Normals Profile** | *Tool > Masking* | Advanced | Curva de control de esa máscara por orientación. |


## Tool > Masking > Mask By Smoothness


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🫧 | **Mask By Smoothness** | *Tool > Masking* | Advanced | Enmascara las zonas LISAS frente a las rugosas. |
| 📏 | **Range** | *Tool > Masking* | Advanced | El margen dentro del cual se considera que una zona es lisa (10 en tu captura). |
| 📉 | **Falloff** | *Tool > Masking* | Advanced | Cómo se desvanece esa máscara hacia los bordes (100 en tu captura). |


## Tool > Masking > Mask By Curvature


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌀 | **Mask By Curvature** | *Tool > Masking* | Advanced | Enmascara según la CURVATURA de la superficie. Ideal para aislar las zonas convexas o las cóncavas. |
| 🎚️ | **Strength** | *Tool > Masking* | Advanced | La fuerza de la máscara por curvatura (25 en tu captura). |
| 🫧 | **Blur** | *Tool > Masking* | Advanced | Suaviza el borde de la máscara por curvatura (1 en tu captura). |


## Tool > Masking > Mask PeaksAndValleys


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⛰️ | **Mask PeaksAndValleys** | *Tool > Masking* | Advanced | Separa los PICOS de los VALLES del relieve. Muy usada para desgastes, porque el uso real desgasta los picos y ensucia los valles. |
| 📏 | **PVRange** | *Tool > Masking* | Advanced | El margen de altura que separa un pico de un valle (4 en tu captura). |
| 📐 | **PVCoverage** | *Tool > Masking* | Advanced | Cuánta superficie abarca la máscara resultante (25 en tu captura). |


## Tool > Masking > Mask By Color


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖌️ | **Mask By Polypaint** | *Tool > Masking* | Advanced | Genera la máscara a partir del COLOR pintado en sí. |
| 🌗 | **Mask By Intensity** | *Tool > Masking* | Advanced | Genera la máscara según lo CLARO U OSCURO del color. |
| 🌈 | **Mask By Hue** | *Tool > Masking* | Advanced | Genera la máscara según el TONO del color. |
| 💧 | **Mask By Saturation** | *Tool > Masking* | Advanced | Genera la máscara según lo VIVO del color. |


## Tool > Masking > Mask By Alpha


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🏷️ | **Mask By Alpha** | *Tool > Masking* | Advanced | Usa un alpha como máscara, estampándolo sobre el modelo. |
| 🎚️ | **Intens** | *Tool > Masking* | Advanced | La fuerza con la que se aplica ese alpha (100 en tu captura). |
| 🔀 | **Blend** | *Tool > Masking* | Advanced | Cómo se mezcla con la máscara que ya hubiera (100 en tu captura). |


## Tool > Masking > Masking Apply


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🏷️ | **Mask Alpha** | *Tool > Masking* | Advanced | Proyecta un ALPHA sobre el modelo como máscara. |
| 🖼️ | **Mask Txtr** | *Tool > Masking* | Advanced | Proyecta una TEXTURA sobre el modelo como máscara. |
| 🎚️ | **Mask Intensity** | *Tool > Masking* | Advanced | Cuánto afecta esa proyección (50 en tu captura). |


## Tool > Polypaint > From Draft


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📐 | **From Draft** | *Tool > Polypaint* | Advanced | Pinta el modelo según su ángulo de desmoldeo respecto a una dirección. Sirve para ver de un vistazo si una pieza se podría fabricar o si tiene zonas en contrasalida. |
| 📐 | **DraftAngle** | *Tool > Polypaint* | Advanced | El ángulo límite de desmoldeo. |
| 🧭 | **SetDir** | *Tool > Polypaint* | Advanced | Toma como dirección de desmoldeo la vista actual de la cámara. |
| 🔃 | **InvDir** | *Tool > Polypaint* | Advanced | Invierte esa dirección. |


## Tool > Polypaint > From Thickness


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📏 | **From Thickness** | *Tool > Polypaint* | Advanced | Pinta según el GROSOR de la malla en cada punto. Es la forma rápida de encontrar las zonas demasiado finas que se van a romper al imprimir en 3D. |
| 🔢 | **Quality** | *Tool > Polypaint* | Advanced | La precisión del cálculo de grosor (16 en tu captura). |
| 📉 | **Min Thickness** | *Tool > Polypaint* | Advanced | El grosor mínimo del rango que se traduce en color. |
| 📈 | **Max Thickness** | *Tool > Polypaint* | Advanced | El grosor máximo del rango que se traduce en color. |


## Tool > UV Map > Create (Projection)


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📦 | **UV Map > Create: las proyecciones geométricas** | *Tool > UV Map > Create (Projection)* | Advanced | Cada botón despliega el modelo con una forma geométrica sencilla, envolviéndolo como si le pusieras un papel encima. Son rápidas y valen para piezas simples, pero deforman en cuanto la forma se complica. |
| 🛢️ | **Uvc** | *Tool > UV Map > Create (Projection)* | Advanced | Proyección CILÍNDRICA, buena para brazos, troncos y columnas. |
| ▭ | **Uvp** | *Tool > UV Map > Create (Projection)* | Advanced | Proyección PLANA, para superficies que miran a un lado. |
| ⚪ | **Uvs** | *Tool > UV Map > Create (Projection)* | Advanced | Proyección ESFÉRICA, para cabezas y objetos redondos. |
| 📦 | **Uvb** | *Tool > UV Map > Create (Projection)* | Advanced | Proyección en CAJA, para piezas rectangulares. |
| 🎁 | **Uvbt** | *Tool > UV Map > Create (Projection)* | Advanced | Proyección en caja con las TAPAS aparte. |
| 🔲 | **UVTile** | *Tool > UV Map > Create (Projection)* | Advanced | Asigna a cada polígono el cuadro entero de textura. |


## Tool > UV Map > Create


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚠️ | **UV Map > Create: los desplegados automáticos de ZBrush** | *Tool > UV Map > Create (Projection)* | Advanced | AVISO IMPORTANTE: estos desplegados sirven para pintar y sacar mapas DENTRO de ZBrush, pero NO son UVs utilizables en Unity, Unreal o Maya, porque no forman islas coherentes ni se pueden retocar en Photoshop — verás un mosaico de trocitos sueltos sin sentido. REGLA PRÁCTICA: para algo que va a un motor, despliega con UV Master (Zplugin) o en Maya, nunca con estas. |
| 🧩 | **AUVTiles** | *Tool > UV Map > Create (Projection)* | Advanced | Reparte cada polígono en su trocito de textura, de forma adaptativa al área real. |
| 🧩 | **PUVTiles** | *Tool > UV Map > Create (Projection)* | Advanced | La variante que reparte los trozos con el mismo tamaño para todos. |
| 🧩 | **GUVTiles** | *Tool > UV Map > Create (Projection)* | Advanced | La variante que agrupa los trozos siguiendo la geometría. |
| 🎚️ | **AUVRatio** | *Tool > UV Map > Create (Projection)* | Advanced | Cuánto se ajusta el tamaño de cada trozo al área real del polígono. |
| ↔️ | **Hrepeat** | *Tool > UV Map > Create (Projection)* | Advanced | Repite la textura en horizontal sobre el objeto. |
| ↕️ | **Vrepeat** | *Tool > UV Map > Create (Projection)* | Advanced | Repite la textura en vertical sobre el objeto. |
| 💇 | **FiberUV** | *Tool > UV Map > Create (Projection)* | Advanced | Desplegado propio de las fibras. Sale en gris porque es solo para FiberMesh. |


## Tool > UV Map > Create (Unwrap)


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✂️ | **UV Map > Create: Unwrap** | *Tool > UV Map > Create (Unwrap)* | Advanced | El desplegado de verdad integrado en ZBrush: abre la malla por unas costuras y la aplana. Aun así, para un desplegado limpio y controlado la herramienta cómoda sigue siendo UV Master, en Zplugin. |
| ✂️ | **Unwrap** | *Tool > UV Map > Create (Unwrap)* | Advanced | Abre la malla por las costuras y la aplana sobre el plano de textura. |
| 🤖 | **Auto Seams** | *Tool > UV Map > Create (Unwrap)* | Advanced | Deja que el programa decida solo dónde cortar. |
| 📏 | **Creased edges** | *Tool > UV Map > Create (Unwrap)* | Advanced | Corta por las aristas marcadas como Crease (activo en naranja en tu captura), lo que te da control sobre dónde quieres las costuras. |
| 🔁 | **Crease Seams** | *Tool > UV Map > Create (Unwrap)* | Advanced | Hace lo contrario: marca como Crease las costuras que han salido del desplegado. |
| 🪞 | **Symmetry** | *Tool > UV Map > Create (Unwrap)* | Advanced | Despliega respetando la simetría del modelo, de modo que las dos mitades quedan idénticas (activo en tu captura). Muy recomendable en personajes, porque permite pintar una vez y reflejar. |


## Tool > UV Map > Adjust


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔄 | **UV Map > Adjust** | *Tool > UV Map > Adjust* | Advanced | Retoques sobre unas UVs que ya existen, sin volver a desplegar. Son los botones que salvan la situación cuando la textura aparece del revés o girada al aplicarla, sin tener que rehacer nada. |
| ↔️ | **AdjU** | *Tool > UV Map > Adjust* | Advanced | Desplaza el desplegado en horizontal. |
| ↕️ | **AdjV** | *Tool > UV Map > Adjust* | Advanced | Desplaza el desplegado en vertical. |
| ✅ | **ApplyAdj** | *Tool > UV Map > Adjust* | Advanced | Confirma el ajuste de desplazamiento. |
| 🔀 | **Switch U<>V** | *Tool > UV Map > Adjust* | Advanced | Intercambia los dos ejes, o sea gira el desplegado 90 grados. |
| 🔄 | **Cycle UV** | *Tool > UV Map > Adjust* | Advanced | Rota la asignación de coordenadas. |
| ↔️ | **Flip U** | *Tool > UV Map > Adjust* | Advanced | Voltea el desplegado en el eje horizontal. |
| ↕️ | **Flip V** | *Tool > UV Map > Adjust* | Advanced | Voltea el desplegado en el eje vertical. |


## Tool > Texture Map > Create


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✨ | **Texture Map > Create** | *Tool > Texture Map > Create* | Advanced | El bloque que convierte información del modelo en una IMAGEN. Es el puente entre lo que has hecho en ZBrush y lo que puede leer un motor. |
| 🎨 | **New From Polypaint** | *Tool > Texture Map > Create* | Advanced | EL botón importante de toda la sub-paleta: pasa el color que has pintado por vértice a una textura de verdad. Es el paso obligatorio para que ese color se vea en Unity o Unreal, y necesita UVs. |
| 🎭 | **New From Masking** | *Tool > Texture Map > Create* | Advanced | Convierte la máscara en una textura en blanco y negro, perfecta como máscara de opacidad, de rugosidad o de mezcla en un shader. |
| 🗺️ | **New From UV Map** | *Tool > Texture Map > Create* | Advanced | Dibuja el desplegado sobre la textura, para verlo como imagen. |
| 🔲 | **New From UV Check** | *Tool > Texture Map > Create* | Advanced | Pinta el patrón de comprobación —el típico damero de cuadros— con el que se ven de un vistazo los estirones y las zonas mal desplegadas. |
| 🔢 | **New From Vertex Order** | *Tool > Texture Map > Create* | Advanced | Codifica en color el orden de los VÉRTICES. Se usa en flujos técnicos y en efectos de shader. |
| 🔢 | **New From Poly Order** | *Tool > Texture Map > Create* | Advanced | Codifica en color el orden de los POLÍGONOS, con el mismo uso técnico. |


## Tool > Displacement Map


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖼️ | **Displacement Map > el mapa asignado** | *Tool > Displacement Map* | Advanced | Un mapa de desplazamiento guarda el detalle de alta resolución como una imagen en escala de grises, para que un modelo de pocos polígonos parezca tenerlo. Es lo que se usa en cine y render; en videojuegos lo normal es el Normal Map, porque el desplazamiento real cuesta mucho en tiempo real. En tu captura todo sale en gris porque aún no hay ningún mapa creado. |
| 🔘 | **Disp On** | *Tool > Displacement Map* | Advanced | Activa el mapa de desplazamiento sobre el modelo. |
| 📋 | **Clone Disp** | *Tool > Displacement Map* | Advanced | Copia el mapa a la paleta Alpha, que es como se saca de aquí para exportarlo o retocarlo. |
| 🎛️ | **Mode** | *Tool > Displacement Map* | Advanced | Cómo se aplica el desplazamiento. |
| 🎚️ | **Intensity** | *Tool > Displacement Map* | Advanced | Cuánto se aplica el desplazamiento. |
| 🧱 | **Apply DispMap** | *Tool > Displacement Map* | Advanced | Aplica de verdad ese desplazamiento a la malla, convirtiéndolo en geometría real. |
| ⚙️ | **Displacement Map > generar el mapa** | *Tool > Displacement Map* | Advanced | El mapa guarda la altura real de cada punto, para recuperar el detalle esculpido en otro programa. EL ORDEN IMPORTA MUCHO: hay que tener el modelo subdividido y BAJAR a SDiv 1 antes de generarlo, porque si no no hay nada que comparar y el mapa sale vacío. |
| ⚙️ | **Create DispMap** | *Tool > Displacement Map* | Advanced | Calcula el mapa a partir de la diferencia entre el nivel de subdivisión más bajo y el más alto. |
| 💾 | **Create And Export Map** | *Tool > Displacement Map* | Advanced | Lo genera y lo guarda en disco de una vez, que es lo cómodo cuando ya tienes los ajustes decididos. |
| 🎚️ | **Displacement Map > los ajustes de generación** | *Tool > Displacement Map* | Advanced | Los ajustes con los que se calcula el mapa. Los dos últimos son los que piden los renderizadores serios. |
| 🎯 | **Adaptive** | *Tool > Displacement Map* | Advanced | Mejora la precisión adaptándose a la malla. |
| 🔬 | **DPSubPix** | *Tool > Displacement Map* | Advanced | Añade precisión de sub-píxel al cálculo. |
| 🫧 | **SmoothUV** | *Tool > Displacement Map* | Advanced | Suaviza el mapa siguiendo las UVs. |
| 🌗 | **Mid** | *Tool > Displacement Map* | Advanced | El valor gris medio, que es el nivel 'cero' del desplazamiento — el equivalente al MidValue de la paleta Alpha. Por debajo hunde y por encima levanta. |
| 🔍 | **Scale** | *Tool > Displacement Map* | Advanced | Multiplica la intensidad del desplazamiento guardado. |
| ↕️ | **Flip V** | *Tool > Displacement Map* | Advanced | Voltea el mapa verticalmente. Es lo que hay que tocar cuando el programa de destino lee las texturas del revés, el clásico desencuentro entre ZBrush y el resto del mundo. |
| 🔀 | **3 Channels** | *Tool > Displacement Map* | Advanced | Guarda el mapa en tres canales en vez de en uno. |
| 💎 | **32Bit** | *Tool > Displacement Map* | Advanced | Guarda en coma flotante de 32 bits, que es lo que piden los renderizadores serios para no perder precisión en las alturas ni ver escalones. |


## Tool > Normal Map


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🟣 | **Normal Map > generar el mapa** | *Tool > Normal Map* | Advanced | EL mapa importante para videojuegos: guarda el detalle como direcciones de superficie (esos mapas azulados) y hace que un modelo de pocos polígonos se vea con todos los poros y arrugas del de millones. |
| 🧭 | **Tangent** | *Tool > Normal Map* | Advanced | Genera el mapa en ESPACIO TANGENTE, que es el que usan Unity y Unreal (activo en naranja en tu captura). Sin él sale en espacio objeto, que solo vale para modelos que no se deforman — o sea, nunca para un personaje animado. |
| ⚙️ | **Create NormalMap** | *Tool > Normal Map* | Advanced | Genera el mapa de normales. |
| 📋 | **Clone NM** | *Tool > Normal Map* | Advanced | Lo copia a la paleta Texture para poder exportarlo o retocarlo. |
| 🔀 | **Normal Map > calidad y orientación de los canales** | *Tool > Normal Map* | Advanced | Los ajustes de calidad y de orientación. Los tres primeros vienen activados y conviene dejarlos así; los últimos son los que arreglan el problema clásico del relieve invertido. |
| 🎯 | **Adaptive** | *Tool > Normal Map* | Advanced | Mejora la precisión del cálculo. |
| 🫧 | **SmoothUV** | *Tool > Normal Map* | Advanced | Suaviza el mapa siguiendo las UVs. |
| 🧭 | **SNormals** | *Tool > Normal Map* | Advanced | Usa las normales suavizadas en vez de las duras. |
| 🔀 | **SwitchRG** | *Tool > Normal Map* | Advanced | Intercambia los canales rojo y verde. |
| 🔴 | **FlipR** | *Tool > Normal Map* | Advanced | Invierte el canal rojo. |
| 🟢 | **FlipG** | *Tool > Normal Map* | Advanced | Invierte el canal verde, y es el que se toca de verdad: unos programas esperan el verde hacia arriba y otros hacia abajo (OpenGL contra DirectX). Si al aplicar el mapa en Unity tus arrugas se ven HUNDIDAS donde deberían sobresalir, este es exactamente el botón, y te ahorra rehacer el mapa entero. |
| 🔵 | **FlipB** | *Tool > Normal Map* | Advanced | Invierte el canal azul. |


## Tool > Vector Displacement Map


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧭 | **Vector Displacement Map** | *Tool > Vector Displacement Map* | Advanced | El hermano mayor del Displacement Map: en vez de guardar solo cuánto sube cada punto, guarda un VECTOR completo, así que puede representar detalle que se dobla sobre sí mismo —orejas, colmillos, pliegues muy salientes— que un mapa en escala de grises no puede. En videojuegos casi no se usa; en cine, Maya o Houdini sí. |
| 🧭 | **vd Tangent** | *Tool > Vector Displacement Map* | Advanced | Calcula el mapa en espacio tangente (activo en tu captura). |
| 💎 | **vd 32Bit** | *Tool > Vector Displacement Map* | Advanced | Lo calcula en 32 bits, casi obligatorio para que no salgan escalones (activo en tu captura). |
| 🫧 | **vd SUV** | *Tool > Vector Displacement Map* | Advanced | Suaviza según las UVs (activo en tu captura). |
| 🧭 | **vd SNormals** | *Tool > Vector Displacement Map* | Advanced | Suaviza según las normales suavizadas (activo en tu captura). |
| 💾 | **CreateAndExport VDMap** | *Tool > Vector Displacement Map* | Advanced | Genera el mapa vectorial y lo guarda en disco. |


## Tool > Vector Displacement Map > Diagnostic


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🩺 | **Create Diagnostic Files** | *Tool > Vector Displacement Map* | Advanced | Saca archivos de comprobación para verificar que el mapa ha salido bien. Está en el bloque Diagnostic. |


## Tool > Display Properties > BPR Settings


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌓 | **Display Properties > BPR Settings: visibilidad y sombra** | *Tool > Display Properties > BPR Settings* | Advanced | Ajustes de ESTE SubTool concreto para el render BPR (Best Preview Render, el render interno de ZBrush). Permiten que una pieza se comporte distinto al renderizar sin tocar ni el modelo ni su material. |
| 👻 | **BPR Transparent Shading** | *Tool > Display Properties > BPR Settings* | Advanced | Dibuja este SubTool transparente en el render. |
| 🎚️ | **BPR Visibility** | *Tool > Display Properties > BPR Settings* | Advanced | Cuánto se ve la pieza en el render, de 0 a 100 (100 en tu captura). Bajarlo permite que salga semitransparente solo al renderizar — muy útil para enseñar lo que hay debajo de una armadura. |
| 🌑 | **BPR Shadows** | *Tool > Display Properties > BPR Settings* | Advanced | Cuánta sombra proyecta esta pieza (100 en tu captura). Bajarlo evita que un elemento suelto ensucie de sombras el resto de la escena. |
| 🎨 | **BPR Material Blend** | *Tool > Display Properties > BPR Settings* | Advanced | Mezcla su material con el de los demás SubTools (0 en tu captura). |
| 🪞 | **Display Properties > BPR Settings: normales y ruido** | *Tool > Display Properties > BPR Settings* | Advanced | El resto del bloque: cómo se suavizan las normales al renderizar y cuánto ruido procedural se calcula. |
| 🫧 | **BPR Smooth Normals** | *Tool > Display Properties > BPR Settings* | Advanced | Suaviza las normales al renderizar (activo en naranja en tu captura), o sea disimula las facetas de un modelo poco subdividido sin tener que subdividirlo más. |
| 🧭 | **Use BPR Smooth Tangent Normals** | *Tool > Display Properties > BPR Settings* | Advanced | Hace que ese suavizado se calcule en espacio tangente, que es lo que evita los bordes facetados en superficies curvas al renderizar. En pantalla queda cortado como 'Tanger...'. |
| 🌾 | **3D Noise Max Resolution** | *Tool > Display Properties > BPR Settings* | Advanced | Limita la resolución del ruido procedural de la sub-paleta Surface cuando se renderiza (8 en tu captura), para que un ruido muy fino no dispare el tiempo de cálculo. |

