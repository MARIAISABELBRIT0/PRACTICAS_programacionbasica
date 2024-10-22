#  ejemplo compra online
valor_compra= int(input("ingrese el costo total de su compra: "))
if valor_compra < 100000 :
    valor_total= valor_compra + 9000
else:
    valor_total= valor_compra

print (f"tu valor total a pagar con envio incluido envio es ${valor_total}")

# avion

km= int(input("ingrese la distancia (en km) del vuelo: "))
combustible= int(input("cuanto es el consumo de combustible por km de la aeronave: "))
op= km * combustible
if km <= 1000 :
    mincantidad_com= op + (op/ 0.1)
else :
    mincantidad_com= op + (op/ 0.15)

print (f"la cantidad de combustible que necesita el aeronave es: {mincantidad_com}")