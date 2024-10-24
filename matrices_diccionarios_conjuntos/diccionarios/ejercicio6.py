"""
Crea un **diccionario de diccionarios llamado `registro_mantenimiento`
donde la clave es el número de serie de una aeronave y el valor es
otro diccionario que contiene las fechas (como cadenas) de los
últimos tres mantenimientos realizados. Luego, escribe código para:

a) Agregar una nueva fecha de mantenimiento a una aeronave específica.

b) Mostrar todas las fechas de mantenimiento de una aeronave dada."""

registro_mantenimiento={}

def agregar_diccionario(num_serie,fechas):
    registro_mantenimiento[num_serie]={
        "fechas": fechas
    }

agregar_diccionario("AD622","04/05/2025")
agregar_diccionario("DS232","13/08/2025")
agregar_diccionario("HD745","12/12/2025")
agregar_diccionario("AD643","23/11/2025")
agregar_diccionario("BH642","30/07/2025")

def cambiarfecha(num_serie,nueva_fecha):
    if num_serie in registro_mantenimiento:
        registro_mantenimiento[num_serie]["fechas"].append(nueva_fecha)
        print(f"Se ha agregado la nueva fecha {nueva_fecha} al registro de la aeronave {num_serie}.")
    else:
        print(f"La aeronave con número de serie {num_serie} no se encuentra en el registro.")