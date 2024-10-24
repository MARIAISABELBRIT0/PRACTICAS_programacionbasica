"""
Dos aerolíneas ofrecen vuelos entre diferentes ciudades. Las rutas de la Aerolínea A son:

```python
rutas_a = {'Madrid-Barcelona', 'Madrid-Londres', 'Madrid-París', 'Barcelona-Roma'}
```

Las rutas de la Aerolínea B son:

```python
rutas_b = {'Madrid-Berlín', 'Madrid-Londres', 'Barcelona-París', 'Barcelona-Roma'}
```

a) Utiliza **operaciones de conjuntos** para encontrar las rutas que ambas aerolíneas comparten.

b) Encuentra las rutas que son exclusivas de la Aerolínea A."""


rutas_a = {'Madrid-Barcelona', 'Madrid-Londres', 'Madrid-París', 'Barcelona-Roma'}
rutas_b = {'Madrid-Berlín', 'Madrid-Londres', 'Barcelona-París', 'Barcelona-Roma'}

# a
comparten = rutas_a.intersection(rutas_b)
print(f"compraten las rutas: {comparten}")

#b
exclusiva_a= rutas_a.difference(rutas_b)
print(f" las rutas que son exclusivas de a son : {exclusiva_a}")