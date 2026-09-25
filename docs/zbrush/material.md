# Material


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚪ | **Material: qué es un material en ZBrush y por qué casi siempre usarás MatCap** | *Menú superior > Material* | Basic | El material define cómo REACCIONA la superficie a la luz: si parece cera, metal, piel o barro. Hay dos familias. Los STANDARD se calculan con las luces de la escena, así que responden a la paleta Light y son los que se usan para renders elaborados. Los MATCAP (los que empiezan por MatCap, como tu MatCap Red Wax) son 'fotografías' de una esfera ya iluminada: no dependen de las luces, van rapidísimos y muestran la forma con mucha claridad, por eso se esculpe casi siempre con uno. Cambiar el material NO cambia el modelo, solo cómo lo ves — pero cambia mucho lo que eres capaz de ver: si te cuesta leer los volúmenes, pasa a un material mate y gris como MatCap Gray y aparecerán errores que la cera roja escondía. |
| 📥 | **Material > cargar, guardar y fijar el material de arranque** | *Menú superior > Material (bloque superior)* | Intermediate | La gestión de materiales como archivo y la biblioteca del programa. |
| 📂 | **Load** | *Menú superior > Material (bloque superior)* | Intermediate | Carga un material desde archivo. |
| 💾 | **Save** | *Menú superior > Material (bloque superior)* | Intermediate | Guarda el material activo como archivo. |
| 🗂️ | **Lightbox▶Materials** | *Menú superior > Material (bloque superior)* | Intermediate | Abre la biblioteca de materiales del programa. |
| 🚀 | **Save As Startup Material** | *Menú superior > Material (bloque superior)* | Intermediate | Deja el material activo como el que aparece al arrancar ZBrush. Cómodo si siempre empiezas con el mismo. |
| 🧱 | **Material > la rejilla de materiales y copiar ajustes entre ellos** | *Menú superior > Material (bloque superior)* | Intermediate | El deslizador con el nombre del material activo ('MatCap Red Wax. 1') y la rejilla de miniaturas de los materiales cargados: en tu captura MatCap Red Wax, SkinShade4 (piel), Chalk (tiza mate, buenísimo para juzgar formas), Chrome A y MatCap Gray. |
| ↩️ | **R** | *Menú superior > Material (bloque superior)* | Intermediate | Restore Configuration, el mismo botón de Alpha y Brush: devuelve a la configuración de fábrica la cantidad de miniaturas visibles. |
| 🔎 | **Show Used** | *Menú superior > Material (bloque superior)* | Intermediate | Filtra y enseña solo los materiales que están asignados a algún SubTool. Muy útil en escenas con muchas piezas. |
| 📋 | **CopyMat** | *Menú superior > Material (bloque superior)* | Intermediate | Copia la configuración del material activo. |
| 📌 | **PasteMat** | *Menú superior > Material (bloque superior)* | Intermediate | Pega esa configuración sobre otro material. |
| ↩️ | **Undo** | *Menú superior > Material (bloque superior)* | Intermediate | Deshace los cambios hechos en esta paleta. |
| ↪️ | **Redo** | *Menú superior > Material (bloque superior)* | Intermediate | Rehace los cambios deshechos. |


## Material > Wax Modifiers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕯️ | **Material > Wax Modifiers: el efecto de cera y translucidez** | *Menú superior > Material > Wax Modifiers* | Advanced | Añade al material un efecto de CERA, es decir de material translúcido en el que la luz entra un poco antes de rebotar — lo que hace que la piel, la cera o el mármol no parezcan plástico. Subiendo un poco Strength en un MatCap de piel se nota mucho. |
| 💪 | **Strength** | *Menú superior > Material > Wax Modifiers* | Advanced | Cuánta cera se aplica (0 en tu captura). Es el que enciende el efecto: con 0 el resto no hace nada. |
| ✨ | **Spec** | *Menú superior > Material > Wax Modifiers* | Advanced | Controla el brillo especular. |
| 🔆 | **Fresnel** | *Menú superior > Material > Wax Modifiers* | Advanced | Regula cuánto se ilumina el material en los BORDES, que es el efecto que da esa sensación de translucidez en las orejas o los dedos. |
| 📈 | **Exponent** | *Menú superior > Material > Wax Modifiers* | Advanced | La curva de ese realce de los bordes. |
| ⭕ | **Radius** | *Menú superior > Material > Wax Modifiers* | Advanced | El alcance del efecto de cera. |
| 🌡️ | **Temperature** | *Menú superior > Material > Wax Modifiers* | Advanced | El tono del efecto, hacia cálido o hacia frío. |


## Material > Modifiers > capas


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎛️ | **Material > Modifiers: las cuatro capas del material** | *Menú superior > Material > Modifiers* | Advanced | El taller donde se fabrica un material desde dentro. Un material de ZBrush se compone de hasta cuatro CAPAS o shaders, que se van sumando, y cada una tiene su propio juego de ajustes. En tu captura tienes activo S1. |
| 📋 | **CopySH** | *Menú superior > Material > Modifiers* | Advanced | Copia una de esas capas de shader. |
| 📌 | **PasteSH** | *Menú superior > Material > Modifiers* | Advanced | Pega la capa copiada. |
| 1️⃣ | **S1** | *Menú superior > Material > Modifiers* | Advanced | La primera capa de shader. Activa en tu captura. |
| 2️⃣ | **S2** | *Menú superior > Material > Modifiers* | Advanced | La segunda capa de shader. |
| 3️⃣ | **S3** | *Menú superior > Material > Modifiers* | Advanced | La tercera capa de shader. |
| 4️⃣ | **S4** | *Menú superior > Material > Modifiers* | Advanced | La cuarta capa de shader. |
| 🌫️ | **Opacity** | *Menú superior > Material > Modifiers* | Advanced | La opacidad de la capa activa (100). |


## Material > Modifiers > cavidad y canales


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕳️ | **Material > Modifiers: la cavidad y los dos canales del shader** | *Menú superior > Material > Modifiers* | Advanced | La detección de cavidades es de lo más rentable de toda la paleta: oscurece automáticamente las grietas y hace que el detalle se lea muchísimo mejor sin pintar nada. Los pares que siguen trabajan sobre los dos canales del shader. |
| 🕳️ | **Cavity Detection** | *Menú superior > Material > Modifiers* | Advanced | Hace que el material cambie en las CAVIDADES del modelo (1). Es lo que oscurece las grietas solo. |
| 📉 | **Cavity Transition** | *Menú superior > Material > Modifiers* | Advanced | La transición de ese efecto de cavidad (-0.5). |
| 💡 | **Intensity A** | *Menú superior > Material > Modifiers* | Advanced | La intensidad del canal A (valor 1 en tu captura). Ojo: la pareja Intensity A / Intensity B aparece DOS veces dentro de Modifiers, aquí junto a Cavity Detection y otra vez más abajo en el bloque de color; por eso cada bloque tiene su propio valor en la columna Paleta. |
| 💡 | **Intensity B** | *Menú superior > Material > Modifiers* | Advanced | La intensidad del canal B. Confirmado con tu captura del 12/09: en pantalla pone 'Intensity B' (valor 1), no 'Intensity R' como decía antes esta fila por una errata mía de una ronda antigua. Ojo: la pareja Intensity A / Intensity B aparece DOS veces dentro de Modifiers, aquí junto a Cavity Detection y otra vez más abajo en el bloque de color; por eso cada bloque tiene su propio valor en la columna Paleta. |
| ⚫ | **Monochromatic A** | *Menú superior > Material > Modifiers* | Advanced | Quita el color del canal A para dejarlo en blanco y negro. |
| ⚫ | **Monochromatic B** | *Menú superior > Material > Modifiers* | Advanced | Quita el color del canal B para dejarlo en blanco y negro. |
| 📏 | **Depth A** | *Menú superior > Material > Modifiers* | Advanced | Cuánto influye la profundidad en el canal A. |
| 📏 | **Depth B** | *Menú superior > Material > Modifiers* | Advanced | Cuánto influye la profundidad en el canal B. |


## Material > Modifiers > color


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌈 | **Material > Modifiers: el color del material y la orientación del MatCap** | *Menú superior > Material > Modifiers* | Advanced | El resto del taller, centrado en el COLOR. El control con más partido es Orientation: gira la esfera del MatCap, lo que cambia de dónde parece venir la luz — un truco rápido para reiluminar el modelo sin tocar la paleta Light. |
| 🎨 | **Colorize** | *Menú superior > Material > Modifiers* | Advanced | Decide si el material TIÑE el color que haya debajo. |
| 🖌️ | **OverwriteColor** | *Menú superior > Material > Modifiers* | Advanced | Decide si el material SUSTITUYE el color que haya debajo. |
| 🌫️ | **Blur** | *Menú superior > Material > Modifiers* | Advanced | Difumina. |
| 🎨 | **Hue A** | *Menú superior > Material > Modifiers* | Advanced | El tono del canal A. |
| 🎨 | **Hue B** | *Menú superior > Material > Modifiers* | Advanced | El tono del canal B. |
| 💧 | **Saturation A** | *Menú superior > Material > Modifiers* | Advanced | La saturación del canal A. |
| 💧 | **Saturation B** | *Menú superior > Material > Modifiers* | Advanced | La saturación del canal B. |
| 💡 | **Intensity A** | *Menú superior > Material > Modifiers* | Advanced | La intensidad del canal A. |
| 💡 | **Intensity B** | *Menú superior > Material > Modifiers* | Advanced | La intensidad del canal B. |
| ✨ | **Retain HighColor A** | *Menú superior > Material > Modifiers* | Advanced | Conserva los tonos claros del canal A para que los brillos no se apaguen. |
| ✨ | **Retain HighColor B** | *Menú superior > Material > Modifiers* | Advanced | Conserva los tonos claros del canal B para que los brillos no se apaguen. |
| 🔄 | **Orientation A** | *Menú superior > Material > Modifiers* | Advanced | Gira la esfera del MatCap del canal A, cambiando de dónde parece venir la luz. |
| 🔄 | **Orientation B** | *Menú superior > Material > Modifiers* | Advanced | Gira la esfera del MatCap del canal B. |
| 🖼️ | **Base** | *Menú superior > Material > Modifiers* | Advanced | La miniatura de la imagen base que forma el material. |
| 🅰️ | **A** | *Menú superior > Material > Modifiers* | Advanced | La miniatura del canal A. |
| 🅱️ | **B** | *Menú superior > Material > Modifiers* | Advanced | La miniatura del canal B. |
| 🎨 | **Col** | *Menú superior > Material > Modifiers* | Advanced | La miniatura del canal de color. |
| 📝 | **Channel Descriptors** | *Menú superior > Material > Modifiers* | Advanced | Describe los canales del material. |
| 🏭 | **Create MatCapTexture** | *Menú superior > Material > Modifiers* | Advanced | Genera una textura a partir del MatCap. |


## Material > Mixer


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔀 | **Material > Mixer: mezclar las capas según una propiedad de la superficie** | *Menú superior > Material > Mixer* | Advanced | Aquí está la gracia del Mixer: en vez de un material uniforme, puedes hacer que una capa aparezca solo en las sombras, solo en las cavidades o solo a cierta profundidad. Cada criterio lleva su exponente al lado para ajustar la curva de la mezcla. |
| 🌑 | **By Shadow** | *Menú superior > Material > Mixer* | Advanced | Mezcla según la SOMBRA. |
| 📈 | **Shadow Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente de la mezcla por sombra. |
| 🌘 | **By AO** | *Menú superior > Material > Mixer* | Advanced | Mezcla según la oclusión ambiental. |
| 📈 | **AO Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente de la mezcla por oclusión ambiental. |
| 🕳️ | **By Cavity** | *Menú superior > Material > Mixer* | Advanced | Mezcla según la CAVIDAD. |
| 📈 | **Cavity Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente de la mezcla por cavidad. |
| 💡 | **By Int** | *Menú superior > Material > Mixer* | Advanced | Mezcla según la INTENSIDAD. |
| 📈 | **Int Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente de la mezcla por intensidad. |
| 🎨 | **By Hue** | *Menú superior > Material > Mixer* | Advanced | Mezcla según el TONO. |
| 📈 | **Hue Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente de la mezcla por tono. |
| 💧 | **By Sat** | *Menú superior > Material > Mixer* | Advanced | Mezcla según la SATURACIÓN. |
| 📈 | **Sat Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente de la mezcla por saturación. |
| 📏 | **By Depth** | *Menú superior > Material > Mixer* | Advanced | Mezcla según la distancia a la cámara. |
| 📈 | **Depth Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente de la mezcla por profundidad. |
| 🅰️ | **Depth A** | *Menú superior > Material > Mixer* | Advanced | El límite A del rango de profundidad de la mezcla. |
| 🅱️ | **Depth B** | *Menú superior > Material > Mixer* | Advanced | El límite B del rango de profundidad de la mezcla. |
| 💠 | **Material > Mixer: translucidez y modo de mezcla** | *Menú superior > Material > Mixer* | Advanced | El bloque de la translucidez, que es lo que hace que una oreja o una vela se vean encendidas por dentro a contraluz. |
| 🔆 | **Fresnel** | *Menú superior > Material > Mixer* | Advanced | Realza el material en los bordes de la silueta. |
| 📈 | **F Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente del efecto Fresnel. |
| 🫧 | **Sss** | *Menú superior > Material > Mixer* | Advanced | Subsurface scattering: la luz que atraviesa el material en vez de rebotar en la superficie. |
| 📈 | **S Exp** | *Menú superior > Material > Mixer* | Advanced | El exponente del subsurface scattering. |
| ⬆️ | **Front** | *Menú superior > Material > Mixer* | Advanced | La componente frontal del efecto. |
| 🔀 | **Replace(Normal)** | *Menú superior > Material > Mixer* | Advanced | El desplegable que elige el modo de mezcla. |
| ⚫ | **Black** | *Menú superior > Material > Mixer* | Advanced | El color base de la mezcla. |
| 🖍️ | **Material > Mixer: cel-shading y límites de opacidad** | *Menú superior > Material > Mixer* | Advanced | Entre Posterize y Outline se consigue el aspecto de cómic o cel-shading, que para un proyecto de videojuegos con estilo ilustrado es justo lo que interesa. |
| 🎴 | **Posterize** | *Menú superior > Material > Mixer* | Advanced | Reduce el material a bandas planas de color (0). |
| ✒️ | **Outline** | *Menú superior > Material > Mixer* | Advanced | Dibuja un CONTORNO alrededor del modelo (0). |
| 📏 | **Depth** | *Menú superior > Material > Mixer* | Advanced | El grosor o alcance de ese contorno (3). |
| 🔽 | **MinOpacity** | *Menú superior > Material > Mixer* | Advanced | El mínimo de opacidad resultante. |
| 🔼 | **MaxOpacity** | *Menú superior > Material > Mixer* | Advanced | El máximo de opacidad resultante. |
| 👁️ | **PreviewOpacity** | *Menú superior > Material > Mixer* | Advanced | La opacidad en la vista previa. |


## Material > Environment, Matcap Maker


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💡 | **Material > Environment y Matcap Maker: respuesta al entorno y crear tu propio MatCap** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | Dos sub-paletas. ENVIRONMENT controla cómo responde el material al entorno. MATCAP MAKER es el creador de MatCaps propios: fabricarte uno para tu proyecto es una forma de que todas tus piezas se presenten con el mismo look. |


## Material > Environment


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌑 | **Shadow** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | Cuánta sombra recibe el material (100). |
| 🌘 | **Ao** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | Cuánta oclusión ambiental recibe (100). |
| 🌈 | **Vibrant Shadows And AO** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | Activo en naranja en tu captura. Hace que esas sombras conserven color en vez de volverse grises, lo que da un resultado bastante más vivo. |


## Material > Matcap Maker


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✨ | **Gloss** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | El brillo del MatCap que estás creando (2). |
| 🔬 | **Refine** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | El detalle del cálculo (25). |
| 💡 | **Intensity** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | La intensidad general (1). |
| 💧 | **Saturation** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | La saturación general (1). |
| ◐ | **Contrast** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | El contraste general (1). |
| 🔦 | **BackLight** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | Una luz de contra que separa la silueta del fondo (0). |
| ✨ | **Specular** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | El reflejo especular (0). |
| 🎲 | **Sample** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | Las muestras de calidad del cálculo (4). |
| ⚪ | **MatCap** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | Genera el material MatCap. |
| 🅱️ | **B** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | El botón que acompaña a MatCap. |
| 📉 | **MatCap Falloff** | *Menú superior > Material > Environment, Matcap Maker* | Advanced | La curva de caída de la luz del MatCap. |

