# Modelling


## Modelling


### Congelar transformaciones del objeto seleccionado

*Basic*

```python
makeIdentity -apply true -translate true -rotate true -scale true;
```


### Borrar el historial de construcción

*Basic*

Sobre el objeto seleccionado.

```python
delete -constructionHistory true;
```


### Combinar los objetos seleccionados en uno

*Intermediate*

```python
polyUnite -ch 0 -mergeUVSets 1;
```

