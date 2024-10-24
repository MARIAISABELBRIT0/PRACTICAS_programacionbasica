"""
Pregunta: Una aerolínea desea mantener un registro de su flota de aviones.
Crea un diccionario donde la clave es el número de registro del avión y el
valor es otro diccionario con el modelo, capacidad de pasajeros y año de
fabricación. Incluye al menos 5 aviones en el diccionario. Luego, escribe
una función que permita buscar un avión por su número de registro y
muestre toda su información.
 
"""
flota_aviones = {}
 
def agregar_persona_dict(numero_registro,modelo,capacidad_pasajeros,año_fabricacion):
 
    flota_aviones[numero_registro] = {
        "modelo": modelo,
        "capacidad_pasajeros": capacidad_pasajeros,
        "año_fabricacion": año_fabricacion
    }
 
agregar_persona_dict("AB733", "Boeing 737",200,2016)
agregar_persona_dict("NE883", "Boeing 747",190,2006)
agregar_persona_dict("JE943", "AIRBUS A350",102,2020)
agregar_persona_dict("GD833", "EMBRAER E195",124,1998)
agregar_persona_dict("KA932", "AIRBUS A380",100,2018)


# Función para buscar un avión por su número de registro
def buscar_avion(numero_registro):
    if numero_registro in flota_aviones:
        avion = flota_aviones[numero_registro]
        print(f"Numero de registro: {numero_registro}, Modelo: {avion['modelo']}, "
              f"Capacidad de pasajeros: {avion['capacidad_pasajeros']}, "
              f"Año de fabricación: {avion['año_fabricacion']}")
    else:
        print(f"Avión con número de registro '{numero_registro}' no encontrado.")

# Solicitar al usuario el número de registro y buscar el avión
numero_registro = input("Ingrese el número de registro del aeronave: ")
buscar_avion(numero_registro)



 
 
