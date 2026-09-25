# Spreadsheet > Table


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📋 | **Estructura de la tabla: columna de índice + una columna por atributo** | *Zona central del Spreadsheet* | Advanced | A la izquierda del todo, sin cabecera, va el ÍNDICE de cada elemento empezando en 0 (0-7 para los 8 vértices del cubo); es el mismo número que usan los nodos que trabajan por índice. Después, una columna por atributo, con su nombre en la cabecera: en la captura 'position' (que al ser un vector se subdivide en 3 subcolumnas, X/Y/Z, con los valores ±1.000 propios del cubo por defecto) y '.select_vert' (booleano, mostrado como casillas marcadas). Cada tipo de dato se dibuja distinto: los números como cifras con decimales, los booleanos como casillas. A medida que el árbol de Geometry Nodes cree atributos nuevos, irán apareciendo aquí como columnas adicionales. |
| 🔢 | **Contador Rows / Columns** | *Esquina inferior derecha del Spreadsheet* | Basic | Resumen permanente de lo que se está mostrando: cuántas filas (elementos del dominio activo) y cuántas columnas (atributos) hay en la tabla ahora mismo — en la captura 'Rows: 8 \| Columns: 2'. Es la forma más rápida de comprobar de un vistazo cuánta geometría está generando un árbol de nodos, y si un filtro está recortando filas. |

