# Modifier: UV Warp


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **UV Map / UV Center / Axis U-V** | *Dentro del modificador* | Advanced | UV Map: el mapa UV que se va a deformar. UV Center (0.500, 0.500): el punto (en coordenadas UV de 0 a 1) alrededor del cual giran/escalan las UV. Axis U/V (X/Y): qué ejes 3D del From/To se usan para calcular el movimiento en cada eje de las UV. |
| - | **Object From / To / Vertex Group** | *Dentro del modificador* | Advanced | From y To son dos objetos (normalmente Empties): el modifier calcula la diferencia de transformación entre ambos y la aplica como desplazamiento a las UV, permitiendo animar una textura moviendo un Empty en vez de editar UVs a mano. Vertex Group limita el efecto a una parte de la malla. |
| - | **Transform: Offset / Scale / Rotation** | *Dentro del modificador > Transform* | Advanced | Valores manuales adicionales (además del From/To) para desplazar (Offset), escalar (Scale) o rotar (Rotation) las UV directamente desde el propio modifier, sin necesidad de un Empty. |

