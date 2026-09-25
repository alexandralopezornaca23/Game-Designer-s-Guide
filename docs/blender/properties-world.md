# Properties > World


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🌍 | **Surface (fondo/entorno)** | *Panel Properties > pestaña World > Surface* | Basic | Color o textura HDRI que se usa como fondo e iluminación ambiental de la escena. |
| - | **Surface > Surface / Color / Strength** | *Panel Properties > World > Surface* | Basic | Surface: nodo shader usado para el fondo (Background por defecto; se puede sustituir por otro nodo, como una textura de entorno HDRI, conectándolo en el Shader Editor con Editor Type = World). Color: color plano del fondo si no hay textura. Strength: intensidad de la luz que este fondo aporta a la escena como iluminación ambiental. |
| ☁️ | **Volume** | *Panel Properties > World > Volume* | Advanced | Permite asignar un shader de volumen (niebla/humo volumétrico) que llena todo el espacio de la escena; por defecto en None (sin volumen atmosférico). |
| 🌫️ | **Mist Pass** | *Panel Properties > World > Mist Pass* | Advanced | Niebla que se puede usar como pasada de render en compositing (profundidad atmosférica); para que se vea hay que activar la pasada Mist en Properties > View Layer > Passes > Data. |
| - | **Mist Pass > Start / Depth / Falloff** | *Panel Properties > World > Mist Pass* | Advanced | Start: distancia desde la cámara a la que empieza a aparecer la niebla. Depth: distancia adicional hasta que la niebla llega a cubrir del todo (opacidad 100%). Falloff: curva con la que aumenta la niebla (Quadratic/Linear/Inverse Quadratic). |
| 🔮 | **Settings > Light Probe: Resolution** | *Panel Properties > World > Settings > Light Probe* | Advanced | Resolución de la textura que EEVEE Next genera al hornear la iluminación del World como Light Probe (más resolución = reflejos/iluminación ambiental más nítidos pero más peso). |
| - | **Settings > Sun: Threshold / Angle** | *Panel Properties > World > Settings > Sun* | Advanced | Cuando el fondo/HDRI tiene una zona muy brillante (como el sol en un cielo), EEVEE Next puede tratarla como una luz Sun automática: Threshold es el brillo mínimo para detectarla, y Angle el tamaño angular de esa 'luz sol' generada (afecta a lo duras o suaves que salen sus sombras). |
| - | **Settings > Shadow: Jitter / Overblur / Filter / Resolution Limit** | *Panel Properties > World > Settings > Shadow* | Advanced | Controla las sombras que proyecta la iluminación del World/HDRI. Jitter + Overblur suavizan el ruido de esas sombras con un desenfoque controlado. Filter suaviza el borde de la sombra. Resolution Limit fija el tamaño mínimo de detalle de sombra que se calcula, para ahorrar rendimiento. |
| 🌓 | **Viewport Display: Color** | *Panel Properties > World > Viewport Display* | Basic | Color simplificado que se muestra en el Viewport 3D en modo Solid, ya que ahí no se renderiza el HDRI/nodo real (solo se ve en modo Rendered o Material Preview). |
| 🔑 | **Animation: World / Shader Node Tree** | *Panel Properties > World > Animation* | Advanced | Permite crear (New) una acción de animación para los valores del propio World (p. ej. animar el Strength), y otra separada para animar los nodos de su árbol de shader (Shader Node Tree). |
| 🔖 | **Custom Properties** | *Panel Properties > World > Custom Properties* | Advanced | Añade atributos propios al World, útiles para pipelines/scripts en Python. |

