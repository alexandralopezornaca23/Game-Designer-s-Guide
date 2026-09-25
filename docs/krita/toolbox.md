# Toolbox


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧰 | **La caja de herramientas: cómo se lee** | *Barra vertical de la izquierda* | Basic | La rejilla de iconos de la izquierda. Al elegir una herramienta, sus opciones aparecen en el docker TOOL OPTIONS, que es donde de verdad se configura cada una. Pasando el ratón por encima de un icono, la nota emergente te dice el nombre y su atajo. Las herramientas se agrupan por familias: pintura, formas, selección, relleno, transformación y utilidades. |
| 🖌️ | **Freehand Brush Tool** | <kbd>B</kbd> | Basic | El PINCEL a mano alzada, la herramienta con la que vas a pasar el 90% del tiempo. Lo que pinta depende del PRESET de pincel elegido en la barra de herramientas, no de esta herramienta: la herramienta solo dice 'trazo libre'. |
| 🧽 | **Alternar el modo BORRADOR** | <kbd>E</kbd> | Basic | Un detalle de Krita que despista viniendo de Photoshop: el borrador NO es una herramienta de la caja, es un MODO del pincel que tengas puesto. Pulsas E y el mismo pincel borra con su misma textura y su mismo tamaño; vuelves a pulsar E y pinta otra vez. Por eso no verás nunca un icono de goma en la caja de herramientas. |
| 🌀 | **Dynamic Brush Tool** | — | Intermediate | Un pincel con inercia: el trazo sigue al cursor con retraso y suaviza el pulso, parecido al Lazy Mouse de ZBrush. Bueno para líneas largas y limpias de entintado. |
| 🔯 | **Multibrush Tool** | <kbd>Q</kbd> | Intermediate | Pinta varias copias simétricas del trazo a la vez, alrededor de un punto. Es la herramienta para mandalas, motivos circulares, adornos y cualquier diseño radial — y también para simetría vertical rápida al bocetar una cara. |
| ✒️ | **Calligraphy Tool** | — | Intermediate | Traza con plumilla caligráfica: el grosor cambia según el ángulo del trazo. Produce un trazo vectorial, no de píxeles. |
| 📏 | **Straight Line Tool** | — | Basic | Línea recta con el pincel activo. |
| 〰️ | **Bezier Curve Tool** | — | Intermediate | Dibuja una curva Bézier punto a punto, con tiradores para ajustar la curvatura. |
| ✏️ | **Freehand Path Tool** | — | Intermediate | Dibuja un trazado a mano alzada que se cierra solo y se puede rellenar. |
| ▭ | **Rectangle Tool** | — | Basic | Dibuja un rectángulo. Como todas las de forma, puede salir como píxeles o como VECTOR según el tipo de capa en la que estés. |
| ⭕ | **Ellipse Tool** | — | Basic | Dibuja una elipse o un círculo. |
| 🔷 | **Polygon Tool** | — | Basic | Dibuja un polígono cerrado de los lados que quieras. |
| 📐 | **Polyline Tool** | — | Basic | Dibuja una sucesión de líneas rectas encadenadas. |
| ▭ | **Rectangular Selection Tool** | — | Basic | Selecciona un área rectangular. Todas las herramientas de selección comparten en Tool Options los modos SUMAR, RESTAR, REEMPLAZAR e INTERSECAR, que es lo que permite construir una selección compleja a base de trozos. |
| ⭕ | **Elliptical Selection Tool** | — | Basic | Selecciona un área elíptica o circular. |
| 🔗 | **Freehand Selection Tool** | — | Basic | Selecciona dibujando el contorno a mano alzada, como un lazo. |
| 📐 | **Polygonal Selection Tool** | — | Basic | Selecciona marcando vértices, con lados rectos entre ellos. |
| 🪄 | **Contiguous Selection Tool** | — | Basic | La 'varita mágica': selecciona la mancha de color continua sobre la que pulsas. El deslizador de tolerancia decide cuánta diferencia de color admite antes de parar. |
| 🎯 | **Similar Color Selection Tool** | — | Intermediate | Como la anterior, pero selecciona TODOS los píxeles de ese color en la capa, estén juntos o no. Útil para cambiar de golpe un color plano repartido por el dibujo. |
| 🧲 | **Magnetic Selection Tool** | — | Intermediate | Selecciona siguiendo los bordes de contraste: vas marcando puntos cerca del contorno y la selección se pega sola a él. Es la más rápida para recortar una figura sobre un fondo distinto. |
| ✏️ | **Path Selection Tool** | — | Intermediate | Selecciona dibujando un trazado Bézier, para contornos curvos precisos. |
| 🔷 | **Shape Selection Tool** | — | Intermediate | Selecciona a partir de una forma vectorial. |
| 🪣 | **Fill Tool** | <kbd>F</kbd> | Basic | El CUBO de pintura: rellena de color la zona sobre la que pulsas. En Tool Options, el ajuste GROW SELECTION (crecer unos píxeles) es el que evita esos bordes blancos feos entre el relleno y la línea. |
| 🫗 | **Enclose and Fill Tool** | — | Intermediate | Rellena TODAS las zonas cerradas que queden dentro del área que marcas, de una sola pasada. Es lo que convierte el coloreado plano de un dibujo lineal en cosa de segundos en vez de ir hueco por hueco con el cubo. |
| 🌈 | **Gradient Tool** | <kbd>G</kbd> | Basic | Traza un DEGRADADO arrastrando. Los degradados son un recurso más, así que puedes cargar juegos enteros. |
| 💉 | **Color Sampler Tool** | <kbd>P</kbd> | Basic | El CUENTAGOTAS: toma un color del lienzo. En la práctica no vas a usar la herramienta, porque manteniendo CTRL con el pincel puesto haces lo mismo sin cambiar de herramienta. |
| 🖍️ | **Colorize Mask** | — | Advanced | La joya escondida de Krita para colorear dibujo lineal: haces unos garabatos de color dentro de cada zona y Krita calcula solo los límites siguiendo las líneas, generando las máscaras de color. Lo que a mano son horas de recortar, aquí son minutos. |
| ✂️ | **Crop Tool** | <kbd>C</kbd> | Basic | Recorta la imagen o la capa. En Tool Options se elige si el recorte afecta a la imagen entera, solo a la capa o solo a una selección. |
| ✋ | **Move Tool** | <kbd>T</kbd> | Basic | Mueve el contenido de la capa o de la selección. Ojo con la opción de Tool Options que decide si mueve la capa activa, el grupo o todas: es la causa típica de 'se me ha movido lo que no era'. |
| 🔀 | **Transform Tool** | <kbd>Ctrl</kbd> + <kbd>T</kbd> | Intermediate | La herramienta de TRANSFORMAR, y una de las más potentes del programa. En Tool Options elige entre transformación libre, perspectiva, malla (warp), jaula (cage) y LICUAR (liquify), que empuja los píxeles como si fueran pintura fresca — perfecto para corregir una proporción sin volver a dibujar. |
| 🔧 | **Shape Edit Tool** | — | Intermediate | Edita los nodos y tiradores de una forma vectorial ya creada. |
| 🔤 | **Text Tool** | — | Intermediate | Escribe texto vectorial, editable después. Para la interfaz de un juego o la portada de una lámina. |
| 💬 | **Comic Panel Editing Tool** | — | Intermediate | Crea y ajusta viñetas de cómic dividiendo la página. Krita trae bastantes herramientas pensadas para el cómic, que es una de las cosas que lo diferencia de otros programas de pintura. |
| 🩹 | **Smart Patch Tool** | — | Intermediate | Tapa una zona copiando y mezclando el contenido de alrededor, para hacer desaparecer algo sin que se note el parche. |
| 📐 | **Assistant Tool** | — | Advanced | Coloca ASISTENTES de dibujo sobre el lienzo: puntos de fuga, perspectiva de 1, 2 y 3 puntos, elipses concéntricas, reglas paralelas y curvas francesas. Con un asistente activo, el trazo del pincel se pega a él. Es la herramienta que hace viable dibujar un escenario en perspectiva correcta sin ser arquitecta. |
| 🖼️ | **Reference Images Tool** | — | Intermediate | Coloca imágenes de referencia FLOTANDO sobre el lienzo, sin que formen parte del dibujo ni se exporten. Es el equivalente dentro de Krita a lo que haces en PureRef, y se guarda con el .KRA. |
| 📏 | **Measure Tool** | — | Intermediate | Mide distancias y ángulos sobre el lienzo. |
| ✋ | **Pan Tool** | — | Basic | Desplaza la vista. En la práctica se usa la BARRA ESPACIADORA mantenida, que hace lo mismo sin cambiar de herramienta. |
| 🔍 | **Zoom Tool** | — | Basic | Acerca y aleja la vista. |

