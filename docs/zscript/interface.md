# Interface


## Interface


### Hola Mundo (probar que el script carga bien)

*Basic*

El script más simple posible. Cárgalo desde Zplugin > Zscript > Load para comprobar que ZBrush lee bien tu archivo .txt.

```python
[Note, "¡Hola desde ZScript!"]
```


### Botón personalizado en un submenú propio

*Intermediate*

Crea tu propio submenú (MisScripts) con un botón que ejecuta el comando que pongas entre corchetes. Buen punto de partida para ir guardando tus scripts como botones reutilizables.

```python
[ISubpalette, Zscript:MisScripts]
[IButton, Zscript:MisScripts:HolaMundo,
  "Muestra un mensaje de prueba",
  [Note, "¡Botón funcionando!"]
]
```

