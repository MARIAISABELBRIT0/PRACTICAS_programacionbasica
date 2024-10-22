"""
Matrices y Sensores de Vuelo:

Una aeronave tiene un sistema de monitoreo que registra la altitud (en metros)
y la velocidad (en km/h) cada 10 minutos durante un vuelo de 5 horas. Crea una
matriz que almacene estas dos variables para cada intervalo de tiempo. 

Llena la matriz (usa una función) con valores aleatorios dentro de rangos razonables 
(por ejemplo, altitud entre 0 y 12,000 metros, velocidad entre 200 y 900 km/h). 
Luego, realiza lo siguiente:

a) Calcula la altitud promedio durante el vuelo.

b) Determina el intervalo de tiempo en el que se alcanzó la **velocidad máxima**.
"""
"""
import random

def valores_aleatorios ():
    matriz = [] 

    for i in range (30): # una fila para cada 10 min en esas 5 horas
        altitud= (random.uniform(00, 12000)) # usamos random.uniform por que nos da numeros decimales
        velocidad= (random.uniform(700, 900))
        columnas= [velocidad, altitud]
        matriz.append(columnas)
        print(matriz[i][j],end="\t")
    print()


suma_altitudes = sum([altitudes in columas])  # Sumamos las altitudes (columna 0)
promedio=suma_altitudes / 30
print (promedio)



if __name__ == "__main__":
    valores_aleatorios()


    return matriz

# Función para calcular la altitud promedio
def calcular_altitud_promedio(matriz):
    suma_altitudes = sum([fila[1] for fila in matriz])  # Sumamos las altitudes (columna 1)
    promedio = suma_altitudes / len(matriz)  # Calculamos el promedio
    return promedio

# Función para encontrar el intervalo de la velocidad máxima
def encontrar_velocidad_maxima(matriz):
    velocidades = [fila[0] for fila in matriz]  # Extraemos las velocidades (columna 0)
    max_velocidad = max(velocidades)  # Encontrar la velocidad máxima
    intervalo = velocidades.index(max_velocidad)  # Obtener el índice del intervalo con la velocidad máxima
    return intervalo, max_velocidad

# Generar la matriz con los valores de altitud y velocidad
matriz_vuelo = valores_aleatorios()

# Mostrar la matriz generada (opcional)
print("Matriz de velocidad (km/h) y altitud (m):")
for fila in matriz_vuelo:
    print(f"Velocidad: {fila[0]:.2f} km/h, Altitud: {fila[1]:.2f} m")

# Calcular la altitud promedio
altitud_promedio = calcular_altitud_promedio(matriz_vuelo)
print(f"\nAltitud promedio durante el vuelo: {altitud_promedio:.2f} metros")

# Encontrar el intervalo donde se alcanzó la velocidad máxima
intervalo_velocidad_maxima, velocidad_maxima = encontrar_velocidad_maxima(matriz_vuelo)
print(f"Velocidad máxima de {velocidad_maxima:.2f} km/h alcanzada en el intervalo {intervalo_velocidad_maxima + 1}")

"""