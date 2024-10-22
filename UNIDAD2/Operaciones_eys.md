# OPERACIONES DE ENTRADA Y SALIDA 
los dispositivos si son de:
- Entrada : permiten que los usuarios introduzcan datos, comandos e interacciones en el sistema 
- Salida :  presentan los resultados del procesamiento de manera comprensible para los usuarios

en el medio de estos dos la computador lo que hace es que los datos pasan a ser procesados para realizar cálculos, ejecutar programas y generar resultados.

Sin los dispositivos de entrada, la computadora no podría recibir instrucciones ni datos para procesar, y sin los dispositivos de salida, los usuarios no podrían obtener información procesada o resultados.

## Representación de los datos en la memoria
Los datos en una computadora se representan en forma de <mark>bits</mark>,la unidad más pequeña de información digital (0 o 1).
<mark>Un grupo de 8 bits forma un **byte**</mark> que es una unidad básica de almacenamiento.

los lenguajes de programcacion usan diferentes tipos de datos para representar informacion como:
- enteros : # completos  
- numeros punto flotantes : manejan valores decimales
- caracteres : simbolos y letras
- booleanos : verdadero o falso

Estos tipos de datos se utilizan para definir variables y estructuras en el código fuente

### int (datos enteros)
Los números enteros (+ o -) son valores numéricos que no contienen componentes fraccionarios ni decimales.

para saber cuantos datos puedo representar con n numero de bits hago lo siguiente para :
- enteros sin signo : de 0 a (2^{n}-1)
- entros con signo : de -(2^{n-1}) a (2^{n-1}-1)

### float (Datos Reales) 
Existen los números de punto flotante de : 
- precisión simple (32 bits)
- doble precisión (64 bits).

### char (Datos tipo caracter)

representar símbolos, letras, dígitos y otros caracteres alfanuméricos.

### string (Cadenas de caracteres)

concatenación de datos tipo caracter que se unen para formar un texto
Las cadenas de caracteres se escriben entre comillas, por ejemplo: “Esta es una cadena”. Cada dato tipo caracter se representa por un dato binario de 8 bits
 
**Nota: debes tener en cuenta que hay una diferencia entre una cadena de caracteres de un número y su representación como entero o real.**

### bool (Datos Booleanos)
 verdadero (true) o falso (false).


## IDLE de Python
*(Integrated Development and Learning Environment)*

### Consola de Python
La consola de Python es una interfaz de línea de comandos que permite interactuar directamente con el intérprete de Python en tiempo real. Es una herramienta útil para probar y ejecutar fragmentos de código de manera rápida y ver resultados inmediatos

###### en python :
- int() → convierte una variable a entera
- float() → convierte una variable a real de precisión simple
- str() → convierte una variable a cadena de caracteres
- bool() → convierte una variable a booleana