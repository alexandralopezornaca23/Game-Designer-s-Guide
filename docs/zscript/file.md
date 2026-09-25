# File


## File


### Guardado incremental automático (v000, v001, v002...)

*Advanced*

Guarda con un nombre que se autoincrementa cada vez que ejecutas el script. Cambia "MiProyecto000.zpr" por tu nombre base. VarSave guarda el número de versión en disco para que se recuerde entre sesiones.

```python
[VarSet, fileName, "MiProyecto000.zpr"]
[FileNameSetNext, #fileName]
[IPress, File:Save As]
[VarSet, fileName, [FileNameAdvance, #fileName, 3]]
[VarSave, "GuiaGameDesigner_incSave", fileName]
```

