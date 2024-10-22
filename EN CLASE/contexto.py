# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

# Usamos 'with' para crear el archivo y escribir datos en él
with open(nombre_archivo, 'w') as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    titulo = input("Ingrese el titulo del del trabajo : ")
    nombre= input( "ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    ciudad= input("ingrese la ciudad : ")
    archivo.write(titulo + "\n")
    archivo.write(nombre + "\n")
    archivo.write(apellido + "\n")
    archivo.write(ciudad + "\n")


# Ahora usamos 'with' para leer los datos del archivo
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)