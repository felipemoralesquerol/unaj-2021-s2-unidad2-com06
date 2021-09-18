tupla = ('20 pesos', 4000, "hola", True, 34.56)
# Acceso por posición a la variable tupla. En este caso devuelve el elemento que se encuentra
# en la posición.
# print(tupla[2])

# Actualizar un elemento de la tupla. NO SE PUEDE HACER
# tupla[2] = "Hola"

# variable = "Chau"
# tuplita = 1, 2, 3, 5, -1
# print(tuplita)
# tupla = ('20 pesos', 4000, "Hola", True, 34.56,
#          "Nuevo elemento", variable, tuplita)
# print(tupla)
# variable = "Nuevo chau"
# tuplita = (1, 2, 3, 5, -10)
# print(tupla)

# tuplaNueva1 = tupla
# tuplaNueva2 = tupla[:]
# tupla = (2, -1)
# print(tuplaNueva1)
# print(tuplaNueva2)
# lista = [1, True, 8, 'chau']
# lista_alumnos = ["sol", "esteban", 'Miguel']
# lista_alumnos.remove('esteban')
# lista = lista + [5] + [lista_alumnos[1]]
# del lista[0]
# del lista[0]
# del lista[0]
# del lista[0]

# print(lista)

# valor = 8.0
# lista = [1, True, valor, 'chau']

# b = 8 in lista
# print(b)


# Inicializo lista con los destinos disponibles
destinos = ['Bariloche', 'Chilecito', 'Rosario', 'Salta',
            'Tilcara', 'Pumamarca']
# Ingresa el nombre de destino nuevo
destino_nuevo = input('Ingrese el destino nuevo: ')
# se agrega el destino
destinos.append(destino_nuevo)
print(destinos)
