###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
codigo = mensaje[7:]
print(f"{codigo}")

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:

numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
numeros[0], numeros[-1] = numeros[-1], numeros[0] #acooooordarse!!!!!!!!!
print(numeros) 

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
sandwich = sandwich = pan + ingredientes + pan_abajo

# Ejercicio 4: Duplicando la lista
# Dada una lista:

lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista_duplicate = lista+lista

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.

lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista
#  (utilizando slicing y concatenación).

lista = [1, 2, 3, 4, 5, 6] #-> Resultado: [3, 2, 1, 4, 5, 6]
mitad = len(lista) // 2
#toma la primera mitad despues la otra:D
lista_reverse = lista[:mitad][::-1] + lista[mitad:]
print(lista_reverse)

#EJercicio 7
# Mitades invertidas, dada una lista invierte la segunda mitad de la lista(no la primera)
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
# acordarse de lista[inicio:fin:paso] , inicio-> indice que comienza incluido
# fin ,hsta donde llega sin incluir
# paso , de cuanto en cuanto
# -1 -> inivierte la lista lista[::-1]

lista_duplicate = lista[:mitad]+ lista[mitad:][::-1]
print(lista_duplicate)

# Ejercicio 8 
# cada dos elementos , muestra solo los elementos pares de la lsira:
numeros = [10, 20, 30, 40, 50, 60]
print(numeros[::2])

# Ejercicio 9
# muestra la lista invertida con slicing
letras = ["a", "b", "c", "d", "e"]
print(letras[::-1])

# Ejerciicio 10
# muestra solo la sgda mitad de una lista (si tine un numero impar ignora el meido)
lista = [1, 2, 3, 4, 5, 6, 7]
mitad = len(lista)//2
print(lista[mitad+1:])

# Ejercicio 11
# extrae los 3 elem del medio de una lista
lista = [1, 2, 3, 4, 5, 6, 7]
mitad = len(lista)//2
sublista = lista[mitad-1:mitad+2]
print(sublista)

# Ejercicio 12: El espejo
# Duplica la lista, pero la segunda mitad debe estar invertida (como un espejo).
lista = [1, 2, 3]
lista_duplicate= lista+ lista[::-1]
print(lista_duplicate)

# Ejercicio 13: toma solo cada tercer elemento de la lista
lista = list(range(1, 16))  
salto3 = lista[::3]
print(salto3)  

# Ejercicio 14: Quitar extremos
# Elimina el primer y el último elemento usando slicing.
frutas = ["🍎", "🍌", "🍓", "🍇", "🍉"]
trim_frutas = frutas[1:-1]
print(trim_frutas)

# Ejercicio 15: Rotar lista (shift)
# Desplaza los elementos una posición hacia la izquierda.
lista = [1, 2, 3, 4, 5]
rotada = lista[1:] + lista[:1]
print(rotada)
