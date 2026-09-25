# Texture


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖼️ | **Texture: qué es la paleta** | *Menú superior > Texture* | Intermediate | El almacén de IMÁGENES del programa: aquí se cargan, se generan y se gestionan las texturas que luego se aplican al modelo, se usan como fondo de referencia o se proyectan con Spotlight. No confundir con Alpha: un alpha es una imagen en grises que se usa como FORMA (relieve, máscara, recorte), y una texture es una imagen en COLOR que se usa como aspecto de la superficie. Contiene el bloque de Spotlight, la cuadrícula de texturas cargadas con sus operaciones, la conversión con la malla, las herramientas de captura del lienzo y el bloque Image Plane con las vistas de referencia. |
| 🔦 | **Texture > gestionar las sesiones de Spotlight** | *Menú superior > Texture (bloque de arriba)* | Intermediate | SPOTLIGHT es la herramienta que deja una imagen flotando sobre el modelo para proyectarla encima mientras pintas — la forma de texturizar una cara a partir de fotos, por ejemplo. Recuerda que Spotlight tiene su propio historial de deshacer, separado del general (está en la paleta Edit). |
| 📂 | **Load Spotlight** | *Menú superior > Texture (bloque de arriba)* | Intermediate | Carga un conjunto de imágenes de Spotlight ya preparado. |
| 💾 | **Save Spotlight** | *Menú superior > Texture (bloque de arriba)* | Intermediate | Guarda el conjunto que tengas montado con sus posiciones y escalas. En gris hasta que hay algo que guardar. |
| 🗂️ | **Lightbox ▶ Spotlights** | *Menú superior > Texture (bloque de arriba)* | Intermediate | Abre la pestaña de LightBox donde están los Spotlight guardados. |
| 📥 | **Texture > cargar, guardar y recorrer las texturas cargadas** | *Menú superior > Texture* | Intermediate | La gestión de las texturas cargadas. Debajo está la CUADRÍCULA de miniaturas con lo que tienes cargado: en tu captura, Texture Off (la casilla de 'ninguna textura'), Texture 01, Texture 27 y Texture 40, que es un degradado de colores. Pulsar una miniatura la selecciona como textura activa. |
| 📂 | **Import** | *Menú superior > Texture* | Intermediate | Trae una imagen desde el disco. |
| 💾 | **Export** | *Menú superior > Texture* | Intermediate | Guarda la textura seleccionada. En gris en tu captura. |
| 🗂️ | **Lightbox ▶ Texture** | *Menú superior > Texture* | Intermediate | Abre la pestaña de texturas de LightBox. |
| 🔢 | **Texture Off.** | *Menú superior > Texture* | Intermediate | El deslizador que recorre la lista de texturas cargadas por número (0). |
| ↩️ | **R** | *Menú superior > Texture* | Intermediate | Restore Configuration: devuelve la cantidad de elementos visibles a la de fábrica. |
| 🖼️ | **Texture > la fila de cuatro iconos: los dos primeros** | *Menú superior > Texture (fila de cuatro botones de icono)* | Intermediate | La fila de cuatro botones de icono que hay encima de los botones de volteo, resuelta ENTERA con tus notas emergentes y en este orden. Aquí van los dos primeros. |
| 🫥 | **Transparent Texture** | *Menú superior > Texture (fila de cuatro botones de icono)* | Intermediate | El PRIMER icono de la fila. Marca la textura como transparente, o sea que respeta las zonas vacías de la imagen en vez de rellenarlas, que es lo que hace falta para proyectar un logo o un recorte sin su fondo. |
| ✨ | **Antialiased Texture** | *Menú superior > Texture (fila de cuatro botones de icono)* | Intermediate | El SEGUNDO icono, el de la etiqueta AA. Suaviza los bordes dentados de la textura. |
| 🔦 | **Texture > la fila de cuatro iconos: los dos de Spotlight** | *Menú superior > Texture (fila de cuatro botones de icono)* | Intermediate | Entre estos dos está el flujo completo de texturizar con fotos: cargas la imagen con Import, la añades con Add To Spotlight y la enciendes con Mayús+Z. OJO con las dos teclas de Spotlight: Mayús+Z enciende y apaga la herramienta, y Z a secas es 'Edit Spotlight' y entra en el modo de edición de la imagen, que es cosa distinta. |
| 🔦 | **Turn On Spotlight** | *Menú superior > Texture (fila de cuatro botones de icono)* | Intermediate | El TERCER icono, el que pone 'on off', con ATAJO Mayús+Z: enciende y apaga Spotlight sin ir a otra paleta. |
| ➕ | **Add To Spotlight** | *Menú superior > Texture (fila de cuatro botones de icono)* | Intermediate | El CUARTO icono. Añade la textura seleccionada al conjunto de imágenes de Spotlight, de modo que se van acumulando varias fotos en la rueda para irlas proyectando sobre el modelo. |
| 🔄 | **Texture > voltear, girar e invertir la textura** | *Menú superior > Texture* | Intermediate | Las operaciones que transforman la textura seleccionada. Son DESTRUCTIVAS sobre la textura cargada, así que si la vas a necesitar sin tocar, duplícala antes con Clone. |
| ↔️ | **Flip H** | *Menú superior > Texture* | Intermediate | Voltea la textura en horizontal. |
| ↕️ | **Flip V** | *Menú superior > Texture* | Intermediate | Voltea la textura en vertical. |
| 🔄 | **Rotate** | *Menú superior > Texture* | Intermediate | Gira la textura. |
| 🔀 | **Invert** | *Menú superior > Texture* | Intermediate | Invierte sus colores (el negativo). En pantalla la etiqueta sale recortada como 'Invers'; su nota emergente da el nombre completo, 'Invert'. |
| 🔁 | **Texture > el intercambio entre textura y malla** | *Menú superior > Texture* | Advanced | Aquí está el paso obligatorio para llevarse el color a Unity o a Unreal, porque los motores no entienden el Polypaint. Recuerda el orden correcto del flujo: primero desplegar las UV (con UV Master, por ejemplo) y después From Mesh, porque sin UV la textura sale inservible. |
| 📤 | **From Mesh** | *Menú superior > Texture* | Advanced | Genera una textura a partir del color que la malla tenga pintado, o sea pasa el Polypaint a una imagen de textura. |
| 📥 | **To Mesh** | *Menú superior > Texture* | Advanced | Lo contrario: aplica la textura al modelo como color por vértice. En gris en tu captura. |
| 📏 | **Disp Scale** | *Menú superior > Texture* | Advanced | La escala de desplazamiento que se usa en esa conversión. |
| 🌈 | **Grad** | *Menú superior > Texture* | Advanced | Rellena la textura con un degradado entre los dos colores activos. |
| 🎨 | **Sec** | *Menú superior > Texture* | Advanced | Elige el color SECUNDARIO para ese degradado. |
| 🎨 | **Main** | *Menú superior > Texture* | Advanced | Elige el color PRINCIPAL para ese degradado. |
| 🧹 | **Clear** | *Menú superior > Texture* | Advanced | Vacía la textura. |
| 📐 | **Texture > crear, duplicar y redimensionar texturas** | *Menú superior > Texture* | Intermediate | Crear y redimensionar. Conviene usar potencias de dos en el tamaño (256, 512, 1024, 2048) porque es lo que esperan los motores de videojuegos. |
| 🎨 | **Adjust Colors** | *Menú superior > Texture* | Intermediate | Abre el ajuste de color de la textura. En gris en tu captura. |
| ↔️ | **Width** | *Menú superior > Texture* | Intermediate | El ancho en píxeles (256). |
| ↕️ | **Height** | *Menú superior > Texture* | Intermediate | El alto en píxeles (256). |
| 📄 | **Clone** | *Menú superior > Texture* | Intermediate | Duplica la textura seleccionada. Es lo que hay que hacer antes de cualquier operación destructiva. |
| ✨ | **New** | *Menú superior > Texture* | Intermediate | Crea una textura vacía con el tamaño indicado. |
| 🅰️ | **MakeAlpha** | *Menú superior > Texture* | Intermediate | Convierte la textura en un ALPHA, o sea la pasa a grises para poder usarla como forma de pincel en vez de como color. Es el puente entre las dos paletas y una forma muy rápida de fabricarte alphas a partir de fotos. En gris en tu captura. |
| 🗑️ | **Remove** | *Menú superior > Texture* | Intermediate | Elimina la textura de la lista. |
| 📸 | **Texture > capturar el lienzo como textura** | *Menú superior > Texture* | Advanced | La manera de sacar imágenes de lo que ves sin salir de ZBrush. La regla práctica: Grab Unshaded Doc es el que se usa para texturizar, y Grab Shaded Doc para presentar. |
| ✂️ | **Cd** | *Menú superior > Texture* | Advanced | Recorta y rellena la textura con el contenido del documento. Activo en naranja en tu captura. |
| 🖼️ | **CropAndFill** | *Menú superior > Texture* | Advanced | La versión completa de ese recorte y relleno. En gris en tu captura. |
| 🌓 | **Grab Shaded Doc** | *Menú superior > Texture* | Advanced | Captura el documento CON el sombreado y las luces aplicadas, tal y como se ve. |
| ⬜ | **Grab Unshaded Doc** | *Menú superior > Texture* | Advanced | Lo captura SIN sombrear, o sea solo el color plano, que es justo lo que quieres si vas a usarlo como textura de color y no quieres las sombras cocidas dentro. |
| 🌓 | **Grab Shaded Doc And Depth** | *Menú superior > Texture* | Advanced | Igual que Grab Shaded Doc, pero captura además el canal de PROFUNDIDAD, o sea la distancia de cada punto a la cámara, con lo que puedes desenfocar por distancia después en Photoshop. |
| ⬜ | **Grab Unshaded Doc And Depth** | *Menú superior > Texture* | Advanced | Igual que Grab Unshaded Doc, añadiendo el canal de profundidad. |


## Texture > Image Plane


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖼️ | **Texture > Image Plane: la imagen de referencia detrás del modelo** | *Menú superior > Texture > Image Plane* | Intermediate | IMAGE PLANE es el sistema para trabajar con imágenes de REFERENCIA detrás del modelo — el concept art de frente y de perfil que se usa para acertar las proporciones. Es hermano del bloque de imágenes de fondo de la paleta Draw: aquel coloca las imágenes en los planos del suelo y las paredes, este las pone directamente detrás del modelo asociadas a una vista. |
| 📂 | **Load Image** | *Menú superior > Texture > Image Plane* | Intermediate | Carga la imagen que quieras usar de guía. |
| 📐 | **Image Size** | *Menú superior > Texture > Image Plane* | Intermediate | El tamaño con el que se coloca sobre el lienzo (100). |
| ❓ | **Help** | *Menú superior > Texture > Image Plane* | Intermediate | Abre la ayuda del bloque, que existe porque este sistema tiene bastante enjundia. |


## Texture > Image Plane > Reference Views


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👁️ | **Texture > Reference Views: una imagen por cada ángulo** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Las VISTAS DE REFERENCIA: a cada ángulo se le asigna su propia imagen, y al girar el modelo a esa vista aparece la imagen correspondiente detrás. Para un trabajo de personaje a partir de concept art, este bloque es la diferencia entre acertar las proporciones y descubrir al final que la cabeza es demasiado grande. |
| ⬆️ | **Front** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | La vista frontal. Activa en naranja en tu captura. |
| ⬇️ | **Back** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | La vista trasera. |
| ➡️ | **Right** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | La vista lateral derecha. |
| ⬅️ | **Left** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | La vista lateral izquierda. |
| 🔝 | **Top** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | La vista superior. |
| 1️⃣ | **Cust1** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Una vista personalizada que defines tú en el ángulo que quieras. Útil para un tres cuartos. |
| 2️⃣ | **Cust2** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | La segunda vista personalizada. |
| 🫥 | **Texture > Reference Views: comparar el modelo con la imagen** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Cómo se comprueba que las proporciones coinciden con el dibujo: si la silueta se sale, se ve al momento. |
| 🫥 | **Model Opacity** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Vuelve el modelo semitransparente sobre la imagen de referencia. |
| 🔘 | **MO** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | El interruptor de Model Opacity. |
| ◀️ | **<<** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Pasa a la vista anterior. |
| ▶️ | **>>** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Pasa a la vista siguiente. |
| 💾 | **Store View** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Guarda el ángulo de cámara actual como una de esas vistas. |
| 🌐 | **All** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Aplica a todas las vistas. |
| 🧹 | **Clear** | *Menú superior > Texture > Image Plane > Reference Views* | Intermediate | Borra las vistas. |

