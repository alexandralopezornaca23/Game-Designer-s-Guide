# Properties > Collection


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| 👁️ | **Restringir visibilidad / seleccionable** | *Panel Properties > pestaña Collection (al seleccionar una colección)* | Intermediate | Oculta la colección en el viewport, en el render, o impide seleccionarla, sin tocar los objetos uno a uno. |
| 🎨 | **Color Tag** | *Panel Properties > Collection* | Basic | Asigna un color a la colección para identificarla rápido en el Outliner. |
| - | **Visibility: Selectable / Show In: Renders** | *Panel Properties > Collection > Visibility* | Intermediate | Selectable: si se pueden seleccionar en el viewport los objetos de esta colección con el ratón. Show In Renders: si esta colección se incluye al renderizar (desactívala para 'apagar' toda una colección del render sin ocultarla del viewport). |
| - | **Visibility > View Layer: Include / Holdout / Indirect Only** | *Panel Properties > Collection > Visibility > View Layer* | Advanced | Include: si esta colección forma parte de la View Layer activa (desactivarlo la excluye del todo de esa capa). Holdout: los objetos de la colección actúan como máscara que 'recorta' lo que hay detrás en el render, sin mostrarse ellos mismos. Indirect Only: los objetos solo aportan su influencia indirecta (rebotes de luz, reflejos) pero no aparecen directamente en el render. |
| - | **Instancing > Instance Offset X / Y / Z** | *Panel Properties > Collection > Instancing* | Advanced | Punto de origen que se usa cuando esta colección se instancia como un todo (p. ej. con un Empty en modo Collection Instance); desplaza dónde queda el 'centro' de la instancia sin mover los objetos originales. |
| 📤 | **Exporters** | *Panel Properties > Collection > Exporters* | Advanced | Permite asignar (botón +) uno o varios formatos de exportación (glTF, FBX, etc.) directamente a la colección, con su propia configuración guardada; el botón Export All exporta todos los formatos añadidos de golpe. |
| ✒️ | **Line Art: Usage / Collection Mask / Masks / Intersection Priority** | *Panel Properties > Collection > Line Art* | Advanced | Configura cómo participa esta colección en el motor de Line Art (líneas de contorno estilo dibujo técnico/cómic): Usage decide si sus objetos generan líneas (Include), las bloquean (Occlusion Only) o se ignoran; Collection Mask + Masks permite que otra colección use esta como máscara de recorte; Intersection Priority decide qué colección 'gana' al calcular líneas donde dos objetos se cruzan. |
| 🔖 | **Custom Properties** | *Panel Properties > Collection > Custom Properties* | Advanced | Añade tus propios atributos a la colección, útiles para pipelines/scripts en Python. |

