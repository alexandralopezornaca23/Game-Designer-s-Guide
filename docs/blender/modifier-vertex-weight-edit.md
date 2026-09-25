# Modifier: Vertex Weight Edit


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Vertex Group / Default Weight** | *Dentro del modificador* | Basic | Vertex Group: el grupo cuyos pesos se van a remapear. Default Weight (0.000): el peso que se asigna a los vértices que NO pertenecen todavía a ese grupo, si acaban entrando en él por Group Add. |
| - | **Group Add / Group Remove / Normalize Weights** | *Dentro del modificador* | Advanced | Group Add (con Threshold 0.01): añade automáticamente al grupo los vértices cuyo peso resultante supere ese umbral. Group Remove (Threshold 0.01) saca del grupo a los que caigan por debajo. Normalize Weights reparte los pesos para que sumen como máximo 1 entre todos los Vertex Groups del vértice. |
| - | **Falloff: Type / botón de invertir curva** | *Dentro del modificador > Falloff* | Advanced | Remapea cada peso a través de una curva antes de aplicarlo, en vez de usarlo tal cual: Type (Linear) elige la forma de esa curva (lineal, suave, en punta...). El icono de flechas junto a Type invierte la curva de izquierda a derecha. |
| - | **Influence: Global Influence / Mask Vertex Group / Mask Texture** | *Dentro del modificador > Influence* | Advanced | Panel común a los 3 modifiers Vertex Weight (Edit/Mix/Proximity): Global Influence (1.00) controla la fuerza total del efecto del modifier. Mask Vertex Group limita dónde se aplica según otro Vertex Group. Mask Texture (con botón New) limita dónde se aplica según el blanco/negro de una textura, permitiendo pintar zonas de efecto. |

