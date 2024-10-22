import csv

with open ('datos_personas.csv', 'r') as csvfile:
    lector=csv.reader(csvfile, delimiter=';')
    encabezado =next (lector)
    print(encabezado)
    for fila in lector:
        print(f"{fila[0]} tendra {int(fila[1]) + 5} años dentro de 5 años")
        fila[2]= fila[2].replace(',','.')
        print (f'{fila [0]} mide {float(fila[2]) * 100 } cm ')