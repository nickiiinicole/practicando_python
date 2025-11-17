###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ['calcetin', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5]

# El tercer parámetro es el paso (step)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares
print(lista1[::-1]) # para devolver índices inversos

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("Longitud de la lista", len(lista1))

#list-comprehension
# CREA UNA LISTA COMPLETA EN MEMORIA
# [] definir la lista
# para cada elemento de lista me devuelves el valor X
lista=[{"x":10, "y":40, "z":5}, {"x":10, "y":40, "z":5}, {"x":10, "y":40, "z":5}]
listaX = [elemento["x"] for elemento in lista]
#con condicion
lista = [{"x":10,"y":20},{"x":5,"y":5},{"x":20,"y":10}]
listaX = [elemento["x"] for elemento in lista if elemento["x"]>5]
# Generator expresSions
# estas devuelven un generator-> no es una list pero tiene iterable
# NO CREA LA LISTA! , GENERA VALORES UNO POR UNO CAUNDO SE NECESITAN
resultado = (x * 2 for x in range(5))
# NO CONTIENE LA LISTA, CONTIENE UN GENERADOR:
# <generator object ... >
# LOS VALORES SOLO SE GENERAN CUANDO LOS PIDES:

# EJEMPLO USAR:

#     LIST COMPEHENSION : CUANDO NECESITAS LA LISTA COMPLETA
#         - convertir temperaturas
#         - filtrar emails validos
#         - cargar datos para analisis
#     GENERATOR EXPRESSION : CUANDO NO QUIERES LA LISTA COMPLETA
#         - leer archivo grande leer linea linea
#         lineas = (linea.strip() for linea in open("logs.txt"))
#         - streaming de datos
#         - calcular enormes sin ocupar memoria

# MAP(function,iterable)
    # aplica a cada funcion a cada de elemento del iterable
    # devuelve un map object
def doble(x):
    return x * 2

resultado = map(doble, [1, 2, 3])
print(list(resultado))
# MAP NO DEVUELVE UNA LISTA DEVUELVE GENERATOR USAMOS EL CONSTRUCTOR LIST

numeros = ["1", "2", "3"]
numeros_int = list(map(int, numeros))

def aplicar_iva(precio):
    return precio * 1.21

precios = [10, 20, 30]
finales = list(map(aplicar_iva, precios))

lineas = [" hola ", " adios ", "   que tal?"]
limpias = list(map(str.strip, lineas))

a = [1, 2, 3]
b = [10, 20, 30]

resultado = list(map(lambda x, y: x + y, a, b))
