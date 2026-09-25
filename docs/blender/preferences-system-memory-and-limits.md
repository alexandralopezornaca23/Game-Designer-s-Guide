# Preferences > System: Memory & Limits


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| - | **Undo Steps** | *Edit > Preferences > System* | Intermediate | Cuántos pasos de deshacer guarda Blender en memoria; más pasos = más seguridad pero más RAM usada. |
| - | **Undo Memory Limit** | *Edit > Preferences > System* | Advanced | Límite de memoria (en MB) dedicado al historial de Undo; 0 = sin límite explícito. |
| - | **Global Undo** | *Edit > Preferences > System* | Intermediate | Si está activo, el Undo funciona de forma global entre todos los modos y editores; desactivarlo ahorra memoria pero hace el Undo menos fiable. |
| - | **Console Scrollback Lines** | *Edit > Preferences > System* | Advanced | Cuántas líneas de historial guarda la consola de Python/sistema antes de empezar a borrar las más antiguas. |
| - | **Texture Time Out / Garbage Collection Rate** | *Edit > Preferences > System* | Advanced | Cada cuánto (segundos) Blender libera de la memoria de la GPU las texturas que no se han usado recientemente. |
| - | **VBO Time Out / Garbage Collection Rate** | *Edit > Preferences > System* | Advanced | Igual que el anterior pero para los VBO: los datos de malla ya preparados para la GPU. |
| - | **Shader Compilation Method (Thread / Subprocess)** | *Edit > Preferences > System* | Advanced | Cómo compila Blender los shaders internamente; Thread es el modo por defecto, Subprocess puede evitar cuelgues en algunos drivers gráficos problemáticos a cambio de algo más de overhead. |
| - | **Threads** | *Edit > Preferences > System* | Advanced | Número de hilos de CPU a usar para tareas generales (0 = detectar automáticamente según tu procesador). |
| - | **Geometry Nodes Stack Limit** | *Edit > Preferences > System* | Advanced | Profundidad máxima de anidamiento permitida en árboles de Geometry Nodes muy complejos, antes de que Blender lo bloquee para evitar cuelgues. |

