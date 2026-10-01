nombreCliente=input("Digite el nombre del cliente:")


nombre_plato = input("Digite el nombre del plato: ")
precio=float(input("Digite el precio del plato:"))
cantidad=int(input("Digite la cantidad de platos: "))

subtotal=preciocantidad
impuesto=subtotal13/100
total=subtotal+impuesto

print("cliente:",nombreCliente)
print("plato:",nombre_plato)
print("subtotal:",subtotal)
print("impuesto:",impuesto)
print("total a pagar:",total)