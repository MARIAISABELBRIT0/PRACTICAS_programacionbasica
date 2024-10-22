# indentación: es el espacio que se deja para marcar un orden en el algoritmo

su= 0
es=float(input("cual es su estatura en m: "))
c= 0
while es > 0:
    su +=es
    es=float(input("cual es su estatura en m: "))
    c +=1
if es == 0:
    print("no hay estatura")
else:
    pr=su/c

print(f"estatura promedio = {pr}")