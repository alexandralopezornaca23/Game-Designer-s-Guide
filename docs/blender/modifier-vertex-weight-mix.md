# Modifier: Vertex Weight Mix


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Vertex Group A / B / Default Weight A-B** | *Dentro del modificador* | Basic | Combina dos Vertex Groups (A y B) de la propia malla en uno solo (el de A, que se sobrescribe con el resultado). Default Weight A/B (0.000) es el peso a usar en los vértices que no pertenezcan todavía a cada grupo. |
| - | **Vertex Set / Mix Mode / Normalize Weights** | *Dentro del modificador* | Advanced | Vertex Set (VGroup A and B) decide sobre qué vértices actúa el resultado: solo los de A, solo los de B, la unión, o solo donde ambos se solapan. Mix Mode (Replace) decide cómo se combinan los dos valores de peso en esos vértices: sustituir, sumar, restar, multiplicar... Normalize Weights reparte el resultado para que no supere el máximo entre todos los grupos del vértice. |
| - | **Influence: Global Influence / Mask Vertex Group / Mask Texture** | *Dentro del modificador > Influence* | Advanced | Mismo panel Influence ya documentado en Vertex Weight Edit: Global Influence controla la fuerza total, Mask Vertex Group y Mask Texture limitan dónde se aplica el resultado según otro grupo o una textura. |

