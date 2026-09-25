# Brushes


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖌️ | **Ventana de selección de pincel** | <kbd>B</kbd> | Basic | Abre la ventana emergente con todos los pinceles cargados. El truco que ahorra tiempo de verdad: no hace falta buscar con el ratón, porque los pinceles están agrupados por INICIAL. Pulsando B y luego dos letras más saltas directamente al que quieres — B, C, L te lleva a ClayBuildup; B, M, V a Move. Aprenderse cuatro o cinco combinaciones de las que más uses es de lo que más agiliza el trabajo diario. |
| ⭕ | **Tamaño de trazo (Draw Size)** | <kbd>S</kbd> | Basic | Abre el deslizador del tamaño del pincel para escribir o arrastrar el valor. En la práctica casi nadie usa esta tecla, porque los corchetes [ y ] hacen lo mismo sin soltar el trazo. Ojo con no confundir Draw Size (el tamaño del círculo del pincel) con Focal Shift (la dureza de su borde, tecla O) ni con Z Intensity (la fuerza con la que empuja la superficie): son tres cosas distintas y las tres están en la barra superior. |
| 🎯 | **Focal Shift** | <kbd>O</kbd> | Intermediate | Controla cuánto se concentra el efecto del pincel en el centro. |
| 🎨 | **Intensidad RGB** | <kbd>I</kbd> | Intermediate | La opacidad con la que se aplica el COLOR al pintar, de 0 a 100. Solo tiene efecto si estás pintando, o sea con Rgb o Mrgb activo en la barra superior; si solo estás esculpiendo, el que manda es Z Intensity. Para pintar piel conviene bajarla bastante, en torno a 10 o 15, e ir construyendo el color por capas suaves en vez de dar un brochazo opaco. Recuerda además que para ver el color hace falta Colorize activo en Tool > Polypaint. |
| 📐 | **Intensidad Z** | <kbd>U</kbd> | Intermediate | Intensidad del efecto de escultura (profundidad). |
| ↕️ | **Aumentar / disminuir tamaño de trazo** | <kbd>] / [</kbd> | Basic | Los corchetes suben y bajan el tamaño del pincel en pasos pequeños, y es el atajo más usado del programa junto con Mayús para suavizar. La ventaja sobre la tecla S es que puedes cambiar el tamaño SIN interrumpir lo que estás haciendo ni levantar el lápiz de la tableta. Si trabajas con teclado en español, comprueba dónde te caen los corchetes; si te resultan incómodos, se pueden reasignar desde Preferences > Hotkeys y guardar con Store. |
| 🔀 | **Alternar Añadir / Restar (ZAdd/ZSub)** | *Alt (mantener) + Clic izquierdo* | Basic | Mientras mantienes Alt pulsada, el pincel hace LO CONTRARIO de lo que hace normalmente: si añade geometría hacia fuera (ZAdd), pasa a restarla hacia dentro (ZSub), y al revés. Vale para casi todos los pinceles, no solo para los de añadir volumen: es la forma de meter hacia dentro con el mismo pincel con el que estabas sacando hacia fuera, sin cambiar de herramienta. Es el mismo Alt que con el botón DERECHO sirve para panear: ver la fila 'Los 4 modificadores del ratón'. |
| ✏️ | **Herramienta Draw (esculpir)** | <kbd>Q</kbd> | Basic | El modo de trabajo normal: el pincel actúa sobre la superficie, esculpiendo o pintando. Es al que hay que volver siempre después de mover o rotar una pieza, y olvidarse de hacerlo es el despiste más habitual de quien empieza — intentas dar un trazo y en vez de eso desplazas el modelo entero. Q, W, E y R son las mismas cuatro teclas seguidas del teclado y en el mismo orden que en Maya, así que la costumbre se transfiere entre los dos programas. |
| ✋ | **Herramienta Move** | <kbd>W</kbd> | Basic | Cambia el pincel por el Gizmo 3D (o la Transpose Line) para DESPLAZAR la pieza entera, o solo la parte que no esté enmascarada. Ahí está la clave de cómo se posa y se ajusta en ZBrush: enmascaras lo que quieres dejar quieto, y lo que queda libre es lo que se mueve. Con la máscara bien puesta y un poco de degradado en su borde, el movimiento sale suave en vez de arrancar la geometría de golpe. |
| 📏 | **Herramienta Scale** | <kbd>E</kbd> | Basic | Cambia el pincel por el manipulador para ESCALAR. Igual que con Move, actúa sobre la pieza entera o sobre lo que no esté enmascarado. Con el Gizmo 3D puedes escalar en un solo eje tirando de su asa correspondiente, que es como se alarga un brazo o se ensancha un torso sin deformar el resto. Ojo: escalar un SubTool cambia su tamaño respecto a los demás, así que si vas a exportar a un motor conviene revisar después la escala real en Zplugin > Scale Master. |
| 🔄 | **Herramienta Rotate** | <kbd>R</kbd> | Basic | Cambia el pincel por el manipulador para GIRAR. Es el modo con el que se posa un personaje: enmascaras el cuerpo, colocas el pivote en la articulación con la Transpose Line o moviendo el Gizmo, y giras solo el miembro libre. Para una pose completa con muchos SubTools, el camino cómodo no es este sino Zplugin > Transpose Master, que fusiona todo en una malla ligera, la posas, y devuelve la pose a cada pieza. |
| 🫧 | **Smooth temporal (mantener Mayús)** | *Mayús (mantener)* | Basic | EL atajo más importante de ZBrush después de los de navegación: mientras mantienes Mayús pulsada, el pincel que tengas activo se convierte temporalmente en Smooth, y al soltarla vuelve el anterior. Permite esculpir y suavizar sin cambiar de herramienta ni una sola vez. La intensidad y el tipo de suavizado se ajustan en Brush > Smooth Brush Modifiers. |
| ⌨️ | **Lazy Mouse** | <kbd>L</kbd> | Intermediate | Lazy Mouse |
| ⌨️ | **Smooth temporal** | *Mayús (mantener)* | Basic | Smooth temporal |
| 🎛️ | **Brush + Stroke + Alpha: anatomía de un pincel** | *Paletas Brush / Stroke / Alpha* | Intermediate | En ZBrush un pincel no es una cosa sino tres combinadas: el PINCEL en sí (qué deformación hace), el STROKE (cómo se reparte a lo largo del trazo: Dots, Freehand, DragRect, Spray, ColorSpray...) y el ALPHA (la forma de la punta, una imagen en blanco y negro). El mismo pincel con otro Stroke y otro Alpha hace algo completamente distinto: entender esto es la diferencia entre usar 5 pinceles y usar 500. |
| 🖌️ | **Brush: familias de pinceles y para qué sirve cada una** | *Paleta Brush (Tecla B)* | Basic | Los que de verdad se usan a diario: Clay y ClayBuildup construyen volumen a base de 'pegotes', ideales para bloquear formas. Standard empuja hacia fuera. DamStandard hace surcos y arrugas finas (el rey del detalle). Move mueve masas grandes sin añadir material. Inflate hincha. hPolish y TrimDynamic aplanan y pulen superficies duras. Pinch junta la malla hacia el trazo, para afilar bordes. Smooth suaviza (ver Mayús). |
| 📏 | **Draw Size vs Focal Shift** | <kbd>S / O</kbd> | Basic | Se confunden mucho y son cosas distintas: Draw Size (S) es el DIÁMETRO del pincel, el círculo que ves. Focal Shift (O) es cómo de blando es su borde dentro de ese círculo: valores negativos concentran el efecto en el centro (punta dura y marcada), valores positivos lo reparten hacia fuera (punta suave y difusa). Ajustar Focal Shift es lo que hace que un trazo parezca profesional en vez de un pegote. |
| 🌊 | **Sculptris Pro** | *\  \|  Barra superior (botón de fondo marrón, entre Rotate y Mrgb)* | Intermediate | ATAJO CONFIRMADO por su nota emergente: la tecla \ activa y desactiva Sculptris Pro ('Activate Sculptris Pro Mode'). Modo de escultura dinámica: en vez de trabajar con una densidad de malla fija, añade y quita polígonos automáticamente justo donde estás esculpiendo. Permite empezar de una esfera básica y sacar detalle en una oreja sin tener que subdividir el modelo entero. Muy cómodo para explorar formas, pero deja una topología desordenada: se suele usar al principio y luego pasar por ZRemesher. |
| ⌨️ | **Sculptris Pro** | <kbd>\</kbd> | Intermediate | Sculptris Pro |


## Biblioteca de pinceles > la ventana y cómo se lee


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗂️ | **Biblioteca de pinceles > la ventana y cómo se lee** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | La rejilla completa de pinceles de fábrica, que se abre con la TECLA B o pulsando la primera miniatura de la barra izquierda. Está ordenada alfabéticamente y arriba tiene un índice de letras A-Z: pulsando B y luego dos letras más saltas directo a un pincel (B,C,L = ClayBuildup). El número pequeño en la esquina de algunas miniaturas es cuántas mallas contiene ese pincel de inserción. Arriba del todo, QUICK PICK guarda los últimos usados; en tu captura, Clay, ClayBuildup, MaskPen, SelectRect y Standard. |
| 📂 | **Load Brush** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Carga un pincel desde archivo (.ZBP). |
| 💾 | **Save As** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Guarda el pincel activo como archivo. |
| 📄 | **Clone** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Duplica el pincel activo para poder trastear sin estropear el original. |
| 🧩 | **Create InsertMesh** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Convierte la herramienta activa en un pincel de INSERTAR esa malla. |
| 🧱 | **Create InsertMultiMesh** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Convierte varios SubTools en un pincel IMM con todas esas piezas dentro. En gris en tu captura porque hace falta más de un SubTool. |
| 🌾 | **Create NanoMesh Brush** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Crea un pincel NanoMesh, que siembra copias de la malla por la superficie. |
| 🅰️ | **Create MultiAlpha Brush** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Crea un pincel que lleva varios alphas dentro y va alternándolos. |
| ↩️ | **Reset All Brushes** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Devuelve TODOS los pinceles a sus ajustes de fábrica. Es el botón al que recurrir cuando un pincel 'se ha vuelto loco' y no sabes qué le tocaste. |


## Biblioteca de pinceles > arcilla y volumen


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🏺 | **Biblioteca de pinceles > arcilla y volumen** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los pinceles de CONSTRUIR masa, que son con los que se bloquea la forma general al principio. La pareja Clay/ClayBuildup es la más usada de ZBrush después de Standard. |
| 🖌️ | **Standard** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | El pincel básico: empuja la superficie hacia fuera, o hacia dentro manteniendo Alt. Es el que sale por defecto y el que más cambia de carácter al ponerle un alpha. |
| 🏺 | **Clay** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | Añade masa como si pegaras pegotes de barro, rellenando en vez de abultar. Aplana un poco mientras construye, así que la superficie sale menos grumosa que con Standard. |
| 🧱 | **ClayBuildup** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | La versión con alpha cuadrado del Clay: construye más rápido y deja un plano marcado. Es EL pincel para bloquear músculos y masas grandes al empezar. |
| 🧵 | **ClayTubes** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Deja tiras de arcilla, como churros pegados. Bueno para masas orgánicas con textura. |
| 🧵 | **ClayTubesConst** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Variante del anterior. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| ☁️ | **SoftClay** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Arcilla blanda: construye más suave y difuminado que Clay, sin aristas. |
| 🧽 | **ThickSkinClay** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Arcilla con 'piel gruesa': el efecto se queda en la superficie y no atraviesa los pliegues cercanos. |
| 🪨 | **SoftConcrete** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Superficie de hormigón blando, con grano. Bueno para roca y materiales duros gastados. |
| 🫧 | **Blob** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Levanta bultos redondeados e irregulares, como gotas. Muy usado para criaturas y para romper una superficie demasiado limpia. |
| 🎈 | **Inflat** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | Infla la zona siguiendo las normales de la malla, o sea la engorda hacia fuera en todas direcciones en vez de empujar en una sola. |
| 📄 | **Layer** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Levanta una capa de altura CONSTANTE: por muchas pasadas que des, no sigue subiendo. Es el pincel para sellos y relieves de grosor uniforme, sobre todo con un alpha. |
| 🌀 | **Crumple** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Arruga la superficie, como papel estrujado. |
| 📐 | **Fold** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Crea pliegues marcados. |
| ❄️ | **Flakes** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Añade escamillas y trocitos sueltos sobre la superficie. |
| 💥 | **Fracture** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Rompe y agrieta la superficie. |
| 🌊 | **Displace** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Desplaza la superficie siguiendo el alpha, sin añadir masa propia. |
| 🎈 | **Elastic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estira la malla como una goma, conservando mejor el volumen que Move. |
| 🔍 | **Magnify** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Agranda localmente lo que hay debajo, como una lupa sobre la geometría. |
| 👻 | **Morph** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Devuelve la zona al estado guardado en el Morph Target: se pinta para 'borrar' lo esculpido solo donde pasas. Es el borrador selectivo de ZBrush. |
| 🌾 | **Noise** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Añade ruido a la superficie. |
| 👉 | **Nudge** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Empuja la superficie lateralmente, arrastrando el detalle sin cambiar el volumen. |
| 🤏 | **Pinch** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | Junta la malla hacia el centro del trazo, afilando un borde. Es lo que convierte un pliegue blando en una arista definida. |
| 〰️ | **Rake** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Rastrillo: deja surcos paralelos, como pasar un peine por el barro. |
| 🌀 | **Spiral** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Retuerce la superficie en espiral. |
| 🧶 | **Weave1** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estampa un trenzado o tejido. |


## Biblioteca de pinceles > suavizar, aplanar y pulir


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✨ | **Biblioteca de pinceles > suavizar, aplanar y pulir** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los pinceles de QUITAR ruido y ordenar la superficie. Recuerda que manteniendo MAYÚS cualquier pincel pasa temporalmente a Smooth, así que no hace falta cambiar de pincel para suavizar. |
| 〰️ | **Smooth** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | El suavizado normal. Es el que se activa manteniendo Mayús con cualquier otro pincel. |
| 〰️ | **SmoothAlt** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Una variante del suavizado con otro comportamiento. |
| 🧵 | **SmoothCloth** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Suaviza conservando los pliegues y bordes de tela, en vez de derretirlos. |
| 🔺 | **SmoothPeaks** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Suaviza SOLO lo que sobresale, dejando intactos los huecos. |
| 🕳️ | **SmoothValleys** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Suaviza SOLO los huecos, dejando intacto lo que sobresale. |
| ✨ | **Polish** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Pule la superficie dejándola lisa y con aspecto de material duro. |
| ✨ | **sPolish** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Variante de pulido más suave. |
| ✨ | **hPolish** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Pulido duro: aplana la zona creando planos limpios con aristas. Es el pincel para objetos manufacturados, armaduras y piedra tallada. |
| ▭ | **Flatten** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Aplana la zona contra un plano, cortando todo lo que sobresale. |
| 📐 | **Planar** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Aplana siguiendo el plano de la superficie donde empezaste el trazo. |
| ◐ | **ContrastDelta** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Ajusta el contraste del relieve según la diferencia con lo que hay alrededor. |
| ◐ | **ContrastTarget** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Ajusta el contraste del relieve respecto a un valor de referencia. |
| ☁️ | **FormSoft** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Suaviza la FORMA general sin comerse el detalle fino de encima. |


## Biblioteca de pinceles > la familia Trim


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✂️ | **Biblioteca de pinceles > la familia Trim** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los TRIM recortan: aplanan la zona contra un plano y se comen lo que sobresale, como si pasaras una gubia. Son los que dan el aspecto de piedra tallada o de metal limado, y manteniendo Alt hacen lo contrario (rellenan el hueco). |
| ✂️ | **TrimAdaptive** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Recorta adaptándose a la curvatura de la superficie. |
| ⭕ | **TrimCircle** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Recorta con una máscara circular que arrastras. |
| 〰️ | **TrimCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Recorta siguiendo una curva que dibujas: el corte sigue exactamente esa línea. |
| ⚡ | **TrimDynamic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | El más usado de la familia: recorta creando planos que siguen la forma, ideal para dar facetas duras a una roca o a una armadura. |
| 🔗 | **TrimLasso** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Recorta con una selección a mano alzada. |
| ▭ | **TrimRect** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Recorta con un rectángulo. |


## Biblioteca de pinceles > mover, estirar y posar


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✋ | **Biblioteca de pinceles > mover, estirar y posar** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los pinceles que DESPLAZAN geometría en vez de añadir o quitar masa. |
| ✋ | **Move** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | Arrastra la zona bajo el pincel. El pincel de las correcciones grandes de silueta. |
| 🎈 | **Move Elastic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Mueve conservando mejor el volumen, como si la malla fuera elástica. |
| 🕸️ | **Move Topological** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Mueve siguiendo la TOPOLOGÍA y no la distancia en el espacio: así puedes mover un labio sin arrastrar el de abajo, aunque estén pegados. |
| 〰️ | **MoveCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Mueve a lo largo de una curva. |
| 📏 | **MoveInfiniteDep** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Mueve sin límite de profundidad, afectando también a lo que está detrás. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🛝 | **Slide** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Desliza los polígonos SOBRE la superficie sin cambiar la forma: sirve para recolocar el mallado sin deformar el modelo. |
| 🪝 | **SnakeHook** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estira un tentáculo desde la superficie, alargando la malla. Es como se sacan cuernos, dedos y apéndices de una masa. |
| 🪝 | **SnakeHook2** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Variante del SnakeHook. |
| ⚪ | **SnakeSphere** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estira terminando en una forma esférica. |
| 🌵 | **SnakeCactus** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estira con forma de púa o de cactus. |
| 📏 | **Transpose** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | El pincel asociado a la Transpose Line, la línea de tres círculos con la que se posa y se dobla el modelo. |
| 📏 | **TransposeClassic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | La versión clásica de Transpose. |
| 🧵 | **TransposeCloth** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Transpose pensado para tela: al mover, la superficie se pliega como un paño. |
| 🎭 | **TransposeSmar** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Transpose con máscara automática. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |


## Biblioteca de pinceles > cortar y seccionar


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔪 | **Biblioteca de pinceles > cortar y seccionar** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los que PARTEN la malla. Los Clip no cortan de verdad: empujan la geometría contra la línea y la dejan plana. Los Slice sí crean un PolyGroup nuevo por el corte, y los Knife separan la malla en trozos. |
| ⭕ | **ClipCircle** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Aplasta contra un círculo todo lo que queda fuera de él. |
| ⭕ | **ClipCircleCenter** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Igual, pero el círculo crece desde el centro donde pulsas. |
| 〰️ | **ClipCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Aplasta contra una curva dibujada a mano, que es la variante más usada: sirve para dejar un corte recto y limpio en una escultura. |
| ▭ | **ClipRect** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Aplasta contra un rectángulo. |
| ⭕ | **SliceCirc** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Traza un corte circular que crea un PolyGroup nuevo, sin separar la malla. |
| 〰️ | **SliceCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Lo mismo siguiendo una curva. |
| ▭ | **SliceRect** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Lo mismo con un rectángulo. |
| 🔪 | **KnifeCircle** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Corta de verdad la malla siguiendo un círculo. |
| 🔪 | **KnifeCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Corta siguiendo una curva. |
| 🔪 | **KnifeLasso** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Corta siguiendo una selección a mano alzada. |
| 🔪 | **KnifeRect** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Corta siguiendo un rectángulo. |
| ⚔️ | **Slash3** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Deja un tajo afilado, como un arañazo o un corte de espada. |


## Biblioteca de pinceles > máscara y selección


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎭 | **Biblioteca de pinceles > máscara y selección** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Pinceles que no tocan la forma: pintan MÁSCARA (zona protegida) o hacen selecciones. Recuerda que Ctrl + arrastrar ya pinta máscara con cualquier pincel. |
| ⭕ | **MaskCircle** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Enmascara un círculo. |
| 〰️ | **MaskCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Enmascara siguiendo una curva. |
| ✏️ | **MaskCurvePen** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Dibuja la curva de la máscara punto a punto, como una pluma. |
| 🔗 | **MaskLasso** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Enmascara con una selección a mano alzada. |
| 🖊️ | **MaskPen** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Pinta la máscara a mano alzada. Es el que tienes en Quick Pick. |
| ⭕ | **MaskPerfectCirc** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Enmascara un círculo perfecto. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| ▭ | **MaskRect** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Enmascara un rectángulo. |
| ⬛ | **MaskSquare** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Enmascara un cuadrado. |
| 🔗 | **SelectLasso** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Selecciona a mano alzada para ocultar o mostrar geometría. |
| ▭ | **SelectRect** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Selecciona con un rectángulo. Es el que tienes en Quick Pick, y el que se usa con Ctrl+Mayús para aislar una parte del modelo. |


## Biblioteca de pinceles > tallar, grabar y estampar


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✒️ | **Biblioteca de pinceles > tallar, grabar y estampar** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los de DETALLE fino: líneas, surcos, grabados y patrones. DamStandard es probablemente el pincel más famoso de ZBrush. |
| ✒️ | **DamStandard** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Basic | Marca una línea hundida y afilada. Es EL pincel de las arrugas, los pliegues de ropa, las junturas entre piezas y la boca de un personaje. Con Alt levanta en vez de hundir. |
| 🪚 | **Chisel** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Talla como un cincel, dejando marcas duras. |
| 🪚 | **Chisel3D** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Cincel que inserta formas en 3D. |
| 🐲 | **ChiselCreature** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Cincel con formas de criatura: escamas, placas. |
| 🌿 | **ChiselOrganic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Cincel con formas orgánicas. |
| ▭ | **ChiselRect** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Cincel con formas rectangulares. |
| 🔶 | **ChiselShapes** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Cincel con un surtido de formas geométricas. |
| ✏️ | **ScribeChisel** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Garabatea líneas talladas tipo cincel. |
| ✏️ | **ScribeStandard** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Garabatea líneas finas. |
| 📐 | **CreaseCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Marca como Crease las aristas que sigue la curva, para que no se redondeen al subdividir. |
| 🧵 | **StitchBasic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estampa costuras. Combinado con una curva sacada de Frame Mesh, da una costura perfecta por el borde de una pieza de ropa. |
| ▦ | **Hatch** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Raya la superficie con tramas cruzadas. |
| ▦ | **HatchBacktrack** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Lo mismo, obligando al trazo a seguir una guía recta. |
| 🔲 | **LayeredPattern** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estampa un patrón por capas. |
| 🔳 | **Pattern01** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estampa un patrón geométrico. |
| 🔳 | **Pattern02** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Otro patrón geométrico. |
| 🎀 | **Deco1** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Estampa un motivo decorativo. |
| 🎨 | **Paint** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Pinta color sobre la superficie (Polypaint) sin tocar la forma. |
| 🖊️ | **Pen A** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Dibuja líneas finas tipo pluma. |
| 🌑 | **Pen Shadow** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Dibuja sombreando, como un lápiz de grafito. |


## Biblioteca de pinceles > la familia Curve


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 〰️ | **Biblioteca de pinceles > la familia Curve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los pinceles de CURVA no actúan donde pasas: dibujas primero una curva y la forma se genera a lo largo de ella, y luego puedes mover la curva y todo se recalcula. Son la forma de hacer tubos, cables, correas, cadenas y ribetes. Sus ajustes están en la paleta Stroke > Curve. |
| 🅰️ | **CurveAlpha** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Reparte un alpha a lo largo de la curva. |
| 🅰️ | **CurveAlphas** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Lo mismo con varios alphas alternándose. |
| 🌉 | **CurveBridge** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Tiende un puente de geometría entre dos bordes. |
| ▭ | **CurveFlat** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Genera una cinta plana a lo largo de la curva. |
| 🧲 | **CurveFlatSnap** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | La cinta plana, pegada a la superficie del modelo. |
| 🏺 | **CurveLathe** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Genera una forma de torno, girando el perfil alrededor de la curva. |
| 🧵 | **CurveMultiTube** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Genera varios tubos paralelos a la vez. |
| 🤏 | **CurvePinch** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Afila la superficie a lo largo de la curva. |
| 🔲 | **CurveQuadFill** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Rellena de cuadrados el área que encierra la curva: sirve para generar una superficie nueva con topología limpia. |
| 🧲 | **CurveSnapSurfa** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Curva pegada a la superficie. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 〰️ | **CurveStandard** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | El de curva básico: aplica el pincel Standard a lo largo de la curva. |
| 🧲 | **CurveStrapSnap** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Genera una correa pegada a la superficie. Ideal para cinturones y tiras de armadura. |
| 🌐 | **CurveSurface** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Genera una superficie a lo largo de la curva. |
| 🔺 | **CurveTriFill** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Rellena con triángulos el área de la curva. |
| 🧵 | **CurveTube** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Genera un TUBO a lo largo de la curva. El más usado de la familia: cables, venas, cuerdas. |
| 🧲 | **CurveTubeSnap** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | El tubo, pegado a la superficie del modelo. |
| ⚫ | **DecoCurveDots** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Reparte puntos decorativos por la curva. |
| 🎀 | **DecoCurveDrag** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Arrastra un motivo decorativo por la curva. |
| 🌊 | **DisplaceCurve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Desplaza la superficie siguiendo la curva. |
| 🐍 | **SnakeCurve1** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Serpentea una forma a lo largo de la curva. |
| 🐍 | **SnakeCurve2** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Otra variante de SnakeCurve. |
| 🐍 | **SnakeCurve4** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Otra variante de SnakeCurve. |
| 🐍 | **SnakeCurve5** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Otra variante de SnakeCurve. |


## Biblioteca de pinceles > la familia Cloth


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧵 | **Biblioteca de pinceles > la familia Cloth** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los pinceles de TELA: deforman la malla como si fuera un paño, generando pliegues creíbles sobre la marcha. Funcionan mejor con una malla densa y son hermanos de la paleta Dynamics, pero aquí simulas pintando en vez de lanzar una simulación entera. |
| ⚪ | **ClothBall** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Empuja la tela formando un bulto redondeado. |
| 🕳️ | **ClothDimple** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Hunde un hoyuelo en la tela. |
| 📐 | **ClothFold** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | El más útil de la familia: crea PLIEGUES a lo largo del trazo. |
| 🪝 | **ClothHook** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Engancha y estira la tela desde un punto. |
| 🎈 | **ClothInflate** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Infla la tela. |
| ✋ | **ClothMove** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Mueve la tela dejando que se pliegue al desplazarse. |
| 👉 | **ClothNudge** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Empuja la tela lateralmente. |
| 🤏 | **ClothPinch** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Junta la tela, afilando un pliegue. |
| 🤏 | **ClothPinchTrails** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Deja un rastro de pliegues afilados. |
| 🧲 | **ClothPull** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Tira de la tela hacia el pincel. |
| 🛝 | **ClothSlide** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Desliza la tela sobre la superficie de debajo. |
| 🌀 | **ClothTwister** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Retuerce la tela. |
| 💨 | **ClothWind** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Mueve la tela como si le diera el viento. Muy vistoso para capas. |


## Biblioteca de pinceles > la familia Groom (pelo)


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💇 | **Biblioteca de pinceles > la familia Groom (pelo)** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los GROOM están hechos para trabajar con FiberMesh, las fibras que ZBrush genera sobre la malla: peinan, alargan, rizan y hasta colorean el pelo. Solo tienen sentido cuando hay fibras generadas desde Tool > FiberMesh. |
| 💨 | **GroomBlower** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Sopla las fibras, como un secador. |
| 🖌️ | **GroomBrush1** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Peina las fibras en la dirección del trazo. |
| 🪢 | **GroomClumps** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Agrupa las fibras en mechones. |
| 🎨 | **GroomColorMic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Colorea las fibras. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🎨 | **GroomColorRoc** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Colorea las fibras. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🎨 | **GroomColorTip** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Colorea las PUNTAS de las fibras, que es como se hacen las mechas y el degradado de color natural del pelo. |
| 💪 | **GroomerStrong** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Peina con fuerza. |
| ⚪ | **GroomHairBall** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Agrupa el pelo en una bola. |
| 📏 | **GroomHairLong** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Trabaja el pelo largo. |
| ✂️ | **GroomHairShort** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Trabaja el pelo corto. |
| 💨 | **GroomHairToss** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Revuelve el pelo. |
| 📏 | **GroomLengthe** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Alarga las fibras. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🔺 | **GroomSpike** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Pone las fibras de punta. |
| 🌀 | **GroomSpinKnot** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Retuerce las fibras en un nudo. |
| 🌪️ | **GroomTurbuler** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Da turbulencia a las fibras. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🌀 | **GroomTwister** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Retuerce las fibras. |


## Biblioteca de pinceles > la familia IMM (Insert Multi Mesh)


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧩 | **Biblioteca de pinceles > la familia IMM (Insert Multi Mesh)** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Los IMM llevan DENTRO un conjunto de mallas ya modeladas y las insertan como geometría nueva sobre el modelo: pulsas y aparece la pieza, que luego colocas y escalas. El número de la esquina de la miniatura es cuántas piezas contiene. Manteniendo la barra espaciadora (o pulsando M) se abre el selector de piezas de ese pincel. Son la forma rápida de vestir un personaje o de poblar de detalle una superficie dura sin modelarlo todo. |
| 🪖 | **IMM Army Curv** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 7 piezas de equipo militar, insertadas por curva. |
| 🔶 | **IMM Basic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | El juego básico de piezas. |
| ➖ | **IMM Boolean** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 37 piezas pensadas para restar y sumar en booleanos. |
| 🦴 | **IMM BParts** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 20 piezas de cuerpo. |
| 🧥 | **IMM Clothing H** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 13 piezas de ropa y complementos. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 〰️ | **IMM Curve** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 30 piezas para insertar a lo largo de una curva. |
| 🔫 | **IMM Gun** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 106 piezas de armas de fuego. |
| ⚙️ | **IMM Ind. Parts** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 12 piezas industriales. |
| ⚙️ | **IMM MachinePa** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 30 piezas de maquinaria. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🧰 | **IMM ModelKit** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 120 piezas de kit de modelado: el más surtido para superficie dura. |
| 🧩 | **IMM Parts** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 68 piezas variadas. |
| 🔷 | **IMM Primitives** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 14 primitivas (cubo, esfera, cilindro...) listas para insertar. El más socorrido para empezar una pieza mecánica. |
| 🔷 | **IMM PrimitivesK** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 12 primitivas más. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🚀 | **IMM SpaceShip** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 162 piezas de nave espacial. |
| ⚙️ | **IMM SteamGear** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 32 piezas de estética steampunk. |
| 🎈 | **IMM Toon** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 52 piezas de estilo caricaturesco. |
| 🧥 | **IMM WinterCoo** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 10 piezas de abrigo de invierno. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🤐 | **IMM ZipperM** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 6 cremalleras (versión M). |
| 🤐 | **IMM ZipperP** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | 6 cremalleras (versión P). |


## Biblioteca de pinceles > insertar geometría y biselar


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ➕ | **Biblioteca de pinceles > insertar geometría y biselar** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Pinceles que AÑADEN geometría nueva al SubTool, no que deforman la que hay. |
| 🎈 | **MeshBalloon** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Infla una malla nueva como un globo. |
| ⬆️ | **MeshExtrude** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Extruye geometría desde la superficie. |
| ⬆️ | **MeshExtrudePr** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Extruye siguiendo un perfil. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| ⚫ | **MeshInsert Dot** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Inserta la malla como un punto suelto. |
| 📽️ | **MeshProject** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Proyecta una malla sobre la superficie. |
| 💦 | **MeshSplat** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Estampa la malla aplastada contra la superficie. |
| 🛢️ | **InsertCylndrExt** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Inserta un cilindro extruido (1 pieza). |
| 🌙 | **BevelArc** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Bisela un borde con forma de arco. |
| 📐 | **BevelFlat** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Bisela un borde dejándolo plano. |
| 📈 | **ExtrudeProfile** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Extruye con 31 perfiles distintos a elegir. |
| 📈 | **ExtrudeProfile2** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Otros 23 perfiles de extrusión. |
| ⚓ | **Anchors** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Clava puntos de anclaje sobre la malla y deforma tirando de ellos, como un rig rápido para posar sin esqueleto (7 variantes). |
| ⚓ | **AnchorsClassic** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | La versión clásica de Anchors (6 variantes). |


## Biblioteca de pinceles > los especiales


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🛠️ | **Biblioteca de pinceles > los especiales** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Intermediate | Pinceles que no esculpen en el sentido normal: son herramientas completas metidas dentro de un pincel. ZModeler es el más importante de todos. |
| 🧰 | **ZModeler** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | El modelador poligonal de ZBrush: con él se trabaja polígono a polígono, arista a arista y punto a punto, con un menú radial que aparece al pulsar Espacio sobre el elemento. Es lo que convierte ZBrush en una herramienta de modelado duro de verdad, y el pincel con el que se hacen armas, cascos y props con topología limpia. |
| 📽️ | **ZProject** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Proyecta sobre el SubTool activo el detalle del que tiene debajo. |
| 〰️ | **ZRemesherGuid** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | No esculpe: dibuja GUÍAS que le dicen a ZRemesher por dónde quieres que corran las aristas al remallar. Es como se controla la topología de un remallado automático. |
| 🕸️ | **Topology** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Dibuja topología nueva a mano sobre una malla existente: se trazan las líneas y ZBrush genera la superficie de cuadrados. Retopología manual dentro de ZBrush. |
| 🎨 | **QuickPolygrou** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Crea PolyGroups rápidamente pintando sobre la malla. ⚠️ PENDIENTE: la etiqueta sale RECORTADA en la rejilla y no se lee entera. Pásale el ratón por encima para ver la nota emergente con el nombre completo y dímelo. |
| 🪞 | **MatchMaker** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Amolda la malla a la forma del SubTool que tiene detrás, como si la apretaras contra él. Sirve para que una pieza de armadura calce exactamente sobre el cuerpo. |
| 🕓 | **HistoryRecall** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Pinta para recuperar el estado ANTERIOR del historial solo donde pasas: un deshacer selectivo por zonas. |
| 🩸 | **XTractor** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Extrae el detalle de la superficie y lo convierte en un alpha, para poder reutilizarlo como sello en otra parte. |
| ⚫ | **XTractorDot** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Lo mismo, extrayendo desde un punto. |
| ▭ | **XTractorDragRe** | *Selector de pinceles (tecla B) / barra izquierda, primera miniatura* | Advanced | Lo mismo, arrastrando un rectángulo. |

