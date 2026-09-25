# Geometry


## Geometry


### Repetir una acción varias veces (bucle)

*Intermediate*

[Loop,n,...] repite lo que hay dentro n veces. Este ejemplo pulsa 3 veces el botón Divide para subdividir la malla. Sustituye [IPress, Tool:Geometry:Divide] por cualquier otro comando que hayas descubierto con Ctrl+clic.

```python
[Loop, 3,
  [IPress, Tool:Geometry:Divide]
]
```

