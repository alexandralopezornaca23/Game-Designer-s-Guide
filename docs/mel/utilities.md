# Utilities


## Utilities


### Renombrar en bloque la selección

*Intermediate*

```python
string $sel[] = `ls -selection`;
int $i = 1;
for ($obj in $sel) {
    rename $obj ("prop_" + $i);
    $i++;
}
```


### Guardar la escena actual

*Basic*

```python
file -save;
```

