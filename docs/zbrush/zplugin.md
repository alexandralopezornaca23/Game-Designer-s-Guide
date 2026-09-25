# Zplugin


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧩 | **Zplugin: qué es la paleta y sus 21 complementos** | *Menú superior > Zplugin* | Intermediate | La paleta donde viven los COMPLEMENTOS, o sea funciones que no forman parte del núcleo de ZBrush pero vienen instaladas de fábrica. En tu versión hay 21: Intersection Masker, QuickSketch, 3D Print Hub, Ambient Occlusion, BevelPro, Maya Blend Shapes, Decimation Master, Misc Utilities, FBX ExportImport, Multi Map Exporter, PolyGroupIt, Projection Master, Scale Master, SubTool Master, Text 3D & Vector Shapes, Transpose Master, USD Format, UV Master, ZBenchMark, ZBrush To Photoshop y ZColor. Los 21 tienen su fila propia debajo. Tres de ellos —BevelPro, Projection Master y ZColor— no se despliegan dentro de la paleta: son botones que abren su propia ventana o una aplicación aparte. |
| ⭐ | **Zplugin: los cuatro complementos imprescindibles para un flujo de videojuegos** | *Menú superior > Zplugin* | Intermediate | De los 21, los que de verdad vas a usar en tu flujo hacia un motor son cuatro, y merece la pena tenerlos localizados. UV MASTER despliega las UV de forma automática, que es lo que te evita hacerlo a mano. DECIMATION MASTER baja la cuenta de polígonos conservando la forma. MULTI MAP EXPORTER saca de una tacada el mapa de normales, el de desplazamiento y el de color de TODOS los SubTools. Y FBX EXPORTIMPORT es el formato con el que el modelo entra en Unity o Unreal. El orden natural de trabajo es ese mismo: desplegar UV, generar mapas, reducir polígonos y exportar. |


## Zplugin > Intersection Masker


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✂️ | **Zplugin > Intersection Masker** | *Menú superior > Zplugin > Intersection Masker* | Advanced | Busca dónde se CRUZAN dos mallas —dónde un SubTool se mete dentro de otro— y crea una máscara justo en esa zona. Es más útil de lo que parece: te dice de un vistazo dónde una pieza de armadura está atravesando el cuerpo, o dónde el pelo se hunde en la cabeza, que son los errores que luego se ven feísimos en el render y cuesta encontrar a ojo. |
| 🎭 | **Create Intersection Mask** | *Menú superior > Zplugin > Intersection Masker* | Advanced | Crea la máscara en la zona de intersección (en gris hasta que hay algo válido seleccionado). Con la máscara creada puedes invertirla y mover solo esa parte hacia fuera para resolver el cruce. |


## Zplugin > QuickSketch


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✍️ | **Zplugin > QuickSketch** | *Menú superior > Zplugin > QuickSketch* | Intermediate | La idea es no salir de ZBrush cuando se te ocurre una silueta: dibujas la forma en plano, la conviertes en volumen y ya tienes la base para esculpir encima. |
| ✍️ | **Quick Sketch** | *Menú superior > Zplugin > QuickSketch* | Intermediate | Convierte el lienzo en una hoja de dibujo 2D para bocetar a mano alzada con el lápiz de la tableta, y después ese boceto se puede pasar a 3D con Make 3D. Las herramientas de dibujo son básicas comparadas con las de un programa 2D de verdad. |


## Zplugin > 3D Print Hub > File Import


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖨️ | **3D Print Hub > File Import** | *Zplugin > 3D Print Hub > File Import* | Advanced | El complemento para preparar una pieza para IMPRESIÓN 3D, que es donde de verdad importan las medidas reales. Este primer bloque trae modelos de fuera. |
| 📥 | **Import STL File** | *Zplugin > 3D Print Hub > File Import* | Advanced | Carga un archivo STL, el formato estándar de impresión. Un STL es geometría pura sin color ni materiales, así que lo que entra por aquí es solo la forma. |
| ⚙️ | **Import Options** | *Zplugin > 3D Print Hub > File Import* | Advanced | Despliega los ajustes de importación. |


## Zplugin > 3D Print Hub > Set Export Size


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📐 | **3D Print Hub > Set Export Size** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | El bloque importante, porque aquí se decide cuánto va a medir la figura de VERDAD. Los tres ejes están enlazados por las proporciones para que no se deforme al cambiar uno. |
| 🔄 | **Update Size Ratios** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | Recalcula las proporciones entre los tres ejes. |
| 📏 | **mm** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | Fija la unidad en milímetros (activo en naranja en tu captura). |
| 📏 | **inch** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | Fija la unidad en pulgadas. |
| ↔️ | **X(mm)** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | La medida real de la pieza en el eje X (25.4 en tu captura, que es exactamente una pulgada: el tamaño por defecto). |
| ↕️ | **Y(mm)** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | La medida real en el eje Y. |
| 🔃 | **Z(mm)** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | La medida real en el eje Z. |
| 🔍 | **Check Mesh Volume** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | Comprueba que la malla sea un volumen CERRADO, sin agujeros ni caras invertidas. Una impresora no puede imprimir una superficie abierta, así que este botón es el que te evita el disgusto de descubrirlo ya en el laminador. |
| ⚙️ | **Size Options** | *Zplugin > 3D Print Hub > Set Export Size* | Advanced | Abre más ajustes de tamaño. |


## Zplugin > 3D Print Hub > File Export


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📤 | **3D Print Hub > File Export: los formatos principales** | *Zplugin > 3D Print Hub > File Export* | Advanced | Sacar la pieza ya dimensionada. |
| 🖨️ | **Send to Preform** | *Zplugin > 3D Print Hub > File Export* | Advanced | La manda directamente a PreForm, el programa de las impresoras Formlabs, sin pasar por archivo. El botón ? de al lado abre su ayuda. |
| 💾 | **Export to STL** | *Zplugin > 3D Print Hub > File Export* | Advanced | El formato clásico, el que acepta cualquier impresora, pero solo guarda la forma, sin color. |
| 🌈 | **Export to 3MF** | *Zplugin > 3D Print Hub > File Export* | Advanced | El formato moderno, que sí guarda color y materiales: es el que quieres si vas a imprimir en color. |
| 💾 | **3D Print Hub > File Export: los otros formatos** | *Zplugin > 3D Print Hub > File Export* | Advanced | CONSEJO: pasa siempre por Decimation Master antes de exportar, porque un STL de veinte millones de polígonos se atraganta en el laminador y para imprimir no aporta nada — la impresora no puede reproducir un detalle más fino que su propia resolución. |
| 🗿 | **Export to VRML** | *Zplugin > 3D Print Hub > File Export* | Advanced | Un formato con color más antiguo, que usan algunas impresoras de escayola. |
| 📦 | **Export to OBJ** | *Zplugin > 3D Print Hub > File Export* | Advanced | El formato general de intercambio, útil si el modelo va a pasar por otro programa antes de imprimirse. |
| ⚙️ | **Export Options** | *Zplugin > 3D Print Hub > File Export* | Advanced | Despliega los ajustes de exportación. |


## Menú superior > Zplugin > Ambient Occlusion


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕳️ | **Zplugin > Ambient Occlusion: el muestreo** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | Calcula la oclusión ambiental y la CUECE en el modelo como Polypaint, en lugar de solo mostrarla en el render. Es distinto de BPR AO: aquí el resultado se queda pintado en la malla y viaja con ella. |
| 📏 | **Distance** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | Hasta qué distancia se busca oclusión (0.0999 en tu captura), o sea el número que decide si se marcan solo las grietas finas o también los huecos grandes. |
| 📐 | **Aperture** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | La apertura del cono de muestreo en grados (90 en tu captura). |
| 🔬 | **Samples** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | Las muestras: cuantas más, más limpio y más lento (256 en tu captura). |
| 🫧 | **Smooth** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | Suaviza el resultado para quitarle el grano (8 en tu captura). |
| ⚙️ | **Zplugin > Ambient Occlusion: el cálculo** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | PARA QUÉ TE SIRVE: si estás preparando una lámina de portafolio, cocer la oclusión como Polypaint y luego multiplicarla sobre el color da un resultado muy sólido y sin coste de render. Y para un modelo de videojuego, es una forma de tener el AO listo para hornearlo a textura. |
| ▶️ | **Compute** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | Lanza el cálculo de la oclusión. |
| 📦 | **OcclusionVolume** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | Define el volumen dentro del cual se calcula. |
| 🔢 | **Resolution** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | La resolución de ese volumen de cálculo (1024 en tu captura). |
| 🔄 | **Recalc** | *Menú superior > Zplugin > Ambient Occlusion* | Advanced | Repite el cálculo sin volver a configurarlo todo, que es lo que usas mientras vas ajustando Distance. |


## Zplugin > BevelPro


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📐 | **Zplugin > BevelPro** | *Menú superior > Zplugin > BevelPro* | Advanced | Lo que hace BevelPro es BISELAR aristas — el pequeño chaflán que redondea un canto vivo. Es el detalle que más separa un objeto que parece modelado de uno que parece real, porque en el mundo físico no existen las aristas perfectamente afiladas: siempre hay un mínimo redondeo que atrapa la luz y dibuja una línea brillante en el canto. Para props de videojuego, pasar BevelPro por los cantos es lo que hace que la silueta se lea y que el objeto deje de parecer un bloque de plastilina. |
| 📐 | **BevelPro** | *Menú superior > Zplugin > BevelPro* | Advanced | Según su nota emergente: 'Open the BevelPro app with current subtool'. NO es un panel que se despliegue dentro de ZBrush, sino un programa APARTE que se abre con tu pieza ya cargada, y por eso su contenido no aparece en la paleta. Trabaja sobre el SubTool activo, así que selecciónalo antes de pulsar. |
| ✨ | **Zplugin > BevelPro: para qué sirve un bisel** | *Menú superior > Zplugin > BevelPro* | Advanced | Lo que hace BevelPro es BISELAR aristas — el pequeño chaflán que redondea un canto vivo. Es el detalle que más separa un objeto que parece modelado de uno que parece real, porque en el mundo físico no existen las aristas perfectamente afiladas: siempre hay un mínimo redondeo, aunque sea de una décima de milímetro, que atrapa la luz y dibuja una línea brillante en el canto. Para props de videojuego —una caja, un arma, una pieza de armadura— pasar BevelPro por los cantos es lo que hace que la silueta se lea y que el objeto deje de parecer un bloque de plastilina. |


## Menú superior > Zplugin > Maya Blend Shapes


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 😀 | **Zplugin > Maya Blend Shapes** | *Menú superior > Zplugin > Maya Blend Shapes* | Advanced | El puente para llevar EXPRESIONES a Maya. Un 'blend shape' es una deformación guardada de la malla —la cara sonriendo, la cara con los ojos cerrados— que luego se mezcla con la neutra para animar. En ZBrush esas variaciones se hacen con Layers, y este complemento las exporta como blend shapes de Maya: esculpes las expresiones donde se esculpe cómodo y llegan a Maya listas para conectarlas al rig facial. |
| 📄 | **New Layer** | *Menú superior > Zplugin > Maya Blend Shapes* | Advanced | Crea una capa nueva para esculpir en ella la expresión. |
| 🔇 | **TurnOff All** | *Menú superior > Zplugin > Maya Blend Shapes* | Advanced | Apaga todas las capas de golpe para volver a la cara neutra. |
| 🎯 | **Selected** | *Menú superior > Zplugin > Maya Blend Shapes* | Advanced | Trabaja solo sobre el SubTool seleccionado. |
| 👁️ | **Visible** | *Menú superior > Zplugin > Maya Blend Shapes* | Advanced | Trabaja sobre los SubTools visibles (activo en naranja en tu captura). |
| 🧩 | **All** | *Menú superior > Zplugin > Maya Blend Shapes* | Advanced | Trabaja sobre todos los SubTools. |
| 📤 | **Export Blend Shapes** | *Menú superior > Zplugin > Maya Blend Shapes* | Advanced | Saca el conjunto de expresiones como blend shapes. |


## Zplugin > Decimation Master > 1-Options


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📉 | **Decimation Master > 1-Options** | *Zplugin > Decimation Master > 1-Options* | Intermediate | El complemento que baja la cuenta de polígonos conservando la forma, y el paso obligado para sacar una escultura hacia un motor de videojuegos o hacia una impresora. Funciona en tres fases numeradas, y esta primera decide QUÉ SE RESPETA. |
| ❄️ | **Freeze borders** | *Zplugin > Decimation Master > 1-Options* | Intermediate | Congela los bordes abiertos para que no se deformen, importante si la pieza tiene que encajar con otra. |
| 🗺️ | **Keep UVs** | *Zplugin > Decimation Master > 1-Options* | Intermediate | Conserva las coordenadas UV: si ya tenías el modelo desplegado y texturizado, la textura sigue funcionando después de reducir. |
| 🎨 | **Use and Keep Polypaint** | *Zplugin > Decimation Master > 1-Options* | Intermediate | Conserva el color pintado y además usa la información de color para decidir dónde hacen falta más polígonos. |
| ⚖️ | **Polypaint weight** | *Zplugin > Decimation Master > 1-Options* | Intermediate | Regula cuánto pesa ese criterio de color (en gris en tu captura). |


## Zplugin > Decimation Master > 2-Pre-process


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⏳ | **Decimation Master > 2-Pre-process** | *Zplugin > Decimation Master > 2-Pre-process* | Intermediate | El cálculo pesado, el que de verdad tarda: puede llevar varios minutos en un modelo de millones de polígonos, pero se hace UNA SOLA VEZ. Después ya puedes probar distintos niveles de reducción al instante. Por eso el orden correcto es preprocesar todo de golpe y luego ir tanteando el porcentaje. |
| 🎯 | **Pre-process Current** | *Zplugin > Decimation Master > 2-Pre-process* | Intermediate | Analiza el SubTool activo. |
| 🧩 | **Pre-process All** | *Zplugin > Decimation Master > 2-Pre-process* | Intermediate | Analiza todos los SubTools de una vez. |


## Zplugin > Decimation Master > 3-Decimate


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚖️ | **Decimation Master > 3-Decimate** | *Zplugin > Decimation Master > 3-Decimate* | Intermediate | La fase que reduce de verdad, con tres formas de decir cuánto. Se usa la que te venga mejor: el porcentaje para ir tanteando, y k Polys cuando el motor te da un presupuesto de triángulos cerrado. |
| 💯 | **% of decimation** | *Zplugin > Decimation Master > 3-Decimate* | Intermediate | Deja ese porcentaje de los polígonos originales (20 en tu captura). |
| 🔺 | **k Polys** | *Zplugin > Decimation Master > 3-Decimate* | Intermediate | Fija un número concreto de MILES de polígonos (200 en tu captura). |
| ⚫ | **Points** | *Zplugin > Decimation Master > 3-Decimate* | Intermediate | Fija miles de puntos (200 en tu captura). |
| 🎯 | **Decimate Current** | *Zplugin > Decimation Master > 3-Decimate* | Intermediate | Reduce el SubTool activo. |
| 🧩 | **Decimate All** | *Zplugin > Decimation Master > 3-Decimate* | Intermediate | Reduce todos los SubTools, cosa que ahorra muchísimo tiempo con un personaje de veinte piezas. |


## Zplugin > Decimation Master


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎚️ | **Decimation Master > Presets y Utilities** | *Zplugin > Decimation Master* | Intermediate | Atajos a valores redondos y utilidades de limpieza. Y recuerda el aviso de siempre: esto da TRIÁNGULOS, muy bien para render e impresión, pero NO es retopología válida para animar — para eso hace falta ZRemesher o rehacerla a mano en cuadrados. |


## Zplugin > Decimation Master > Presets


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔢 | **20k** | *Zplugin > Decimation Master* | Intermediate | Atajo que fija el objetivo en 20.000 polígonos. |
| 🔢 | **35k** | *Zplugin > Decimation Master* | Intermediate | Atajo que fija el objetivo en 35.000 polígonos. |
| 🔢 | **75k** | *Zplugin > Decimation Master* | Intermediate | Atajo que fija el objetivo en 75.000 polígonos. |
| 🔢 | **150k** | *Zplugin > Decimation Master* | Intermediate | Atajo que fija el objetivo en 150.000 polígonos. |
| 🔢 | **250k** | *Zplugin > Decimation Master* | Intermediate | Atajo que fija el objetivo en 250.000 polígonos. |
| ✏️ | **Custom** | *Zplugin > Decimation Master* | Intermediate | Permite fijar un valor propio en vez de uno de los atajos. |
| 🔢 | **Custom k Points** | *Zplugin > Decimation Master* | Intermediate | El valor propio en miles de puntos (30 en tu captura). |


## Zplugin > Decimation Master > Utilities


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗑️ | **Delete Caches** | *Zplugin > Decimation Master* | Intermediate | Borra los preprocesados guardados, que ocupan mucho disco. |
| 📤 | **Export All SubTools** | *Zplugin > Decimation Master* | Intermediate | Saca todos los SubTools ya reducidos de una tacada. |


## Zplugin > Misc Utilities


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📋 | **Misc Utilities > valores de exportación y pinceles** | *Zplugin > Misc Utilities* | Advanced | Los dos primeros son importantísimos y se olvidan siempre: si cada pieza se exporta con valores distintos, el personaje llega descuadrado al motor y hay que recolocarlo pieza por pieza. |
| 📋 | **Copy Export Values** | *Zplugin > Misc Utilities* | Advanced | Copia los ajustes de exportación del SubTool activo. |
| 📥 | **Paste Export Values** | *Zplugin > Misc Utilities* | Advanced | Los pega en otro SubTool, para que todas las piezas salgan con la misma escala y orientación. |
| ⬅️ | **<<Brush** | *Zplugin > Misc Utilities* | Advanced | Pasa al pincel anterior de la lista. |
| ➡️ | **Brush>>** | *Zplugin > Misc Utilities* | Advanced | Pasa al pincel siguiente de la lista. |
| 🔢 | **Brush Increment** | *Zplugin > Misc Utilities* | Advanced | De cuántos en cuántos salta al pasar de pincel (4 en tu captura). |
| 🔦 | **Misc Utilities > luz interactiva y utilidades** | *Zplugin > Misc Utilities* | Advanced | El primero es de los que más cambian la comodidad al iluminar. |
| 🔦 | **InteractiveLight** | *Zplugin > Misc Utilities* | Advanced | Permite mover la luz arrastrando DIRECTAMENTE sobre el modelo, que es muchísimo más rápido e intuitivo que ajustar los ángulos a mano en la paleta Light: ves el resultado mientras arrastras. |
| 🌐 | **Home Page** | *Zplugin > Misc Utilities* | Advanced | Abre la web del complemento. |
| 📐 | **Snap Angle** | *Zplugin > Misc Utilities* | Advanced | El ángulo al que se engancha la rotación, para girar en pasos exactos (1 en tu captura). |
| 🎯 | **Set Snap Angle** | *Zplugin > Misc Utilities* | Advanced | Fija ese ángulo de enganche. |
| 📄 | **TextFileViewer** | *Zplugin > Misc Utilities* | Advanced | Abre un visor de archivos de texto dentro de ZBrush, útil para leer notas o un ZScript sin salir del programa. |


## Zplugin > FBX ExportImport


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📦 | **FBX ExportImport > alcance, versión y formato** | *Zplugin > FBX ExportImport* | Advanced | El formato con el que tu modelo entra en Unity o en Unreal, así que esta sub-paleta te importa más que casi ninguna otra. |
| 🎯 | **Selected** | *Zplugin > FBX ExportImport* | Advanced | Exporta solo el SubTool seleccionado (activo en tu captura). |
| 👁️ | **Visible** | *Zplugin > FBX ExportImport* | Advanced | Exporta los SubTools visibles. |
| 🧩 | **All** | *Zplugin > FBX ExportImport* | Advanced | Exporta todos los SubTools. |
| 🔢 | **FBX 2020** | *Zplugin > FBX ExportImport* | Advanced | La VERSIÓN del formato. Conviene que coincida con la que espera el programa de destino, porque una versión demasiado nueva puede sencillamente no abrirse y el error no siempre lo explica. |
| 💾 | **bin** | *Zplugin > FBX ExportImport* | Advanced | Guarda en binario (activo en tu captura): pesa mucho menos y es lo normal. |
| 📄 | **ascii** | *Zplugin > FBX ExportImport* | Advanced | Guarda en texto, que se puede abrir con un editor para depurar qué se ha exportado realmente. |
| 🧭 | **FBX ExportImport > qué viaja dentro del archivo** | *Zplugin > FBX ExportImport* | Advanced | Lo que se incluye en el FBX. Dos de estos evitan los disgustos clásicos: el personaje tumbado y la carpeta de texturas olvidada. |
| 📄 | **Layers** | *Zplugin > FBX ExportImport* | Advanced | Exporta las capas de escultura. |
| 🔺 | **Tris** | *Zplugin > FBX ExportImport* | Advanced | Convierte los cuadrados en triángulos al salir, que es lo que acaba haciendo el motor de todas formas. |
| ↕️ | **MayaYUp** | *Zplugin > FBX ExportImport* | Advanced | Corrige la orientación de los ejes para Maya, donde el eje vertical es la Y. Es el botón que evita que el personaje llegue tumbado. |
| 🖼️ | **Embed Maps** | *Zplugin > FBX ExportImport* | Advanced | Mete las texturas DENTRO del archivo FBX en vez de dejarlas sueltas, comodísimo para pasarle el modelo a otra persona sin olvidarte media carpeta. |
| 🫧 | **SNormals** | *Zplugin > FBX ExportImport* | Advanced | Exporta las normales suavizadas (activo en tu captura). |
| 🖼️ | **TGA** | *Zplugin > FBX ExportImport* | Advanced | Formato TGA para las texturas que acompañan al archivo. |
| 🖼️ | **16Bit TIF** | *Zplugin > FBX ExportImport* | Advanced | Formato TIF de 16 bits para esas texturas. |
| 📤 | **Export** | *Zplugin > FBX ExportImport* | Advanced | Exporta el archivo FBX. El botón ? de al lado abre la ayuda. |
| 📥 | **Import** | *Zplugin > FBX ExportImport* | Advanced | Importa un archivo FBX. |
| ⚙️ | **Options** | *Zplugin > FBX ExportImport* | Advanced | Abre el resto de ajustes del formato. |


## Zplugin > Multi Map Exporter


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗺️ | **Multi Map Exporter > los mapas de relieve** | *Zplugin > Multi Map Exporter* | Advanced | El complemento que saca DE UNA VEZ todos los mapas de todos los SubTools, en lugar de ir uno por uno: es lo que convierte una tarde de trabajo repetitivo en dos minutos. |
| 🏔️ | **Displacement** | *Zplugin > Multi Map Exporter* | Advanced | Guarda la altura real de cada punto, para recuperar el detalle en otro programa (activo en naranja en tu captura). |
| 🧭 | **Vector Displacement** | *Zplugin > Multi Map Exporter* | Advanced | Lo mismo pero pudiendo desplazar en cualquier dirección, así que aguanta formas que se doblan sobre sí mismas. |
| 🟣 | **Normal** | *Zplugin > Multi Map Exporter* | Advanced | El mapa de normales, el que finge el relieve sin añadir geometría. El que de verdad usas para videojuegos. |
| 🎨 | **Multi Map Exporter > color, sombreado y el botón final** | *Zplugin > Multi Map Exporter* | Advanced | Los mapas de color y sombreado, más el botón que lo lanza todo. |
| 🎨 | **Texture from Polypaint** | *Zplugin > Multi Map Exporter* | Advanced | Pasa el color pintado a imagen, que es el paso obligatorio para llevarse el color a un motor. |
| 🕳️ | **Ambient Occlusion** | *Zplugin > Multi Map Exporter* | Advanced | Guarda el oscurecimiento de los recovecos, que luego se usa en el motor para añadir suciedad sin coste. |
| 🪨 | **Cavity** | *Zplugin > Multi Map Exporter* | Advanced | Guarda el oscurecimiento de las grietas finas. |
| 📦 | **Export Mesh** | *Zplugin > Multi Map Exporter* | Advanced | Saca además la malla junto con los mapas. |
| ▶️ | **Create All Maps** | *Zplugin > Multi Map Exporter* | Advanced | Lanza la generación de todo lo marcado, para todos los SubTools seleccionados. Es el botón que dejas pulsado y te vas a por café. |
| ⚙️ | **Multi Map Exporter > alcance y tamaño del mapa** | *Zplugin > Multi Map Exporter* | Advanced | Sobre qué piezas se trabaja y con qué resolución. |
| 🧩 | **SubTools** | *Zplugin > Multi Map Exporter* | Advanced | Elige sobre qué SubTools se generan los mapas. |
| 🔗 | **Merge Maps** | *Zplugin > Multi Map Exporter* | Advanced | Fusiona los mapas de varios SubTools en una sola imagen, que interesa cuando comparten un mismo despliegue UV (en gris en tu captura). |
| 📄 | **Layers** | *Zplugin > Multi Map Exporter* | Advanced | Tiene en cuenta las capas al generar. |
| 📐 | **Map Size** | *Zplugin > Multi Map Exporter* | Advanced | La resolución de los mapas (2048 en tu captura): 2048 es lo normal para un personaje de juego, y 4096 solo si va a verse muy de cerca — cada salto dobla el lado y cuadruplica el peso en memoria. |
| 🔢 | **512** | *Zplugin > Multi Map Exporter* | Advanced | Atajo que fija el mapa en 512 píxeles. |
| 🔢 | **1024** | *Zplugin > Multi Map Exporter* | Advanced | Atajo que fija el mapa en 1024 píxeles. |
| 🔢 | **2048** | *Zplugin > Multi Map Exporter* | Advanced | Atajo que fija el mapa en 2048 píxeles. |
| 🔢 | **4096** | *Zplugin > Multi Map Exporter* | Advanced | Atajo que fija el mapa en 4096 píxeles. |
| 🔄 | **Multi Map Exporter > los dos ajustes que evitan disgustos** | *Zplugin > Multi Map Exporter* | Advanced | Estos dos son los que más problemas ahorran al llevar los mapas a un motor. |
| ⬜ | **Map Border** | *Zplugin > Multi Map Exporter* | Advanced | El margen en píxeles que se dibuja alrededor de cada isla UV (4 en tu captura): sin ese margen aparecen costuras visibles en el modelo cuando el motor reduce la textura de tamaño, así que NO lo pongas a 0. |
| ↕️ | **FlipV** | *Zplugin > Multi Map Exporter* | Advanced | Voltea el mapa en vertical (activo en naranja en tu captura): es el ajuste del que depende que el relieve se vea hundido en vez de salido al llegar al motor, porque cada programa cuenta la coordenada V al revés. |
| ♻️ | **ReUV** | *Zplugin > Multi Map Exporter* | Advanced | Rehace las UV antes de generar los mapas. |
| ⚙️ | **Export Options** | *Zplugin > Multi Map Exporter* | Advanced | Abre el resto de ajustes de exportación. |


## Menú superior > Zplugin > PolyGroupIt


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎨 | **Zplugin > PolyGroupIt** | *Menú superior > Zplugin > PolyGroupIt* | Intermediate | El generador automático de POLYGROUPS. Hacerlos a mano es tedioso, y esto los propone solo y bastante bien: separa la cabeza, los brazos, cada pieza de la armadura. PARA QUÉ TE SIRVE: unos polygroups bien puestos hacen que puedas ocultar el cuerpo y trabajar solo en la mano con un Ctrl+Mayús+clic, y además son la base para que ZRemesher respete las divisiones al rehacer la topología. |
| 🪄 | **PolyGroupIt** | *Menú superior > Zplugin > PolyGroupIt* | Intermediate | Abre una ventana que analiza la forma y propone la división sola. |
| 🖌️ | **PolyGroupIt from Paint** | *Menú superior > Zplugin > PolyGroupIt* | Intermediate | Crea los grupos a partir de lo que hayas pintado tú sobre el modelo, para cuando quieres decidir la división a mano. |
| ➖ | **Border** | *Menú superior > Zplugin > PolyGroupIt* | Intermediate | Trabaja sobre los bordes. |


## Menú superior > Zplugin > Projection Master


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖌️ | **Zplugin > Projection Master** | *Menú superior > Zplugin > Projection Master* | Advanced | Es una herramienta veterana: hoy Spotlight y los alphas normales cubren casi todo lo que hacía, pero sigue siendo la forma más PRECISA de proyectar una imagen exacta sobre una superficie, porque trabajas sobre píxeles y no sobre una proyección aproximada. OJO CON UNA CONSECUENCIA PRÁCTICA que descoloca la primera vez: mientras está activo NO puedes girar el modelo, porque está congelado en esa vista; hay que salir del modo para poder moverlo otra vez. Si alguna vez te has quedado con el modelo 'atascado' sin poder rotarlo, era esto. |
| 🖌️ | **Projection Master** | *Menú superior > Zplugin > Projection Master* | Advanced | Su nota emergente lo explica mejor que ninguna descripción: 'Place the active 3D object in the canvas and switch to painting mode'. Congela el modelo en la vista actual y lo deja estampado en el lienzo como si fuera una imagen plana, para que puedas pintar o esculpir encima con todos los recursos del 2.5D, y al terminar proyecta lo hecho de vuelta sobre la malla en 3D. |


## Zplugin > Projection Master


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚠️ | **Zplugin > Projection Master: cuándo usarlo y el aviso** | *Menú superior > Zplugin > Projection Master* | Advanced | Es una herramienta veterana: hoy Spotlight y los alphas normales cubren casi todo lo que hacía, pero sigue siendo la forma más PRECISA de proyectar una imagen exacta sobre una superficie, porque trabajas sobre píxeles y no sobre una proyección aproximada. OJO CON UNA CONSECUENCIA PRÁCTICA que descoloca la primera vez: mientras está activo NO puedes girar el modelo, porque está congelado en esa vista; hay que salir del modo (volviendo a pulsar el botón) para poder moverlo otra vez. Si alguna vez te has quedado con el modelo 'atascado' sin poder rotarlo, era esto. |


## Zplugin > Scale Master


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📏 | **Scale Master > la escala de la escena** | *Zplugin > Scale Master* | Advanced | El complemento de la ESCALA REAL, que resuelve uno de los problemas más molestos de ZBrush: el programa trabaja en unidades propias sin relación con el mundo, y luego el personaje llega a Unity midiendo doscientos metros o dos centímetros. |
| 📐 | **Set Scene Scale** | *Zplugin > Scale Master* | Advanced | Fija la escala de la escena. |
| 🔗 | **ZBrush Scale Unify** | *Zplugin > Scale Master* | Advanced | Unifica la escala de todo el proyecto. |
| 🎯 | **Center Subtools to World** | *Zplugin > Scale Master* | Advanced | Coloca las piezas en el origen del mundo, que es donde tienen que estar para que el motor las sitúe y las rote bien — un modelo descentrado gira alrededor de un punto que no es el suyo. |
| 📐 | **Scale Master > la medida de la pieza** | *Zplugin > Scale Master* | Advanced | Dar a la pieza un tamaño concreto en unidades reales. |
| 📏 | **mm** | *Zplugin > Scale Master* | Advanced | Milímetros (activo en tu captura). |
| 📏 | **cm** | *Zplugin > Scale Master* | Advanced | Centímetros. |
| 📏 | **In** | *Zplugin > Scale Master* | Advanced | Pulgadas. |
| 📏 | **ft** | *Zplugin > Scale Master* | Advanced | Pies. |
| 📊 | **Sliders to Subtool Size** | *Zplugin > Scale Master* | Advanced | Rellena los deslizadores con el tamaño actual de la pieza. El botón R de al lado es Restore Configuration. |
| ↔️ | **X** | *Zplugin > Scale Master* | Advanced | La medida en el eje X (1 en tu captura). |
| ↕️ | **Y** | *Zplugin > Scale Master* | Advanced | La medida en el eje Y. En tu captura este deslizador no muestra etiqueta, pero por su posición es el eje Y. |
| 🔃 | **Z** | *Zplugin > Scale Master* | Advanced | La medida en el eje Z (1 en tu captura). |
| ✅ | **Resize Subtool** | *Zplugin > Scale Master* | Advanced | Aplica ese tamaño al SubTool, con el botón All de al lado para hacerlo en todos a la vez, que es lo que quieres si el personaje entero tiene que cambiar de escala junto. |
| 📦 | **Scale Master > ayudas visuales y exportación** | *Zplugin > Scale Master* | Advanced | Las referencias de tamaño y el botón que hace que el personaje llegue al motor midiendo lo que debe. |
| 📦 | **New Subtool** | *Zplugin > Scale Master* | Advanced | Crea una pieza de referencia nueva. |
| 1️⃣ | **1 Unit Helper** | *Zplugin > Scale Master* | Advanced | Crea una pieza que mide exactamente UNA unidad, para comparar a ojo el tamaño de tu modelo contra algo conocido — el equivalente a poner una moneda al lado de una foto. |
| 🔲 | **New Bounding Box Subtool** | *Zplugin > Scale Master* | Advanced | Crea una caja del tamaño exacto del modelo, útil para comprobar sus dimensiones de un vistazo. |


## Zplugin > Scale Master > Export to Unit Scale


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📤 | **Export to Unit Scale** | *Zplugin > Scale Master* | Advanced | Exporta el modelo ya convertido a esa escala, con su propio botón All para hacerlo en todos. Tiene su propia fila de unidades encima. |


## Zplugin > SubTool Master


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗂️ | **SubTool Master > operaciones en masa** | *Zplugin > SubTool Master* | Intermediate | Operaciones EN MASA sobre muchos SubTools a la vez, que es lo que salva la vida en un personaje con treinta piezas: todas estas son operaciones que a mano habría que repetir treinta veces. |
| 💾 | **Save ZTool** | *Zplugin > SubTool Master* | Intermediate | Guarda la herramienta completa. |
| 📁 | **Folder Only** | *Zplugin > SubTool Master* | Intermediate | Limita la operación a una carpeta, para no aplicarla a todo el modelo sin querer. |
| 📎 | **MultiAppend** | *Zplugin > SubTool Master* | Intermediate | Añade varios SubTools al final de golpe, en vez de uno a uno. |
| 📌 | **MultiInsert** | *Zplugin > SubTool Master* | Intermediate | Inserta varios SubTools de golpe en la posición elegida. |
| 📤 | **Export** | *Zplugin > SubTool Master* | Intermediate | Exporta todos los SubTools de una vez. |
| 🪞 | **Mirror** | *Zplugin > SubTool Master* | Intermediate | Refleja varios SubTools a la vez. |
| 🔗 | **Merge** | *Zplugin > SubTool Master* | Intermediate | Fusiona varios SubTools. |
| 🪣 | **Fill** | *Zplugin > SubTool Master* | Intermediate | Rellena varios SubTools de golpe. |
| 👁️ | **SubTool Master > visibilidad y resolución** | *Zplugin > SubTool Master* | Intermediate | Aquí está EL TRUCO para que el programa deje de arrastrarse cuando la escena pesa. |
| 🔄 | **Invert Vis** | *Zplugin > SubTool Master* | Intermediate | Invierte qué SubTools están visibles. |
| 🗑️ | **Delete Invis** | *Zplugin > SubTool Master* | Intermediate | Borra lo oculto. Cuidado con este, que no tiene vuelta atrás. |
| 🔽 | **Low Res vis** | *Zplugin > SubTool Master* | Intermediate | Pone todos los SubTools visibles en su nivel de subdivisión más BAJO. Mucho más rápido que bajar de nivel pieza por pieza, y es lo que hace que una escena pesada vuelva a ir fluida. |
| 🔼 | **Hi Res vis** | *Zplugin > SubTool Master* | Intermediate | Pone todos los SubTools visibles en su nivel más ALTO. |
| 🔍 | **ScaleOffset** | *Zplugin > SubTool Master* | Intermediate | Escala y desplaza varios SubTools a la vez. |
| 👁️ | **Do Visible** | *Zplugin > SubTool Master* | Intermediate | Limita la operación a los SubTools visibles. |
| ⬆️ | **Shift Up** | *Zplugin > SubTool Master* | Intermediate | Mueve un SubTool hacia arriba en la lista. |
| 🙈 | **Show-HideAll** | *Zplugin > SubTool Master* | Intermediate | Enseña u oculta todos los SubTools de golpe. |
| 🔄 | **SubTool Master > conversión y carpetas** | *Zplugin > SubTool Master* | Intermediate | Convertir en geometría real lo que hasta ahora era una vista previa, y gestionar las carpetas. |
| 🔢 | **ArrayToMesh** | *Zplugin > SubTool Master* | Intermediate | Convierte en geometría REAL las repeticiones de ArrayMesh, que hasta entonces son solo una vista previa que no se puede exportar ni esculpir. |
| 🌾 | **NanoToMesh** | *Zplugin > SubTool Master* | Intermediate | Hace lo mismo con las siembras de NanoMesh. |
| 📂 | **Open-Close All** | *Zplugin > SubTool Master* | Intermediate | Abre y cierra todas las carpetas de la lista de un golpe. |
| ⧉ | **Clone Folder** | *Zplugin > SubTool Master* | Intermediate | Duplica una carpeta entera con lo que lleve dentro. |
| 📋 | **Copy Folder** | *Zplugin > SubTool Master* | Intermediate | Copia una carpeta entera. |
| ✏️ | **Rename** | *Zplugin > SubTool Master* | Intermediate | Renombra el SubTool o la carpeta. |
| 🔝 | **Toggle Top ST** | *Zplugin > SubTool Master* | Intermediate | Alterna el SubTool de arriba de la lista. |


## Zplugin > Text 3D & Vector Shapes


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔤 | **Text 3D & Vector Shapes > crear y editar el texto** | *Zplugin > Text 3D & Vector Shapes* | Intermediate | Convierte TEXTO y formas vectoriales en geometría 3D, sin tener que modelarlos. Para props con letras —una lápida, un cartel, un emblema— esto ahorra un trabajo considerable frente a modelar cada letra. |
| 💾 | **Save** | *Zplugin > Text 3D & Vector Shapes* | Intermediate | Guarda un texto ya montado con todos sus ajustes. |
| 📂 | **Load** | *Zplugin > Text 3D & Vector Shapes* | Intermediate | Carga un texto guardado. |
| 🆕 | **New Text** | *Zplugin > Text 3D & Vector Shapes* | Intermediate | Crea un texto nuevo. Debajo aparece <NO TEXT> mientras no has escrito nada. |
| ✏️ | **Edit Text** | *Zplugin > Text 3D & Vector Shapes* | Intermediate | Modifica el texto existente. |


## Zplugin > Text 3D & Vector Shapes > Font & Style


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🅰️ | **Text 3D & Vector Shapes > fuentes y SVG** | *Zplugin > Text 3D & Vector Shapes > Font & Style* | Intermediate | La tipografía y los dibujos vectoriales. El bloque de SVG encaja bien con que ya tienes Illustrator en tu flujo: dibujas el logotipo o el emblema allí, lo guardas como SVG y lo traes convertido en volumen. |
| 🔤 | **Font & Style** | *Zplugin > Text 3D & Vector Shapes > Font & Style* | Intermediate | El rótulo del bloque: las flechas < y > pasan por las fuentes instaladas y por los estilos. |
| 🅰️ | **Noto Sans** | *Zplugin > Text 3D & Vector Shapes > Font & Style* | Intermediate | La fuente seleccionada en tu captura. |
| 🔠 | **Regular** | *Zplugin > Text 3D & Vector Shapes > Font & Style* | Intermediate | El estilo seleccionado en tu captura. |
| 📂 | **Load a Font file from Disk** | *Zplugin > Text 3D & Vector Shapes > Font & Style* | Intermediate | Carga un archivo de fuente que tengas suelto, sin instalarlo en el sistema. |
| 🆕 | **New SVG** | *Zplugin > Text 3D & Vector Shapes > Font & Style* | Intermediate | Trae un dibujo VECTORIAL nuevo desde un archivo SVG. |
| ✏️ | **Edit SVG** | *Zplugin > Text 3D & Vector Shapes > Font & Style* | Intermediate | Modifica el SVG cargado. |


## Zplugin > Text 3D & Vector Shapes > 3D Shape


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧱 | **Text 3D & Vector Shapes > 3D Shape** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | Convierte el dibujo plano en volumen. |
| ⬆️ | **Extrusion** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | El GROSOR: cuánto sale la letra hacia fuera (0.14999 en tu captura). |
| 🔢 | **Resolution** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | La densidad de la malla resultante. Súbela si las curvas de las letras salen facetadas. |
| ↔️ | **Spacing** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | El espacio entre caracteres (0 en tu captura). |
| 🌊 | **Adaptive** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | Reparte los polígonos de forma adaptativa, poniendo más donde hay curva y menos en las rectas. |
| ◗ | **Bevel** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | El bisel de los cantos (0 en tu captura). Aunque sea un valor pequeño, poner algo de bisel es lo que hace que las letras atrapen la luz en el borde en vez de verse cortadas a cuchillo. |
| 🔢 | **Bevel Res** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | La resolución de ese bisel (en gris en tu captura). |
| 🌙 | **Curvature** | *Zplugin > Text 3D & Vector Shapes > 3D Shape* | Intermediate | Curva el texto para que siga un arco. |


## Zplugin > Text 3D & Vector Shapes > Options


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚙️ | **Text 3D & Vector Shapes > Options** | *Zplugin > Text 3D & Vector Shapes > Options* | Intermediate | Los ajustes de comportamiento del generador de texto. |
| ♻️ | **Replace** | *Zplugin > Text 3D & Vector Shapes > Options* | Intermediate | Sustituye el texto anterior en vez de añadir otro nuevo. |
| 🔄 | **AutoUpdate** | *Zplugin > Text 3D & Vector Shapes > Options* | Intermediate | Regenera la geometría cada vez que cambias algo, lo que es cómodo para ir viendo el resultado pero pesado si el texto es largo. |
| ↕️ | **Vertical** | *Zplugin > Text 3D & Vector Shapes > Options* | Intermediate | Escribe en vertical. |
| 🔀 | **Reverse** | *Zplugin > Text 3D & Vector Shapes > Options* | Intermediate | Invierte el orden de los caracteres. |
| 🔒 | **No Scaling** | *Zplugin > Text 3D & Vector Shapes > Options* | Intermediate | Impide que la geometría se reescale sola al generarse, para que mantenga el tamaño que le has dado. |


## Zplugin > Transpose Master


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧍 | **Transpose Master > el flujo de posado** | *Zplugin > Transpose Master* | Advanced | El complemento para POSAR un personaje con muchos SubTools, y resuelve un problema muy concreto: mover un brazo cuando ese brazo está formado por la piel, la manga, el guante y tres correas, cada una un SubTool distinto. Es el flujo estándar para sacar una pose de presentación de portafolio a partir de un modelo hecho en T. |
| 🧍 | **TPoseMesh** | *Zplugin > Transpose Master* | Advanced | Fusiona todos los SubTools visibles en una única malla de baja resolución, la 'T-pose mesh', sobre la que puedes posar cómodamente con la Transpose Line o con un rig. |
| ↩️ | **TPose\|SubT** | *Zplugin > Transpose Master* | Advanced | Devuelve esa pose a los SubTools originales, cada uno con su detalle intacto. |
| 🦴 | **Transpose Master > el rig y las opciones** | *Zplugin > Transpose Master* | Advanced | Las opciones del posado, para hacerlo de forma más controlada que a mano. |
| 🦴 | **ZSphere Rig** | *Zplugin > Transpose Master* | Advanced | Monta un esqueleto de ZSpheres para posar de forma más controlada que con la Transpose Line: colocas las esferas en las articulaciones y mueves desde ahí. |
| 🎨 | **Grps** | *Zplugin > Transpose Master* | Advanced | Respeta los polygroups al fusionar. |
| 📄 | **Layer** | *Zplugin > Transpose Master* | Advanced | Trabaja sobre una capa, lo que permite deshacer la pose o graduarla después. |
| 💾 | **StoreTM Rig** | *Zplugin > Transpose Master* | Advanced | Guarda un rig ya montado. |
| 📥 | **PasteTM Rig** | *Zplugin > Transpose Master* | Advanced | Pega ese rig guardado, así que puedes reutilizar el mismo esqueleto en varios personajes en vez de rehacerlo cada vez. |


## Menú superior > Zplugin > USD Format


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💽 | **Zplugin > USD Format** | *Menú superior > Zplugin > USD Format* | Advanced | Exporta e importa en formato USD (Universal Scene Description), el estándar que Pixar liberó y que se ha convertido en el formato común de la industria para intercambiar escenas enteras entre programas — no solo un modelo, sino la escena con sus materiales, jerarquías y variantes. Va ganando peso rápido: Unreal y Maya ya lo entienden bien, así que conviene que te suene aunque de momento uses FBX. |
| 🎯 | **Selected** | *Menú superior > Zplugin > USD Format* | Advanced | Exporta solo el SubTool seleccionado (activo en naranja en tu captura). |
| 👁️ | **Visible** | *Menú superior > Zplugin > USD Format* | Advanced | Exporta los SubTools visibles. |
| 🧩 | **All** | *Menú superior > Zplugin > USD Format* | Advanced | Exporta todos los SubTools. |
| 💾 | **Save** | *Menú superior > Zplugin > USD Format* | Advanced | Guarda un archivo USD nuevo. |
| ♻️ | **ReSave** | *Menú superior > Zplugin > USD Format* | Advanced | Reescribe el mismo archivo sin volver a preguntar la ruta. |
| 📂 | **Load** | *Menú superior > Zplugin > USD Format* | Advanced | Trae un archivo USD de fuera. |
| 🔄 | **Reload** | *Menú superior > Zplugin > USD Format* | Advanced | Lo vuelve a cargar para recoger los cambios que otra persona haya hecho. |


## Zplugin > UV Master > 1-Unwrap


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗺️ | **UV Master > 1-Unwrap: desplegar** | *Zplugin > UV Master > 1-Unwrap* | Advanced | El complemento que despliega las UV automáticamente, y probablemente el que más tiempo te va a ahorrar de todos. Las UV son el patrón plano del modelo, como el despiece de tela de una camiseta, y sin ellas no se puede aplicar ninguna textura. RECUERDA: hay que desplegar ANTES de generar cualquier mapa con Multi Map Exporter o con Texture > From Mesh, porque sin UV esos mapas salen inservibles. |
| ✂️ | **Unwrap** | *Zplugin > UV Master > 1-Unwrap* | Advanced | Despliega las UV del SubTool activo. |
| 🧩 | **Unwrap All** | *Zplugin > UV Master > 1-Unwrap* | Advanced | Despliega las UV de todos los SubTools. |
| 🧭 | **UV Master > 1-Unwrap: las guías** | *Zplugin > UV Master > 1-Unwrap* | Advanced | Las tres guías del desplegado automático. |
| 🪞 | **Symmetry** | *Zplugin > UV Master > 1-Unwrap* | Advanced | Aprovecha la simetría del modelo para que los dos lados salgan iguales (activo en naranja en tu captura), lo que además deja el patrón más limpio y permite pintar una vez para los dos lados. |
| 🎨 | **Polygroups** | *Zplugin > UV Master > 1-Unwrap* | Advanced | Usa las divisiones por polygroups como guía de las costuras: si has separado bien las piezas con PolyGroupIt, el despliegue sale ordenado por piezas en vez de en un revoltijo. |
| ➖ | **Use Existing UV Seams** | *Zplugin > UV Master > 1-Unwrap* | Advanced | Respeta las costuras que ya hubiera, para no perder un trabajo previo. |


## Zplugin > UV Master > 2-Painting


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖍️ | **UV Master > 2-Painting: pintar las guías** | *Zplugin > UV Master > 2-Painting* | Advanced | Donde le dices TÚ por dónde quieres que corte, y es lo que separa un despliegue aceptable de uno realmente bueno. |
| 🖌️ | **Enable Control Painting** | *Zplugin > UV Master > 2-Painting* | Advanced | Activa el modo de pintar guías sobre el modelo. |
| 🔴 | **Protect** | *Zplugin > UV Master > 2-Painting* | Advanced | Se pinta en rojo y marca las zonas donde NO quieres que pase una costura — la cara, por ejemplo, porque una costura en mitad de la mejilla se nota siempre. |
| 🔵 | **Attract** | *Zplugin > UV Master > 2-Painting* | Advanced | Se pinta en azul y marca donde SÍ prefieres que corte: la nuca, el interior de los brazos, la parte de atrás. |
| 🧹 | **Erase** | *Zplugin > UV Master > 2-Painting* | Advanced | Borra lo pintado. |
| 🪄 | **AttractFromAmbientOccl** | *Zplugin > UV Master > 2-Painting* | Advanced | Propone las costuras automáticamente usando la oclusión ambiental, o sea metiéndolas por los recovecos, que es justo donde menos se ven. |
| 📊 | **UV Master > 2-Painting: la densidad por zonas** | *Zplugin > UV Master > 2-Painting* | Advanced | Sirve para repartir el espacio de textura donde de verdad hace falta: le das x4 a la cara, que es lo que el jugador va a mirar de cerca, y /4 a la suela de la bota, que no se ve nunca. Con una textura de 2048 bien repartida se consigue más detalle aparente que con una de 4096 repartida a partes iguales. |
| 📊 | **Density** | *Zplugin > UV Master > 2-Painting* | Advanced | La densidad de píxeles de textura que recibe cada zona. |
| 📊 | **X density** | *Zplugin > UV Master > 2-Painting* | Advanced | El multiplicador de esa densidad. |
| ➗ | **/4** | *Zplugin > UV Master > 2-Painting* | Advanced | Divide la densidad de la zona pintada entre cuatro. |
| ➗ | **/3** | *Zplugin > UV Master > 2-Painting* | Advanced | Divide la densidad entre tres. |
| ➗ | **/2** | *Zplugin > UV Master > 2-Painting* | Advanced | Divide la densidad entre dos. |
| 1️⃣ | **1** | *Zplugin > UV Master > 2-Painting* | Advanced | Deja la densidad normal. |
| ✖️ | **x2** | *Zplugin > UV Master > 2-Painting* | Advanced | Dobla la densidad de la zona pintada. |
| ✖️ | **x3** | *Zplugin > UV Master > 2-Painting* | Advanced | Triplica la densidad. |
| ✖️ | **x4** | *Zplugin > UV Master > 2-Painting* | Advanced | Cuadruplica la densidad. |


## Zplugin > UV Master > 3-Utilities


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧰 | **UV Master > 3-Utilities** | *Zplugin > UV Master > 3-Utilities* | Advanced | Las utilidades, y una de ellas hay que pulsarla SIEMPRE: sin Work On Clone, desplegar un modelo pesado puede tardar una eternidad. |
| ⧉ | **Work On Clone** | *Zplugin > UV Master > 3-Utilities* | Advanced | Crea una copia del modelo en baja resolución, para desplegar sobre ella —que es rapidísimo— y luego traer el resultado al modelo bueno de millones de polígonos. El botón que hay que pulsar siempre. |
| 📋 | **Copy UVs** | *Zplugin > UV Master > 3-Utilities* | Advanced | Copia las UV del clon. |
| 📥 | **Paste UVs** | *Zplugin > UV Master > 3-Utilities* | Advanced | Las pega en el modelo original de alta resolución. |
| 🦋 | **Flatten** | *Zplugin > UV Master > 3-Utilities* | Advanced | Aplana el modelo para ver el patrón UV desplegado en pantalla: es la manera de comprobar visualmente que no hay islas superpuestas ni estiradas. |
| ↩️ | **UnFlatten** | *Zplugin > UV Master > 3-Utilities* | Advanced | Devuelve el modelo a su forma. |
| ➖ | **CheckSeams** | *Zplugin > UV Master > 3-Utilities* | Advanced | Enseña dónde han quedado las costuras. |
| 🗑️ | **Clear Maps** | *Zplugin > UV Master > 3-Utilities* | Advanced | Borra los mapas generados. |
| 📂 | **LoadCtrlMap** | *Zplugin > UV Master > 3-Utilities* | Advanced | Carga un mapa de control pintado previamente. |
| 💾 | **SaveCtrlMap** | *Zplugin > UV Master > 3-Utilities* | Advanced | Guarda el mapa de control que pintaste en la fase anterior, para reutilizarlo si tienes que volver a desplegar. |


## Menú superior > Zplugin > ZBenchMark


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⏱️ | **Zplugin > ZBenchMark** | *Menú superior > Zplugin > ZBenchMark* | Basic | Una prueba de rendimiento del ordenador. No cambia nada de tu trabajo; sirve para saber si el equipo rinde lo que debería, para comparar antes y después de un cambio de configuración, o para decidir si merece la pena una ampliación de memoria. Ejecútalo una vez con el equipo recién arrancado y guarda el número, así tienes una referencia si algún día notas que el programa va más lento de lo normal. |
| ▶️ | **Run ZBenchMark** | *Menú superior > Zplugin > ZBenchMark* | Basic | Lanza la batería completa de pruebas y da una puntuación comparable. |
| 🔢 | **las pruebas 1 a 10** | *Menú superior > Zplugin > ZBenchMark* | Basic | Los botones numerados del 1 al 10 ejecutan cada prueba por separado, para medir una operación concreta. |


## Zplugin > ZBrush To Photoshop


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🅿️ | **ZBrush To Photoshop > las capas de imagen** | *Zplugin > ZBrush To Photoshop* | Advanced | Manda el render a Photoshop ya partido en CAPAS, cada una con su información, para retocar la lámina sin volver a renderizar. Es el complemento estrella para montar una imagen de portafolio. |
| 🎨 | **Albedo** | *Zplugin > ZBrush To Photoshop* | Advanced | El color puro, sin luces ni sombras. |
| 🕳️ | **Ao** | *Zplugin > ZBrush To Photoshop* | Advanced | La oclusión de los recovecos. |
| 🏆 | **Best** | *Zplugin > ZBrush To Photoshop* | Advanced | El render en calidad Best. |
| 🎬 | **BPR** | *Zplugin > ZBrush To Photoshop* | Advanced | El render BPR de calidad (activo en tu captura). |
| 🏔️ | **Color Bump** | *Zplugin > ZBrush To Photoshop* | Advanced | El relieve en color. |
| 📏 | **Depth** | *Zplugin > ZBrush To Photoshop* | Advanced | La profundidad en grises (activo en tu captura), con la que luego desenfocas por distancia. |
| 💡 | **Lights** | *Zplugin > ZBrush To Photoshop* | Advanced | Las luces. |
| ⬛ | **Mask** | *Zplugin > ZBrush To Photoshop* | Advanced | El recorte del modelo sobre el fondo (activo en tu captura), imprescindible para cambiar el fondo sin recortar a mano. |
| 🎨 | **ZBrush To Photoshop > las capas de información** | *Zplugin > ZBrush To Photoshop* | Advanced | El resto de capas. Separar los brillos en su propia capa permite subir o bajar el brillo de toda la pieza en Photoshop sin tocar nada más. |
| 🟣 | **OS Normal** | *Zplugin > ZBrush To Photoshop* | Advanced | Las normales en espacio de OBJETO. |
| 🟣 | **TS Normal** | *Zplugin > ZBrush To Photoshop* | Advanced | Las normales en espacio TANGENTE. |
| 👀 | **Preview** | *Zplugin > ZBrush To Photoshop* | Advanced | La vista previa. |
| 🌑 | **Shadow** | *Zplugin > ZBrush To Photoshop* | Advanced | Las sombras (activo en tu captura). |
| ✨ | **Spec** | *Zplugin > ZBrush To Photoshop* | Advanced | Los brillos especulares. |
| 🩸 | **Sss** | *Zplugin > ZBrush To Photoshop* | Advanced | La luz que atraviesa la piel. |
| 🧱 | **Structure** | *Zplugin > ZBrush To Photoshop* | Advanced | Información de estructura del modelo. |
| 🎭 | **SubtoolMasks** | *Zplugin > ZBrush To Photoshop* | Advanced | Las máscaras por pieza. |
| 🕸️ | **Wireframe** | *Zplugin > ZBrush To Photoshop* | Advanced | Dibuja el mallado encima, que va bien para las láminas técnicas de un portafolio, donde se enseña la topología junto al render. |
| 🆔 | **ZBrush To Photoshop > identificación y envío** | *Zplugin > ZBrush To Photoshop* | Advanced | Las capas de IDENTIFICACIÓN son las más útiles y las menos conocidas de todo el complemento. |
| 🎨 | **PolygroupID** | *Zplugin > ZBrush To Photoshop* | Advanced | Genera una capa donde cada polygroup sale de un COLOR PLANO distinto, lo que te permite seleccionar una pieza concreta en Photoshop con la varita mágica en un segundo, sin recortar nada a mano. |
| 🧩 | **SubtoolID** | *Zplugin > ZBrush To Photoshop* | Advanced | Lo mismo pero un color plano por cada SubTool. |
| 1️⃣ | **Material 1** | *Zplugin > ZBrush To Photoshop* | Advanced | Una capa con el primer material. |
| 2️⃣ | **Material 2** | *Zplugin > ZBrush To Photoshop* | Advanced | Una capa con el segundo material. |
| 3️⃣ | **Material 3** | *Zplugin > ZBrush To Photoshop* | Advanced | Una capa con el tercer material. |
| 4️⃣ | **Material 4** | *Zplugin > ZBrush To Photoshop* | Advanced | Una capa con el cuarto material. |
| 5️⃣ | **Material 5** | *Zplugin > ZBrush To Photoshop* | Advanced | Una capa con el quinto material. |
| 📤 | **Send To Photoshop CC** | *Zplugin > ZBrush To Photoshop* | Advanced | Envía todas las capas marcadas a Photoshop. |
| 🧹 | **Clear Layer Cache** | *Zplugin > ZBrush To Photoshop* | Advanced | Vacía las capas guardadas. El botón R de al lado es Restore Configuration. |


## Menú superior > Zplugin > ZColor


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎨 | **Zplugin > ZColor** | *Menú superior > Zplugin > ZColor* | Intermediate | ZColor es el gestor de PALETAS DE COLOR. Para un personaje esto importa más de lo que parece, porque el color de la piel, el de la ropa y el de los metales tienen que estar relacionados entre sí para que la pieza se lea como un conjunto; sacar la paleta de un concept art o de una fotografía y trabajar siempre desde ahí es lo que da esa coherencia. |
| 🎨 | **ZColor** | *Menú superior > Zplugin > ZColor* | Intermediate | Un solo botón con un icono de cuadrícula de colores. Su nota emergente dice 'Show ZColor interface': muestra la interfaz de ZColor, que se abre en una VENTANA PROPIA y por eso no se despliega dentro de la paleta. Permite guardar conjuntos de colores, cargarlos y tomarlos de una imagen de referencia, para pintar el modelo con una gama coherente en lugar de ir eligiendo tonos sueltos en la rueda de color. |

