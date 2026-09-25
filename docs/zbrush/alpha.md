# Alpha


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🅰️ | **Alpha: qué es un alpha y para qué sirve esta paleta** | *Menú superior > Alpha* | Basic | Un ALPHA es una imagen en blanco y negro que hace de sello para el pincel: el blanco es lo que sobresale, el negro lo que no afecta, y los grises los valores intermedios. Cambiar el alpha del pincel Standard lo convierte en un pincel de escamas, de poros, de remaches o de lo que sea esa imagen, así que es la forma más rápida de meter detalle sin esculpirlo a mano. Esta paleta es donde se cargan, se guardan, se retocan y se fabrican esos alphas. El alpha activo también se ve y se cambia desde la tercera miniatura de la barra izquierda. |
| 📥 | **Alpha > importar, exportar y la biblioteca** | *Menú superior > Alpha (bloque superior)* | Intermediate | La gestión del alpha como archivo. Para importar, lo normal es un PNG o un TIFF en escala de grises, y en 16 bits si lo tienes, porque con 8 bits salen escalones en el relieve. |
| 📂 | **Import** | *Menú superior > Alpha (bloque superior)* | Intermediate | Carga un alpha desde un archivo de imagen. |
| 💾 | **Export** | *Menú superior > Alpha (bloque superior)* | Intermediate | Guarda el alpha activo como imagen, en su versión original. |
| 📤 | **Ep** | *Menú superior > Alpha (bloque superior)* | Advanced | Su nota emergente dice 'Export Processed Alpha': exporta el alpha CON los retoques de Modify ya aplicados. La diferencia importa si has tocado MidValue, Contrast o los tiles y quieres el resultado tal y como lo ves en la miniatura. |
| 🗂️ | **Lightbox ▶ Alphas** | *Menú superior > Alpha (bloque superior)* | Intermediate | Abre la biblioteca de alphas que trae ZBrush de fábrica. |
| 🔢 | **Alpha > el deslizador del alpha activo y el botón R** | *Menú superior > Alpha (bloque superior)* | Intermediate | El deslizador que hay debajo de los botones muestra el ALPHA ACTIVO y su número dentro de la lista ('Alpha 01. 1'). Arrastrándolo se recorren los alphas cargados sin abrir la cuadrícula de miniaturas, y además regula cuántas miniaturas se ven en el bloque de acceso rápido. |
| ↩️ | **R** | *Menú superior > Alpha (bloque superior)* | Intermediate | Su nota emergente dice 'Restore Configuration': devuelve el número de elementos visibles a la configuración por defecto, o sea que deshace de un clic cualquier lío que hayas montado con el deslizador. Es el mismo botón R que aparece en Brush y en Tool. |
| 🖼️ | **Alpha > las miniaturas: el alpha activo y el inventario (Alpha 01, Alpha 28, Alpha 58...)** | *Menú superior > Alpha (bloque superior)* | Basic | El recuadro grande de la izquierda es el ALPHA ACTIVO (en tu captura, Alpha Off: ninguno). Pulsando sobre él se abre la rejilla con todos los alphas cargados en la sesión, y a su lado se ven los primeros como acceso rápido: Alpha 01 es la mancha suave clásica, Alpha 28 el cuadrado duro y Alpha 58 el círculo duro. Esos tres son los más socorridos: Alpha 01 para detalle blando, y el cuadrado y el círculo para estampar formas limpias con el trazo DragRect. Los alphas se pierden al cerrar el programa salvo que los guardes. |
| 🔃 | **Alpha > voltear, girar e invertir el alpha activo** | *Menú superior > Alpha (bloque superior)* | Basic | Cuatro transformaciones rápidas que se aplican al alpha en sí, no al modelo. |
| ↔️ | **Flip H** | *Menú superior > Alpha (bloque superior)* | Basic | Voltea el alpha en horizontal. Es lo que se usa para tener la versión izquierda y derecha de un mismo detalle (una cicatriz, una oreja) sin cargar dos archivos. |
| ↕️ | **Flip V** | *Menú superior > Alpha (bloque superior)* | Basic | Voltea el alpha en vertical. |
| 🔄 | **Rotate** | *Menú superior > Alpha (bloque superior)* | Basic | Gira el alpha 90 grados cada vez que lo pulsas. |
| 🔀 | **Inverse** | *Menú superior > Alpha (bloque superior)* | Basic | Invierte los grises, y ése es el importante: con él, un alpha que HUNDE pasa a SOBRESALIR o al revés. Si un sello te sale metido hacia dentro cuando lo querías hacia fuera, prueba esto antes de tocar nada más. |
| 🧊 | **Alpha > el puente rápido entre alpha y geometría** | *Menú superior > Alpha (bloque superior)* | Advanced | La conversión directa entre alpha y malla. En tu captura salen en gris porque no hay ningún alpha activo. Para la conversión a 3D con más control está la sub-paleta Make 3D, un poco más abajo. |
| 🧊 | **To Mesh** | *Menú superior > Alpha (bloque superior)* | Advanced | Convierte el alpha en una malla 3D usando los grises como altura. |
| ▭ | **Flat** | *Menú superior > Alpha (bloque superior)* | Advanced | Hace que esa malla salga con la parte de atrás plana en vez de abombada. |
| 🅰️ | **From Mesh** | *Menú superior > Alpha (bloque superior)* | Advanced | El camino contrario: genera un alpha a partir de la profundidad de la malla que tengas. |
| 🖌️ | **Alpha > From Brush y From IMM: fabricar un alpha con lo que ya tienes** | *Menú superior > Alpha (bloque superior)* | Advanced | Dos generadores de alphas a partir de cosas que ya tienes. Son un atajo estupendo: si ya has modelado un remache o un botón, puedes convertirlo en sello y repetirlo por todas partes sin gastar geometría. Ambos bloques salen en gris en tu captura. |
| 🖌️ | **From Brush** | *Menú superior > Alpha (bloque superior)* | Advanced | Fabrica un alpha con la forma del pincel activo. |
| 📏 | **Alpha Width** | *Menú superior > Alpha (bloque superior)* | Advanced | El tamaño de la imagen resultante de From Brush. |
| 🌫️ | **Blur Seam** | *Menú superior > Alpha (bloque superior)* | Advanced | Difumina el borde para que no se note el corte al estampar. |
| 🧩 | **From IMM** | *Menú superior > Alpha (bloque superior)* | Advanced | Hace lo mismo con las mallas de un pincel Insert Multi-Mesh. |
| ☝️ | **One Item** | *Menú superior > Alpha (bloque superior)* | Advanced | Convierte solo la pieza seleccionada del IMM en vez de todas. |
| 🔬 | **Size** | *Menú superior > Alpha (bloque superior)* | Advanced | Fija la resolución del alpha generado desde el IMM. |


## Alpha > BasRelief


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🗿 | **Alpha > BasRelief: los ajustes del bajorrelieve** | *Menú superior > Alpha > BasRelief* | Advanced | BASRELIEF convierte una imagen en un BAJORRELIEVE: aplasta el rango de alturas para que el detalle quepa en muy poco grosor, como una moneda o una placa tallada. Es lo que necesitas cuando estampas una foto o un dibujo sobre una superficie y te sale una montaña deforme en vez de un relieve. |
| 🔁 | **Relief Repeat Count** | *Menú superior > Alpha > BasRelief* | Advanced | Las pasadas del cálculo (1000 en tu captura). Más pasadas, resultado más fino y más lento. |
| ◐ | **Relief Contrast** | *Menú superior > Alpha > BasRelief* | Advanced | Cuánto se diferencian las alturas entre sí (0). |
| 📶 | **Relief Step Tolerance** | *Menú superior > Alpha > BasRelief* | Advanced | Cuánto salto tolera entre dos valores vecinos antes de suavizarlo (0.2), o sea lo que evita los escalones. |
| 🌫️ | **Relief Blur Radius** | *Menú superior > Alpha > BasRelief* | Advanced | Difumina el resultado final (4). |
| 🖼️ | **Alpha > BasRelief: calcular, aplicar y recoger el resultado** | *Menú superior > Alpha > BasRelief* | Advanced | Los tres botones que ejecutan el bajorrelieve una vez ajustados los deslizadores de arriba. El orden de trabajo es ese: ajustas, Make para ver cómo queda, y Apply cuando te convence. |
| ⚙️ | **Make BasRelief** | *Menú superior > Alpha > BasRelief* | Advanced | CALCULA el bajorrelieve con los valores que tengas puestos. |
| ✅ | **Apply BasRelief** | *Menú superior > Alpha > BasRelief* | Advanced | Lo APLICA al alpha activo, sustituyéndolo por la versión aplanada. |
| 🖼️ | **BTxtr** | *Menú superior > Alpha > BasRelief* | Advanced | Su nota emergente dice 'Grab BasRelief Texture': recoge el bajorrelieve resultante como TEXTURA, para poder usarlo como imagen de color además de como alpha de relieve. |


## Alpha > Modify


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🪵 | **Alpha > Modify: el generador de vetas y estrías** | *Menú superior > Alpha > Modify* | Advanced | MODIFY es el laboratorio de la paleta: retoca el alpha activo sin salir de ZBrush ni pasar por Photoshop, y los cambios se ven al momento en la miniatura. Estos cinco deslizadores, confirmados con tus notas emergentes, estiran el alpha en tiras finas, lo que sirve para convertir una mancha en fibras, madera, pelo o rayado metálico. |
| 📏 | **Streak Length** | *Menú superior > Alpha > Modify* | Advanced | Lo largas que son las vetas (0). |
| 🔢 | **Streak Density** | *Menú superior > Alpha > Modify* | Advanced | Cuántas vetas hay (0.005). |
| 💡 | **Streak Intensity** | *Menú superior > Alpha > Modify* | Advanced | La intensidad de las vetas (1). |
| 💪 | **Streak Strength** | *Menú superior > Alpha > Modify* | Advanced | La fuerza de las vetas (50). |
| 📉 | **Streak Falloff** | *Menú superior > Alpha > Modify* | Advanced | Cómo se desvanecen hacia el final (0.5), que es lo que evita que terminen en un corte seco. |
| 🌫️ | **Alpha > Modify: el grupo de acabado** | *Menú superior > Alpha > Modify* | Advanced | Ruido, desenfoque y limpieza de bordes. Un poco de ruido es lo que evita que un sello se vea demasiado limpio y artificial. |
| 🌾 | **Noise** | *Menú superior > Alpha > Modify* | Advanced | Mete ruido en el alpha (0). |
| ⭕ | **NRadius** | *Menú superior > Alpha > Modify* | Advanced | El tamaño del grano de ese ruido (0). |
| 🌫️ | **Blur** | *Menú superior > Alpha > Modify* | Advanced | Difumina el alpha entero (0). Es el arreglo cuando un sello deja un escalón feo en el borde al estampar. |
| 📊 | **Max** | *Menú superior > Alpha > Modify* | Advanced | Su nota emergente dice 'Maximize Range': estira el rango de grises hasta ocupar de negro puro a blanco puro, lo que le da al alpha todo su relieve disponible. Por eso viene activado de serie. |
| ✨ | **Aa** | *Menú superior > Alpha > Modify* | Advanced | Su nota emergente dice 'Antialiased Alpha': suaviza los dientes de sierra del borde. Con alphas hechos a partir de fotos o de capturas de pantalla se nota bastante. |
| 🧱 | **Alpha > Modify: la repetición en mosaico** | *Menú superior > Alpha > Modify* | Advanced | El grupo de REPETICIÓN, que es lo que convierte un motivo suelto en un patrón: escamas, ladrillos o tejidos. |
| ↔️ | **H Tiles** | *Menú superior > Alpha > Modify* | Advanced | Repite el alpha en horizontal (1). Subiéndolo, un solo motivo cubre toda la zona de un trazo. |
| ↕️ | **V Tiles** | *Menú superior > Alpha > Modify* | Advanced | Repite el alpha en vertical (1). |
| 🧵 | **Seamless** | *Menú superior > Alpha > Modify* | Advanced | Trabaja los bordes para que esa repetición no cante (0), eliminando la línea que se ve donde una copia se junta con la siguiente. |
| ⭕ | **Rf** | *Menú superior > Alpha > Modify* | Advanced | Su nota emergente dice 'Radial Fade': un desvanecido circular desde el centro hacia el borde, que es justo lo que hace falta para que un sello cuadrado no deje las esquinas marcadas al estampar. |
| 🎚️ | **Alpha > Modify: cómo se traducen los grises en altura** | *Menú superior > Alpha > Modify* | Advanced | El grupo que decide cómo se traducen los grises en altura, y donde está el control más importante de toda la paleta. |
| ⚖️ | **MidValue** | *Menú superior > Alpha > Modify* | Advanced | Fija qué gris cuenta como 'ALTURA CERO' (0): todo lo más claro que ese valor sobresale y todo lo más oscuro se hunde. Si lo dejas mal, un alpha que debería hundir una grieta acaba levantando un bulto alrededor — es la causa número uno de que un sello 'no haga lo que debería'. |
| 💡 | **Intensity** | *Menú superior > Alpha > Modify* | Advanced | La fuerza general del alpha (0). |
| ◐ | **Contrast** | *Menú superior > Alpha > Modify* | Advanced | Exagera la diferencia entre claros y oscuros (1). |
| 📈 | **AlphaAdjust** | *Menú superior > Alpha > Modify* | Advanced | Una CURVA para remapear los grises a mano, cuando ni MidValue ni Contrast te dan lo que buscas. |
| 🪨 | **Surface** | *Menú superior > Alpha > Modify* | Advanced | Su nota emergente dice 'Surface Details Mode': hace que el alpha se trate como detalle de superficie (relieve fino sobre lo que ya hay) en lugar de como una forma maciza. |


## Alpha > Create


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ✨ | **Alpha > Create: fabricar un alpha desde cero** | *Menú superior > Alpha > Create* | Advanced | Genera un alpha NUEVO. Es la forma de hacerte texturas de piel, roca o metal picado sin salir del programa ni buscar imágenes por internet. |
| ↔️ | **Width** | *Menú superior > Alpha > Create* | Advanced | El ancho en píxeles de la imagen que se va a generar (256). Para detalle fino conviene subirlo a 1024 o 2048, teniendo en cuenta que ocupa y tarda más. |
| ↕️ | **Height** | *Menú superior > Alpha > Create* | Advanced | El alto en píxeles (256). |
| 🌾 | **Create From NoiseMaker** | *Menú superior > Alpha > Create* | Advanced | Genera el alpha con el editor de ruido procedural de ZBrush, el mismo NoiseMaker que usa Tool > Surface: eliges un patrón, lo ajustas con sus curvas y sale un alpha listo para estampar. |


## Alpha > Make 3D


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧱 | **Alpha > Make 3D: convertir el alpha en malla con control** | *Menú superior > Alpha > Make 3D* | Advanced | Convierte el alpha activo en una MALLA 3D de verdad, con los grises como relieve. El bloque entero está confirmado con tus notas emergentes. Sirve para pasar un logo o un motivo plano a geometría de golpe y pegarlo al modelo como SubTool. |
| 🔺 | **MRes** | *Menú superior > Alpha > Make 3D* | Advanced | Su nota emergente dice 'Mesh Resolution' (64): cuántos polígonos tendrá la malla. Más resolución, más detalle y más peso. |
| 📏 | **MDep** | *Menú superior > Alpha > Make 3D* | Advanced | Su nota emergente dice 'Mesh Depth Resolution' (25): cuánto sobresale el relieve. |
| 〰️ | **MSm** | *Menú superior > Alpha > Make 3D* | Advanced | Su nota emergente dice 'Mesh Smooth' (10): cuánto se suaviza la malla para que el relieve no salga con escalones heredados de los píxeles. |
| 🪞 | **DblS** | *Menú superior > Alpha > Make 3D* | Advanced | Su nota emergente dice 'Double Sided'. Activo en tu captura: genera la malla a doble cara. |
| 🧊 | **Make 3D** | *Menú superior > Alpha > Make 3D* | Advanced | Su nota emergente dice 'Make 3D Mesh': crea la malla y la mete en el inventario de herramientas. |


## Alpha > Transfer


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🔀 | **Alpha > Transfer: pasar el alpha a otros formatos del programa** | *Menú superior > Alpha > Transfer* | Advanced | Convierte el alpha en textura, en stencil o en captura del lienzo. GrabDoc es el más útil de todos y es como se hacen los alphas propios. |
| 🖼️ | **Make Tx** | *Menú superior > Alpha > Transfer* | Advanced | Convierte el alpha en TEXTURA y lo manda a la paleta Texture. |
| 📄 | **Make St** | *Menú superior > Alpha > Transfer* | Advanced | Lo convierte en STENCIL, la plantilla que se queda flotando sobre el modelo y a través de la cual se esculpe. |
| 💾 | **Make Modified Alpha** | *Menú superior > Alpha > Transfer* | Advanced | Guarda como alpha NUEVO el resultado de los retoques que hayas hecho en Modify, en vez de machacar el original. Acuérdate de este botón antes de trastear. |
| ✂️ | **CropAndFill** | *Menú superior > Alpha > Transfer* | Advanced | Recorta el documento y lo rellena con el alpha. |
| 📸 | **GrabDoc** | *Menú superior > Alpha > Transfer* | Advanced | Captura la PROFUNDIDAD de lo que se ve en el lienzo y la convierte en un alpha: pones tu modelo en una pose, pulsas GrabDoc y ya tienes un sello con su forma exacta. |
| 📏 | **Alpha Depth Factor** | *Menú superior > Alpha > Transfer* | Advanced | Cuánta profundidad se recoge en esa captura (0). |

