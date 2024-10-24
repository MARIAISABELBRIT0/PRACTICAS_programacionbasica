"""
Una aerolínea desea analizar el consumo de combustible en diferentes rutas.
Crea un **diccionario de diccionarios** donde la clave es el código de
la ruta (por ejemplo, 'MAD-LON') y el valor es otro diccionario que contiene
el tipo de avión utilizado y el consumo promedio de combustible (en litros).
Incluye al menos 4 rutas. Luego:

a) Escribe una función que calcule el consumo total de combustible si se realizan dos vuelos de ida y vuelta en cada ruta.

b) Identifica la ruta con el mayor consumo promedio de combustible."""

diccionario={}

def diccionario_dentro(codigo,tipo,consumo):
    diccionario[codigo]= {
        "tipo": tipo,
        "consumo": consumo
    }

diccionario_dentro("MAD-LON","boeing 737",80)
diccionario_dentro("PAT-LED","boeing 747",100)
diccionario_dentro("MFG-AFF","Embrae E190",120)
diccionario_dentro("GSW-FDS","Airbus A350",170)

print(diccionario)

def total_combustible(rutas):
    total= 0
    for codigo, dato in diccionario.items():
        consumopedido=dato['consumo'] * 4
        total += consumopedido
    return total

        


total_combustible(4)