fp= open("texto.txt","r")
datos = fp.read(5)
print (datos)
datos = fp.read(5)
print(datos)
fp.close()