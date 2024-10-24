"""
**Pregunta:** Para planificar vuelos, se necesita el pronóstico meteorológico 
de una semana en una ciudad, registrando temperatura y humedad cada día. Crea
una **matriz** de 7x2 donde cada fila representa un día y las columnas
representan temperatura y humedad. Llena la matriz con valores aleatorios.
Luego:

a) Identifica el día con la temperatura más baja.

b) Calcula la humedad promedio de la semana.
"""


import random
dias_semana= 7

matriz=[]
for i in range(dias_semana):
    temperatura= random.randint(00, 30)
    humedad= random.randint(10,80)
    matriz.append([temperatura,humedad])
   
print("Matriz de temperatura y humedad (Temperatura, Humedad) por día:")
for dia in range(dias_semana):
    print(f"Día {dia+1}: {matriz[dia]}")

temperaturas = [dia[0] for dia in matriz]  # Extraer solo las temperaturas
print (temperaturas)
min_temp = min(temperaturas)  # Encontrar la temperatura mínima
dia_min_temp = temperaturas.index(min_temp) + 1  # Encontrar el índice del día con temperatura mínima

print(f"\nEl día con la temperatura más baja es el Día {dia_min_temp} con {min_temp} grados.")

# b) Calcular la humedad promedio de la semana
humedades = [dia[1] for dia in matriz]  # Extraer solo las humedades
promedio_humedad = sum(humedades) / len(humedades)  # Calcular el promedio de humedad

print(f"La humedad promedio de la semana es: {promedio_humedad:.2f}%")   