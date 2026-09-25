# ZScript


## Zscript


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📜 | **Zscript: qué es la paleta** | *Menú superior > Zscript* | Advanced | ZSCRIPT es el lenguaje de macros propio de ZBrush, y esta paleta es donde se cargan, se graban y se ejecutan esos scripts. No es un lenguaje de programación general como Python: es una lista de ÓRDENES que reproducen lo que harías tú con el ratón, así que sirve para automatizar tareas repetitivas — aplicar la misma secuencia de deformaciones a veinte SubTools, preparar un modelo para exportar siempre igual, montar un botón propio en la interfaz. Casi todos los complementos de Zplugin están escritos en ZScript, que es lo que explica por qué se pueden instalar copiando un archivo en una carpeta. Ojo con no confundir esta paleta con la pestaña ZScript de tu propio Excel: aquella es para tus apuntes de código, esta es la paleta del programa. |
| 📂 | **Zscript > cargar y recargar el script** | *Menú superior > Zscript (bloque de arriba)* | Advanced | La gestión del script cargado. |
| 📂 | **Load** | *Menú superior > Zscript (bloque de arriba)* | Advanced | Abre un archivo de ZScript desde el disco. |
| 🔄 | **Reload** | *Menú superior > Zscript (bloque de arriba)* | Advanced | Lo vuelve a cargar para recoger los cambios si lo has estado editando en un editor de texto por fuera. Es el botón que más se pulsa mientras se escribe uno. |
| ◀️ | **Previous** | *Menú superior > Zscript (bloque de arriba)* | Advanced | Pasa al script anterior de los que has usado. |
| ▶️ | **Next** | *Menú superior > Zscript (bloque de arriba)* | Advanced | Pasa al script siguiente. |
| 🙈 | **Hide Zscript** | *Menú superior > Zscript (bloque de arriba)* | Advanced | Esconde la ventana del script, que normalmente se coloca en la parte baja de la pantalla y ocupa sitio. Si un complemento te ha dejado una franja abajo que no sabes cómo quitar, este es el botón. |
| ▶️ | **Zscript > cómo se reproduce un script** | *Menú superior > Zscript* | Advanced | Pensado sobre todo para los tutoriales interactivos que ZBrush trae en formato ZScript. |
| 👁️ | **Show Actions** | *Menú superior > Zscript* | Advanced | Muestra las acciones que va ejecutando. En gris en tu captura. |
| 📝 | **&Notes** | *Menú superior > Zscript* | Advanced | Muestra las notas explicativas que acompañan a esas acciones: eso es lo que hace que un tutorial en ZScript vaya señalando los botones y contándote qué hace en cada paso. En gris en tu captura. |
| ⏭️ | **Skip Notes** | *Menú superior > Zscript* | Advanced | Se salta esas notas, para cuando ya te sabes el tutorial. |
| 🔇 | **Skip Audio** | *Menú superior > Zscript* | Advanced | Se salta el audio. |
| ⏱️ | **Store ZTime** | *Menú superior > Zscript* | Advanced | Guarda una marca de tiempo, que se usa dentro de los scripts para medir cuánto tarda una operación. |
| ⏺️ | **Zscript > grabar un script sin escribir una línea** | *Menú superior > Zscript* | Advanced | La forma realista de empezar. El flujo para automatizar algo sin saber programar: pulsas Record, haces una vez la tarea a mano, pulsas End Rec, y a partir de ahí Run la repite las veces que quieras. |
| ⏺️ | **Record** | *Menú superior > Zscript* | Advanced | Empieza a grabar todo lo que hagas en el programa. |
| ⏹️ | **End Rec** | *Menú superior > Zscript* | Advanced | Detiene la grabación. En gris hasta que estás grabando. |
| ⌨️ | **Cmd** | *Menú superior > Zscript* | Advanced | El modo de ventana que muestra los comandos. |
| 🔴 | **Rec** | *Menú superior > Zscript* | Advanced | El modo de grabación. En gris en tu captura. |
| 📄 | **Txt** | *Menú superior > Zscript* | Advanced | El modo que muestra el texto del script. |
| ▶️ | **Run** | *Menú superior > Zscript* | Advanced | EJECUTA el script. Activo en naranja en tu captura. |
| ⏱️ | **Zscript > la velocidad de la reproducción** | *Menú superior > Zscript* | Advanced | Subir Replay Delay es justo lo que quieres cuando estás depurando un script tuyo y algo falla. |
| 🔁 | **Repeat Show Actions** | *Menú superior > Zscript* | Advanced | Cuántas veces se repite la demostración de cada acción (1), para que dé tiempo a verla en un tutorial. |
| ⏳ | **Replay Delay** | *Menú superior > Zscript* | Advanced | La pausa entre una acción y la siguiente (0). Subirlo hace que el script se ejecute despacio y puedas seguir lo que va haciendo. |
| ⚡ | **Zscript > acelerar la ejecución y sacar la documentación** | *Menú superior > Zscript* | Advanced | Los dos modos mínimos aceleran mucho a cambio de no ver bien lo que pasa. |
| ✏️ | **Minimal Stroke** | *Menú superior > Zscript* | Advanced | Dibuja el mínimo trazo mientras se reproduce. |
| 🖥️ | **Minimal Update** | *Menú superior > Zscript* | Advanced | Refresca la pantalla lo mínimo mientras se reproduce. |
| 📋 | **Export Commands** | *Menú superior > Zscript* | Advanced | Saca la lista completa de comandos disponibles de ZScript a un archivo, que es la documentación de referencia para escribir uno. Si algún día te animas con esto, ese archivo es por donde se empieza. |

