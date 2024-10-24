"""
Una compañía aérea tiene pilotos con diferentes certificaciones. Las certificaciones disponibles son:

certificaciones = {'Vuelo Nocturno', 'Vuelo Instrumental', 'Aterrizaje en Pista Corta', 'Vuelo Internacional'}

Cada piloto tiene un conjunto de certificaciones. Por ejemplo:

piloto_1 = {'Vuelo Nocturno', 'Vuelo Instrumental'}
piloto_2 = {'Aterrizaje en Pista Corta', 'Vuelo Internacional'}
piloto_3 = {'Vuelo Nocturno', 'Aterrizaje en Pista Corta', 'Vuelo Internacional'}


a) Determina qué certificaciones son comunes a todos los pilotos.

b) Encuentra las certificaciones exclusivas del piloto_1.
"""

piloto_1 = {'Vuelo Nocturno', 'Vuelo Instrumental'}
piloto_2 = {'Aterrizaje en Pista Corta', 'Vuelo Internacional'}
piloto_3 = {'Vuelo Nocturno', 'Aterrizaje en Pista Corta', 'Vuelo Internacional'}

# Determina qué certificaciones son comunes a todos los pilotos.
comunes_1y3 = piloto_1.intersection(piloto_3)
comunes_2y3=piloto_2.intersection(piloto_3)
print(f"el piloto 1 y el piloto 3 tienen en comun {comunes_1y3}, mientras que el piloto 2 y 3 tienen en comun {comunes_2y3} ")

# Encuentra las certificaciones exclusivas del piloto_1.
diferencia= piloto_1.difference(piloto_3)
print(f"el piloto 1 es el unico que cuenta con {diferencia}")