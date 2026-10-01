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
edad = int(input("Ingrese su edad: "))
cantidadEntradas = int(input("Ingrese la cantidad de entradas: "))

#-------------------------------------------------Proceso 

if edad < 12:
    print("Ha recibido un descuento del 20%")
elif edad >= 65:
    print("Ha recibido un deescuento del 15%")
else:
    print("El precio de la entrada es de 3500")


if cantidadEntradas >= 4:
    print("¡Felicidades! Ha comprado 4 o más entradas y se le ha regalado una bebida.")
else:
    print("Gracias por su Compra")

#-------------------------------------------------Datos de Salida
