"""
04 - Listas: Métodos Fundamentales y Operaciones Avanzadas

Módulo para demostrar las funcionalidades esenciales y avanzadas (filter)
de la estructura de datos 'list' en Python.
"""

from os import system

# Configuración inicial para limpiar la consola en diferentes sistemas operativos
def clear_console():
    """Limpia la consola. Compatible con sistemas UNIX y Windows."""
    if system("clear") != 0:
        system("cls")

clear_console()


## 1. Métodos de Modificación y Mutación
# -------------------------------------

lista_basica = ['a', 'b', 'c', 'd']
print(f"Lista inicial: {lista_basica}\n")

# Añadir o insertar elementos
# Utilizar .append() es O(1) en tiempo promedio, la forma más eficiente de añadir.
lista_basica.append('e')  # Añade un elemento al final
print(f"Después de .append('e'): {lista_basica}")

# .insert() es O(n) ya que requiere desplazar el resto de elementos, evitar en listas muy grandes.
lista_basica.insert(1, '@')  # Inserta '@' en el índice 1
print(f"Después de .insert(1, '@'): {lista_basica}")

# .extend() para fusionar de forma eficiente (O(k) donde k es la longitud del iterable).
lista_basica.extend(['😃', '😍'])  # Agrega elementos de un iterable al final
print(f"Después de .extend(['😃', '😍']): {lista_basica}\n")

# Eliminar elementos de la lista
# .remove() busca el valor O(n) y luego elimina O(n), por lo que es O(n).
lista_basica.remove('@')  # Elimina la primera aparición del valor '@'
print(f"Después de .remove('@'): {lista_basica}")

# .pop() es O(1) si no se especifica índice (elimina el último).
ultimo_elemento = lista_basica.pop()
print(f"Elemento eliminado con .pop(): {ultimo_elemento}")
print(f"Lista después de .pop(): {lista_basica}")

# .pop(i) es O(n)
lista_basica.pop(1)  # Elimina el elemento en el índice 1 ('c' o 'd' dependiendo del estado)
print(f"Después de .pop(1): {lista_basica}")

# Usar 'del' para eliminar por índice/slicing. Eficiente si se conoce el índice.
del lista_basica[-1]  # Elimina el último elemento
print(f"Después de del lista_basica[-1]: {lista_basica}")

# Eliminar todos los elementos de manera eficiente.
lista_basica.clear()
print(f"Después de .clear(): {lista_basica}")

# Eliminar un rango de elementos usando slicing y del.
lista_slicing = ['🐼', '🐨', '🐶', '😿', '🐹']
# El slicing [1:3] incluye el índice 1 y 2, excluyendo el 3.
del lista_slicing[1:3]
print(f"Lista después de del lista_slicing[1:3]: {lista_slicing}\n")


## 2. Métodos de Ordenamiento y Consulta
# -------------------------------------

numbers = [3, 10, 2, 8, 99, 101]

# .sort(): Ordena la lista IN-PLACE (mutación). Es más eficiente en memoria.
print('--- Ordenar listas ---')
print(f"Lista original antes de .sort(): {numbers}")
numbers.sort()
print(f"Lista después de .sort() (mutada): {numbers}")

# sorted(): Devuelve una NUEVA lista ordenada (no muta la original).
numbers_unsorted = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers_unsorted)
print(f"Lista original después de sorted(): {numbers_unsorted} (sin mutar)")
print(f"Nueva lista ordenada con sorted(): {sorted_numbers}")

# Ordenar con 'key' para personalización (O(n log n))
print("\n--- Ordenar strings con key ---")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
# La key=str.lower permite ordenar ignorando la capitalización
frutas.sort(key=str.lower)
print(f"Lista ordenada con key=str.lower: {frutas}")

# Métodos de consulta
print('\n--- Métodos de Consulta ---')
animals = ['🐶', '🐼', '🐨', '🐶']
print(f"Tamaño de la lista (len()): {len(animals)}")
print(f"Veces que aparece '🐶' (.count()): {animals.count('🐶')}")
print(f"Comprobar existencia de '🐼' ('in'): {'🐼' in animals}")
print(f"Comprobar existencia de '🐹' ('in'): {'🐹' in animals}\n")


## 3. Uso Avanzado: La función filter()
# -------------------------------------

# filter() es una función de orden superior que aplica una función
# booleana a cada elemento de un iterable y devuelve un iterador
# con los elementos que resultaron True. Es una alternativa 'funcional'
# a las list comprehensions.

print('--- Operación filter() ---')

# Ejemplo 1: Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
# Se usa lambda para la función de predicado: x % 2 == 0
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Ejemplo 2: Filtrar diccionarios por valor
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Libro", "precio": 20},
    {"nombre": "Monitor", "precio": 150}
]
# Filtrar productos cuyo precio es mayor a 100
caros = list(filter(lambda p: p["precio"] > 100, productos))
print(f"Productos caros (>100): {caros}")

# Nota: Para la mayoría de los casos de uso, las 'list comprehensions'
# suelen ser más legibles y performantes que list(filter(...)).
# Ejemplo equivalente con list comprehension:
# caros_lc = [p for p in productos if p["precio"] > 100]

## 4. Uso Avanzado: La función ALL()
# -------------------------------------

# all(iterable) Devuelve True si TODOS los elementos cumplen la condición (o son True)
numeros = [2, 3, 6]
resultado = all(n % 2 == 0 for n in numeros)
print(resultado)   # False

# Any , Devuelve True si AL MENOS UN elemento cumple la condición.
numeros = [1, 3, 4, 7]
resultado = any(n % 2 == 0 for n in numeros)
print(resultado)   # True

numeros = [1, 3, 5]
resultado = any(n % 2 == 0 for n in numeros)
print(resultado)   # False


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
lista = [i for i in range(1,6)]

# Añade el número 6 al final usando append().
lista.insert(len(lista), 6)
# Inserta el número 10 en la posición 2 usando insert().
lista.insert(2,10)
# Modifica el primer elemento de la lista para que sea 0.
lista[0]= 0
# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
lista_a.extend(lista_b)
print(lista_a)
# Elimina la primera aparición del número 1 en lista_a usando remove().
lista_a.remove(1)
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
print(lista_a.pop(3))
# Limpia completamente lista_b usando clear().
lista_b.clear()
# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.


# --------------------------------------------------------------
# EJERCICIOS A PARTE
# I. EJERCICIOS FUNDAMENTALES (Revisión y Consolidación)
# Ejercicio 1: Gestión de Stock y Rendimiento
# Crea una lista llamada inventario con los números del 1 al 10.

# Utiliza el método más eficiente para añadir los números 11 y 12 al final.

# Utiliza pop() sin argumentos para simular la venta del último producto. Almacena su valor en una variable y imprímela.

# El producto con ID 5 ha sido retirado. Usa remove() para eliminar el primer 5 de la lista.

# Imprime el estado final del inventario.

# Ejercicio 2: Slicing Avanzado y Mutación
# Crea una lista alfabeto que contenga las letras de 'a' a 'j'.

# Utiliza una asignación con slicing (lista[i:j] = ...) para reemplazar las letras 'c', 'd', 'e' por las letras 'x', 'y', 'z'.

# Utiliza el comando del con slicing para eliminar las letras 'h', 'i' y 'j' de una sola vez.

# Imprime el alfabeto resultante.

# Ejercicio 3: Copia Profunda vs. Copia Superficial (Referencia)
# Crea una lista original = [1, [2, 3], 4].

# Crea una copia superficial (shallow copy) llamada copia_s usando list.copy() o slicing.

# Crea una copia profunda (deep copy) llamada copia_p importando copy y usando copy.deepcopy().

# Modifica el primer elemento de la lista anidada dentro de original (es decir, cambia el 2 a 99).

# Imprime original, copia_s y copia_p. Explica en un comentario por qué copia_s se vio afectada y copia_p no.