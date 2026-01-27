#Slicing (Cortar secuencias): lista[inicio:fin:paso]
lista = [0, 1, 2, 3, 4, 5]
ultimos = lista[-2:]       # [4, 5]
invertida = lista[::-1]    # [5, 4, 3, 2, 1, 0]
pares_idx = lista[::2]     # [0, 2, 4] (índices pares)
copia = lista[:]           # Copia superficial
# print(colores[1:4]) # desde la posición 1 hasta la posición anterior a 4, la 3
# print(colores[1:4]) # desde la posición 1 muestra (4-1) = 3 elementos -> 1 2 3

# Si se omite el valor inicial comienza desde 0.
# print(colores[:3])
# es lo mismo que
# print(colores[0:3])
# ['azul', 'blanco', 'verde']
# De la misma forma si omitimos el final se muestra hasta el final.
# print(colores[1:])
# es lo mismo que
# print(colores[1:len(colores)])
# ['blanco', 'verde', 'blanco']
# Si queremos ver los dos últimos colores se puede hacer
# print(colores[-2:])
# ['verde', 'blanco']
# Si omitimos ambos valores es la lista completa:
# print(colores[:])
# es lo mismo que
# print(colores[0:len(colores)])
# ['azul', 'blanco', 'verde', 'blanco']
# Al igual que con los elementos individuales se pueden asignar rangos que incluso pueden
# cambiar el tamaño de la lista:
# Por ejemplo:
# colores = [ 'azul', 'blanco', 'verde', 'blanco' ]
# colores[1:3]=["rojo","amarillo"]
# print(colores)
# ['azul', 'rojo', 'amarillo', 'blanco']
# En el que cambiamos el segundo elemento (blanco) por rojo y el tercero (verde) por
# amarillo.
# Pero incluso:
# colores = [ 'azul', 'blanco', 'verde', 'blanco' ]
# colores[1:2]=["rojo","amarillo"]
# print(colores)
# ['azul', 'rojo', 'amarillo', 'verde', 'blanco']
# Donde se cambia la segunda posición, blanco. por lo colores rojo y amarillo
# O borrar elementos:
# colores = [ 'azul', 'blanco', 'verde', 'blanco' ]
# colores[1:3]=["rojo"]
# print(colores)
# ['azul', 'rojo', 'blanco']
# Incluso vaciar la lista:
# colores[:]=[]
# En Python cuando se hace una asignación de una estructura, como puede ser una lista, no
# se copian los valores de una lista en otra, sino que a la nueva variable se la asigna la
# dirección de memoria de la primera (en el ejemplo a nuevosColores se le asigna la dirección
# de memoria de colores). Por lo que a todos los efectos son la misma variable y si se modifica
# una se modifica la otra ya que son la misma.
# En cambio slices devuelve una nueva lista por lo que:
# colores = [ 'azul', 'blanco', 'verde', 'blanco' ] # puede repetir valores
# nuevosColores=colores
# nuevosColores2=colores[:]
# nuevosColores[1]="negro"
# nuevosColores2[2]="marron"
# for color in colores:
# print(color, end=" ")
# azul negro verde blanco
# Pero si queremos comprobar si dos listas son iguales, se cumple si el valor devuelto por la
# función id es el mismo:
# print(id(nuevosColores)==id(colores))
# True
# print(id(nuevosColores2)==id(colores))
# False