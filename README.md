# BFS-DFS
Implementación de algoritmos BFS y DFS en una librería de Grafos.

Uso:

Para aplicar BFS a un grafo generado (por ejemplo, con el modelo de malla), utilizamos el siguiente código.

```python
from BFS import BFS
from grid import grid

g1 = grid(20,5)
g1.show(nombre='grid20_25')

g2 = BFS(g1,'1')
g2.show(nombre='BFS_grid20_25')
```

De manera similar, podemos aplicar lo mismo para las dos variantes de DFS:


```python
from DFS_I import DFS_I
from DFS_R import DFS_R

g3 = DFS_I(g1,'1')
g3.show(nombre='DFS_I_grid20_25')

g4 = DFS_R(g1,'1')
g4.show(nombre='DFS_R_grid20_25')

```
