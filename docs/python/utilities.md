# Utilities


## Utilities


### Seleccionar objetos cuyo nombre contiene un texto

*Blender · Intermediate*

```python
import bpy
texto = "Prop_"
for obj in bpy.data.objects:
    obj.select_set(texto in obj.name)
```


### Exportar la selección como FBX

*Blender · Intermediate*

Cambia la ruta (filepath) antes de ejecutarlo.

```python
import bpy
bpy.ops.export_scene.fbx(
    filepath="C:/export/modelo.fbx",
    use_selection=True
)
```


### Guardar copia incremental (_v01, _v02...)

*Blender · Advanced*

Requiere que el nombre del archivo ya termine en "_v01.blend", etc.

```python
import bpy, re
path = bpy.data.filepath
m = re.search(r"_v(\d+)\.blend$", path)
if m:
    n = int(m.group(1)) + 1
    nuevo = re.sub(r"_v\d+\.blend$", f"_v{n:02d}.blend", path)
else:
    nuevo = path.replace(".blend", "_v01.blend")
bpy.ops.wm.save_as_mainfile(filepath=nuevo)
```


### Renombrar en bloque la selección

*Maya · Intermediate*

```python
import maya.cmds as cmds
sel = cmds.ls(selection=True)
for i, obj in enumerate(sel):
    cmds.rename(obj, f"prop_{i+1:02d}")
```


### Exportar la selección como FBX

*Maya · Intermediate*

Requiere tener cargado el plugin fbxmaya (Windows > Settings/Preferences > Plug-in Manager).

```python
import maya.cmds as cmds
cmds.file("C:/export/modelo.fbx",
          exportSelected=True,
          type="FBX export", force=True)
```

