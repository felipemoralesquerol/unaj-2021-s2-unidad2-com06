# Ejercicio 11:
# Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar
# cuánto se gasta por cada producto y el total

# Lectura desde teclado de la información de productos
producto_comprado1 = input("Ingrese el nombre del producto 1: ")
cantidad_comprado1 = int(input("Ingrese la cantidad: "))
precio_unitario_comprado1 = float(input("Ingrese el precio unitario: "))

producto_comprado2 = input("Ingrese el nombre del producto 2: ")
cantidad_comprado2 = int(input("Ingrese la cantidad: "))
precio_unitario_comprado2 = float(input("Ingrese el precio unitario: "))

# Realizo los calculos
subtotal_comprado1 = cantidad_comprado1 * precio_unitario_comprado1
subtotal_comprado2 = cantidad_comprado2 * precio_unitario_comprado2


total = subtotal_comprado1 + subtotal_comprado2

# Imprimo los resultados
print('Subtotal de producto ' + producto_comprado1 +
      ': ' + str(subtotal_comprado1))
print('Subtotal de producto ' + producto_comprado2 +
      ': ' + str(subtotal_comprado2))

print('Total: ' + str(total))
