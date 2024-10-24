"""
Durante una prueba, se registró el consumo de combustible de un motor
en diferentes niveles de potencia y revoluciones por minuto (RPM).
Crea una **matriz bidimensional** que represente el consumo (en litros
por hora) para combinaciones de potencia (50%, 75%, 100%) y RPM
(1000, 2000, 3000). Llena la matriz con valores hipotéticos. Luego:

a) Encuentra el consumo máximo y mínimo registrados.

b) Indica en qué combinación de potencia y RPM se dieron estos consumos."""

import random
matriz= []

for i in range (10):
    
    consumo_combustible= random.randint(5,30)

    lista_num_potencias=[50,75,100]
    potencia= random.choice(lista_num_potencias)

    lista_num_rpm=[1000,2000,3000]
    rpm=random.choice(lista_num_rpm)

    matriz.append([consumo_combustible,potencia,rpm])

for dato in range(10):
    print(f"{matriz[dato]}")


#a
solo_combustible=[dato[0] for dato in matriz]
print(solo_combustible)
maximo_com=max(solo_combustible)
minimo_com= min(solo_combustible)

print(f"el maximo de combustible registrado es {maximo_com} y el minimo es {minimo_com} ")

#b

for dato in matriz:
    if dato[0] == maximo_com:
        print(f"\nEl máximo de combustible ({maximo_com} litros/hora) se registró con una potencia del {dato[1]}% y {dato[2]} RPM")
    if dato[0] == minimo_com:
        print(f"El mínimo de combustible ({minimo_com} litros/hora) se registró con una potencia del {dato[1]}% y {dato[2]} RPM")


