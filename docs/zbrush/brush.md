# Brush


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🖌️ | **Brush: qué es esta paleta y por qué casi todo sale en gris** | *Menú superior > Brush (Tecla B abre el selector)* | Basic | Esta paleta NO elige el pincel (para eso está la Tecla B o la primera miniatura de la barra izquierda): es donde se AJUSTA por dentro el pincel que ya tienes activo. Cada pincel de ZBrush es en realidad una plantilla con decenas de parámetros, y aquí están todos. Por eso, con el Standard activo, la mayoría de sub-paletas salen en gris: solo se encienden las opciones que ese pincel concreto usa (las de FiberMesh solo con un pincel de pelo, las de Curve solo con un pincel de curva, las de Clip solo con un Clip...). No te preocupes por el gris, es normal. Lo que toques aquí se queda hasta que cierres ZBrush o pulses Reset, así que si un pincel empieza a portarse raro, la última fila de esta categoría es la solución. |
| 💾 | **Brush > cargar, guardar y clonar pinceles** | *Menú superior > Brush* | Intermediate | La gestión de los pinceles como archivo. Si afinas un Standard para escamas, guárdalo y lo tendrás siempre. |
| 📂 | **Load Brush** | *Menú superior > Brush* | Intermediate | Carga un pincel desde archivo (.ZBP). Así se instalan los pinceles que te bajas de internet, que es algo que vas a hacer mucho. |
| 💾 | **Save As** | *Menú superior > Brush* | Intermediate | Guarda el pincel activo CON todos los ajustes que le hayas cambiado. |
| ⧉ | **Clone** | *Menú superior > Brush* | Intermediate | Duplica el pincel activo para trastear sin romper el original (en gris en tu captura). |
| 🖼️ | **SelectIcon** | *Menú superior > Brush* | Intermediate | Le pone un icono propio al pincel para reconocerlo en la rejilla (en gris en tu captura). |
| 📚 | **Lightbox▶Brushes** | *Menú superior > Brush* | Intermediate | Abre la biblioteca de pinceles que trae el programa. |
| 🎚️ | **el deslizador del pincel activo** | *Menú superior > Brush* | Intermediate | Muestra el pincel activo ('Standard.' en tu captura) y sirve para ir pasando por los cargados. |
| 🔄 | **R** | *Menú superior > Brush* | Intermediate | Es RESTORE CONFIGURATION, el mismo botón que aparece en Alpha y en Tool: devuelve el número de elementos visibles a la configuración por defecto. |
| 🎛️ | **Brush > la rejilla de pinceles** | *Menú superior > Brush* | Basic | El recuadro grande es el pincel activo y, al pulsarlo, se abre la rejilla completa de pinceles (lo mismo que la tecla B). A su lado están los últimos usados como acceso rápido. Los botones To Mesh y From Mesh que hay junto a la rejilla tienen su propia fila justo debajo. |
| 🖌️ | **Standard** | *Menú superior > Brush* | Basic | El pincel base, el de empujar la superficie hacia fuera o hacia dentro. |
| 🏺 | **Clay** | *Menú superior > Brush* | Basic | Construye volumen a base de 'pegotes' de barro. |
| 🧱 | **ClayBuildup** | *Menú superior > Brush* | Basic | La variante que acumula más, y uno de los más usados para bloquear formas. |
| 🎭 | **MaskPen** | *Menú superior > Brush* | Basic | Pinta máscara a mano. |
| ▭ | **SelectRect** | *Menú superior > Brush* | Basic | Oculta geometría con un rectángulo. |
| 🧊 | **To Mesh** | *Menú superior > Brush* | Advanced | Convierte en malla 3D la geometría que lleve dentro el pincel. Útil con los pinceles de inserción, para sacar la pieza y editarla. |
| 🖌️ | **From Mesh** | *Menú superior > Brush* | Advanced | El camino contrario: mete una malla dentro del pincel. Sale en gris porque el Standard no lleva geometría dentro. |
| ↩️ | **Brush > los dos botones de reinicio** | *Menú superior > Brush* | Basic | Conviene tenerlos MUY presentes: como en esta paleta cualquier cambio se queda puesto hasta que cierras el programa, es facilísimo dejar un pincel tocado sin acordarte y luego pensar que ZBrush se ha vuelto loco. Antes de volverte loca tú, prueba Reset Current Brush. Y si guardaste una versión tuya con Save As, no la pierdes: sigue en su archivo. |
| ↩️ | **Reset Current Brush** | *Menú superior > Brush* | Basic | Devuelve el pincel activo a como venía de fábrica. |
| 🔄 | **Reset All Brushes** | *Menú superior > Brush* | Basic | Hace lo mismo con todos los pinceles cargados. |


## Menú superior > Brush > Create


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ➕ | **Brush > Create: fabricar pinceles propios** | *Menú superior > Brush > Create* | Advanced | Aquí es donde se FABRICAN pinceles a partir de geometría tuya, y es de lo más útil de la paleta para un flujo de videojuegos. Todo sale en gris si el pincel activo no es de inserción. |
| 📌 | **Create InsertMesh** | *Menú superior > Brush > Create* | Advanced | Convierte el SubTool activo en un pincel que estampa esa pieza sobre el modelo: modelas un remache una vez y luego lo colocas cien veces. |
| 🗂️ | **Create InsertMultiMesh** | *Menú superior > Brush > Create* | Advanced | Lo mismo con VARIAS piezas dentro del mismo pincel (los pinceles IMM), y luego eliges cuál insertar: así se monta un juego completo de tornillos, hebillas y correas en un solo pincel. |
| 🌾 | **Create NanoMesh Brush** | *Menú superior > Brush > Create* | Advanced | Crea un pincel que reparte copias en masa sobre la superficie. |
| 🏷️ | **Create MultiAlpha Brush** | *Menú superior > Brush > Create* | Advanced | Agrupa varios alphas en un solo pincel para ir alternando entre ellos. |
| 📋 | **Brush > Create: gestionar las piezas de un pincel IMM** | *Menú superior > Brush > Create* | Advanced | Con estos se reorganiza un pincel de inserción sin tener que rehacerlo entero, que es lo que quieres cuando descubres que te falta una variante. |
| 📋 | **Copy Meshes** | *Menú superior > Brush > Create* | Advanced | Copia TODAS las mallas del pincel. |
| 📄 | **Copy One Mesh** | *Menú superior > Brush > Create* | Advanced | Copia solo la malla seleccionada. |
| ♻️ | **Paste Replace** | *Menú superior > Brush > Create* | Advanced | Sustituye las mallas que había por las copiadas. |
| 📥 | **Paste Append** | *Menú superior > Brush > Create* | Advanced | Añade las copiadas al final de la lista. |
| 📌 | **Paste Insert** | *Menú superior > Brush > Create* | Advanced | Las mete en el punto que tengas marcado. |
| 🗑️ | **Delete Mesh** | *Menú superior > Brush > Create* | Advanced | Quita la pieza seleccionada del pincel. |
| ✏️ | **Edit Brush Credit** | *Menú superior > Brush > Create* | Advanced | Deja escrita la autoría del pincel. Conviene rellenarlo si vas a compartirlo o si forma parte de tu portafolio. |


## Menú superior > Brush > Curve


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 〰️ | **Brush > Curve** | *Menú superior > Brush > Curve* | Advanced | Solo se enciende con los pinceles de CURVA (CurveTube, CurveStrap, los IMM en modo curva, Snake Hook con curva...), esos con los que dibujas una línea y ZBrush construye geometría a lo largo de ella. |
| ✏️ | **Edit Curve** | *Menú superior > Brush > Curve* | Advanced | Permite seguir moviendo la curva DESPUÉS de dibujarla, en vez de deshacer y repetir. |
| 🎯 | **AccuCurve** | *Menú superior > Brush > Curve* | Advanced | Afina la precisión con que la curva sigue tu trazo. |
| 🔁 | **WrapMode** | *Menú superior > Brush > Curve* | Advanced | Controla cómo se envuelve o repite lo que se genera a lo largo de la curva (0 en tu captura). |
| ✒️ | **Curve By Pen** | *Menú superior > Brush > Curve* | Advanced | Hace que la presión del lápiz module la curva. |
| 📈 | **Zero Curve** | *Menú superior > Brush > Curve* | Advanced | Uno de los dos editores de curva (las rampas grises): define cómo varía el efecto de un extremo al otro del trazo, que es lo que hace que un tubo se afile en las puntas en vez de quedar del mismo grosor. |
| 📈 | **Pen Curve** | *Menú superior > Brush > Curve* | Advanced | El otro editor de curva del bloque, ligado a la presión del lápiz. |


## Menú superior > Brush > Depth


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⬇️ | **Brush > Depth: Imbed** | *Menú superior > Brush > Depth* | Advanced | Un solo control, pero es el que vas a usar con todos los pinceles de inserción. |
| ⬇️ | **Imbed** | *Menú superior > Brush > Depth* | Advanced | Decide cuánto se HUNDE la pieza insertada dentro del modelo. Con Imbed bajo, el remache queda apoyado encima de la superficie; con Imbed alto, queda medio enterrado, que es lo que se quiere para que parezca clavado y no pegado. Es el primer valor a revisar cuando insertas una pieza y flota. |
| 📏 | **Brush > Depth: la franja de profundidad** | *Menú superior > Brush > Depth* | Advanced | A qué PROFUNDIDAD actúa el pincel respecto a la superficie. El círculo naranja grande de arriba es la representación visual de esa franja. |
| 🎭 | **Depth Mask** | *Menú superior > Brush > Depth* | Advanced | Enmascara automáticamente todo lo que quede fuera de la franja: es lo que permite esculpir solo lo que sobresale o solo lo que está hundido, sin pintar ninguna máscara. |
| ⬆️ | **OuterDepth** | *Menú superior > Brush > Depth* | Advanced | Define hasta dónde llega la franja hacia FUERA de la superficie. |
| ⬇️ | **InnerDepth** | *Menú superior > Brush > Depth* | Advanced | Define hasta dónde llega hacia DENTRO. |
| 📈 | **Brush Depth Curve** | *Menú superior > Brush > Depth* | Advanced | Ajusta el reparto del efecto dentro de esa franja con una curva. |
| ♾️ | **Infinite Depth** | *Menú superior > Brush > Depth* | Advanced | Quita el límite y hace que el pincel llegue hasta donde sea. |
| 🌍 | **Gravity Strength** | *Menú superior > Brush > Depth* | Advanced | Hace que el trazo caiga hacia abajo mientras lo aplicas, muy útil para dar sensación de peso en telas y carnes. |


## Menú superior > Brush > Samples


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔬 | **Brush > Samples: BuildUp** | *Menú superior > Brush > Samples* | Intermediate | El ajuste de esta sub-paleta que más se nota al esculpir. |
| 📶 | **BuildUp** | *Menú superior > Brush > Samples* | Intermediate | Con él activado, el efecto del pincel se ACUMULA si mantienes el cursor quieto o pasas varias veces por el mismo sitio, igual que un aerógrafo que va cargando pintura; sin él, cada pasada llega a un tope y por mucho que insistas no profundiza más. Los pinceles de detalle fino suelen quererlo apagado y los de construir volumen encendido. |
| 📡 | **Brush > Samples: cómo lee el pincel la superficie** | *Menú superior > Brush > Samples* | Advanced | ZBrush toma varias MUESTRAS del terreno alrededor del cursor y promedia lo que encuentra. Los tres nombres están confirmados con tus notas emergentes. |
| ⚡ | **Fast Samples** | *Menú superior > Brush > Samples* | Advanced | Es 'Use Fast Samples': un cálculo más rápido y menos preciso. Viene activado, y es lo que hace que el pincel responda ágil. |
| 📏 | **ConstSamples** | *Menú superior > Brush > Samples* | Advanced | Es 'Constant Samples Radius': mantiene fijo el radio de muestreo en vez de escalarlo con el tamaño del pincel. |
| 📐 | **Samples Radius** | *Menú superior > Brush > Samples* | Advanced | Es 'Surface Samples Radius': el tamaño de esa zona que se muestrea. |
| 🧭 | **Brush > Samples: cuánto obedece el pincel al promedio** | *Menú superior > Brush > Samples* | Advanced | Entre estos dos está la diferencia entre un pincel que se pega bien a una superficie curva y uno que resbala. |
| 🧭 | **Normal** | *Menú superior > Brush > Samples* | Advanced | Es 'Align Normal With Avg Surface Samples' (por defecto 1): cuánto se alinea la ORIENTACIÓN del pincel con el promedio de la superficie. |
| 📍 | **Pos** | *Menú superior > Brush > Samples* | Advanced | Es 'Align Position With Avg Surface Samples' (también 1): lo mismo pero con su POSICIÓN. |
| 📐 | **Brush > Samples: estabilizar y encarrilar el trazo** | *Menú superior > Brush > Samples* | Advanced | Los tres últimos hacen un trabajo parecido al de Lazy Mouse en la paleta Stroke, pero desde el propio pincel. |
| 🌐 | **OnSurface** | *Menú superior > Brush > Samples* | Advanced | Hace que el trazo SIGA la superficie en vez de proyectarse recto desde la pantalla, que es la diferencia entre una línea que abraza un brazo redondo y una que lo atraviesa. |
| ➖ | **Preserve Edge** | *Menú superior > Brush > Samples* | Advanced | Protege los bordes de la malla para que no se deformen ni se abran (1 en tu captura). |
| 🧭 | **Stabilize Orientation** | *Menú superior > Brush > Samples* | Advanced | Estabiliza la orientación del trazo. |
| ➡️ | **Stabilize Direction** | *Menú superior > Brush > Samples* | Advanced | Estabiliza la dirección del trazo (0 en tu captura), útil para conseguir líneas limpias sin depender del pulso. |
| 📏 | **Ortho** | *Menú superior > Brush > Samples* | Advanced | Fuerza el trazo a ir recto, en horizontal o en vertical. |
| 🔦 | **Brush > Samples: los controles de Spotlight** | *Menú superior > Brush > Samples* | Advanced | Cómo trabaja este pincel con SPOTLIGHT, la herramienta que deja una imagen flotando sobre el modelo para proyectarla (Mayús+Z cuando hay una textura cargada). Es el flujo clásico para meter detalle de fotos de piel o de roca. |
| 🔦 | **Spotlight Projection** | *Menú superior > Brush > Samples* | Advanced | Permite que el pincel esculpa o pinte tomando la información de esa imagen (activo en naranja en tu captura). |
| 🌗 | **Spotlight MidValue** | *Menú superior > Brush > Samples* | Advanced | Hace el mismo papel que el MidValue de los alphas: fija qué gris de la imagen cuenta como altura cero, o sea qué sobresale y qué se hunde (0 en tu captura). |
| 🫧 | **Spotlight Alpha Blur** | *Menú superior > Brush > Samples* | Advanced | Difumina el borde de lo proyectado para que no quede un corte duro (1 en tu captura). |


## Menú superior > Brush > Elasticity


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎈 | **Brush > Elasticity** | *Menú superior > Brush > Elasticity* | Advanced | Para los pinceles ELÁSTICOS, tipo Move Elastic, que al arrastrar una zona hacen que la de alrededor la acompañe estirándose como una goma en vez de romperse. Con el Standard activo no hacen nada. |
| 🎈 | **Elasticity Strength** | *Menú superior > Brush > Elasticity* | Advanced | Cuánta elasticidad hay (0 en tu captura). |
| 🤖 | **Elasticity Auto Adjust** | *Menú superior > Brush > Elasticity* | Advanced | La regula sola según el caso (0 en tu captura). |
| 🔌 | **Elasticity Auto Off** | *Menú superior > Brush > Elasticity* | Advanced | Desactiva el efecto pasado cierto umbral (25 en tu captura). |
| 🔁 | **Simulation Iterations** | *Menú superior > Brush > Elasticity* | Advanced | Las pasadas de cálculo de esa simulación: más pasadas, resultado más creíble y más lento (0 en tu captura). |


## Menú superior > Brush > FiberMesh


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧶 | **Brush > FiberMesh** | *Menú superior > Brush > FiberMesh* | Advanced | Solo funciona con los pinceles de PEINAR FIBRAS (los Groom, que se usan sobre pelo, hierba o plumas hechos con FiberMesh). |
| 📏 | **Preserve Length** | *Menú superior > Brush > FiberMesh* | Advanced | Mantiene el largo de la fibra mientras la peinas, para que no se estire ni encoja (0 en tu captura). |
| ⬆️ | **Forward Propagation** | *Menú superior > Brush > FiberMesh* | Advanced | Reparte el movimiento hacia la PUNTA, que es lo que hace que un mechón se mueva entero en vez de doblarse solo por donde tocas. |
| ⬇️ | **Inverse Propagation** | *Menú superior > Brush > FiberMesh* | Advanced | Reparte el movimiento hacia la RAÍZ. |
| 🪵 | **Stiffness** | *Menú superior > Brush > FiberMesh* | Advanced | La rigidez de la fibra. |
| 🌀 | **Spring** | *Menú superior > Brush > FiberMesh* | Advanced | Cuánto tiende la fibra a volver a su sitio. |
| 💥 | **Front Collision Tolerance** | *Menú superior > Brush > FiberMesh* | Advanced | Cómo chocan las fibras entre sí y con el modelo, para que el pelo no atraviese la cabeza. |
| 🎲 | **Front Collision Variations** | *Menú superior > Brush > FiberMesh* | Advanced | La variación aleatoria de esa colisión entre fibras. |


## Brush > Twist, Orientation


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌀 | **Brush > Twist y Brush > Orientation** | *Menú superior > Brush* | Advanced | Dos sub-paletas pequeñas que hacen girar el efecto del pincel: una retuerce la geometría y la otra gira el alpha. Subiendo SpinRate un poco, un alpha de escamas o de piedras deja de verse como un patrón calcado. |


## Menú superior > Brush > Twist


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌀 | **Twist Rate** | *Menú superior > Brush* | Advanced | Cuánto retuerce la geometría mientras trazas (0 en tu captura). |
| 💫 | **Centrifugal** | *Menú superior > Brush* | Advanced | Cuánto se abre hacia fuera al girar (0 en tu captura). |
| 📏 | **Radius** | *Menú superior > Brush* | Advanced | El alcance de ese giro (1 en tu captura). |


## Menú superior > Brush > Orientation


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎯 | **SpinCenter** | *Menú superior > Brush* | Advanced | Mueve el punto sobre el que gira el alpha (0 en tu captura). |
| 📐 | **SpinAngle** | *Menú superior > Brush* | Advanced | El ángulo de partida del giro (0 en tu captura). |
| 🔄 | **SpinRate** | *Menú superior > Brush* | Advanced | Cuánto gira el alpha en cada pasada (0 en tu captura). Es el que evita que un sello repetido se note repetido. |


## Menú superior > Brush > Surface


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌊 | **Brush > Surface** | *Menú superior > Brush > Surface* | Advanced | El mismo ruido procedural de Tool > Surface, pero aplicado AL PINCEL en vez de a todo el SubTool: así el pincel va dejando textura (piel, roca, corteza) según pintas, solo donde tú pasas. Es una forma muy rápida de que un modelo deje de parecer de plastilina. |
| 🌾 | **Noise** | *Menú superior > Brush > Surface* | Advanced | Activa el ruido y abre el editor NoiseMaker. |
| ✏️ | **Edit** | *Menú superior > Brush > Surface* | Advanced | Vuelve a abrir ese editor para retocar el ruido. |
| 🗑️ | **Del** | *Menú superior > Brush > Surface* | Advanced | Borra el ruido del pincel. |
| 🧭 | **Local Projection Mode** | *Menú superior > Brush > Surface* | Advanced | Cambia el sistema con el que el ruido se proyecta sobre la superficie. |
| 🔍 | **Dynamic Scale** | *Menú superior > Brush > Surface* | Advanced | Hace que el tamaño del ruido se ajuste solo al tamaño del pincel (activo en naranja en tu captura). |
| 📏 | **Base Scale** | *Menú superior > Brush > Surface* | Advanced | Fija la escala de partida del ruido. |


## Menú superior > Brush > Modifiers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚙️ | **Brush > Modifiers: los generales** | *Menú superior > Brush > Modifiers* | Advanced | OJO con el primero, porque es especial: su significado CAMBIA según el pincel que tengas activo. |
| 🃏 | **Brush Modifier** | *Menú superior > Brush > Modifiers* | Advanced | Un deslizador COMODÍN cuyo significado cambia según el pincel: en unos controla la dureza, en otros la forma del efecto, en otros el número de repeticiones. Por eso no se puede dar una definición única, y por eso merece la pena tocarlo cuando un pincel no hace exactamente lo que quieres. |
| ✖️ | **Strength Multiplier** | *Menú superior > Brush > Modifiers* | Advanced | Multiplica la fuerza general del pincel más allá de lo que da Z Intensity (1 en tu captura), útil cuando 100 se te queda corto. |
| 🫧 | **Smooth** | *Menú superior > Brush > Modifiers* | Advanced | Mezcla suavizado en el propio trazo (0 en tu captura). |
| ✒️ | **Pressure** | *Menú superior > Brush > Modifiers* | Advanced | Ata el efecto a la presión del lápiz. |
| 📐 | **Tilt Brush** | *Menú superior > Brush > Modifiers* | Advanced | Inclina el pincel respecto a la superficie (0 en tu captura), lo que cambia bastante el resultado de un alpha estampado. |
| 📐 | **ConstantTilt** | *Menú superior > Brush > Modifiers* | Advanced | Mantiene esa inclinación constante. |
| 🧩 | **Brush > Modifiers: inserción** | *Menú superior > Brush > Modifiers* | Advanced | Solo se enciende con pinceles IMM y de curva; esta mitad es la de INSERCIÓN. |
| 👀 | **MeshInsert Preview** | *Menú superior > Brush > Modifiers* | Advanced | Muestra la pieza antes de soltarla, para colocarla con calma. |
| 🗂️ | **MultiMesh Select** | *Menú superior > Brush > Modifiers* | Advanced | Elige cuál de las mallas del pincel se va a insertar, lo mismo que se hace con la ventana que sale al mantener M. |
| 🎲 | **Variations** | *Menú superior > Brush > Modifiers* | Advanced | Aplica variaciones automáticas de tamaño y giro para que las copias no salgan idénticas: es lo que evita que una hilera de remaches se vea calcada. |
| 🎯 | **Projection Strength** | *Menú superior > Brush > Modifiers* | Advanced | Cuánto se pega la pieza a la superficie del modelo. |
| 🔺 | **Tri Parts** | *Menú superior > Brush > Modifiers* | Advanced | Afecta a cómo se corta la geometría al insertarla (activo en naranja en tu captura). |
| 🔗 | **Weld Points** | *Menú superior > Brush > Modifiers* | Advanced | Afecta a cómo se suelda la geometría al insertarla. |
| 〰️ | **Brush > Modifiers: curva** | *Menú superior > Brush > Modifiers* | Advanced | La mitad que gobierna los pinceles de CURVA: los que reparten una pieza a lo largo de una línea que dibujas. Es el grupo al que hay que venir siempre que un pincel de curva no da lo que esperas. |
| ↔️ | **Stretch** | *Menú superior > Brush > Modifiers* | Advanced | Decide si las piezas se ESTIRAN para cubrir la curva. |
| ⧉ | **Overlap** | *Menú superior > Brush > Modifiers* | Advanced | Decide si las piezas se SOLAPAN entre ellas. Entre este y Stretch se ajusta que una cadena quede con los eslabones enganchados y no separados ni aplastados. |
| 🔢 | **Curve Res** | *Menú superior > Brush > Modifiers* | Advanced | La resolución de la curva, o sea cuántas piezas caben. |
| 📐 | **Max Bend Angle** | *Menú superior > Brush > Modifiers* | Advanced | Cuánto puede doblarse una pieza antes de romper. Es el valor a revisar cuando una cremallera o una cuerda salen deformadas en las esquinas cerradas. |
| 💨 | **Brush > Modifiers: dispersión del trazo** | *Menú superior > Brush > Modifiers* | Advanced | El bloque que dispersa y multiplica el trazo, el que usan por dentro los pinceles tipo spray. Subiendo aperturas y orientaciones, un solo trazo suelta un rociado de marcas distintas: es la forma de hacer poros, salpicaduras o pecas sin ir una a una. |
| 👣 | **Trails** | *Menú superior > Brush > Modifiers* | Advanced | Cuántas copias del trazo se dejan a la vez (1 en tu captura). |
| 🎚️ | **Intensity** | *Menú superior > Brush > Modifiers* | Advanced | La fuerza de esas copias secundarias (0.4 en tu captura). |
| ↕️ | **V Aperture** | *Menú superior > Brush > Modifiers* | Advanced | La apertura vertical de la dispersión (0.25 en tu captura). |
| ↔️ | **H Aperture** | *Menú superior > Brush > Modifiers* | Advanced | La apertura horizontal de la dispersión (0.25 en tu captura). |
| 🌍 | **GPosition** | *Menú superior > Brush > Modifiers* | Advanced | Desplaza esas copias de forma GLOBAL (0.25 en tu captura). |
| 📍 | **LPosition** | *Menú superior > Brush > Modifiers* | Advanced | Las desplaza de forma LOCAL. |
| 🔄 | **GOrientation** | *Menú superior > Brush > Modifiers* | Advanced | Gira esas copias de forma global. |
| 🔄 | **LOrientation** | *Menú superior > Brush > Modifiers* | Advanced | Las gira de forma local. |


## Menú superior > Brush > Sculptris Pro


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔺 | **Brush > Sculptris Pro: permisos del pincel** | *Menú superior > Brush > Sculptris Pro* | Intermediate | SCULPTRIS PRO es el modo (tecla \) en el que ZBrush añade y quita polígonos SOLO donde estás esculpiendo, sin tener que subdividir el modelo entero: puedes sacar un cuerno de una esfera de pocos polígonos y el programa va creando malla sobre la marcha. Este grupo decide si ESTE pincel puede usarlo. |
| 🔘 | **Enable** | *Menú superior > Brush > Sculptris Pro* | Intermediate | Permite que este pincel use Sculptris Pro (activo en naranja en tu captura). |
| 🌍 | **Use Global** | *Menú superior > Brush > Sculptris Pro* | Intermediate | Hace que use la configuración general del programa en vez de una propia para este pincel (también activo). |
| 🪄 | **Wants SculptrisPro** | *Menú superior > Brush > Sculptris Pro* | Intermediate | Hace que al elegir este pincel se active el modo solo, sin tener que pulsar la tecla. Cómodo en pinceles que solo tienen sentido con Sculptris Pro. |
| ⚖️ | **Brush > Sculptris Pro: la malla que se genera** | *Menú superior > Brush > Sculptris Pro* | Intermediate | AVISO importante: la malla que sale es de TRIÁNGULOS y desordenada, muy buena para explorar formas al principio pero no para detallar en serio — antes de eso hay que pasar por ZRemesher. |
| 📏 | **Adaptive Size** | *Menú superior > Brush > Sculptris Pro* | Intermediate | Ajusta el tamaño de los triángulos nuevos al tamaño del pincel, así que un pincel pequeño crea detalle fino y uno grande malla más suelta. |
| 🔀 | **Combined** | *Menú superior > Brush > Sculptris Pro* | Intermediate | Mezcla los dos criterios de subdivisión. |
| 🔬 | **SubDivide Size** | *Menú superior > Brush > Sculptris Pro* | Intermediate | Marca lo pequeños que se crean los triángulos nuevos. |
| 🧹 | **UnDivide Ratio** | *Menú superior > Brush > Sculptris Pro* | Intermediate | Cuánto se simplifica lo que dejas de tocar. Entre este y el anterior se decide si acabas con una malla razonable o con millones de triángulos sin control. |


## Menú superior > Brush > Auto Masking


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎭 | **Brush > Auto Masking: Topological** | *Menú superior > Brush > Auto Masking* | Advanced | AUTO MASKING es una de las sub-paletas más útiles de todas: hace que el pincel se enmascare SOLO mientras esculpes, sin que tengas que pintar ninguna máscara. La estructura se repite en casi todos sus modos: un botón que lo activa, un deslizador de intensidad y una CURVA con la que se afina el reparto. |
| 🔗 | **Topological** | *Menú superior > Brush > Auto Masking* | Advanced | La estrella y el que más te va a ahorrar: hace que el pincel afecte únicamente a la geometría conectada POR LA SUPERFICIE, no a la que está cerca en el aire. Con él puedes esculpir el labio de arriba sin arrastrar el de abajo, o un dedo sin mover el de al lado. |
| 📏 | **Range** | *Menú superior > Brush > Auto Masking* | Advanced | Hasta dónde llega esa conexión (5 en tu captura). |
| 🫧 | **Smooth** | *Menú superior > Brush > Auto Masking* | Advanced | Cómo se difumina el borde del efecto (10 en tu captura). |
| 🛡️ | **Brush > Auto Masking: por superficie, cavidad y color** | *Menú superior > Brush > Auto Masking* | Advanced | Tres modos que enmascaran según lo que hay en la superficie, cada uno con su trío de botón, intensidad y curva. Las curvas salen en gris hasta que activas el modo al que pertenecen. |
| 🔙 | **BackfaceMask** | *Menú superior > Brush > Auto Masking* | Advanced | Protege las caras que miran al otro lado, imprescindible en ropa y superficies finas para no deformar la cara de atrás sin darte cuenta. |
| 🎚️ | **BackMaskInt** | *Menú superior > Brush > Auto Masking* | Advanced | La intensidad de esa máscara de caras traseras. |
| 📈 | **BackMaskCurve** | *Menú superior > Brush > Auto Masking* | Advanced | El reparto de esa máscara. |
| 🪨 | **CavityMask** | *Menú superior > Brush > Auto Masking* | Advanced | Limita el efecto a las cavidades o a los salientes. Es el que se usa para que un trazo de color se meta solo en las grietas y quede esa suciedad realista de los recovecos. |
| 🎚️ | **CavityMaskInt** | *Menú superior > Brush > Auto Masking* | Advanced | La intensidad de la máscara por cavidad. |
| 📈 | **CavityMaskCurve** | *Menú superior > Brush > Auto Masking* | Advanced | El reparto de la máscara por cavidad. |
| 🎨 | **ColorMask** | *Menú superior > Brush > Auto Masking* | Advanced | Enmascara según el COLOR ya pintado: sirve para esculpir solo donde antes pintaste de un tono. |
| 🎚️ | **ColorMaskInt** | *Menú superior > Brush > Auto Masking* | Advanced | La intensidad de la máscara por color. |
| 📈 | **ColorMaskCurve** | *Menú superior > Brush > Auto Masking* | Advanced | El reparto de la máscara por color. |
| 🧭 | **Brush > Auto Masking: dirección, grupos e inserción** | *Menú superior > Brush > Auto Masking* | Advanced | El resto de modos de enmascarado automático. |
| ➡️ | **Directional** | *Menú superior > Brush > Auto Masking* | Advanced | Enmascara según la DIRECCIÓN del trazo: da trazos que se desvanecen según hacia dónde vas. |
| ✒️ | **ByPressure** | *Menú superior > Brush > Auto Masking* | Advanced | Ata ese efecto a la presión del lápiz de la tableta. |
| 📈 | **DirectionalMask Curve** | *Menú superior > Brush > Auto Masking* | Advanced | El reparto de la máscara direccional. |
| 🎨 | **Mask By Polygroups** | *Menú superior > Brush > Auto Masking* | Advanced | Respeta los PolyGroups existentes, o sea que el pincel no salta de un grupo de polígonos a otro (0 en tu captura). Muy práctico si has separado las piezas con PolyGroupIt. |
| 📌 | **Auto Mask Mesh Insert** | *Menú superior > Brush > Auto Masking* | Advanced | Enmascara automáticamente al insertar mallas, para que lo insertado no se deforme mientras sigues esculpiendo alrededor (activo de fábrica). |
| 💇 | **Auto Mask FiberMesh** | *Menú superior > Brush > Auto Masking* | Advanced | Hace lo mismo al trabajar con fibras (también activo de fábrica). |
| 📈 | **FiberMesh Mask Curve** | *Menú superior > Brush > Auto Masking* | Advanced | El reparto de esa máscara de fibras. |


## Menú superior > Brush > Tablet Pressure


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✒️ | **Brush > Tablet Pressure** | *Menú superior > Brush > Tablet Pressure* | Intermediate | Aquí se decide qué hace la PRESIÓN del lápiz en este pincel. Cada línea es una CURVA que va de 'apenas aprieto' a 'aprieto del todo'. Merece la pena tocarlo si notas que tienes que apretar demasiado para que el pincel responda, o al revés, que con rozar ya te hace un destrozo. |
| 🌍 | **Use Global Settings** | *Menú superior > Brush > Tablet Pressure* | Intermediate | Hace que el pincel use la curva general del programa en vez de la suya propia. |
| 📏 | **Size** | *Menú superior > Brush > Tablet Pressure* | Intermediate | Relaciona la presión con el TAMAÑO del trazo. |
| ⬇️ | **Z Intensity** | *Menú superior > Brush > Tablet Pressure* | Intermediate | Relaciona la presión con la FUERZA de escultura. |
| 🎨 | **Rgb Intensity** | *Menú superior > Brush > Tablet Pressure* | Intermediate | Relaciona la presión con la fuerza del COLOR. |
| 🃏 | **BrushMod** | *Menú superior > Brush > Tablet Pressure* | Intermediate | Relaciona la presión con el deslizador comodín Brush Modifier. |
| ⬇️ | **Brush Imbed** | *Menú superior > Brush > Tablet Pressure* | Intermediate | Relaciona la presión con lo que se hunde una pieza insertada. |


## Menú superior > Brush > Alpha and Texture


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🅰️ | **Brush > Alpha and Texture: colocación del alpha** | *Menú superior > Brush > Alpha and Texture* | Advanced | Cómo se coloca el alpha dentro de la huella del pincel. |
| 🛤️ | **AlignToPath** | *Menú superior > Brush > Alpha and Texture* | Advanced | El que más se nota: hace que el alpha se oriente siguiendo la DIRECCIÓN del trazo, así que al dibujar una curva las marcas giran contigo en vez de quedarse siempre en vertical. Imprescindible para escamas, plumas o cuerdas, y la explicación de por qué a veces un patrón sale 'de lado'. |
| 🔁 | **AlphaTile** | *Menú superior > Brush > Alpha and Texture* | Advanced | Repite el alpha dentro de la huella (1 en tu captura). |
| ↕️ | **Vertical Aperture** | *Menú superior > Brush > Alpha and Texture* | Advanced | Estira o encoge el alpha en vertical, para pasar de una marca redonda a una alargada sin tocar la imagen original. |
| ↔️ | **Horizontal Aperture** | *Menú superior > Brush > Alpha and Texture* | Advanced | Lo mismo en horizontal. |
| 📈 | **Magnify Curve** | *Menú superior > Brush > Alpha and Texture* | Advanced | Controla cómo se amplía el alpha al agrandar el pincel. |
| 🔽 | **Low Magnify** | *Menú superior > Brush > Alpha and Texture* | Advanced | El extremo bajo de esa curva de ampliación. |
| 🔼 | **High Magnify** | *Menú superior > Brush > Alpha and Texture* | Advanced | El extremo alto de esa curva. |
| 🖼️ | **Brush > Alpha and Texture: el alpha y la textura del pincel** | *Menú superior > Brush > Alpha and Texture* | Advanced | El resto del bloque, incluidos los dos huecos donde viven el alpha y la textura de ESTE pincel. |
| 🎨 | **Polypaint Mode** | *Menú superior > Brush > Alpha and Texture* | Advanced | Define cómo se mezcla el color pintado con el que ya hay (1 en tu captura). |
| 📐 | **Adaptive Map Size** | *Menú superior > Brush > Alpha and Texture* | Advanced | Ajusta la resolución del alpha al tamaño del pincel, para no gastar memoria de más con pinceles pequeños (0 en tu captura). |
| 🔺 | **Max Alpha To Mesh Size** | *Menú superior > Brush > Alpha and Texture* | Advanced | Limita el tamaño de la malla al convertir un alpha en geometría (64 en tu captura). |
| 🏷️ | **Alpha** | *Menú superior > Brush > Alpha and Texture* | Advanced | El hueco del alpha de este pincel, el mismo que ves en la barra izquierda (ALPHA OFF en tu captura). |
| 🖼️ | **Texture** | *Menú superior > Brush > Alpha and Texture* | Advanced | El hueco de la textura de este pincel (TEXTURE OFF en tu captura). |
| 📈 | **Alpha Transition** | *Menú superior > Brush > Alpha and Texture* | Advanced | Define cómo entra y sale el efecto del alpha a lo largo del trazo, para que el sello no empiece y termine de golpe sino con un degradado. |
| 📈 | **Texture Transition** | *Menú superior > Brush > Alpha and Texture* | Advanced | Lo mismo para la textura. |


## Menú superior > Brush > Clip Brush Modifiers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✂️ | **Brush > Clip Brush Modifiers** | *Menú superior > Brush > Clip Brush Modifiers* | Advanced | Ajustes de los pinceles CLIP (ClipCurve, ClipRect, ClipCircle), esos con los que trazas una línea y todo lo que queda a un lado se aplasta contra ella, como cortar barro con un hilo. |
| ◗ | **BRadius** | *Menú superior > Brush > Clip Brush Modifiers* | Advanced | Controla el redondeo de la esquina que queda al cortar, para que no salga un filo perfecto si no lo quieres. |
| 🎨 | **PolyGroup** | *Menú superior > Brush > Clip Brush Modifiers* | Advanced | El más práctico: asigna un PolyGroup nuevo a la parte recortada, con lo que después puedes aislarla al instante. |
| ↩️ | **Unclip** | *Menú superior > Brush > Clip Brush Modifiers* | Advanced | Deshace el recorte. |
| 🧩 | **Split To Parts** | *Menú superior > Brush > Clip Brush Modifiers* | Advanced | Separa en piezas independientes lo que ha quedado cortado. |


## Menú superior > Brush > Smooth Brush Modifiers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✨ | **Brush > Smooth Brush Modifiers: tamaño y algoritmo** | *Menú superior > Brush > Smooth Brush Modifiers* | Intermediate | Ajusta el SUAVIZADO, que es el que sale al mantener Mayús y el que más usas sin darte cuenta. |
| 📏 | **Alt Brush Size** | *Menú superior > Brush > Smooth Brush Modifiers* | Intermediate | Muy práctico: multiplica el tamaño del pincel cuando pasas a suavizar, así puedes esculpir con un pincel pequeño y suavizar con uno grande sin cambiar Draw Size a cada rato (1 en tu captura). |
| ⚖️ | **Weighted Smooth Mode** | *Menú superior > Brush > Smooth Brush Modifiers* | Intermediate | Elige entre los distintos algoritmos de suavizado que trae ZBrush (0 en tu captura). |
| 🎚️ | **Weight Strength** | *Menú superior > Brush > Smooth Brush Modifiers* | Intermediate | Cuánto pesa cada algoritmo (50 en tu captura): cambiarlo es la diferencia entre un suavizado que respeta la forma y otro que se come el volumen que te ha costado sacar. |
| ✨ | **PolishStrength** | *Menú superior > Brush > Smooth Brush Modifiers* | Intermediate | Añade pulido al suavizar, para acabados duros tipo metal o cerámica. |
| 🧲 | **Brush > Smooth Brush Modifiers: conexión y convergencia** | *Menú superior > Brush > Smooth Brush Modifiers* | Advanced | Ajustes finos que rara vez hay que tocar, pero explican por qué dos pinceles de suavizado distintos se comportan de forma diferente. |
| 🔗 | **Min Connected** | *Menú superior > Brush > Smooth Brush Modifiers* | Advanced | Evita que el suavizado salte a geometría que solo está cerca en el aire pero no conectada por la superficie. Es el equivalente de Topological pero para el suavizado, y evita que al suavizar un pliegue de la ropa se te aplaste la piel de debajo. |
| 📍 | **Converge Position** | *Menú superior > Brush > Smooth Brush Modifiers* | Advanced | Cuánto converge la POSICIÓN al suavizar, o sea hacia qué promedio tira (100 en tu captura). |
| 📏 | **Converge Radius** | *Menú superior > Brush > Smooth Brush Modifiers* | Advanced | El alcance de esa convergencia (20 en tu captura). |
| 🎨 | **Converge Color** | *Menú superior > Brush > Smooth Brush Modifiers* | Advanced | Cuánto converge el COLOR al suavizar (50 en tu captura). |


## Menú superior > Brush > MaskMesh Modifiers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎭 | **Brush > MaskMesh Modifiers** | *Menú superior > Brush > MaskMesh Modifiers* | Advanced | Los tres ajustes de los pinceles que convierten una MÁSCARA en geometría. Salen en gris con el Standard activo. |
| 🔢 | **Resolution** | *Menú superior > Brush > MaskMesh Modifiers* | Advanced | La densidad de la malla que se genera. |
| 🫧 | **Smoothness** | *Menú superior > Brush > MaskMesh Modifiers* | Advanced | Cuánto se suavizan sus bordes. |
| ◗ | **Bevel** | *Menú superior > Brush > MaskMesh Modifiers* | Advanced | Cuánto se biselan, para que la pieza nueva no salga con un canto totalmente recto. |

