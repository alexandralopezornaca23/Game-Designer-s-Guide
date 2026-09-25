# Visibility


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👁️ | **Ocultar geometría (aislar una zona)** | *Ctrl + Mayús + arrastrar* | Intermediate | Al arrastrar con Ctrl+Mayús aparece el pincel de selección (por defecto un rectángulo): lo que quede DENTRO se mantiene visible y todo lo demás se oculta. Sirve para trabajar cómodamente en una parte del modelo sin que el resto estorbe. |
| ⌨️ | **Ocultar geometría / aislar** | *Ctrl + Mayús + arrastrar* | Intermediate | Ocultar geometría / aislar |
| ⌨️ | **Mostrar toda la geometría** | <kbd>Ctrl</kbd> + <kbd>Mayús</kbd> + <kbd>clic en el fondo</kbd> | Intermediate | Mostrar toda la geometría |
| 🔄 | **Invertir la selección al ocultar** | *Ctrl + Mayús + arrastrar, y pulsar Alt durante el arrastre* | Intermediate | Si durante el arrastre pulsas Alt, se invierte el criterio: en vez de aislar lo seleccionado, lo OCULTA y deja visible el resto. Es la forma rápida de quitar de en medio justo la zona que molesta. |
| ⚠️ | **Ocultar no es borrar (pero cuidado)** | *Concepto general* | Intermediate | Ocultar solo afecta a lo que se ve y se puede editar; la geometría sigue ahí. PERO muchas operaciones actúan solo sobre lo visible, y eso es un arma de doble filo: DynaMesh, ZRemesher o Delete Hidden trabajan con lo visible, así que ocultar mal antes de una de esas operaciones puede destruir parte del modelo. Comprueba siempre con Ctrl+Mayús+clic en el fondo que lo tienes todo visible antes de remallar. |

