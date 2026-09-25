# Modelling


## Modelling


### Aplicar todas las transformaciones

*Blender · Basic*

Sobre los objetos seleccionados. Hazlo antes de exportar a Unity/Unreal para evitar problemas de escala.

```python
import bpy
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
```


### Añadir un cubo en el origen

*Blender · Basic*

```python
import bpy
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
```


### Unir los objetos seleccionados en uno

*Blender · Basic*

El objeto activo (el último seleccionado) es el que absorbe a los demás.

```python
import bpy
bpy.ops.object.join()
```


### Congelar transformaciones del objeto seleccionado

*Maya · Basic*

```python
import maya.cmds as cmds
cmds.makeIdentity(apply=True, translate=True,
                  rotate=True, scale=True)
```


### Borrar el historial de construcción

*Maya · Basic*

Sobre el objeto seleccionado.

```python
import maya.cmds as cmds
cmds.delete(constructionHistory=True)
```


### Combinar los objetos seleccionados en uno

*Maya · Intermediate*

```python
import maya.cmds as cmds
cmds.polyUnite(ch=False, mergeUVSets=True)
```

