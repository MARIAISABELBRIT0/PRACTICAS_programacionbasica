

"""a) Utiliza un conjunto para obtener los puntos de navegación únicos.
b) Calcula cuántos puntos de navegación únicos hay en total."""

puntos_navegacion = ['ABN', 'CDE', 'FGH', 'ABN', 'IJK', 'CDE', 'LMN', 'OPQ', 'RST', 'FGH']

# a) Utiliza un conjunto para obtener los puntos de navegación únicos.
puntos_unicos = set (puntos_navegacion)
print("el conjunto de puntos de navegacion unicos es:")
print(puntos_unicos)
# b) Calcula cuántos puntos de navegación únicos hay en total.
total_puntos= len(puntos_unicos)
print ("el total de puntos unicos es:")
print(total_puntos)