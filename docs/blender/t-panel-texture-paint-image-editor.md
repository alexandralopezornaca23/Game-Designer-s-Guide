# T Panel: Texture Paint (Image Editor)


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Herramientas comunes** | *Barra T (Texture Paint, Image Editor)* | Basic | El Image Editor (el panel izquierdo con la textura/UV) tiene su propio desplegable de modo arriba a la izquierda (Paint / View / Mask), independiente del modo 3D de la escena; según cuál esté activo, la barra T de ESTE panel muestra herramientas distintas. Aquí se documentan las de 'Paint', usadas para pintar directamente sobre la textura 2D. |
| 🖌️ | **Brush** | *Barra T (Image Editor > Paint) > Brush (Mayús+Barra espaciadora → 1)* | Basic | Pincel general de pintura 2D: pinta sobre la imagen/textura activa con el pincel elegido en el Brush Asset Shelf inferior (Paint Hard y similares). |
| ⭕ | **Radio y fuerza del pincel** | *F (radio) / Mayús + F (fuerza)* | Basic | Arrastra el ratón tras pulsar; clic para confirmar. Válido también en Texture Paint (Viewport 3D). |
| 🌫️ | **Blur** | *Barra T (Image Editor > Paint) > Blur (Mayús+Barra espaciadora → 2)* | Intermediate | Difumina/suaviza los píxeles de la textura por donde pasas el pincel, mezclando cada píxel con sus vecinos; útil para suavizar transiciones o quitar dureza a una pincelada anterior. |
| 👆 | **Smear** | *Barra T (Image Editor > Paint) > Smear (Mayús+Barra espaciadora → 3)* | Intermediate | Arrastra (embarra) el color de la textura en la dirección del trazo, como si mancharas pintura fresca con el dedo, en vez de añadir color nuevo. |
| 🖨️ | **Clone** | *Barra T (Image Editor > Paint) > Clone (Mayús+Barra espaciadora → 4)* | Advanced | Clona (sello) píxeles desde otra zona de la misma imagen (o de otra imagen de referencia) hacia donde pintas; funciona como el tampón de clonar de un editor de fotos. |
| 🪣 | **Fill** | *Barra T (Image Editor > Paint) > Fill (Mayús+Barra espaciadora → 5)* | Basic | Rellena de golpe una región de la imagen (o toda la imagen si no hay selección) con el color/pincel activo, en vez de pintarla trazo a trazo. |
| 🎭 | **Mask** | *Barra T (Image Editor > Paint) > Mask (Mayús+Barra espaciadora → 6)* | Intermediate | Pinta una máscara 2D sobre la imagen que protege zonas para que el resto de pinceles (Brush, Blur, Smear, Clone, Fill) no las modifiquen. |
| 💧 | **Sample** | *Barra T (Image Editor > View) > Sample (Mayús+Barra espaciadora → 1)* | Basic | Sample pixel values under the cursor: al cambiar el desplegable a 'View' (solo inspección, sin pintar), la barra T se reduce a esta herramienta, que muestra/toma el valor de color del píxel bajo el cursor, más Annotate (ver 'Barra T: Comunes a todos los modos'). |
| - | **Herramientas del submodo Mask** | *Barra T (Image Editor > Mask)* | Intermediate | Al cambiar el desplegable del Image Editor a 'Mask', la barra T pasa a mostrar 7 de las 9 herramientas 'Comunes a todos los modos' (ver esa categoría): Select Box, Cursor, Move, Rotate, Scale, Transform y Annotate — pero NO Measure ni Add Cube, que no tienen sentido aquí. Se usan para seleccionar y mover los puntos de control de una máscara 2D (curva de rotoscopia/enmascarado) en vez de vértices de una malla 3D u objetos. |

