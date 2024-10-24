"""
Un avión está compuesto por múltiples componentes. Durante una inspección, se identificaron piezas
que necesitan reemplazo en dos secciones del avión:

seccion_a = {'Alerón', 'Flap', 'Motor Derecho', 'Tren de Aterrizaje'}
seccion_b = {'Motor Izquierdo', 'Flap', 'Estabilizador', 'Tren de Aterrizaje'}

a) Utiliza conjuntos para determinar qué piezas necesitan reemplazo en ambas secciones.

b) Enumera todas las piezas que requieren reemplazo sin duplicados. """

seccion_a = {'Alerón', 'Flap', 'Motor Derecho', 'Tren de Aterrizaje'}
seccion_b = {'Motor Izquierdo', 'Flap', 'Estabilizador', 'Tren de Aterrizaje'}

# a

comun= seccion_a.intersection(seccion_b)
print(f"las piezas que necesita remplazo en ambas secciones son {comun}")

# b

piezas= seccion_a.union(seccion_b)
cantidad_piezas=len(piezas)
print(f"la cantidad de pieza que nesesitan remplazo es de {cantidad_piezas} y son {piezas}") 
