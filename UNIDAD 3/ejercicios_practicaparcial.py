
import random
filas = 12
columnas = 5
Lista = []              
for i in range(filas):     
    Lista.append([])      
    for j in range(columnas):  
        n = (random.randint(100, 1000))
        Lista[i].append(n)
        print(Lista[i][j],end="\t")
    print()


a = [0]*5        #Se hace una repetición del elemento 0
print(a)
Matriz = [a]*3   #Se crea una referencia a la lista anterior // NO es una nueva lista
print(Matriz)
#Observe que si al elemento Matriz[0][0] se le asigna el valor de 20
Matriz [0][0] = 20   #Todos los elementos de esa columna quedan con dicho valor
print(Matriz)
print('?'*30)