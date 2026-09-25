# Dynamics


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⚙️ | **Dynamics: qué es y para qué sirve** | *Menú superior > Dynamics* | Advanced | La paleta de SIMULACIÓN FÍSICA, y una de las más modernas del programa. Aplica gravedad y colisiones a la malla para que caiga, se pliegue y se apoye sola, en vez de esculpir los pliegues a mano. Su uso estrella es la ROPA: modelas una capa o una falda como un plano o un cilindro sencillo, la sueltas sobre el personaje y la simulación hace los pliegues realistas en segundos. También sirve para inflar formas, asentar una pieza contra otra o dar sensación de peso. |
| ▶️ | **Dynamics: el flujo de trabajo y con qué se combina** | *Menú superior > Dynamics* | Advanced | EL FLUJO es: tener una malla con densidad suficiente (una malla de pocos polígonos no se pliega bien, así que conviene subdividir o usar DynaMesh antes), ajustar aquí las opciones y pulsar Run Simulation. Se combina muy bien con los pinceles de la familia Cloth, que simulan mientras pintas. Para un personaje de videojuego es la forma más rápida de conseguir ropa creíble sin ser experta en telas. |
| 🔁 | **Dynamics > los tres controles base de la simulación** | *Menú superior > Dynamics* | Advanced | Entre Firmness e Iterations está casi todo el carácter del resultado. Si la tela se queda a medias, aún tiesa, lo primero es subir las iteraciones. |
| 🔁 | **Simulation Iterations** | *Menú superior > Dynamics* | Advanced | Las pasadas de cálculo (100 en tu captura). Cuantas más, más se asienta la tela y más creíbles quedan los pliegues, pero más tarda. |
| 💪 | **Strength** | *Menú superior > Dynamics* | Advanced | La fuerza con la que actúa la simulación (1). |
| 🧱 | **Firmness** | *Menú superior > Dynamics* | Advanced | La FIRMEZA del material (2). Valores bajos dan una tela blanda y fluida con muchos pliegues pequeños; valores altos, una tela rígida tipo cuero o lona, con pliegues grandes y marcados. |
| 🎭 | **Dynamics > dónde se aplica la simulación** | *Menú superior > Dynamics* | Advanced | Permite simular a mano y por partes en vez de todo el objeto de golpe: muy útil para arreglar un pliegue concreto sin rehacer la tela entera. |
| 🎭 | **On Masked** | *Menú superior > Dynamics* | Advanced | Limita la simulación a la zona ENMASCARADA. |
| 🖌️ | **On Brushed** | *Menú superior > Dynamics* | Advanced | Activo en naranja en tu captura. La limita solo a la zona por la que vas pasando el pincel. |
| 🌫️ | **Fade Border** | *Menú superior > Dynamics* | Advanced | Difumina el borde de esa zona (6) para que la parte simulada se funda con la que no se ha tocado, en lugar de dejar un escalón brusco. |
| 💥 | **Dynamics > las reglas de choque y de estiramiento** | *Menú superior > Dynamics* | Advanced | Para ropa suele interesar dejar Allow Shrink y Allow Expand apagados, para que no se deforme la talla de la prenda. |
| 🔀 | **Self Collision** | *Menú superior > Dynamics* | Advanced | Evita que la malla se atraviese a sí misma (0), que es lo que pasa cuando una tela se dobla mucho y una capa se mete dentro de otra. Subirlo cuesta cálculo pero arregla los pliegues que se comen entre sí. |
| 🪟 | **Floor Collision** | *Menú superior > Dynamics* | Advanced | Activo en naranja en tu captura. Hace que la tela choque contra el suelo y se apoye en él en vez de atravesarlo: es lo que permite que una capa quede amontonada de forma creíble. |
| 📉 | **Allow Shrink** | *Menú superior > Dynamics* | Advanced | Permite que la superficie se ENCOJA durante la simulación. |
| 📈 | **Allow Expand** | *Menú superior > Dynamics* | Advanced | Permite que la superficie se ESTIRE y dé de sí. |
| 🌍 | **Dynamics > la gravedad y su dirección** | *Menú superior > Dynamics* | Advanced | El motor de la simulación. Set Direction es el truco socorrido para poses heroicas. |
| 🌍 | **Gravity** | *Menú superior > Dynamics* | Advanced | Activo en naranja en tu captura. El modo normal: la malla cae hacia abajo. |
| ⬇️ | **Gravity Strength** | *Menú superior > Dynamics* | Advanced | La fuerza de esa caída (10). Subirlo hace que la tela se desplome más rápido y se pegue más al cuerpo. |
| 🧭 | **Set Direction** | *Menú superior > Dynamics* | Advanced | Fija la DIRECCIÓN de la gravedad, que no tiene por qué ser hacia abajo: apuntándola de lado se consigue el efecto de una capa ondeando al viento. |
| 💧 | **Dynamics > Liquify: la gravedad líquida** | *Menú superior > Dynamics* | Advanced | El modo alternativo a Gravity. Su nota emergente confirma el nombre pero no detalla más, así que el matiz exacto de su comportamiento se ve mejor probándolo con Gravity Strength bajo. |
| 💧 | **Liquify** | *Menú superior > Dynamics* | Advanced | Su nota emergente dice 'Gravity Liquify': la variante LÍQUIDA de la gravedad. En vez de caer manteniendo su forma como una tela, la superficie fluye y se derrama. Sirve para efectos de cera, barro o materia derritiéndose. |
| 🎈 | **Dynamics > las cuatro fuerzas y sus cantidades** | *Menú superior > Dynamics* | Advanced | Cuatro fuerzas que se suman a la simulación, cada una con su botón interruptor, su deslizador de cantidad y sus tres letras X, Y y Z para elegir en qué EJES actúa. Combinadas con la gravedad son las que hacen que una tela no quede pegada al cuerpo como pintada, sino con aire dentro. Cada fuerza tiene su propio valor en la columna Paleta porque las tres letras se repiten en las cuatro. En tu captura los deslizadores salen en gris porque los botones no están activados. |
| 🔘 | **Dynamics > las cuatro fuerzas: cómo se activan y por qué salen en gris** | *Menú superior > Dynamics* | Advanced | Combinadas con la gravedad son las que hacen que una tela no quede pegada al cuerpo como pintada, sino con aire dentro. En tu captura los deslizadores salen en gris porque los botones no están activados. Confirmado con tu nota emergente: el botón Inflate es 'INFLATE ON', o sea que es el interruptor que enciende esa fuerza; los cuatro funcionan igual, se activa el botón y se regula con su deslizador de cantidad. |
| ▶️ | **Dynamics > lanzar la simulación** | *Menú superior > Dynamics* | Advanced | Consejo práctico: guarda antes de simular, porque una simulación mal ajustada puede dejar la malla hecha un nudo y no siempre se arregla deshaciendo. |
| ▶️ | **Run Simulation** | *Menú superior > Dynamics* | Advanced | Pone todo en marcha: la malla empieza a caer y a plegarse con los ajustes de arriba. Se puede pulsar varias veces seguidas para que la tela siga asentándose un poco más en cada pasada, que suele dar mejor resultado que subir muchísimo las iteraciones de golpe. |
| 🔢 | **Max Simulation Points** | *Menú superior > Dynamics* | Advanced | Limita cuántos puntos de la malla se simulan a la vez (250). Es un tope de rendimiento: si tu ordenador se atasca con una tela muy densa, bajarlo lo hace manejable a costa de precisión. |


## Dynamics > Inflate


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎈 | **Inflate** | *Menú superior > Dynamics* | Advanced | Su nota emergente dice 'Inflate On': el interruptor de la fuerza que hincha la malla hacia fuera siguiendo sus normales, como si le metieras aire. Es lo que da volumen a una manga o a un cojín. |
| 🔢 | **I Amount** | *Menú superior > Dynamics* | Advanced | La cantidad de la fuerza Inflate. |
| ✚ | **X** | *Menú superior > Dynamics* | Advanced | El eje X de la fuerza Inflate: con él activo, la fuerza hace que la malla se hinche también en la dirección X. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Y** | *Menú superior > Dynamics* | Advanced | El eje Y de la fuerza Inflate: con él activo, la fuerza hace que la malla se hinche también en la dirección Y. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Z** | *Menú superior > Dynamics* | Advanced | El eje Z de la fuerza Inflate: con él activo, la fuerza hace que la malla se hinche también en la dirección Z. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |


## Dynamics > Deflate


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🫧 | **Deflate** | *Menú superior > Dynamics* | Advanced | La fuerza contraria: vacía la malla. |
| 🔢 | **D Amount** | *Menú superior > Dynamics* | Advanced | La cantidad de la fuerza Deflate. |
| ✚ | **X** | *Menú superior > Dynamics* | Advanced | El eje X de la fuerza Deflate: con él activo, la fuerza hace que la malla se vacíe también en la dirección X. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Y** | *Menú superior > Dynamics* | Advanced | El eje Y de la fuerza Deflate: con él activo, la fuerza hace que la malla se vacíe también en la dirección Y. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Z** | *Menú superior > Dynamics* | Advanced | El eje Z de la fuerza Deflate: con él activo, la fuerza hace que la malla se vacíe también en la dirección Z. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |


## Dynamics > Expand


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ↔️ | **Expand** | *Menú superior > Dynamics* | Advanced | Agranda la malla. A diferencia de inflar, trabaja sobre el tamaño general y no sobre el grosor. |
| 🔢 | **E Amount** | *Menú superior > Dynamics* | Advanced | La cantidad de la fuerza Expand. |
| ✚ | **X** | *Menú superior > Dynamics* | Advanced | El eje X de la fuerza Expand: con él activo, la fuerza hace que la malla se agrande también en la dirección X. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Y** | *Menú superior > Dynamics* | Advanced | El eje Y de la fuerza Expand: con él activo, la fuerza hace que la malla se agrande también en la dirección Y. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Z** | *Menú superior > Dynamics* | Advanced | El eje Z de la fuerza Expand: con él activo, la fuerza hace que la malla se agrande también en la dirección Z. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |


## Dynamics > Contract


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ↕️ | **Contract** | *Menú superior > Dynamics* | Advanced | Encoge la malla. |
| 🔢 | **C Amount** | *Menú superior > Dynamics* | Advanced | La cantidad de la fuerza Contract. |
| ✚ | **X** | *Menú superior > Dynamics* | Advanced | El eje X de la fuerza Contract: con él activo, la fuerza hace que la malla encoja también en la dirección X. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Y** | *Menú superior > Dynamics* | Advanced | El eje Y de la fuerza Contract: con él activo, la fuerza hace que la malla encoja también en la dirección Y. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |
| ✚ | **Z** | *Menú superior > Dynamics* | Advanced | El eje Z de la fuerza Contract: con él activo, la fuerza hace que la malla encoja también en la dirección Z. Las tres letras se combinan, así que dejando solo una activa la deformación va en un único eje —útil para que una manga se hinche a lo ancho pero no a lo largo— y con las tres actúa en todas las direcciones. |


## Dynamics > CollisionVolum


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🧱 | **Dynamics > CollisionVolum: contra qué choca la tela** | *Menú superior > Dynamics* | Advanced | El VOLUMEN DE COLISIÓN es la forma simplificada que usa el programa para calcular contra qué choca la tela: en vez de comprobar millones de polígonos, ZBrush genera una versión de baja resolución del cuerpo y simula contra ella, que es lo que hace que la simulación vaya fluida. |
| 🧱 | **CollisionVolum** | *Menú superior > Dynamics* | Advanced | El botón que genera ese volumen. |
| 🔬 | **Resolution** | *Menú superior > Dynamics* | Advanced | Lo detallado que se genera (204 en tu captura): bajo va rápido pero se pierde el detalle de la anatomía y la ropa flota; alto se ajusta mejor y tarda más. |
| 🔄 | **Recalc** | *Menú superior > Dynamics* | Advanced | Lo vuelve a calcular. Hay que pulsarlo cada vez que cambies el cuerpo de debajo, o la tela seguirá chocando contra la forma antigua. Sale en gris hasta que hay volumen que recalcular. |
| 🎈 | **Dynamics > CollisionVolum: la holgura entre cuerpo y tela** | *Menú superior > Dynamics* | Advanced | Es el ajuste al que hay que recurrir cuando la tela se mete dentro del personaje por algún sitio. Ojo con no confundirlo con el Inflate de las fuerzas de la simulación: este actúa sobre el volumen de colisión, no sobre la malla. Por eso van en Paletas distintas. |
| 🎈 | **Inflate** | *Menú superior > Dynamics* | Advanced | Su nota emergente dice 'Collision Volume Inflate' (1): hincha el volumen de colisión respecto a la superficie real, dejando una holgura entre el cuerpo y la tela para que no se atraviesen. Subirlo separa más la ropa del cuerpo; bajarlo la pega. |

