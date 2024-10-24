"""
Pregunta: En un vuelo, se lleva un registro de pasajeros donde cada asiento 
(identificado por su número) tiene asignado un pasajero con su nombre y 
preferencias de comida (vegetariano, vegano, estándar). Crea un diccionario
 que represente este escenario para al menos 5 pasajeros. Luego, escribe 
 una función que, dado un número de asiento, devuelva las preferencias 
 de comida del pasajero.
"""

registro = {}

def agregar_Datos(numero_asiento, nombre, comida):
    registro[numero_asiento] = {
         "nombre": nombre,
         "comida": comida
    }

agregar_Datos(1,"maria","estandar")
agregar_Datos(2,"juan","vegano")
agregar_Datos(3,"isa","vegetariano")
agregar_Datos(4,"daniel", "estandar")
agregar_Datos(5,"ana","estandar")

def buscar_info(numero_asiento):
    if numero_asiento in registro:
        puesto = registro[numero_asiento]
        print(f"preferencias del pasajero: {puesto['comida']}")
    else:
        print(f"el numero {numero_asiento} de asiento no esta en el registro")    

numero_asiento = int(input("ingrese el numero de asiento: "))
buscar_info(numero_asiento)
    