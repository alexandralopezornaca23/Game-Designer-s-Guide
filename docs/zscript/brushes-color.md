# Brushes / Color


## Brushes / Color


### Botón de color rápido con atajo de teclado

*Basic*

Crea un botón (con atajo Mayús+Alt+R) que cambia el color activo a rojo. Cambia los valores RGB para cualquier otro color; útil para tener a mano tu paleta de Polypaint habitual.

```python
[IButton, "Rojo", "Selecciona el rojo como color principal",
  [IColorSet, 255, 0, 0]
  ,80, SHIFT+ALT+'R'
]
```

