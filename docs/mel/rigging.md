# Rigging


## Rigging


### Crear un joint en el origen

*Basic*

```python
select -clear;
joint -position 0 0 0 -name "joint_root";
```


### Crear un grupo vacío (control de rig) en el origen

*Basic*

Útil como nulo/control dentro de una jerarquía de rig.

```python
group -empty -name "grp_control";
```


### Fusionar shapes (curvas) sin mover el objeto

*Advanced*

Añade como hija la shape del objeto seleccionado al último objeto seleccionado (el destino), sin moverla de sitio. Útil para fusionar varias curvas de control en un único transform.

```python
parent -r -s;
```

