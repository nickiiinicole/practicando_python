"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.
- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.
Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""
# forma no tan eficiente peor difernete para raticar 
# lista_a = [2, 4, 2]
# lista_b = [3, 3, 4]

# def battle(lista_a, lista_b):
#     to_delete = []
#     for i, value in enumerate(lista_a):
#         if value > lista_b[i]:
#             if i + 1 < len(lista_a):
#                 lista_a[i+1]+=value
#         elif value == lista_b[i]:
#             to_delete.append(i)
#         else:
#              if i + 1 < len(lista_b):
#                 lista_b[i + 1] += lista_b[i]
#     # Eliminamos , acoradrse!!! empezando desde atrás para no romper índices!!
#     for i in reversed(to_delete):
#         del lista_a[i]
#         del lista_b[i]

#     if len(lista_a)== len(lista_b):
#         print("X")
#     elif len(lista_a)>len(lista_b):
#         print(f"{len(lista_a)}a")
#     else:
#         print(f"{len(lista_b)}b")

# battle(lista_a, lista_b)

# from os import system
# if system("clear") != 0: system("cls")

# Fuerza bruta: buscar la solución A SACO.
# Algoritmos ocultos o cálculos o fórmulas
# Programación dinámica: buscar una solución mas eficiente


def battle(lista_a, lista_b):
    puntos_a = sum(lista_a)
    puntos_b = sum(lista_b)
    return f"{puntos_a - puntos_b}a" if puntos_a > puntos_b else f"{puntos_b - puntos_a}b" if puntos_b > puntos_a else "x"


lista_a = [4, 4, 4]
lista_b = [2, 8, 2]
winner = battle(lista_a, lista_b)
print(winner)