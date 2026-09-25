# Render


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎬 | **Render: qué es la paleta y sus sub-paletas** | *Menú superior > Render* | Basic | La paleta que convierte tu escultura en una imagen presentable. ZBrush no es un motor de render al uso, pero trae varios sistemas propios y desde 2022 lleva REDSHIFT incorporado, que sí es un motor de verdad. En tu versión son 20 sub-paletas: Render Booleans, Redshift Renderer, Redshift AOV Passes, External Renderer, Render Properties, BPR RenderPass, BPR Transparency, BPR Shadow, BPR AO, BPR SSS, BPR Filters, Antialiasing, Depth Cue, Fog, Fast Render, Preview Shadows, Preview AO, Preview Wax, Environment y Adjustments. La palabra clave que aparece por todas partes es BPR — 'Best Preview Render' — que es el render propio de ZBrush, rápido y suficientemente bueno para enseñar avances o montar un portafolio sin salir del programa. |
| 📂 | **Render > guardar y recuperar configuraciones** | *Menú superior > Render* | Intermediate | Guardar y recuperar CONFIGURACIONES de render enteras, que es de las cosas que más tiempo ahorran. Una vez que has peleado un render bonito, lo guardas y lo reutilizas en todas las piezas de tu portafolio para que tengan el mismo acabado. |
| 📂 | **Load** | *Menú superior > Render* | Intermediate | Carga un 'render set': todos los ajustes de esta paleta de golpe, desde un archivo. |
| 💾 | **Save** | *Menú superior > Render* | Intermediate | Guarda todos los ajustes de render actuales en un archivo. |
| ❄️ | **Freeze** | *Menú superior > Render* | Intermediate | Congela el render: deja la imagen calculada fija en el lienzo aunque sigas moviéndote, útil para comparar antes y después de un cambio. |
| 📚 | **Lightbox ▶ RenderSet** | *Menú superior > Render* | Intermediate | Abre la pestaña de LightBox donde están esas configuraciones guardadas, incluidas las de fábrica. |
| 📥 | **Load From Project** | *Menú superior > Render* | Intermediate | Saca los ajustes de render de un archivo de proyecto que ya tengas hecho. |
| 👁️ | **Render > los modos de calidad** | *Menú superior > Render* | Intermediate | Las cuatro calidades de dibujado, de menos a más, más la pareja que decide sobre qué se aplican. |
| 🖱️ | **Cursor** | *Menú superior > Render* | Intermediate | Aplica el modo de render a lo que hay bajo el cursor. |
| 🎬 | **Render** | *Menú superior > Render* | Intermediate | Aplica el modo de render a la escena completa. |
| ▬ | **Flat** | *Menú superior > Render* | Intermediate | Plano del todo, sin luces ni sombras, solo el color liso. Rapidísimo, sirve para trabajar en mallas muy pesadas. |
| ⚡ | **Fast** | *Menú superior > Render* | Intermediate | El modo normal de esculpir, con el material y poco más. |
| 👀 | **Preview** | *Menú superior > Render* | Intermediate | El punto dulce (encendido en naranja, es el que tienes): enseña materiales, luces y sombras en tiempo real mientras trabajas. |
| 🏆 | **Best** | *Menú superior > Render* | Intermediate | El render completo de alta calidad, el famoso BPR: tarda unos segundos y saca sombras suaves, oclusión ambiental, subsuperficie y transparencias. Su atajo es Mayús+R, aunque conviene comprobarlo en tu paleta de atajos. |
| 🌫️ | **Render > Fade Opacity y Fade Color** | *Menú superior > Render* | Intermediate | El DESVANECIDO que se aplica sobre la imagen ya renderizada. Sirve para fundir el render hacia un fondo — por ejemplo dejar que la parte baja de una figura se desvanezca en blanco en lugar de cortarse de golpe. No cambia nada del modelo, solo la imagen final. Los dos salen en gris hasta que se usan. |
| 🌫️ | **Fade Opacity** | *Menú superior > Render* | Intermediate | Cuánto se difumina la imagen renderizada. |
| 🎨 | **Fade Color** | *Menú superior > Render* | Intermediate | Hacia qué color se difumina. |
| ⏪ | **Render > Render Recall y Modifiers** | *Menú superior > Render* | Advanced | Un pequeño historial de renders, muy práctico cuando estás probando variaciones de luz: renderizas tres o cuatro versiones y luego las repasas para elegir. Sale en gris cuando todavía no has hecho ningún render. |
| ⏪ | **Render Recall** | *Menú superior > Render* | Advanced | El historial en sí: las flechas << y >> van pasando por las imágenes que has renderizado en esta sesión, para compararlas sin tener que exportarlas. La barra naranja del centro indica en qué punto estás. |
| ⚙️ | **Modifiers** | *Menú superior > Render* | Advanced | Abre los ajustes generales que afectan a todos los modos de render. |


## Render > Render Booleans


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⭕ | **Render Booleans > Live Boolean y Show Coplanar** | *Render > Render Booleans* | Advanced | El visor de problemas del sistema booleano, donde se resuelven la mayoría de los disgustos con Live Boolean. |
| 👁️ | **Live Boolean** | *Render > Render Booleans* | Advanced | Enciende la vista previa en tiempo real de las sumas y restas entre SubTools, así ves el resultado antes de aplicarlo. |
| 📐 | **Show Coplanar** | *Render > Render Booleans* | Advanced | Resalta las zonas donde dos superficies quedan pegadas en el mismo plano: esa es la causa NÚMERO UNO de que un boolean falle, porque el programa no sabe si esas dos caras se cortan o solo se rozan. |
| 🔍 | **Render Booleans > Show Issues y los botones de recorrido** | *Render > Render Booleans* | Advanced | EL FLUJO que ahorra tiempo: enciendes Live Boolean, pulsas Show Issues, y con Next vas recorriendo cada punto marcado para arreglarlo antes de hacer el boolean definitivo. Diez minutos aquí ahorran una hora de reparar malla después. Todo el bloque sale en gris mientras no tengas Live Boolean activo. |
| ⚠️ | **Show Issues** | *Render > Render Booleans* | Advanced | Resalta directamente los puntos conflictivos que ZBrush ha detectado. |
| 🔦 | **Inside** | *Render > Render Booleans* | Advanced | Permite mirar el problema por DENTRO de la malla (en naranja en tu captura). Acompaña tanto a Show Issues como a Show Coplanar. |
| 🧩 | **Solo** | *Render > Render Booleans* | Advanced | Aísla esa zona y esconde el resto para verla sin estorbos. |
| ⬅️ | **Prev** | *Render > Render Booleans* | Advanced | Salta al problema anterior. |
| ➡️ | **Next** | *Render > Render Booleans* | Advanced | Salta al problema siguiente, uno a uno. |


## Render > Redshift Renderer


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔴 | **Redshift Renderer > el motor y el entorno** | *Render > Redshift Renderer* | Advanced | REDSHIFT es el motor de render profesional que ZBrush trae incluido: al encenderlo, el render deja de ser el BPR de ZBrush y pasa a calcularlo Redshift, con calidad de producción. |
| 🔘 | **Redshift** | *Render > Redshift Renderer* | Advanced | Enciende el motor Redshift como renderizador. |
| ⚪ | **la esfera de vista previa** | *Render > Redshift Renderer* | Advanced | La esfera gris grande de la izquierda: enseña cómo está iluminando el HDRI la escena, y es la forma rápida de ver si la luz viene de donde crees. |
| 🟫 | **Floor Color** | *Render > Redshift Renderer* | Advanced | El color del suelo virtual sobre el que se apoya el modelo, que además rebota luz sobre él — un suelo cálido tiñe de cálido la parte baja del personaje. |
| 💡 | **Redshift Renderer > gamma, luces y panorama** | *Render > Redshift Renderer* | Advanced | Tres ajustes generales de cómo se ilumina y se expone la escena. |
| 📈 | **Gamma Correction** | *Render > Redshift Renderer* | Advanced | Ajusta la curva de brillo general de la imagen. |
| 🔄 | **Rotate lights with Camera** | *Render > Redshift Renderer* | Advanced | Hace que las luces giren pegadas a la cámara, así el modelo siempre queda iluminado igual desde donde lo mires. Muy cómodo para trabajar y comprobar la forma, pero poco realista para la imagen final, donde normalmente quieres que la luz se quede quieta y el modelo gire dentro de ella. |
| 🌄 | **Use Default Panorama** | *Render > Redshift Renderer* | Advanced | Usa el HDRI de entorno que trae Redshift de serie (encendido en tu captura). Apágalo cuando quieras cargar el tuyo propio, que es lo que de verdad cambia el aspecto de un render de metal. |
| ⚡ | **Redshift Renderer > calidad contra tiempo** | *Render > Redshift Renderer* | Advanced | El bloque de la eterna negociación del render. El primero es el ajuste que MÁS TIEMPO AHORRA de toda la paleta: súbelo antes que ningún otro. |
| 🧹 | **Denoising** | *Render > Redshift Renderer* | Advanced | Quita el ruido granulado de la imagen con un filtro inteligente: te permite bajar muchísimo las muestras y aun así sacar una imagen limpia. |
| 🎚️ | **Render Quality** | *Render > Redshift Renderer* | Advanced | El mando general de calidad del render. |
| 📏 | **Error Threshold** | *Render > Redshift Renderer* | Advanced | La tolerancia al ruido: cuanto más bajo, más limpio y más lento. |
| 📶 | **Progressive Rendering** | *Render > Redshift Renderer* | Advanced | Hace que la imagen vaya apareciendo entera y se afine poco a poco en vez de ir por cuadritos. Es cómodo porque te permite parar en cuanto veas que la composición no funciona, sin esperar al final. |
| 🔢 | **Progressive Iterations** | *Render > Redshift Renderer* | Advanced | Cuántas pasadas da ese refinado progresivo. |
| 🌍 | **Redshift Renderer > iluminación global (GI)** | *Render > Redshift Renderer* | Advanced | El bloque GI es la ILUMINACIÓN GLOBAL, la luz rebotada entre superficies, y es lo que hace que una imagen parezca real en vez de plana: sin ella, lo que no recibe luz directa queda negro; con ella, una pared blanca cercana devuelve luz al personaje. |
| 1️⃣ | **Primary GI Engine Quality** | *Render > Redshift Renderer* | Advanced | La calidad del PRIMER rebote, que es el que más se ve. Si hay que recortar, se recorta en el secundario. |
| 2️⃣ | **Secondary GI Engine Quality** | *Render > Redshift Renderer* | Advanced | La calidad de los rebotes siguientes. |
| 🔁 | **GI Bounce** | *Render > Redshift Renderer* | Advanced | Cuántas veces se permite rebotar a la luz. Dos o tres rebotes bastan para casi todo. |
| ☀️ | **GI Rays** | *Render > Redshift Renderer* | Advanced | Cuántos rayos se lanzan para calcular esa luz rebotada. |
| 🔄 | **Retrace Threshold** | *Render > Redshift Renderer* | Advanced | Cuándo recalcular en vez de reutilizar lo ya calculado. |
| 🔬 | **Redshift Renderer > muestras y vista previa** | *Render > Redshift Renderer* | Advanced | Las muestras por píxel y los dos ajustes que solo afectan a la ventanita de previsualización dentro de ZBrush, no al render final. |
| 🔬 | **Samples Per Pixel** | *Render > Redshift Renderer* | Advanced | Las muestras por píxel, el mando más directo entre grano y tiempo: doblarlas casi dobla el tiempo de render. Por eso conviene subir Denoising antes que esto — sale mucho más a cuenta, porque limpia el grano sin pagar el tiempo. |
| 👀 | **Preview Quality in ZBrush** | *Render > Redshift Renderer* | Advanced | La calidad de la previsualización dentro de ZBrush. Bajarla hace que la previa vaya fluida mientras colocas luces. |
| 📐 | **Preview Size in ZBrush** | *Render > Redshift Renderer* | Advanced | El tamaño de esa ventanita de previsualización. |
| 📷 | **Redshift Renderer > profundidad de campo** | *Render > Redshift Renderer* | Advanced | El desenfoque de fotografía. Bien usado le da un aire fotográfico inmediato a un render de personaje: enfocas la cara y dejas los hombros suaves, que es exactamente lo que hace un retrato con un 85 mm abierto. Cuidado con pasarse: un desenfoque demasiado agresivo esconde el trabajo de escultura que quieres enseñar. |
| 📷 | **Depth Of Field** | *Render > Redshift Renderer* | Advanced | Activa la profundidad de campo. |
| 🎯 | **Focus Depth** | *Render > Redshift Renderer* | Advanced | A qué distancia está el plano enfocado. |
| 📏 | **Focus Radius** | *Render > Redshift Renderer* | Advanced | Lo ancha que es esa franja nítida. |
| 🚫 | **Redshift Renderer > las válvulas de escape** | *Render > Redshift Renderer* | Advanced | Tres interruptores que le dicen a Redshift que IGNORE esas tecnologías de ZBrush al renderizar. Las tres son geometría generada al vuelo y multiplican la cuenta de polígonos muchísimo, a veces por cien. Apagándolas el render sale mucho más rápido, a cambio de perder esos elementos en la imagen: sirven para hacer pruebas de luz rápidas y volver a encenderlas para la pasada final. |
| ⚡ | **Disable DynamicSubdiv** | *Render > Redshift Renderer* | Advanced | Ignora la subdivisión dinámica al renderizar. |
| 🔢 | **Disable ArrayMesh** | *Render > Redshift Renderer* | Advanced | Ignora las repeticiones de ArrayMesh al renderizar. |
| 🌾 | **Disable NanoMesh** | *Render > Redshift Renderer* | Advanced | Ignora las mallas sembradas de NanoMesh al renderizar. |


## Render > Redshift Renderer > Redshift Baker 360


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌐 | **Redshift Renderer > Redshift Baker 360** | *Render > Redshift Renderer > Redshift Baker 360* | Advanced | Cocina la iluminación en una imagen panorámica de 360 grados, o sea genera un HDRI a partir de tu escena. |
| ↔️ | **Bake Longitude Steps** | *Render > Redshift Renderer > Redshift Baker 360* | Advanced | En cuántos pasos recorre la panorámica en horizontal: más pasos, resultado más fino y más lento. |
| ↕️ | **Bake Latitude Steps** | *Render > Redshift Renderer > Redshift Baker 360* | Advanced | En cuántos pasos la recorre en vertical. |
| 🎨 | **Bake Color Mode** | *Render > Redshift Renderer > Redshift Baker 360* | Advanced | Cómo trata el color al cocinar la panorámica. |
| ✨ | **Preserve Highlights** | *Render > Redshift Renderer > Redshift Baker 360* | Advanced | Evita que las luces fuertes se quemen a blanco puro, que en un HDRI importa mucho porque esa información de brillo alto es justamente lo que luego ilumina otra escena. |


## Render > Redshift AOV Passes


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎞️ | **Redshift AOV Passes > las casillas Bty a Depth** | *Render > Redshift AOV Passes* | Advanced | AOV significa 'Arbitrary Output Variables' y son las CAPAS SUELTAS del render: en vez de darte solo la imagen final, Redshift te entrega por separado las sombras, los reflejos, la profundidad, etc., para que luego las montes y ajustes en Photoshop sin volver a renderizar. Esta es la rejilla de doce casillas con los nombres abreviados, con el icono del cubo rojo de Redshift a su izquierda. |
| 🖼️ | **Bty** | *Render > Redshift AOV Passes* | Advanced | Beauty: la imagen final completa. |
| 🌑 | **Shdw** | *Render > Redshift AOV Passes* | Advanced | Shadow: las sombras. |
| 🕳️ | **AmOc** | *Render > Redshift AOV Passes* | Advanced | Ambient Occlusion: la suciedad de los recovecos. |
| 🩸 | **Sss** | *Render > Redshift AOV Passes* | Advanced | Subsurface Scattering: la luz que atraviesa la piel. |
| 💡 | **GI** | *Render > Redshift AOV Passes* | Advanced | Global Illumination: la luz rebotada. |
| 📏 | **Depth** | *Render > Redshift AOV Passes* | Advanced | La profundidad en grises, que sirve para desenfocar después. |
| 🔤 | **Redshift AOV Passes > las casillas Bkgrd a Refract** | *Render > Redshift AOV Passes* | Advanced | Las otras seis abreviaturas de la rejilla. En tu captura salen todas en gris porque el bloque no está activo todavía. Merece la pena saberse las abreviaturas, porque esta rejilla compacta es la forma rápida de ver de un vistazo qué capas están encendidas sin desplegar la lista larga de debajo. |
| 🌄 | **Bkgrd** | *Render > Redshift AOV Passes* | Advanced | Background: el fondo. |
| 🏔️ | **BuNo** | *Render > Redshift AOV Passes* | Advanced | Bump Normal: el relieve. |
| 🎨 | **Dif** | *Render > Redshift AOV Passes* | Advanced | Diffuse: el color base sin luces ni sombras. |
| 🌍 | **W Pos** | *Render > Redshift AOV Passes* | Advanced | World Position: la posición de cada punto en el espacio. |
| 🪞 | **Reflect** | *Render > Redshift AOV Passes* | Advanced | Los reflejos. |
| 💎 | **Refract** | *Render > Redshift AOV Passes* | Advanced | Las refracciones. |


## Render > Redshift AOV Passes > AOV Passes


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗂️ | **Redshift AOV Passes > AOV Passes: elegir las capas** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | Aquí es donde se ELIGEN las capas, ya con el nombre completo. PARA TU PORTAFOLIO esto vale mucho la pena: renderizas UNA vez con Beauty + AOcclusion + Depth, y luego en Photoshop puedes oscurecer recovecos o añadir desenfoque de cámara sin volver a esperar el render entero. |
| 🖼️ | **Beauty** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | La imagen final completa (encendida en naranja en tu captura). |
| 🌑 | **Shadows** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | Las sombras (disponible pero sin activar en tu captura). |
| 🕳️ | **AOcclusion** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | La oclusión ambiental (encendida en naranja en tu captura). |
| 🩸 | **Sss** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | La dispersión subsuperficial (disponible pero sin activar). |
| 💡 | **GI** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | La iluminación global (encendida en naranja en tu captura). |
| 📏 | **Depth** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | La profundidad (disponible pero sin activar). |
| 🌄 | **Background** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | El fondo (en gris: no disponible con la configuración actual). |
| 🏔️ | **Bump Normal** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | El relieve (en gris en tu captura). |
| 🎨 | **Diffuse** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | El color base (encendido en naranja en tu captura). |
| 🌍 | **World Position** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | La posición en el espacio (en gris en tu captura). |
| 🪞 | **Reflection** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | Los reflejos (en gris en tu captura). |
| 💎 | **Refraction** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | Las refracciones (en gris en tu captura). |
| ✅ | **All** | *Render > Redshift AOV Passes > AOV Passes* | Advanced | Enciende todas las capas de golpe. |


## Render > Redshift AOV Passes > ajustes por capa


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚙️ | **Redshift AOV Passes > la lista de ajustes por capa** | *Render > Redshift AOV Passes* | Advanced | Debajo de las casillas hay una segunda lista con seis entradas. NO son capas nuevas, sino los AJUSTES propios de cada pasada: al pulsar una se despliega su bloque de opciones justo debajo. Es importante no confundirlos con las casillas de arriba: aquellas ENCIENDEN la capa, y estos CONFIGURAN cómo se calcula. Los seis tienen su fila propia en esta hoja. |
| 🧹 | **Denoising** | *Render > Redshift AOV Passes* | Advanced | Abre los ajustes de a qué capas se les quita el ruido. |
| 🩸 | **Sub Surface Scatter (SSS)** | *Render > Redshift AOV Passes* | Advanced | Abre los ajustes de la pasada de dispersión subsuperficial. |
| 💡 | **Global Illumination (GI)** | *Render > Redshift AOV Passes* | Advanced | Abre los ajustes de la pasada de iluminación global. |
| 📏 | **Depth** | *Render > Redshift AOV Passes* | Advanced | Abre los ajustes de la pasada de profundidad. |
| 🌍 | **World Position** | *Render > Redshift AOV Passes* | Advanced | Abre los ajustes de la pasada de posición en el mundo. |
| 🪞 | **Reflections** | *Render > Redshift AOV Passes* | Advanced | Abre los ajustes de la pasada de reflejos. |


## Render > Redshift AOV Passes > World Position


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌍 | **AOV Passes > World Position** | *Render > Redshift AOV Passes > World Position* | Advanced | La capa WORLD POSITION guarda en colores la posición de cada punto del modelo dentro del espacio: el rojo codifica la coordenada X, el verde la Y y el azul la Z. Parece un psicodélico sin sentido, pero es una capa de oro en composición, porque permite seleccionar en Photoshop o Nuke una zona por su POSICIÓN — por ejemplo oscurecer solo lo que está por debajo de la cintura — sin haber hecho ninguna máscara. |
| 🔍 | **Filter Type** | *Render > Redshift AOV Passes > World Position* | Advanced | El tipo de filtrado con el que se muestrea (▶ Full en tu captura). |
| ↔️ | **X Size** | *Render > Redshift AOV Passes > World Position* | Advanced | El tamaño en X del cubo de referencia sobre el que se normalizan esas coordenadas, o sea la escala del espacio que se está codificando. |
| ↕️ | **Y Size** | *Render > Redshift AOV Passes > World Position* | Advanced | El tamaño en Y de ese cubo de referencia. |
| 🔃 | **Z Size** | *Render > Redshift AOV Passes > World Position* | Advanced | El tamaño en Z de ese cubo de referencia. |


## Render > Redshift AOV Passes > Reflections


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🪞 | **AOV Passes > Reflections** | *Render > Redshift AOV Passes > Reflections* | Advanced | El único ajuste de la capa de REFLEXIONES. |
| 🔆 | **Sec.Ray Visibility** | *Render > Redshift AOV Passes > Reflections* | Advanced | 'Visibilidad de los rayos secundarios' (▶ Disabled en tu captura). Los rayos secundarios son los que salen rebotados después del primer impacto — los que producen los reflejos dentro de los reflejos. Desactivado, el render sale bastante más rápido y para casi todo da igual; solo interesa activarlo cuando la pieza tiene superficies muy pulidas enfrentadas entre sí, tipo armadura cromada o cristal. |


## Render > Redshift AOV Passes > Denoising


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧹 | **AOV Passes > Denoising: capa por capa** | *Render > Redshift AOV Passes > Denoising* | Advanced | Elige a QUÉ capas se les quita el ruido, una por una. Tiene sentido hacerlo por separado porque no todas lo necesitan igual. Confirmado con tus notas emergentes, cada botón es 'Denoise <capa> pass'. |
| 🖼️ | **Beauty** | *Render > Redshift AOV Passes > Denoising* | Advanced | Limpia el ruido de la imagen final completa ('Denoise Beauty pass'). |
| 🌑 | **Shadows** | *Render > Redshift AOV Passes > Denoising* | Advanced | Limpia el ruido de la capa de sombras. |
| 🩸 | **Sss** | *Render > Redshift AOV Passes > Denoising* | Advanced | Limpia la dispersión subsuperficial ('Denoise Sub Surface Scattering pass'). Es de las que más lo agradecen. |
| 💡 | **GI** | *Render > Redshift AOV Passes > Denoising* | Advanced | Limpia la iluminación global ('Denoise Global Illumination pass'). Junto con SSS, la que más lo agradece, porque son las que salen más granuladas al bajar las muestras. |
| 🌄 | **Background** | *Render > Redshift AOV Passes > Denoising* | Advanced | Limpia el ruido del fondo. |
| 🪞 | **Reflection** | *Render > Redshift AOV Passes > Denoising* | Advanced | Limpia el ruido de los reflejos. |
| 💎 | **Refraction** | *Render > Redshift AOV Passes > Denoising* | Advanced | Limpia el ruido de las refracciones. |
| 🔘 | **AOV Passes > Denoising: All y qué NO limpiar nunca** | *Render > Redshift AOV Passes > Denoising* | Advanced | EL CRITERIO PRÁCTICO de todo este bloque: las capas de PROFUNDIDAD y de POSICIÓN no deben limpiarse NUNCA, porque no son imágenes sino datos numéricos, y suavizar un dato de distancia inventa valores intermedios que no existen y estropea el desenfoque que hagas después. En tu captura sale todo en gris porque el bloque no está activo. |
| 🔘 | **All** | *Render > Redshift AOV Passes > Denoising* | Advanced | Distinto de los demás: su nota emergente dice 'Enable/Disable Denoising for all AOVs', o sea que enciende y apaga el denoising de TODAS las capas de golpe, en vez de ser una capa más. |


## Render > Redshift AOV Passes > Sub Surface Scatter


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🩸 | **AOV Passes > Sub Surface Scatter (SSS)** | *Render > Redshift AOV Passes > Sub Surface Scatter* | Advanced | Un solo ajuste para la capa de dispersión subsuperficial: la luz que entra en la piel, rebota dentro y sale por otro sitio. |
| 🔆 | **Sec.Ray Visibility** | *Render > Redshift AOV Passes > Sub Surface Scatter* | Advanced | 'Secondary Ray Visibility' según tu nota emergente (▶ Disabled en tu captura). Decide si esta pasada recoge también el SSS visto A TRAVÉS de un reflejo o de una refracción. Desactivado el render sale bastante más rápido; solo interesa si el personaje está junto a una superficie muy pulida donde el reflejo de su piel tenga que verse igual de bien que la piel misma. |


## Render > Redshift AOV Passes > Global Illumination


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 💡 | **AOV Passes > Global Illumination (GI)** | *Render > Redshift AOV Passes > Global Illumination* | Advanced | El mismo ajuste único que en SSS y en Reflections, aplicado ahora a la luz rebotada entre superficies. Que las tres capas compartan exactamente el mismo control tiene su lógica: las tres son efectos que dependen de rayos que rebotan, y en las tres la pregunta es la misma — si el segundo rebote cuenta o no. |
| 🔆 | **Sec.Ray Visibility** | *Render > Redshift AOV Passes > Global Illumination* | Advanced | 'Secondary Ray Visibility' (▶ Disabled en tu captura): decide si esta pasada incluye también la luz rebotada que se ve a través de reflejos y refracciones. Como norma, déjalo desactivado salvo que veas que falta información en una zona reflejada. |


## Render > Redshift AOV Passes > Depth


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔍 | **AOV Passes > Depth: Filter Type** | *Render > Redshift AOV Passes > Depth* | Advanced | La capa de PROFUNDIDAD guarda en grises la distancia de cada punto a la cámara, y luego sirve para desenfocar por distancia o meter niebla en Photoshop. |
| 🔍 | **Filter Type** | *Render > Redshift AOV Passes > Depth* | Advanced | El tipo de filtrado con el que se muestrea (▶ Full en tu captura; tu nota emergente lo confirma como 'Filter Type'). En una capa de DATOS como esta conviene un filtrado que no mezcle valores vecinos, porque promediar dos profundidades muy distintas inventa una intermedia que no existe y deja un halo alrededor de los bordes — ese halo es justo lo que delata un desenfoque mal hecho. |
| 📏 | **AOV Passes > Depth: Depth Mode** | *Render > Redshift AOV Passes > Depth* | Advanced | Cómo se mide esa distancia. |
| 📏 | **Depth Mode** | *Render > Redshift AOV Passes > Depth* | Advanced | 'Depth Mode' según su nota emergente (▶ Z en tu captura). El modo Z mide la profundidad a lo largo del eje de la cámara, o sea la distancia perpendicular al plano de la imagen; el otro modo habitual mide la distancia real en línea recta desde el objetivo, que en los bordes del encuadre da valores algo mayores. Para desenfocar en Photoshop, el modo Z es el que se corresponde con cómo funciona una lente de verdad, así que es el que quieres dejar puesto. |


## Render > External Renderer


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔗 | **External Renderer > el motor externo** | *Render > External Renderer* | Intermediate | El puente hacia un motor de render de fuera. |
| 🎬 | **Keyshot** | *Render > External Renderer* | Intermediate | El motor que aparece en tu instalación: es el que usa el puente ZBrush to KeyShot y el motor con el que están hechas la mayoría de las láminas de portafolio bonitas que se ven por ArtStation. |
| 🔺 | **Max Faces** | *Render > External Renderer* | Intermediate | Limita cuántas caras se mandan, para que no intentes enviar veinte millones de polígonos y se atragante el envío. Si la escultura es más pesada, conviene bajarla antes con Decimation Master, que para render da un resultado indistinguible. |
| ⚙️ | **External Renderer > cómo viaja la geometría** | *Render > External Renderer* | Intermediate | Cómo se empaqueta el modelo al mandarlo fuera. Los elementos en gris se encienden cuando el puente está instalado y con licencia. |
| 🔗 | **Auto Merge** | *Render > External Renderer* | Intermediate | Fusiona automáticamente los SubTools al enviarlos, en vez de mandarlos como objetos sueltos (activo en marrón en tu captura). |
| 🧱 | **Groups By Materials** | *Render > External Renderer* | Intermediate | Agrupa la geometría según el material que tenga asignado, que es justo lo que quieres para luego poder asignar materiales distintos en el otro programa sin tener que volver a separar nada a mano. |
| 🎨 | **Send Document Color** | *Render > External Renderer* | Intermediate | Manda también el color de fondo del documento de ZBrush. |


## Render > Render Properties


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚙️ | **Render Properties > detalle y posterizado** | *Render > Render Properties* | Advanced | Las propiedades generales que afectan a todos los renders. |
| 🔬 | **Details** | *Render > Render Properties* | Advanced | El nivel de detalle con el que se calcula la superficie (3 en tu captura). |
| 🖍️ | **3D Posterize** | *Render > Render Properties* | Advanced | Reduce el número de tonos, dando ese efecto de bandas planas tipo cartel serigrafiado (0 en tu captura, o sea apagado). |
| 📈 | **Exp** | *Render > Render Properties* | Advanced | El exponente del posterizado, la curva con la que reparte esas bandas (1 en tu captura). |
| 🫧 | **SmoothNormals** | *Render > Render Properties* | Advanced | Suaviza las normales al renderizar, o sea disimula las facetas de un modelo poco subdividido sin tener que subdividirlo más. Es la forma barata de que una malla ligera se vea redondeada. |
| 🔍 | **Render Properties > qué geometría al vuelo se dibuja** | *Render > Render Properties* | Advanced | Qué elementos generados sobre la marcha aparecen en el render. Los dos primeros desconciertan bastante cuando están apagados, porque tienes algo puesto y no se ve. |
| 🧶 | **Draw MicroMesh** | *Render > Render Properties* | Advanced | Dibuja la geometría MicroMesh, que sustituye cada polígono por una malla en miniatura (escamas, hojas, remaches). Si está apagado no se ve en el render aunque la tengas puesta. |
| 🌾 | **Draw NoiseMaker3D** | *Render > Render Properties* | Advanced | Hace lo mismo con el ruido de superficie generado por NoiseMaker (activo en naranja en tu captura). Apágalo si quieres ver la forma limpia sin la textura de ruido. |
| 🎨 | **Materials Blend-Radius** | *Render > Render Properties* | Advanced | La anchura de la transición cuando dos materiales distintos se encuentran sobre la misma malla (0 en tu captura): a 0 el corte es seco, subiéndolo se funden poco a poco. |
| ✨ | **Smooth Enhance Edges** | *Render > Render Properties* | Advanced | Resalta los bordes suavizándolos (0 en tu captura). |
| 🌑 | **Render Properties > Shadows y AOcclusion** | *Render > Render Properties* | Advanced | Los dos interruptores de sombra, y conviene tener clara la diferencia entre ellos porque no son lo mismo. |
| 🌑 | **Shadows** | *Render > Render Properties* | Advanced | Enciende las sombras PROYECTADAS, las que un volumen tira sobre otro cuando le da una luz (activo en naranja en tu captura). |
| 🕳️ | **AOcclusion** | *Render > Render Properties* | Advanced | Enciende la OCLUSIÓN AMBIENTAL, que es otra cosa: no son sombras de una luz concreta, sino el oscurecimiento natural de los recovecos, las axilas, los pliegues de la ropa. Es LA opción que hace que una escultura se lea bien, porque separa las formas unas de otras; en un modelo gris sin texturizar, encenderla es la diferencia entre ver el trabajo y no verlo. |
| 🎨 | **Render Properties > el color de las sombras** | *Render > Render Properties* | Advanced | Uno de los cambios más baratos y que más se notan en un render. |
| 🟦 | **Shadow&AO** | *Render > Render Properties* | Advanced | El recuadro de color con el que se tiñen las sombras y la oclusión (negro en tu captura). Poniéndolo en un AZUL MUY OSCURO en vez de negro puro, el render gana muchísimo, porque en la realidad las sombras nunca son negras sino del color de la luz ambiente que llega a ellas. |
| ▬ | **Flat Shadow** | *Render > Render Properties* | Advanced | Da sombras planas, de un solo tono, sin degradado. Útil para un acabado de ilustración o cel-shading. |
| 💧 | **Vibrant** | *Render > Render Properties* | Advanced | La saturación con la que se aplica ese color de sombra (50 en tu captura): a más valor, la sombra tira más de color y menos de gris. |
| ✨ | **Render Properties > los efectos de material** | *Render > Render Properties* | Advanced | Los interruptores de los efectos de material; sus ajustes finos están cada uno en su propia sub-paleta más abajo. |
| 🩸 | **Sss** | *Render > Render Properties* | Advanced | Activa la dispersión subsuperficial, la luz que atraviesa un material translúcido: es lo que hace que una oreja se vea rojiza a contraluz, y lo que separa una piel creíble de una de plástico. |
| 🫧 | **Transparent** | *Render > Render Properties* | Advanced | Activa las transparencias en el render. |
| 🕯️ | **WaxPreview** | *Render > Render Properties* | Advanced | Una vista previa rápida del efecto de cera, mucho más ligera que el SSS de verdad. Para presentar una escultura sin texturizar suele bastar con esta. |
| 🌫️ | **Render Properties > fibras, HD y atmósfera** | *Render > Render Properties* | Advanced | Más interruptores de lo que se dibuja y de los recursos atmosféricos. |
| 🌫️ | **View Blur** | *Render > Render Properties* | Advanced | Desenfoca la vista. |
| 💇 | **Fibers** | *Render > Render Properties* | Advanced | Dibuja las fibras de FiberMesh (pelo, hierba, alfombras). Si has hecho un FiberMesh y no aparece en el render, este es el botón. |
| 🎚️ | **Af** | *Render > Render Properties* | Advanced | El ajuste que acompaña a Fibers. |
| 🔬 | **HDGeometry** | *Render > Render Properties* | Advanced | Dibuja la geometría de alta definición, esos niveles de detalle extra que ZBrush guarda aparte y que no están en la malla normal. |
| ☁️ | **Fog** | *Render > Render Properties* | Advanced | Enciende la niebla, que tiene su propia sub-paleta más abajo. |
| 🌫️ | **Depth Cue** | *Render > Render Properties* | Advanced | Enciende el difuminado por distancia, también con sub-paleta propia. |
| 🖼️ | **Render Properties > el acabado de la imagen** | *Render > Render Properties* | Advanced | Cómo se remata la imagen final. |
| 🫧 | **SoftZ** | *Render > Render Properties* | Advanced | Suaviza el canal de profundidad al renderizar, quitando el escalonado de los bordes. |
| 🫧 | **SoftRGB** | *Render > Render Properties* | Advanced | Hace lo mismo con el canal de color. |
| 📄 | **Flatten** | *Render > Render Properties* | Advanced | Aplana el resultado en una sola capa (activo en naranja en tu captura). |
| 🌓 | **3D Shading** | *Render > Render Properties* | Advanced | La intensidad general del sombreado tridimensional (100 en tu captura): bajándolo, el modelo se va aplanando hasta parecer un dibujo, lo que combinado con Flat Shadow y 3D Posterize da un acabado de ilustración en vez de uno fotográfico. |
| 💡 | **Render Properties > los mandos globales de iluminación** | *Render > Render Properties* | Advanced | Los tres mandos globales, que se suman por encima de lo que hagan las luces de la paleta Light. Los tres están a 0 en tu captura, que es lo normal: solo se tocan cuando quieres corregir el conjunto sin ir material por material. |
| 🔆 | **Global Ambient** | *Render > Render Properties* | Advanced | La luz ambiente general, la que llega de todas partes por igual: subiéndola se aclaran las zonas de sombra, pero pasarse aplana el modelo porque elimina el contraste. |
| 🎨 | **Global Diffuse** | *Render > Render Properties* | Advanced | La intensidad global del color difuso, o sea del color propio de la superficie. |
| ✨ | **Global Specular** | *Render > Render Properties* | Advanced | La intensidad global de los brillos especulares, los reflejos puntuales de la luz; subirlo hace que todo parezca más húmedo o más pulido. |


## Render > BPR RenderPass


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔬 | **BPR RenderPass > calidad del muestreo** | *Render > BPR RenderPass* | Advanced | BPR RENDERPASS es el equivalente de las AOV pero para el render propio de ZBrush: te entrega el render partido en CAPAS separadas para montarlo luego en Photoshop, y es probablemente la sub-paleta más útil de toda la paleta Render para tu portafolio. Arriba, la miniatura BPR muestra la última pasada calculada. |
| 🔬 | **SPix** | *Render > BPR RenderPass* | Advanced | El sobremuestreo: cuántas muestras por píxel se toman, lo que quita el escalonado de los bordes (3 en tu captura). 3 es un buen valor y subirlo mucho solo alarga el cálculo. |
| 🔪 | **SSharp** | *Render > BPR RenderPass* | Advanced | Reenfoca el resultado después de ese suavizado, para recuperar nitidez (0 en tu captura). |
| 🌫️ | **VBlur Radius** | *Render > BPR RenderPass* | Advanced | El radio del desenfoque de la capa de vista (en gris en tu captura). |
| 🗂️ | **BPR RenderPass > las capas** | *Render > BPR RenderPass* | Advanced | Las capas en sí: cada botón guarda su imagen por separado. LA COMBINACIÓN MÍNIMA que merece la pena guardar siempre: Com, Dep, AmOc y Mask. |
| 🖼️ | **Com** | *Render > BPR RenderPass* | Advanced | El compuesto: todo junto, la imagen final. |
| 🎨 | **Img** | *Render > BPR RenderPass* | Advanced | La imagen de color. |
| 📏 | **Dep** | *Render > BPR RenderPass* | Advanced | Depth: la profundidad en grises, con la que luego desenfocas por distancia. |
| 🌑 | **Shdw** | *Render > BPR RenderPass* | Advanced | Las sombras. |
| 🕳️ | **AmOc** | *Render > BPR RenderPass* | Advanced | La oclusión ambiental. |
| ⬛ | **Mask** | *Render > BPR RenderPass* | Advanced | La máscara del modelo recortado sobre el fondo, imprescindible para poner otro fondo detrás sin recortar a mano. |
| 🩸 | **Sss** | *Render > BPR RenderPass* | Advanced | La luz que atraviesa la piel. |
| ▬ | **Floor** | *Render > BPR RenderPass* | Advanced | El suelo. |
| ♻️ | **Reuse Existing Maps** | *Render > BPR RenderPass* | Advanced | Reutiliza los mapas ya calculados en vez de rehacerlos, lo que ahorra un montón de tiempo cuando solo cambias un detalle. |


## Render > BPR Transparency


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🫧 | **Render > BPR Transparency** | *Render > BPR Transparency* | Advanced | Los ajustes finos de las transparencias en el render BPR. Hay que tener Transparent encendido en Render Properties, si no todo el bloque sale en gris como en tu captura. |
| 🎚️ | **Strength** | *Render > BPR Transparency* | Advanced | Cuánta transparencia se aplica. |
| 🧭 | **NFactor** | *Render > BPR Transparency* | Advanced | El factor de las normales: cuánto influye la inclinación de la superficie en lo transparente que se ve. Es lo que hace que un cristal se vea claro de frente y opaco de canto. |
| 🎨 | **ByColor** | *Render > BPR Transparency* | Advanced | Hace que la transparencia dependa del COLOR de la superficie: las zonas claras dejan pasar más luz que las oscuras. |
| 🎚️ | **CFactor** | *Render > BPR Transparency* | Advanced | Regula la fuerza de esa relación con el color. |
| 💎 | **Refract** | *Render > BPR Transparency* | Advanced | Activa la refracción, el desvío de la luz al atravesar el material: es lo que hace que lo que se ve a través de una gema salga desplazado y deformado en vez de simplemente translúcido. |
| 🎚️ | **RFactor** | *Render > BPR Transparency* | Advanced | El índice de esa refracción. |


## Render > BPR Shadow


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌓 | **BPR Shadow > fuerza, rayos y ángulo** | *Render > BPR Shadow* | Advanced | La calidad de las sombras proyectadas del render BPR, y una de las tres sub-paletas que de verdad merece la pena aprender. |
| 🔦 | **FStrength** | *Render > BPR Shadow* | Advanced | La fuerza de la sombra en el primer plano (1 en tu captura). |
| 🌑 | **GStrength** | *Render > BPR Shadow* | Advanced | La fuerza de la sombra general (0.75 en tu captura). |
| ☀️ | **Rays** | *Render > BPR Shadow* | Advanced | El número de rayos que se lanzan (12 en tu captura): pocos rayos dan sombras con grano, muchos las dan limpias pero tardan más. 12 es razonable para trabajar; súbelo a 50 o más para la imagen final. |
| 📐 | **Angle** | *Render > BPR Shadow* | Advanced | EL parámetro: la apertura del cono de la luz, lo que decide si la sombra es dura y recortada (0) o blanda y difusa (valores altos). Una sombra blanda es lo que da sensación de luz de estudio, y subirlo es el cambio que más acerca un render de ZBrush a una fotografía. |
| ⚙️ | **BPR Shadow > los ajustes de cálculo** | *Render > BPR Shadow* | Advanced | Cómo se calcula el mapa de sombras. |
| 🔢 | **Res** | *Render > BPR Shadow* | Advanced | La resolución del mapa de sombras (4096 en tu captura). Si el borde de la sombra sale con escalones, es este el que hay que subir. |
| 🫧 | **Blur** | *Render > BPR Shadow* | Advanced | El desenfoque que se le aplica al terminar (2 en tu captura). |
| 👁️ | **VDepth** | *Render > BPR Shadow* | Advanced | El desplazamiento desde la VISTA, que sirve para quitar el 'acné' de sombra: ese moteado que aparece cuando una superficie se sombrea a sí misma por error de precisión (0 en tu captura). |
| 💡 | **LDepth** | *Render > BPR Shadow* | Advanced | El mismo desplazamiento pero desde la LUZ (0 en tu captura). |
| ⚡ | **Spd** | *Render > BPR Shadow* | Advanced | El modo rápido de cálculo (activo en naranja en tu captura). |
| 📈 | **Gamma** | *Render > BPR Shadow* | Advanced | La curva de brillo de la sombra (2 en tu captura), que decide si el paso de luz a sombra es progresivo o brusco. |
| 📉 | **BPR Shadow > el desvanecido con la distancia** | *Render > BPR Shadow* | Advanced | Un detalle pequeño con mucho efecto. En la realidad una sombra es nítida y oscura justo donde el objeto toca la superficie, y se va difuminando y aclarando a medida que se aleja; reproducir eso es lo que separa una figura que parece apoyada de una que parece flotando. |
| 📉 | **Falloff** | *Render > BPR Shadow* | Advanced | La caída general de la sombra (0 en tu captura). |
| 📏 | **Max Dist** | *Render > BPR Shadow* | Advanced | Hasta qué distancia se proyecta la sombra (0 en tu captura). |
| 📈 | **DistFalloff** | *Render > BPR Shadow* | Advanced | La curva de ese desvanecido (2 en tu captura). |


## Render > BPR AO


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕳️ | **BPR AO > fuerza, rayos y resolución** | *Render > BPR AO* | Advanced | La misma lista de controles que BPR Shadow pero aplicada a la OCLUSIÓN AMBIENTAL, la que oscurece recovecos, pliegues y puntos donde dos superficies se juntan. Para una escultura sin texturizar es el efecto que más hace por que se lea el volumen. |
| 🔦 | **FStrength** | *Render > BPR AO* | Advanced | La fuerza de la oclusión en el primer plano. |
| 🕳️ | **GStrength** | *Render > BPR AO* | Advanced | La fuerza de la oclusión general (0.75 en tu captura). |
| ☀️ | **Rays** | *Render > BPR AO* | Advanced | Los rayos de muestreo. Aquí conviene subirlos MÁS que en las sombras, porque la oclusión con pocos rayos sale sucia y moteada. |
| 📐 | **Angle** | *Render > BPR AO* | Advanced | La apertura del muestreo. |
| 🔢 | **Res** | *Render > BPR AO* | Advanced | La resolución del mapa de oclusión. |
| 🫧 | **Blur** | *Render > BPR AO* | Advanced | El suavizado final. |
| 📏 | **BPR AO > distancia y desvanecido** | *Render > BPR AO* | Advanced | Todo el bloque sale en gris hasta que enciendes AOcclusion en Render Properties. Aquí están los dos ajustes clave de la sub-paleta. |
| 👁️ | **VDepth** | *Render > BPR AO* | Advanced | Desplaza el cálculo desde la vista para evitar el moteado. |
| 💡 | **LDepth** | *Render > BPR AO* | Advanced | Desplaza el cálculo desde la luz, con el mismo fin. |
| ⚡ | **Spd** | *Render > BPR AO* | Advanced | El modo rápido de cálculo (activo en tu captura). |
| 📈 | **Gamma** | *Render > BPR AO* | Advanced | La curva de intensidad de la oclusión. |
| 📉 | **Falloff** | *Render > BPR AO* | Advanced | Cómo se desvanece la oclusión (0 en tu captura). |
| 📏 | **Max Dist** | *Render > BPR AO* | Advanced | Hasta qué distancia se busca oclusión. Ponerlo demasiado alto ensucia toda la pieza con manchas grandes en vez de marcar solo los recovecos: si tu AO sale como una mancha gris general y no como suciedad en los pliegues, ese es exactamente el número a bajar. |
| 📈 | **DistFalloff** | *Render > BPR AO* | Advanced | La curva de ese desvanecido con la distancia. |


## Render > BPR SSS


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🩸 | **BPR SSS > SSS Across Subtools** | *Render > BPR SSS* | Advanced | La dispersión subsuperficial es la luz que entra en un material translúcido, rebota dentro y sale por otro lado: el efecto que hace que la piel parezca piel y no plástico, o que una vela de cera se vea encendida por dentro. |
| 🧩 | **SSS Across Subtools** | *Render > BPR SSS* | Advanced | Permite que ese efecto pase de un SubTool a otro, o sea que la luz que atraviesa el brazo ilumine también la manga que lo cubre. Sin él, cada SubTool se calcula por su cuenta y los contactos entre piezas se ven partidos, con un corte antinatural justo donde una acaba y otra empieza. |
| ⚙️ | **BPR SSS > los ajustes de cálculo** | *Render > BPR SSS* | Advanced | Los mismos que en Shadow y AO. Sale todo en gris hasta que enciendes Sss en Render Properties y usas un material que lo soporte. |
| ☀️ | **Rays** | *Render > BPR SSS* | Advanced | Los rayos de muestreo. |
| 📐 | **Angle** | *Render > BPR SSS* | Advanced | La apertura del muestreo. |
| 🔢 | **Res** | *Render > BPR SSS* | Advanced | La resolución del mapa. |
| 🫧 | **Blur** | *Render > BPR SSS* | Advanced | El suavizado. En SSS conviene tenerlo generoso, porque la luz dentro de la piel se reparte de forma muy difusa y un resultado nítido delata que es falso. |
| 👁️ | **VDepth** | *Render > BPR SSS* | Advanced | El desplazamiento desde la vista. |
| 💡 | **LDepth** | *Render > BPR SSS* | Advanced | El desplazamiento desde la luz. |
| ⚡ | **Spd** | *Render > BPR SSS* | Advanced | El modo rápido de cálculo. |


## Render > BPR Filters


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎛️ | **BPR Filters > gestión de configuraciones** | *Render > BPR Filters* | Advanced | BPR FILTERS es un mini-Photoshop dentro de ZBrush: aplica efectos sobre el render YA calculado, en tiempo real y sin volver a renderizar. EL TRUCO DE FLUJO: monta tu combinación de filtros favorita una vez, guárdala con Save, y reutilízala en todas las piezas del portafolio — eso es lo que hace que una colección de trabajos parezca de la misma mano. |
| 📂 | **Load** | *Render > BPR Filters* | Advanced | Carga un juego de filtros entero desde archivo. |
| 💾 | **Save** | *Render > BPR Filters* | Advanced | Guarda el juego de filtros actual. |
| ❄️ | **Freeze** | *Render > BPR Filters* | Advanced | Congela el resultado filtrado. |
| 📚 | **Lightbox ▶ Filter** | *Render > BPR Filters* | Advanced | Abre la pestaña de LightBox con los filtros de fábrica. |
| 📥 | **Load From Project** | *Render > BPR Filters* | Advanced | Saca los filtros de otro proyecto. |
| 🔢 | **BPR Filters > las ranuras F1 a F12** | *Render > BPR Filters* | Advanced | Se pueden encadenar hasta doce filtros y se aplican EN ORDEN, igual que una pila de capas de ajuste en Photoshop, así que el orden importa: un filtro de contraste antes o después de uno de color da resultados distintos. |
| 📋 | **Copy** | *Render > BPR Filters* | Advanced | Copia el filtro de la ranura activa. |
| 📥 | **Paste** | *Render > BPR Filters* | Advanced | Pega el filtro copiado en otra ranura. |
| ✂️ | **Cut** | *Render > BPR Filters* | Advanced | Corta el filtro de la ranura activa. |
| 📌 | **Insert** | *Render > BPR Filters* | Advanced | Inserta un filtro en medio de la pila. |
| 🧹 | **Reset Filter** | *Render > BPR Filters* | Advanced | Borra el filtro de la ranura activa. |
| 🔘 | **F1 - F12** | *Render > BPR Filters* | Advanced | Las doce ranuras de filtro, cada una con su botón redondo. F1 está seleccionada en tu captura. |
| 🎚️ | **BPR Filters > qué filtro es y cómo se mezcla** | *Render > BPR Filters* | Advanced | Lo que define la ranura de filtro seleccionada. Cambiar solo el modo de fusión de un filtro ya montado puede darte un resultado completamente distinto sin tocar ningún número. |
| 🎛️ | **Filter** | *Render > BPR Filters* | Advanced | El desplegable donde eliges QUÉ filtro es esta ranura (▶ Noise en tu captura, pero ahí dentro está toda la lista de efectos disponibles). |
| 🔀 | **BlendMode** | *Render > BPR Filters* | Advanced | El modo de fusión con el que ese filtro se mezcla con la imagen de debajo (▶ Replace(Normal) en tu captura), exactamente igual que los modos de capa de Photoshop: Replace lo sustituye, y hay otros para multiplicar, aclarar, superponer, etc. |
| 🎨 | **BPR Filters > cantidad, opacidad y colores** | *Render > BPR Filters* | Advanced | Los mandos básicos del filtro activo. |
| 🌾 | **Noise** | *Render > BPR Filters* | Advanced | La cantidad del efecto. El deslizador cambia de nombre según el filtro elegido; en tu captura el filtro es Noise. |
| 🌗 | **Opacity** | *Render > BPR Filters* | Advanced | La opacidad con la que se aplica: bajarla es la forma de dosificar cualquier filtro que se pase de fuerte, y casi siempre es mejor que reducir el efecto en sí. |
| ⬛ | **Back Color** | *Render > BPR Filters* | Advanced | Uno de los dos colores entre los que trabaja el filtro; en uno de degradado o de tinte, el de las zonas oscuras. |
| ⬜ | **Front Color** | *Render > BPR Filters* | Advanced | El otro color, el de las zonas claras. |
| ⚙️ | **Modifiers** | *Render > BPR Filters* | Advanced | Despliega el bloque de ajustes por canal, que es lo que convierte esto en una herramienta seria. |


## Render > BPR Filters > Modifiers


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎭 | **BPR Filters > Modifiers: dónde se aplica** | *Render > BPR Filters > Modifiers* | Advanced | La parte que convierte el filtro en una herramienta seria en vez de un efecto global: decidir en qué zonas actúa. |
| 🖼️ | **Txtr** | *Render > BPR Filters > Modifiers* | Advanced | Permite usar una TEXTURA como máscara del filtro, o sea decidir con una imagen dónde actúa. |
| ➖ | **Mask Border** | *Render > BPR Filters > Modifiers* | Advanced | Limita el efecto a los bordes de la máscara. |
| 🫧 | **MBlur** | *Render > BPR Filters > Modifiers* | Advanced | El desenfoque de esa máscara, para que la transición no sea seca. |
| 🫧 | **MSoft** | *Render > BPR Filters > Modifiers* | Advanced | El suavizado de esa máscara. |
| 📏 | **Radius** | *Render > BPR Filters > Modifiers* | Advanced | El radio de acción del filtro. |
| 🔵 | **Normal Gaus** | *Render > BPR Filters > Modifiers* | Advanced | El tipo de desenfoque que se usa: gaussiano normal. |
| 💫 | **BPR Filters > Modifiers: máscara y Fresnel** | *Render > BPR Filters > Modifiers* | Advanced | Conviene entender el patrón porque se repite en todos los canales: el primero es CUÁNTO y el segundo (Exp) es la CURVA, o sea si el paso de aplicado a no aplicado es suave o brusco. |
| 🎭 | **Mask** | *Render > BPR Filters > Modifiers* | Advanced | La intensidad con la que la máscara controla el filtro. |
| 📈 | **Mask Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de esa máscara. |
| 💫 | **Fresnel** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro solo en los bordes donde la superficie se gira y se aleja de la cámara. Es lo que da ese halo de luz en el contorno del personaje, el 'rim light', y es posiblemente el truco más rentable de toda la sub-paleta para una lámina de portafolio: separa la figura del fondo sin recortarla. |
| 📈 | **Fresnel Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva del efecto Fresnel: si la franja luminosa es ancha o estrecha. |
| 🗂️ | **BPR Filters > Modifiers: sombra, oclusión y SSS** | *Render > BPR Filters > Modifiers* | Advanced | Aquí se elige que el filtro actúe SOLO sobre una parte concreta de la información del render, lo que permite cosas muy finas sin pintar ninguna máscara. |
| 🌑 | **Shadow** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro únicamente donde hay sombra: subiéndolo puedes, por ejemplo, teñir de azul solo las zonas en penumbra, que es el viraje clásico de cine. |
| 📈 | **Shadow Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de ese canal de sombra. |
| 🕳️ | **Ao** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro solo en la oclusión ambiental, o sea solo en los recovecos: perfecto para meter suciedad en los pliegues. |
| 📈 | **AO Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva del canal de oclusión. |
| 🩸 | **Sss** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro solo donde la luz atraviesa el material. |
| 📈 | **SSS Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva del canal de dispersión subsuperficial. |
| 📏 | **BPR Filters > Modifiers: profundidad** | *Render > BPR Filters > Modifiers* | Advanced | Usar la PROFUNDIDAD para decidir dónde actúa el filtro. Así es como se hace una niebla atmosférica creíble (aclarar y desaturar lo lejano) o un desenfoque de cámara, y es la forma de aislar al personaje del fondo sin recortarlo. |
| 📏 | **Depth** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro según la distancia: solo a lo que está lejos o solo a lo que está cerca. |
| 📈 | **Depth Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de ese canal de profundidad. |
| 🅰️ | **Depth A** | *Render > BPR Filters > Modifiers* | Advanced | El primer límite de la franja de profundidad afectada. |
| 🅱️ | **Depth B** | *Render > BPR Filters > Modifiers* | Advanced | El segundo límite: entre A y B defines una banda, y solo lo que caiga dentro recibe el efecto. |
| 🪨 | **BPR Filters > Modifiers: cavidades** | *Render > BPR Filters > Modifiers* | Advanced | Aplicar el filtro en las grietas y hendiduras de la superficie. Es lo que se usa para oscurecer las grietas de la piel, meter polvo en las juntas de una armadura o marcar el fondo de los poros. |
| 🪨 | **Cavity** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro en las CAVIDADES de la superficie. |
| 📈 | **Cavity Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de ese canal. |
| 📏 | **CavityRadius** | *Render > BPR Filters > Modifiers* | Advanced | Hasta qué tamaño de hueco cuenta como cavidad. Ajustarlo es lo que decide si detecta solo los poros finos o también los pliegues grandes. |
| 🎚️ | **CavitySense** | *Render > BPR Filters > Modifiers* | Advanced | La sensibilidad del detector de cavidades. |
| ⚡ | **BPR Filters > Modifiers: detección de bordes** | *Render > BPR Filters > Modifiers* | Advanced | Lo contrario que Cavity: detecta los BORDES, las aristas salientes. Aplicando un aclarado sobre ellos sale el efecto de DESGASTE DEL METAL, ese brillo en las esquinas de una pieza usada donde la pintura se ha ido. LA RECETA CLÁSICA de esta sub-paleta: Cavity oscureciendo grietas + EdgeDetect aclarando aristas. Con esos dos filtros encadenados, una escultura gris pasa a parecer un objeto real y usado. |
| ⚡ | **EdgeDetect** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro en las aristas salientes. |
| 📈 | **ED Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de ese canal. |
| 📏 | **Ed Ds** | *Render > BPR Filters > Modifiers* | Advanced | La distancia de la detección de bordes. |
| 📏 | **ED Radius** | *Render > BPR Filters > Modifiers* | Advanced | El radio de detección. |
| 🎚️ | **E Sense** | *Render > BPR Filters > Modifiers* | Advanced | La sensibilidad del detector de bordes. |
| 🎲 | **BPR Filters > Modifiers: ruido y rango de grises** | *Render > BPR Filters > Modifiers* | Advanced | El ruido procedural y el rango tonal sobre el que actúa el filtro. El rango de grises es el equivalente a los controles de Niveles de Photoshop: sirve para actuar solo sobre las luces, solo sobre las sombras o solo sobre los medios tonos. |
| 🎲 | **NoiseMaker** | *Render > BPR Filters > Modifiers* | Advanced | Añade ruido procedural al filtro, para que el efecto no sea uniforme sino moteado. |
| 📈 | **Edit Noise** | *Render > BPR Filters > Modifiers* | Advanced | Abre el editor de curvas de ese ruido. |
| ⬛ | **G1** | *Render > BPR Filters > Modifiers* | Advanced | El primer extremo del rango de grises sobre el que se aplica el filtro. |
| 🌗 | **Gray Range** | *Render > BPR Filters > Modifiers* | Advanced | La franja entre los dos extremos. |
| ⬜ | **G2** | *Render > BPR Filters > Modifiers* | Advanced | El segundo extremo del rango de grises. |
| 🌈 | **BPR Filters > Modifiers: el bloque de color** | *Render > BPR Filters > Modifiers* | Advanced | Todo con el mismo patrón valor + exponente. Con estos y el rango de grises se montan virados completos sin salir de ZBrush: girar el matiz de las sombras hacia el azul y el de las luces hacia el ámbar es la fórmula de casi cualquier lámina de portafolio. |
| 🎨 | **Color** | *Render > BPR Filters > Modifiers* | Advanced | El recuadro que elige el tono base del filtro. |
| 🌈 | **RGB Int** | *Render > BPR Filters > Modifiers* | Advanced | La intensidad sobre los tres canales de color a la vez. |
| 📈 | **RGB Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de esa intensidad. |
| 🔆 | **Int** | *Render > BPR Filters > Modifiers* | Advanced | La luminosidad. |
| 📈 | **Int Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de la luminosidad. |
| 🌈 | **Hue** | *Render > BPR Filters > Modifiers* | Advanced | El matiz, o sea el giro de color en la rueda. |
| 📈 | **Hue Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva del matiz. |
| 💧 | **Sat** | *Render > BPR Filters > Modifiers* | Advanced | La saturación. |
| 📈 | **Sat Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de la saturación. |
| 🧭 | **BPR Filters > Modifiers: orientación y canales** | *Render > BPR Filters > Modifiers* | Advanced | El último bloque: aplicar el filtro según hacia dónde mira la superficie, y elegir sobre qué canal de color trabaja. |
| 🧭 | **Normal** | *Render > BPR Filters > Modifiers* | Advanced | Aplica el filtro según la ORIENTACIÓN de la superficie: por ejemplo, girar el tono solo en las caras que miran hacia arriba imita la luz del cielo cayendo sobre el personaje, mientras las que miran abajo reciben el rebote del suelo. Es un recurso de iluminación muy eficaz y que no cuesta nada de render. |
| 📈 | **Normal Exp** | *Render > BPR Filters > Modifiers* | Advanced | La curva de ese canal de orientación. |
| 🔴 | **Red** | *Render > BPR Filters > Modifiers* | Advanced | Enciende o apaga el canal rojo para que el filtro trabaje solo sobre él. |
| 🟢 | **Green** | *Render > BPR Filters > Modifiers* | Advanced | Lo mismo con el canal verde. |
| 🔵 | **Blue** | *Render > BPR Filters > Modifiers* | Advanced | Lo mismo con el canal azul. |


## Render > Antialiasing


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🪒 | **Render > Antialiasing** | *Render > Antialiasing* | Intermediate | El suavizado de los bordes dentados, esos escalones de píxeles que delatan una imagen sin acabar. Para las láminas finales del portafolio, la costumbre es otra aún mejor: renderizar el documento al doble de tamaño y reducirlo después en Photoshop. |
| 🫧 | **Blur** | *Render > Antialiasing* | Intermediate | Cuánto se difumina el borde (100 en tu captura). |
| ➖ | **Edge** | *Render > Antialiasing* | Intermediate | La sensibilidad con la que se detecta qué es un borde (25 en tu captura). Si lo subes mucho empieza a suavizar detalles que no lo son y la imagen pierde nitidez. |
| 📏 | **Size** | *Render > Antialiasing* | Intermediate | El tamaño de la zona que se trata alrededor de cada borde (1 en tu captura). |
| 🔬 | **Super Sample** | *Render > Antialiasing* | Intermediate | El método bueno y el que de verdad importa (0 en tu captura): en vez de retocar el borde a posteriori, renderiza la imagen a mayor tamaño y luego la reduce, de modo que el suavizado sale del propio muestreo. Es lento pero da la mejor calidad con diferencia. |


## Render > Depth Cue


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌫️ | **Render > Depth Cue** | *Render > Depth Cue* | Intermediate | El difuminado por distancia, o perspectiva atmosférica: lo que está lejos se ve más borroso y con menos contraste, igual que unas montañas en el horizonte. Recurso barato y muy eficaz para dar profundidad. Con un personaje, lo típico es poner Depth1 justo detrás de la cara para que la cabeza salga nítida y la espalda se vaya diluyendo. |
| 🎚️ | **Intensity** | *Render > Depth Cue* | Intermediate | La fuerza del efecto (100 en tu captura). |
| 🫧 | **Softness** | *Render > Depth Cue* | Intermediate | Lo gradual que es la transición entre lo nítido y lo difuminado (4 en tu captura). |
| 1️⃣ | **Depth1** | *Render > Depth Cue* | Intermediate | La distancia donde empieza a notarse el efecto (-0.5 en tu captura). |
| 2️⃣ | **Depth2** | *Render > Depth Cue* | Intermediate | La distancia donde llega al máximo (0.5 en tu captura). El degradado gris que se ve encima de los deslizadores es la vista previa de esa transición. |


## Render > Fog


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ☁️ | **Render > Fog** | *Render > Fog* | Intermediate | La niebla, que es Depth Cue pero con COLOR en lugar de solo difuminado: rellena la distancia con un tono, así que sirve tanto para una escena de bosque neblinoso como para separar al personaje de un fondo plano. |
| 🎚️ | **Intensity** | *Render > Fog* | Intermediate | La densidad de la niebla (100 en tu captura). |
| 1️⃣ | **Depth1** | *Render > Fog* | Intermediate | La distancia donde empieza la niebla (0 en tu captura). |
| 2️⃣ | **Depth2** | *Render > Fog* | Intermediate | La distancia donde ya lo tapa todo (1 en tu captura). |
| ⬜ | **los dos colores de niebla** | *Render > Fog* | Intermediate | Los dos recuadros de color (blancos en tu captura) son el color de la niebla cerca y lejos, y el degradado gris de debajo enseña cómo se pasa de uno al otro. Ponerlos de dos tonos distintos, por ejemplo un azul frío al fondo y un gris cálido cerca, es lo que le da atmósfera de verdad en vez de un velo blanco uniforme. |


## Render > Fast Render


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🏃 | **Render > Fast Render** | *Render > Fast Render* | Intermediate | La sub-paleta más pequeña de toda la paleta. Fast Render es el modo de dibujo rápido que ZBrush usa mientras esculpes para que el visor vaya fluido, y estos dos números son su iluminación básica. La proporción entre los dos decide cuánto contraste ves mientras trabajas, y no afecta para nada al render final: si te cuesta apreciar el detalle porque todo se ve muy plano, sube Diffuse y baja Ambient. |
| 🔆 | **Ambient** | *Render > Fast Render* | Intermediate | La luz ambiente, la que llega por igual desde todas partes y evita que las sombras queden negras del todo (0.1 en tu captura). |
| 💡 | **Diffuse** | *Render > Fast Render* | Intermediate | La luz difusa, la que viene de una dirección y modela el volumen (0.75 en tu captura). |


## Render > Preview Shadows


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌘 | **Preview Shadows > tipo e intensidad** | *Render > Preview Shadows* | Intermediate | Las sombras que se ven MIENTRAS esculpes, sin esperar a un render completo. Son mucho más baratas que las de BPR Shadow y su papel es puramente ayudarte a leer el volumen mientras trabajas. |
| 🌑 | **ObjShadow** | *Render > Preview Shadows* | Intermediate | La intensidad de la sombra que un objeto proyecta (0.3 en tu captura): a 0 desaparece, a 1 es negra del todo. |
| 🌓 | **DeepShadow** | *Render > Preview Shadows* | Intermediate | El modo de sombra con profundidad, el que tiene en cuenta la distancia real entre las superficies y da un resultado bastante creíble (activo en naranja en tu captura). |
| ▬ | **Flat Shadow** | *Render > Preview Shadows* | Intermediate | La alternativa plana, más rápida y menos exacta, que interesa si el ordenador va justo. |
| 📐 | **Preview Shadows > la forma de la sombra** | *Render > Preview Shadows* | Intermediate | Dedicar un rato a ajustar Length y Slope hasta que los pliegues y las arrugas se lean bien es de las cosas que más cómodo hacen esculpir durante horas: con la luz en un ángulo rasante el detalle fino se ve muchísimo mejor que con la luz de frente. |
| 📏 | **Length** | *Render > Preview Shadows* | Intermediate | Lo larga que se dibuja la sombra (22 en tu captura). |
| 📐 | **Slope** | *Render > Preview Shadows* | Intermediate | La inclinación con la que cae, o sea el ángulo aparente de la luz (2 en tu captura). |
| 📏 | **Depth** | *Render > Preview Shadows* | Intermediate | Hasta qué profundidad se calcula (0.2 en tu captura). |


## Render > Preview AO


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔆 | **Preview AO > activar y calidad** | *Render > Preview AO* | Intermediate | La oclusión ambiental de vista previa: el oscurecimiento de recovecos que se ve mientras esculpes, sin renderizar. Es probablemente el ajuste que más se nota al trabajar, porque sin él una escultura gris se ve lisa y con él aparecen de golpe todos los pliegues y arrugas. |
| 🔘 | **Occlusion** | *Render > Preview AO* | Intermediate | El interruptor que enciende la oclusión de vista previa. |
| 🎚️ | **Quality** | *Render > Preview AO* | Intermediate | La calidad del cálculo. Súbela si ves manchas o bandas en vez de un degradado limpio. |
| 🌗 | **Intensity** | *Render > Preview AO* | Intermediate | La fuerza del oscurecimiento. |
| 📏 | **Preview AO > los radios** | *Render > Preview AO* | Intermediate | Los radios son lo que decide qué se marca. En tu captura sale todo en gris porque Occlusion no está activo. |
| 📏 | **Main Radius** | *Render > Preview AO* | Intermediate | El radio principal de búsqueda, o sea a qué distancia se considera que una superficie está tapando a otra. |
| 📏 | **Radius Secondary** | *Render > Preview AO* | Intermediate | Un segundo radio que se suma al primero. La combinación de uno GRANDE y uno PEQUEÑO es lo que hace que se marquen a la vez las sombras amplias de los volúmenes y las finas de las arrugas: con un solo radio siempre pierdes una de las dos escalas. |
| 🫧 | **Blur** | *Render > Preview AO* | Intermediate | Suaviza el resultado para quitarle el grano. |


## Render > Preview Wax


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🕯️ | **Preview Wax > fuerza y Fresnel** | *Render > Preview Wax* | Advanced | El efecto CERA de vista previa: una imitación barata de la translucidez, que hace que el modelo parezca hecho de cera o de jabón y deje pasar algo de luz por los bordes finos. Se usa muchísimo para presentar esculturas sin texturizar, porque disimula lo plano del gris y da un aspecto de figura de resina. |
| 🎚️ | **Strength** | *Render > Preview Wax* | Advanced | La fuerza del efecto. |
| 💫 | **Fresnel** | *Render > Preview Wax* | Advanced | Cuánto se nota en los bordes que se giran alejándose de la cámara: es lo que produce ese contorno luminoso. |
| 📈 | **Exponent** | *Render > Preview Wax* | Advanced | La curva del Fresnel, o sea si esa franja luminosa es ancha y suave o estrecha y marcada. |
| 🌡️ | **Preview Wax > penetración y temperatura** | *Render > Preview Wax* | Advanced | Sale casi todo en gris porque el efecto no está activo; se enciende con WaxPreview en Render Properties. |
| 📏 | **Radius** | *Render > Preview Wax* | Advanced | Hasta qué profundidad penetra la luz simulada dentro del material: poco radio da un efecto sutil en los bordes finos, mucho radio hace que zonas gruesas también se vean translúcidas. |
| 🌡️ | **Temperature** | *Render > Preview Wax* | Advanced | La temperatura de color de esa luz interna, y es el ajuste que decide de qué material parece la pieza: hacia el CÁLIDO para piel y cera, hacia el FRÍO para mármol o hielo. |
| 📏 | **Max Depth Tolerance** | *Render > Preview Wax* | Advanced | Limita la profundidad máxima que se tiene en cuenta (0 en tu captura). |


## Render > Environment


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🏞️ | **Environment > los modos de entorno** | *Render > Environment* | Advanced | El ENTORNO que rodea al modelo, o sea qué hay a su alrededor iluminándolo y reflejándose en él. Un HDRI decente cargado aquí cambia por completo el aspecto de un render de metal o de cualquier superficie brillante, porque los reflejos dejan de ser inventados y pasan a ser de un sitio real. |
| 🚫 | **Off** | *Render > Environment* | Advanced | Sin entorno (activo en naranja en tu captura). |
| 🎨 | **Color** | *Render > Environment* | Advanced | Usa un color plano como entorno. |
| 🖼️ | **Txtr** | *Render > Environment* | Advanced | Usa una imagen o HDRI cargada como entorno. |
| 🏞️ | **Scene** | *Render > Environment* | Advanced | Usa la propia escena como entorno. |
| 🔲 | **las dos miniaturas de entorno** | *Render > Environment* | Advanced | Las imágenes de entorno cargadas —en tu captura una azul lisa y otra con una textura— que son las que se eligen cuando el modo es Txtr. |
| 🔭 | **Environment > cómo se proyecta** | *Render > Environment* | Advanced | Cómo envuelve ese entorno a la escena. |
| 📏 | **Trace Distance** | *Render > Environment* | Advanced | Hasta qué distancia se rastrea el entorno al calcular los reflejos (en gris en tu captura). |
| 🔁 | **Repeat** | *Render > Environment* | Advanced | Cuántas veces se repite la imagen alrededor de la escena (1 en tu captura): con más de una el panorama se repite en mosaico, lo que rara vez interesa salvo para texturas abstractas. |
| 👁️ | **Field Of View** | *Render > Environment* | Advanced | El ángulo de visión con el que se proyecta (0 en tu captura), o sea si el entorno envuelve al modelo de cerca —con reflejos grandes y deformados— o queda lejos como un fondo panorámico con reflejos pequeños. |


## Render > Adjustments


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎚️ | **Adjustments > contraste** | *Render > Adjustments* | Intermediate | El retoque final de la imagen, el equivalente a las capas de ajuste de Photoshop pero dentro de ZBrush. Debajo del bloque hay una gráfica que muestra la curva resultante. |
| 🔘 | **Adjust** | *Render > Adjustments* | Intermediate | Enciende los ajustes de imagen. |
| 🧹 | **Clr** | *Render > Adjustments* | Intermediate | Los reinicia todos a cero. |
| 🌓 | **Contrast** | *Render > Adjustments* | Intermediate | El contraste general: separa claros y oscuros en toda la imagen. |
| 🔴 | **Red Contrast** | *Render > Adjustments* | Intermediate | El contraste solo del canal rojo. Los tres de color permiten desequilibrar la imagen a propósito, que es como se hacen los virados cinematográficos. |
| 🟢 | **Green Contrast** | *Render > Adjustments* | Intermediate | El contraste solo del canal verde. |
| 🔵 | **Blue Contrast** | *Render > Adjustments* | Intermediate | El contraste solo del canal azul. |
| 💡 | **Adjustments > brillo y gamma** | *Render > Adjustments* | Intermediate | Las otras dos familias. La diferencia entre las tres conviene tenerla clara: BRIGHTNESS suma luz a todo por igual, CONTRAST separa claros y oscuros, y GAMMA actúa sobre los TONOS MEDIOS sin tocar los extremos — este último suele ser el más útil, porque aclara u oscurece sin quemar las luces ni empastar las sombras. Subir el gamma azul y bajar el rojo da sombras frías; al revés, un ambiente de atardecer. |
| 🔆 | **Brightness** | *Render > Adjustments* | Intermediate | El brillo general: suma luz a toda la imagen por igual. |
| 🔴 | **Red Brightness** | *Render > Adjustments* | Intermediate | El brillo solo del canal rojo. |
| 🟢 | **Green Brightness** | *Render > Adjustments* | Intermediate | El brillo solo del canal verde. |
| 🔵 | **Blue Brightness** | *Render > Adjustments* | Intermediate | El brillo solo del canal azul. |
| 📈 | **Gamma** | *Render > Adjustments* | Intermediate | El gamma general: actúa sobre los tonos medios sin tocar los extremos. |
| 🔴 | **Red Gamma** | *Render > Adjustments* | Intermediate | El gamma solo del canal rojo. |
| 🟢 | **Green Gamma** | *Render > Adjustments* | Intermediate | El gamma solo del canal verde. |
| 🔵 | **Blue Gamma** | *Render > Adjustments* | Intermediate | El gamma solo del canal azul. |

