# Los conjuntos son como listas pero no tienen elementos
# repetidos, ni orden, son mutables
s = {1, 2, 3, 2}
print(s)  # {1, 2, 3} → los duplicados desaparecen

# USAR POR EJEMPLO
#     ELIMNAR DUPLICADOS DE UNA LISTA
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3}
    # PARA OPERACIONES MATEMÁTICAS DE CONJUNTOS
    # union, interseccion, diferencia, diferencia simétrica
a = {1, 2, 3}
b = {3, 4, 5}
c = {4,5,6}
print(a | b)  # unión → {1,2,3,4,5}
print(a & b)  # intersección → {3}
print(a - b)  # diferencia → {1,2}
print(a ^ b)  # diferencia simétrica → {1,2,4,5}
