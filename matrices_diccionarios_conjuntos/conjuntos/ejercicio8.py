"""
Un equipo de ingenieros trabaja en dos proyectos diferentes. Los ingenieros en el **Proyecto X** son:
ingenieros_x = {'Ana', 'Luis', 'María', 'Jorge', 'Sofía'}

Los ingenieros en el Proyecto Y son:
ingenieros_y = {'María', 'Carlos', 'Sofía', 'Miguel', 'Elena'}

a) Utiliza conjuntos para determinar qué ingenieros trabajan en ambos proyectos.

b) Encuentra los ingenieros que trabajan únicamente en el Proyecto Y."""

ingenieros_x = {'Ana', 'Luis', 'María', 'Jorge', 'Sofía'}
ingenieros_y = {'María', 'Carlos', 'Sofía', 'Miguel', 'Elena'}

#a
ambos=ingenieros_x.intersection(ingenieros_y)
print(f"los ingenieros que estan en ambos proyectos son: {ambos}")

#b
unicos= ingenieros_y.difference(ingenieros_x)
print(f"los ingenieros que solo estan en y son {unicos}")