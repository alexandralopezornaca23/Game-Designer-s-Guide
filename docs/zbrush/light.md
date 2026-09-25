# Light


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💡 | **Light: qué es la paleta** | *Menú superior > Light* | Intermediate | Las LUCES de la escena. Aquí se decide de dónde viene la luz, de qué color es y con qué fuerza pega, y eso afecta tanto a lo que ves mientras esculpes como al render BPR. Es la última paleta que quedaba por documentar. Contiene diez bloques: Lights Properties, Redshift Light Properties, Background, LightCap, LightCap Adjustment, LightCap Horizon, Lights Type, Lights Placement, Lights Shadow y Environment Maps. Lo importante para tu trabajo: para ESCULPIR conviene dejar una luz sencilla y un material mate, porque una iluminación bonita disimula los defectos de la forma; y para PRESENTAR, el sistema LightCap es lo que separa un render plano de uno que parece una fotografía de estudio. |
| 💾 | **Light > guardar y deshacer la iluminación** | *Menú superior > Light* | Intermediate | El control de las luces sueltas. |
| 📂 | **Load** | *Menú superior > Light* | Intermediate | Carga una configuración de iluminación entera desde archivo. |
| 💾 | **Save** | *Menú superior > Light* | Intermediate | Guarda la configuración actual, para reutilizarla en todas las piezas del portafolio y que se vean como una serie. |
| ↩️ | **Undo** | *Menú superior > Light* | Intermediate | Deshace el último cambio de luz (en gris en tu captura). |
| ↪️ | **Redo** | *Menú superior > Light* | Intermediate | Rehace el cambio deshecho (en gris en tu captura). |
| 🔆 | **Light > la esfera, las bombillas y el color** | *Menú superior > Light* | Intermediate | El bloque visual: dónde está la luz, cuál de las ocho estás editando y de qué color es. |
| ⚪ | **la esfera de vista previa** | *Menú superior > Light* | Intermediate | La esfera grande de la izquierda: enseña cómo queda iluminada una bola con la configuración actual, y el puntito naranja sobre ella es la POSICIÓN de la luz — se arrastra directamente ahí para moverla, que es lo más cómodo del bloque. |
| 💡 | **las 8 bombillas** | *Menú superior > Light* | Intermediate | La rejilla de ocho bombillas: son las ocho luces que admite la escena, y cada una se enciende pulsando su bombilla (en tu captura hay una activa, en naranja). |
| 🎨 | **el color de la luz** | *Menú superior > Light* | Intermediate | El recuadro blanco de abajo, que fija el color de la luz seleccionada. |
| 🎚️ | **Light > Intensity, Ambient y Distance** | *Menú superior > Light* | Intermediate | Los tres deslizadores generales de la luz activa. |
| 🔆 | **Intensity** | *Menú superior > Light* | Intermediate | La fuerza de la luz seleccionada (0.85 en tu captura). |
| 🌍 | **Ambient** | *Menú superior > Light* | Intermediate | La luz ambiente general, la que llega de todas partes y evita que las sombras queden negras del todo (3 en tu captura). |
| 📏 | **Distance** | *Menú superior > Light* | Intermediate | La distancia de la luz al objeto, que solo importa en los tipos de luz que se atenúan (en gris en tu captura). |


## Light > Lights Properties


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌗 | **Light > Lights Properties** | *Light > Lights Properties* | Intermediate | Las tres propiedades de la luz seleccionada. |
| 🌑 | **Shadow** | *Light > Lights Properties* | Intermediate | Decide si esa luz PROYECTA SOMBRA o no (activo en naranja en tu captura). Es más útil de lo que parece: en una iluminación de tres puntos, la luz principal proyecta sombra y las de relleno no, porque si todas la proyectan la imagen se llena de sombras cruzadas y se ensucia. |
| 🩸 | **Sss** | *Light > Lights Properties* | Intermediate | Hace que esa luz contribuya al efecto de dispersión subsuperficial, la luz que atraviesa la piel. |
| 📈 | **Intensity Curve** | *Light > Lights Properties* | Intermediate | La barra gris: en vez de un valor plano, permite dibujar cómo cae la fuerza de la luz desde el centro hacia los bordes de su cono, que es lo que da un degradado suave en vez de un corte seco. |


## Light > Redshift Light Properties


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌑 | **Redshift Light Properties > la sombra** | *Light > Redshift Light Properties* | Advanced | Las mismas luces, pero con los ajustes que entiende REDSHIFT, el motor de render incluido. Todo el bloque sale en gris hasta que Redshift está activo. |
| 🌑 | **Shadow** | *Light > Redshift Light Properties* | Advanced | Enciende la sombra de esa luz en Redshift (activo en tu captura). |
| 🎚️ | **Shadow Strength** | *Light > Redshift Light Properties* | Advanced | Lo oscura que sale la sombra. |
| 🫧 | **Shadow Softness** | *Light > Redshift Light Properties* | Advanced | Lo difuminado de su borde. Es EL parámetro de la iluminación creíble, porque en la realidad ninguna sombra tiene el canto perfectamente recortado. |
| 🔬 | **Shadow Samples** | *Light > Redshift Light Properties* | Advanced | Las muestras con que se calcula: pocas dan grano, muchas tardan más. |
| 📉 | **Redshift Light Properties > distancia y caída** | *Light > Redshift Light Properties* | Advanced | Cómo se comporta la luz con la distancia dentro de Redshift. |
| ✖️ | **Intensity Multiplier** | *Light > Redshift Light Properties* | Advanced | Multiplica la fuerza de la luz por encima del Intensity del bloque de arriba. |
| 📏 | **Light Distance** | *Light > Redshift Light Properties* | Advanced | A qué distancia está la luz. |
| 📐 | **Light Range** | *Light > Redshift Light Properties* | Advanced | Hasta dónde llega la luz. |
| 📉 | **Decay Type** | *Light > Redshift Light Properties* | Advanced | El TIPO de caída de la luz con la distancia. La física real es la caída cuadrática, que es la que da un resultado natural. |
| 🎯 | **Decay Start** | *Light > Redshift Light Properties* | Advanced | A partir de qué distancia empieza a atenuarse. |


## Light > Background


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌄 | **Light > Background: activar y cargar el entorno** | *Light > Background* | Advanced | El ENTORNO que rodea a la escena, o sea la imagen panorámica (HDRI) que ilumina el modelo y se refleja en él. |
| 🔘 | **On** | *Light > Background* | Advanced | Activa el fondo de entorno. |
| 🔍 | **Zoom** | *Light > Background* | Advanced | Acerca o aleja esa imagen. |
| ➕ | **Create** | *Light > Background* | Advanced | Genera un fondo nuevo. |
| 🖼️ | **Texture** | *Light > Background* | Advanced | Elige qué imagen se usa: aquí es donde se carga el HDRI, y cargar uno decente es probablemente lo que más cambia el aspecto de un render de metal o de cualquier superficie brillante, porque los reflejos dejan de ser inventados y pasan a ser de un sitio real. |
| ☀️ | **Light > Background: brillo y desenfoque** | *Light > Background* | Advanced | Los ajustes de exposición del entorno y su desenfoque. |
| 📈 | **Gamma** | *Light > Background* | Advanced | Ajusta la curva de brillo de esa imagen. |
| 🔆 | **Exposure** | *Light > Background* | Advanced | Ajusta la exposición de esa imagen. |
| 🔴 | **Redshift Exposure** | *Light > Background* | Advanced | Lo mismo, pero solo para el motor Redshift. |
| 🌑 | **Redshift HDR Shadows** | *Light > Background* | Advanced | Activa las sombras generadas por el propio HDRI, que son las que dan esa luz envolvente tan característica. |
| 🔬 | **Redshift HDR Samples** | *Light > Background* | Advanced | Las muestras con que se calculan esas sombras. |
| 🫧 | **Blur** | *Light > Background* | Advanced | Desenfoca el fondo, que interesa para que el entorno no compita con el modelo y siga aportando su luz. |
| 🧭 | **Light > Background: la orientación del entorno** | *Light > Background* | Advanced | De dónde entra la luz del HDRI. Girar la longitud hasta que la luz pegue en tres cuartos sobre la cara es el ajuste que más rentabilidad da de todo el bloque. |
| ↔️ | **Longitude** | *Light > Background* | Advanced | Gira el entorno horizontalmente. |
| ↕️ | **Latitude** | *Light > Background* | Advanced | Gira el entorno verticalmente. |
| 📐 | **Tilt** | *Light > Background* | Advanced | Inclina el entorno. |
| 🔄 | **Rotate With Object** | *Light > Background* | Advanced | Hace que el entorno gire PEGADO al modelo, así que al rotar la escultura la iluminación no cambia (activo en naranja en tu captura). Cómodo para trabajar, pero para la imagen final normalmente se quiere lo contrario, que el entorno se quede quieto. |
| 🎛️ | **LightCaps** | *Light > Background* | Advanced | Conecta este fondo con el sistema LightCap (en gris en tu captura). |
| 🔬 | **Samples** | *Light > Background* | Advanced | Las muestras del cálculo del entorno. |
| 🪞 | **Reflect** | *Light > Background* | Advanced | Decide si el entorno se refleja en el modelo o solo lo ilumina. |


## Light > LightCap


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎛️ | **Light > LightCap: qué es y cómo se guarda** | *Light > LightCap* | Advanced | LIGHTCAP es el sistema de iluminación bueno de ZBrush y merece la pena entenderlo: en vez de colocar luces en el espacio, PINTAS la luz sobre una esfera de entorno, y el material la lee de ahí. El resultado es una iluminación de estudio montada en dos minutos y sin cálculo de render. |
| 📂 | **Open** | *Light > LightCap* | Advanced | Carga un LightCap entero desde archivo. |
| 💾 | **Save** | *Light > LightCap* | Advanced | Guarda el LightCap actual. |
| 💡 | **Light > LightCap: las capas y las luces del entorno** | *Light > LightCap* | Advanced | Las dos capas que se editan por separado y cómo se añaden luces a la esfera. |
| 🌗 | **Diffuse** | *Light > LightCap* | Advanced | La capa DIFUSA, la luz que modela el volumen (activo en naranja en tu captura). |
| ✨ | **Specular** | *Light > LightCap* | Advanced | La capa ESPECULAR, la que produce los brillos. Poder ajustarlas por separado es lo que permite tener un brillo pequeño y duro sobre una luz general suave. |
| ⬛ | **la vista previa** | *Light > LightCap* | Advanced | El recuadro negro grande: la vista previa del entorno que estás pintando. |
| ➕ | **New Light** | *Light > LightCap* | Advanced | Añade una luz nueva a ese entorno. |
| 🗑️ | **Del Light** | *Light > LightCap* | Advanced | Borra la luz seleccionada del entorno. |
| 🔢 | **Light Index** | *Light > LightCap* | Advanced | Con las flechas << y >>, pasa de una luz a otra del entorno para editarlas. |
| 💫 | **Light > LightCap: fuerza, sombra y apertura** | *Light > LightCap* | Advanced | Los ajustes de la luz de LightCap que tengas seleccionada. |
| 🎚️ | **Strength** | *Light > LightCap* | Advanced | La fuerza de esa luz. |
| 🌗 | **Opacity** | *Light > LightCap* | Advanced | Su opacidad sobre las demás luces. |
| 🌑 | **Shadow** | *Light > LightCap* | Advanced | Cuánta sombra genera. |
| 📐 | **Aperture** | *Light > LightCap* | Advanced | El TAMAÑO de la mancha de luz sobre la esfera: una apertura pequeña imita un foco puntual y da brillos duros y contrastados, una grande imita una ventana o un difusor y da luz suave y envolvente. Es el equivalente a elegir el modificador en un plató de fotografía. |
| 📉 | **Falloff** | *Light > LightCap* | Advanced | Cómo se desvanece esa mancha hacia los bordes. |
| 🎨 | **Light > LightCap: exposición, color y mezcla** | *Light > LightCap* | Advanced | El acabado de cada luz del LightCap. |
| 🔆 | **Exposure** | *Light > LightCap* | Advanced | Ajusta el brillo de esa luz. |
| 📈 | **Gamma** | *Light > LightCap* | Advanced | Ajusta su curva de brillo. |
| 🎨 | **Color** | *Light > LightCap* | Advanced | El color de la luz: dar un tono ligeramente cálido a la principal y frío al relleno es el truco clásico para que un render gris parezca tener atmósfera. |
| 🔀 | **Blend Mode** | *Light > LightCap* | Advanced | El modo con el que esa luz se mezcla con las que ya hay, igual que los modos de capa de Photoshop. |
| 🖼️ | **Light > LightCap: usar una imagen como luz** | *Light > LightCap* | Advanced | Usar una IMAGEN como fuente de luz en lugar de una mancha lisa: así se imita el reflejo de una ventana con marco, de una persiana o de un cartel luminoso, y el brillo que aparece en el modelo lleva esa forma dentro. |
| 🖼️ | **Txtr** | *Light > LightCap* | Advanced | Carga una textura que pasa a ser la forma de esa luz. |
| 🏷️ | **Alpha** | *Light > LightCap* | Advanced | Carga un alpha con el mismo fin. |
| ↔️ | **HTile** | *Light > LightCap* | Advanced | Repite esa imagen en horizontal. |
| ↕️ | **VTile** | *Light > LightCap* | Advanced | La repite en vertical. |
| ↔️ | **Scale Width** | *Light > LightCap* | Advanced | Estira o encoge la imagen a lo ancho. |
| ↕️ | **Scale Height** | *Light > LightCap* | Advanced | La estira o encoge a lo alto. |
| 🫧 | **Blur** | *Light > LightCap* | Advanced | La desenfoca. Desenfocar un poco casi siempre ayuda, porque un reflejo demasiado nítido delata que es una imagen pegada. |
| 🔄 | **Orientation** | *Light > LightCap* | Advanced | Gira la imagen sobre la esfera. |
| 🌍 | **Create Environment** | *Light > LightCap* | Advanced | Convierte lo que has montado en un entorno completo (en gris hasta que hay algo que convertir). |
| 🖼️ | **Create Texture** | *Light > LightCap* | Advanced | Lo saca como textura (también en gris hasta que hay algo). |


## Light > LightCap Adjustment


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎚️ | **Light > LightCap Adjustment** | *Light > LightCap Adjustment* | Advanced | El retoque global del LightCap ya montado, sin tener que ir luz por luz. Con Hue y Saturation se cambia el ambiente entero de la imagen de un tirón, de cálido de atardecer a frío de luna. |
| 🔆 | **Exposure** | *Light > LightCap Adjustment* | Advanced | Sube o baja el brillo general del LightCap. |
| 📈 | **Gamma** | *Light > LightCap Adjustment* | Advanced | Ajusta su curva de brillo. |
| 🌈 | **Hue** | *Light > LightCap Adjustment* | Advanced | Gira el tono de toda la iluminación. |
| 💧 | **Saturation** | *Light > LightCap Adjustment* | Advanced | Satura o desatura toda la iluminación. |
| 🎚️ | **Intensity** | *Light > LightCap Adjustment* | Advanced | La fuerza general del LightCap. |
| ✨ | **Retain Highlight** | *Light > LightCap Adjustment* | Advanced | Protege los brillos para que no se quemen a blanco puro al subir la exposición. Conviene tenerlo en cuenta, porque un brillo quemado es información perdida que ya no se recupera en Photoshop. |
| 📈 | **Use Material Curves** | *Light > LightCap Adjustment* | Advanced | Hace que se respeten las curvas definidas en el material en vez de las de aquí (en gris en tu captura). |


## Light > LightCap Horizon


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌅 | **Light > LightCap Horizon** | *Light > LightCap Horizon* | Advanced | Construye un HORIZONTE de colores como entorno, o sea un degradado tipo cielo-suelo, sin necesidad de cargar ninguna imagen. Con cuatro bandas se monta un cielo creíble: azul arriba, claro en el horizonte, y tierra abajo. Es la forma más rápida de dar una iluminación ambiental decente cuando no tienes un HDRI a mano. |
| ↔️ | **Longitude** | *Light > LightCap Horizon* | Advanced | Orienta el horizonte horizontalmente. |
| ↕️ | **Latitude** | *Light > LightCap Horizon* | Advanced | Lo orienta verticalmente. |
| 🌗 | **Horizon Opacity** | *Light > LightCap Horizon* | Advanced | Lo visible que resulta el horizonte (0 en tu captura). |
| 🎨 | **C1** | *Light > LightCap Horizon* | Advanced | El COLOR de la primera banda del degradado, la de arriba del todo. |
| 🌗 | **O1** | *Light > LightCap Horizon* | Advanced | La OPACIDAD de esa primera banda (0.5 en tu captura). |
| 🎨 | **C2** | *Light > LightCap Horizon* | Advanced | El color de la segunda banda. |
| 🌗 | **O2** | *Light > LightCap Horizon* | Advanced | La opacidad de la segunda banda (1 en tu captura). |
| 🎨 | **C3** | *Light > LightCap Horizon* | Advanced | El color de la tercera banda. |
| 🌗 | **O3** | *Light > LightCap Horizon* | Advanced | La opacidad de la tercera banda (1 en tu captura). |
| 🎨 | **C4** | *Light > LightCap Horizon* | Advanced | El color de la cuarta banda, la de abajo del todo. |
| 🌗 | **O4** | *Light > LightCap Horizon* | Advanced | La opacidad de la cuarta banda (0.5 en tu captura). |
| 📈 | **Rate Top** | *Light > LightCap Horizon* | Advanced | La velocidad de transición en la parte de ARRIBA, o sea si el paso de una banda a otra es suave o brusco (1 en tu captura). |
| 📉 | **Rate Bot** | *Light > LightCap Horizon* | Advanced | Lo mismo en la parte de abajo (1 en tu captura). |


## Light > Lights Type


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ☀️ | **Light > Lights Type** | *Light > Lights Type* | Intermediate | El TIPO de la luz seleccionada, y cada uno se comporta de forma distinta. Para un personaje de portafolio, lo habitual es un Sun como luz principal y uno o dos Point de relleno. |
| ☀️ | **Sun** | *Light > Lights Type* | Intermediate | Luz SOLAR: los rayos llegan paralelos desde el infinito, así que la posición no importa, solo la dirección, y las sombras salen todas en el mismo ángulo (activo en naranja en tu captura). Es la que se usa por defecto y la que da un resultado más limpio para presentar una escultura. |
| 💡 | **Point** | *Light > Lights Type* | Intermediate | Luz PUNTUAL, una bombilla desnuda que irradia en todas direcciones desde un punto concreto: aquí la posición sí importa y la luz se atenúa con la distancia. |
| 🔦 | **Spot** | *Light > Lights Type* | Intermediate | Un FOCO, con un cono de luz dirigido — el de teatro. |
| ✨ | **Glow** | *Light > Lights Type* | Intermediate | Un resplandor. |
| ⭕ | **Radial** | *Light > Lights Type* | Intermediate | Una luz radial. |


## Light > Lights Placement


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📍 | **Light > Lights Placement** | *Light > Lights Placement* | Intermediate | La posición NUMÉRICA de la luz seleccionada, para cuando quieres precisión en vez de arrastrar el puntito sobre la esfera de vista previa. |
| ↔️ | **X Pos** | *Light > Lights Placement* | Intermediate | La coordenada de la luz en el eje X (0 en tu captura). |
| ↕️ | **Y Pos** | *Light > Lights Placement* | Intermediate | La coordenada en el eje Y (-1 en tu captura, o sea algo por debajo del modelo). |
| 🔃 | **Z Pos** | *Light > Lights Placement* | Intermediate | La coordenada en el eje Z (1 en tu captura, o sea por delante del modelo). |
| 📏 | **Radius** | *Light > Lights Placement* | Intermediate | El TAMAÑO físico de la fuente de luz, y ese número decide lo blandas que salen las sombras: una fuente pequeña da sombras duras y recortadas, una grande las da suaves y difusas. Es el mismo principio que en fotografía, donde un flash desnudo da sombras duras y un paraguas grande las da suaves. Sale en gris con los tipos de luz que no tienen tamaño, como Sun. |


## Light > Lights Shadow


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌑 | **Light > Lights Shadow** | *Light > Lights Shadow* | Advanced | La sombra que proyecta la luz seleccionada. |
| 🌑 | **Intensity** | *Light > Lights Shadow* | Advanced | Lo oscura que sale la sombra (100 en tu captura). |
| 📈 | **Shadow Curve** | *Light > Lights Shadow* | Advanced | La gráfica que define cómo se degrada desde el borde hacia dentro. |
| 📏 | **Length** | *Light > Lights Shadow* | Advanced | Lo larga que se dibuja la sombra (150 en tu captura). |
| ⚡ | **ZMode** | *Light > Lights Shadow* | Advanced | El modo de sombra basado en profundidad, rápido y suficiente para trabajar (activo en naranja en tu captura). |
| ▬ | **Uni** | *Light > Lights Shadow* | Advanced | El modo de sombra uniforme. |
| 🫧 | **Blur** | *Light > Lights Shadow* | Advanced | Desenfoca el borde de la sombra (1 en tu captura). |
| ☀️ | **Rays** | *Light > Lights Shadow* | Advanced | Los rayos con los que se calcula (100 en tu captura): pocos dan una sombra granulada, muchos la dan limpia pero tardan más. |
| 📐 | **Aperture** | *Light > Lights Shadow* | Advanced | La apertura del cono de la luz en grados (90 en tu captura), y es lo que de verdad decide si la sombra es dura y recortada o blanda y de estudio. Subirla es el camino más corto para que un render deje de parecer de videojuego de los noventa. |


## Light > Environment Maps


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗺️ | **Light > Environment Maps: los dos mapas** | *Light > Environment Maps* | Advanced | Los mapas de entorno globales, o sea la iluminación que envuelve la escena por defecto. Que sean dos mapas distintos permite tener una luz general suave y a la vez brillos marcados, que es exactamente lo que hace que una superficie se lea como metal o como piel húmeda. |
| ⚪ | **DefaultDiffuse** | *Light > Environment Maps* | Advanced | El mapa DIFUSO —la esfera gris de la izquierda— que aporta la luz general que modela el volumen. |
| ✨ | **DefaultSpecular** | *Light > Environment Maps* | Advanced | El mapa ESPECULAR —la esferita brillante de la derecha— que aporta los reflejos y los brillos. |
| 🔢 | **Light > Environment Maps: las intensidades** | *Light > Environment Maps* | Advanced | Los dos a 0 en tu captura significa que ahora mismo la escena no está usando iluminación de entorno y solo trabajan las luces sueltas. |
| ⚪ | **Gdi** | *Light > Environment Maps* | Advanced | La intensidad del mapa difuso ('Global Diffuse Intensity' por las iniciales, aunque el nombre completo no aparece en pantalla). |
| ✨ | **Gsi** | *Light > Environment Maps* | Advanced | La intensidad del mapa especular ('Global Specular Intensity'). |

