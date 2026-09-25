# Shader Editor > Node


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 📄 | **Node: menú general** | *Barra superior del Shader Editor > Node* | Basic | Agrupa todos los comandos para manipular los nodos ya colocados: transformar (Move/Rotate/Resize), Cut/Copy/Paste/Duplicate/Delete, organización en Frames y Groups, gestión de los cables (Make Links/Cut Links/Mute Links), Swap (sustituir el tipo de nodo) y Show/Hide (plegar/mostrar sockets). |
| ↔️ | **Move / Rotate / Resize** | *Barra superior del Shader Editor > Node* | Basic | Transforman el/los nodo(s) seleccionados dentro del grafo: Move (G) los desplaza, Rotate (R) los rota sobre su propio centro, Resize (S) cambia su tamaño visual en el editor; funcionan igual que sus equivalentes de objetos en el Viewport 3D pero aplicados a la posición/tamaño de los nodos en el lienzo 2D del editor. |
| ⌨️ | **Move** | <kbd>G</kbd> | Basic | Move |
| ⌨️ | **Rotate** | <kbd>R</kbd> | Basic | Rotate |
| ⌨️ | **Resize** | <kbd>S</kbd> | Basic | Resize |
| 📋 | **Cut / Copy / Paste** | *Barra superior del Shader Editor > Node* | Basic | Cut corta (copia y borra) los nodos seleccionados. Copy los copia al portapapeles sin borrarlos. Paste pega los nodos copiados en la posición del cursor. En el menú no aparece ningún atajo de teclado junto a estos 3 comandos (a diferencia de Delete que sí usa X); se accede a ellos solo desde este menú o clic derecho. |
| ⌨️ | **Duplicate** | <kbd>Mayús</kbd> + <kbd>D</kbd> | Basic | Duplicate |
| ⌨️ | **Duplicate Linked** | <kbd>Alt</kbd> + <kbd>D</kbd> | Intermediate | Duplicate Linked |
| 🗑️ | **Delete / Delete with Reconnect** | *Barra superior del Shader Editor > Node* | Basic | Delete (X) borra los nodos seleccionados junto con sus cables. Delete with Reconnect (Ctrl+X) los borra pero intenta reconectar automáticamente la entrada y salida principal del nodo eliminado, para no dejar el cable cortado. |
| ⌨️ | **Delete** | <kbd>X</kbd> | Basic | Delete |
| ⌨️ | **Delete with Reconnect** | <kbd>Ctrl</kbd> + <kbd>X</kbd> | Basic | Delete with Reconnect |
| 🖼️ | **Join in New Frame / Remove from Frame / Join Group Inputs / Join in Named Frame** | *Barra superior del Shader Editor > Node* | Intermediate | Join in New Frame mete los nodos seleccionados dentro de un Frame nuevo. Remove from Frame (Alt+P) los saca del Frame que los contiene. Join Group Inputs (Ctrl+J) los conecta al nodo Group Input dentro de un Node Group. Join in Named Frame (F) pide el nombre de un Frame (nuevo o existente) y mete ahí los nodos. |
| ⌨️ | **Remove from Frame** | <kbd>Alt</kbd> + <kbd>P</kbd> | Intermediate | Remove from Frame |
| ⌨️ | **Join Group Inputs** | <kbd>Ctrl</kbd> + <kbd>J</kbd> | Intermediate | Join Group Inputs |
| ⌨️ | **Join in Named Frame** | <kbd>F</kbd> | Intermediate | Join in Named Frame |
| ✏️ | **Rename...** | <kbd>F2</kbd> | Basic | Rename... |
| 🔗 | **Make Links / Make and Replace Links** | *Barra superior del Shader Editor > Node* | Intermediate | Make Links (J) conecta la salida del nodo activo a la entrada equivalente de los demás nodos seleccionados. Make and Replace Links (Mayús+J) hace lo mismo pero sustituyendo cualquier cable que ya existiera en esas entradas en vez de dejarlo aparte. |
| ⌨️ | **Make Links** | <kbd>J</kbd> | Intermediate | Make Links |
| ⌨️ | **Make and Replace Links** | <kbd>Mayús</kbd> + <kbd>J</kbd> | Intermediate | Make and Replace Links |
| ✂️ | **Cut Links / Detach Links / Mute Links** | *Barra superior del Shader Editor > Node* | Intermediate | Cut Links (Ctrl+arrastrar con Botón Derecho) corta los cables por los que pase el trazo, igual que la herramienta Links Cut de la Barra T. Detach Links desconecta todos los cables del nodo seleccionado sin borrar el nodo. Mute Links (Ctrl+Alt+arrastrar con Botón Derecho) silencia los cables por los que pase el trazo, igual que la herramienta Mute Links de la Barra T. |
| 👥 | **Make Group / Insert Into Group / Edit Group / Ungroup** | *Barra superior del Shader Editor > Node* | Advanced | Make Group (Ctrl+G) convierte los nodos seleccionados en un Node Group nuevo, reutilizable. Insert Into Group los mete dentro de un Node Group ya existente. Edit Group (Tab) entra a editar el interior de un Node Group. Ungroup (Ctrl+Alt+G) deshace la agrupación, devolviendo los nodos sueltos al grafo principal. |
| 🔄 | **Swap** | *Barra superior del Shader Editor > Node > Swap* | Advanced | Sustituye el/los nodo(s) seleccionados por otro tipo, intentando conservar las conexiones que coincidan. Usa exactamente el mismo árbol de categorías que el menú Add (ver 'Shader Editor > Add'): Input/Output/Shader/Displacement/Color/Texture/Utilities/Group/Layout. |
| ⌨️ | **Swap** | <kbd>Mayús</kbd> + <kbd>S</kbd> | Advanced | Swap |
| 👁️ | **Show/Hide: Mute / Node Options / Unconnected Sockets / Collapse / Collapse and Hide Unused Sockets** | *Barra superior del Shader Editor > Node > Show/Hide* | Intermediate | Mute (M) silencia el nodo (lo salta, dejando pasar los datos como si no estuviera). Node Options muestra/oculta el bloque de opciones extra en la cabecera del nodo (como 'Show Options' en el panel N). Unconnected Sockets (Ctrl+H) muestra/oculta los sockets del nodo que no tienen ningún cable conectado. Collapse (H) pliega el nodo a solo su cabecera. Collapse and Hide Unused Sockets hace lo mismo que Collapse pero además oculta los sockets sin usar al volver a expandirlo. |
| ⌨️ | **Mute** | <kbd>M</kbd> | Intermediate | Mute |
| ⌨️ | **Unconnected Sockets** | <kbd>Ctrl</kbd> + <kbd>H</kbd> | Intermediate | Unconnected Sockets |
| ⌨️ | **Collapse** | <kbd>H</kbd> | Intermediate | Collapse |

