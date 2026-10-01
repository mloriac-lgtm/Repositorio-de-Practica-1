"""
Un cine desea calcular el precio que debe pagar un cliente por sus entradas. El precio normal de cada entrada es de ₡3 500.

El programa debe solicitar:

Edad del cliente.
Cantidad de entradas.

Utilice las siguientes reglas:

Las personas menores de 12 años reciben un 20 % de descuento.
Las personas de 65 años o más reciben un 15 % de descuento.
Las demás personas pagan el precio normal.
Si el cliente compra 4 entradas o más, recibe 1 bebida gratis.

El programa debe mostrar: subtotal, descuento aplicado, total a pagar e indicar si el cliente recibe la bebida gratis.
"""

#-------------------------------------------------Datos de Entrada
precioEntradas = 3500
edad = int(input("Ingrese su edad: "))
cantidadEntradas = int(input("Ingrese la cantidad de entradas: "))

#-------------------------------------------------Proceso 

if edad < 12:
    primerDescuento = precioEntradas * 0.20 * cantidadEntradas
    primerTotal = cantidadEntradas * precioEntradas - primerDescuento
    print("Ha recibido un descuento del 20% su total es de:", primerTotal,)
elif edad >= 65:
    segundoDescuento = precioEntradas * 0.15 * cantidadEntradas #segundoDescuento = 3500 * 0.15 = 525
    segundoTotal = cantidadEntradas * precioEntradas - segundoDescuento #segundoTotal = 2 * (3500 - 525) = 6475 
    print("Ha recibido un deescuento del 15% su total es de:", segundoTotal,)
else:
    totalRegular = cantidadEntradas * precioEntradas
    print("El precio de la entrada es de 3500 su total es de:", totalRegular,)


if cantidadEntradas >= 4:
    print("¡Felicidades! Ha comprado 4 o más entradas y se le ha regalado una bebida.")
else:
    print("Gracias por su Compra")

"""
primerDescuento = precioEntradas * 0,20
segundoDescuento = precioEntradas * 0,15

primerTotal = cantidadEntradas * precioEntradas - primerDescuento
segundoTotal = cantidadEntradas * precioEntradas - segundoDescuento
totalRegular = cantidadEntradas * precioEntradas

#-------------------------------------------------Datos de Salida
print("Usted resibió un descuento del 20% su total es de:", primerTotal,)
print("Usted resibió un descuento del 15% su total es de:", segundoTotal,)
print("Su total es de:", precioRegular,)
"""