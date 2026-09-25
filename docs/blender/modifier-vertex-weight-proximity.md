# Modifier: Vertex Weight Proximity


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Vertex Group / Target Object / Proximity Mode** | *Dentro del modificador* | Basic | Genera automáticamente los pesos de un Vertex Group según lo cerca o lejos que esté cada vértice de un Target Object. Proximity Mode (Object) mide la distancia al ORIGEN de ese objeto; otras opciones miden a su geometría (vértice, arista o cara más cercana) en vez de a un único punto. |
| - | **Lowest / Highest / Normalize Weights** | *Dentro del modificador* | Intermediate | Lowest (0 m) y Highest (1 m) definen el rango de distancias que se mapea a peso 0 y peso 1 respectivamente: los vértices más cerca que Lowest quedan a 0, los más lejos que Highest a 1, y los intermedios se interpolan. Normalize Weights reparte el resultado para no superar el máximo entre grupos. |
| ✨ | **Falloff / Influence: Global Influence / Mask Vertex Group / Mask Texture** | *Dentro del modificador > Falloff / Influence* | Advanced | Mismos paneles Falloff e Influence ya documentados en Vertex Weight Edit: Falloff remapea la curva de 0 a 1 antes de aplicarla; Influence (Global Influence/Mask Vertex Group/Mask Texture) controla la fuerza y dónde se limita el efecto. |

