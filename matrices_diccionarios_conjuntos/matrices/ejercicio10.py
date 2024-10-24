"""
La distribución de peso en una aeronave es crítica para su equilibrio. 
Crea una **matriz bidimensional** de 3x4 que represente el peso (en kg)
en diferentes secciones de la aeronave (3 filas y 4 columnas). Llena
la matriz con valores aleatorios entre 50 kg y 200 kg. Luego:

a) Calcula el peso total de la aeronave.

b) Determina cuál fila tiene el mayor peso acumulado.
"""
import random
matriz=[]

for i in range(3):
    matriz.append([])
    for j in range(4):
        n= int(random.randint(50,200))
        matriz[i].append(n)

print("la matriz de pesos en diferentes secciones del aeronave es: ")        

for peso in range(3):
    print(f"{matriz[peso]}")

#a) Calcula el peso total de la aeronave.

fila1= [peso[0]for peso in matriz]
fila2= [peso[1]for peso in matriz]
fila3= [peso[2]for peso in matriz]

suma_fila1=sum(fila1)
suma_fila2=sum(fila2)
suma_fila3=sum(fila3)
suma= suma_fila1 + suma_fila2 + suma_fila3

print(f"el peso total del aeronavees: {suma}")

#b) Determina cuál fila tiene el mayor peso acumulado.

pesos= [peso for peso in matriz]

maximo= max(pesos)

print(f"la fila con mayor peso acumulado es : {maximo}")