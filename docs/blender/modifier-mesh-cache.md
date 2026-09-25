# Modifier: Mesh Cache


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Format / File Path / Influence** | *Dentro del modificador* | Basic | Format (MDD): el formato del archivo de caché externo a importar — MDD o PC2, dos formatos clásicos de animación de malla por vértice. File Path: ruta al archivo en disco. Influence (1.000): cuánto se aplica la deformación importada, de 0 (ninguna) a 1 (completa). |
| - | **Deform Mode / Interpolation / Vertex Group** | *Dentro del modificador* | Intermediate | Deform Mode (Overwrite): Overwrite sustituye la posición de los vértices por la del caché; Integrate la suma a la deformación que ya tuviera la malla por otros modifiers. Interpolation (Linear): cómo se interpola la posición entre un frame del caché y el siguiente. Vertex Group limita el efecto a una parte de la malla. |
| - | **Time Remapping: Frame / Time / Factor** | *Dentro del modificador > Time Remapping* | Advanced | 3 formas distintas de decidir qué frame del archivo de caché se muestra en cada frame de Blender: Frame (la pestaña activa) usa directamente el número de fotograma; Time lo hace por tiempo en segundos; Factor por una posición proporcional (0 a 1) dentro de la animación del caché. |
| - | **Time Remapping (Frame) > Play Mode / Frame Start / Frame Scale** | *Dentro del modificador > Time Remapping* | Advanced | Play Mode (Scene): Scene sincroniza el caché con el frame actual de la escena; Custom permite controlarlo de forma independiente. Frame Start desplaza en qué fotograma de la escena empieza a reproducirse el caché. Frame Scale (1.000) acelera o ralentiza su reproducción respecto a la escena. |
| - | **Axis Mapping: Forward / Up / Flip Axis** | *Dentro del modificador > Axis Mapping* | Advanced | Forward (+Y) y Up (+Z) indican a Blender qué ejes del archivo importado corresponden a 'adelante' y 'arriba', ya que otros programas usan convenciones de ejes distintas (por ejemplo Z-up frente a Y-up). Flip Axis (X/Y/Z) invierte manualmente uno o varios ejes si el resultado se importa reflejado o al revés. |

