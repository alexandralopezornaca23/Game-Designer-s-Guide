# Top Menu > Render


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 🎬 | **Render Image** | *Render > Render Image (F12)* | Basic | Renderiza el frame actual y abre automáticamente el Image Editor con el resultado; no guarda nada en disco por sí solo, para eso hay que usar Image > Save As en esa misma ventana o tener configurada la ruta de salida. |
| 🎬 | **Render Animation** | *Render > Render Animation (Ctrl+F12)* | Basic | Renderiza todos los frames del rango configurado en Properties > Output y los va guardando automáticamente en la ruta y formato definidos ahí mismo; a diferencia de Render Image, esta sí escribe en disco sin pasos extra. |
| 🔊 | **Render Audio...** | *Render > Render Audio...* | Intermediate | Exporta solo la pista de audio de la escena (mezcla de todos los Speakers y de las tiras de sonido del Video Sequence Editor) a un archivo de sonido, sin renderizar ni un solo frame de vídeo. |
| 🎬 | **View Render** | *Render > View Render (F11)* | Basic | Reabre la ventana del último render de imagen ya realizado, sin tener que volver a renderizar; útil para revisar un resultado después de haber cerrado esa ventana. |
| 🎬 | **View Animation** | *Render > View Animation (Ctrl+F11)* | Intermediate | Reabre y reproduce el Render Result de la última animación ya renderizada, leyendo los frames ya generados en disco en vez de volver a calcularlos. |
| - | **Lock Interface** | *Render > Lock Interface* | Advanced | Casilla activable: bloquea la interfaz mientras se renderiza (sobre todo relevante en Cycles) para que no se pueda interactuar con la escena por accidente durante el cálculo; a cambio, evita que la interfaz se congele visualmente en renders largos, así que muchos la dejan activada. |

