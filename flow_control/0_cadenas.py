# CADENAS EN PYTHON


# INMUTABILIDAD DE LAS CADENAS
# En Python las cadenas SON INMUTABLES.
# Esto significa que no puedes modificar una cadena directamente, solo crear una nueva.


# Ejemplo:
# mensaje = "hola"
# mensaje = mensaje.upper()   # crea una nueva cadena
# print(mensaje)  # "HOLA"
# Python no da error al “cambiar” una cadena porque en realidad está creando otra nueva, no modificando la anterior.
# Ejemplo de método:
# 'temperatures and facts about the moon'.title()



# DIVIDIR UNA CADENA
# El método .split() divide una cadena y devuelve una lista.


# Sin argumentos, separa por espacios:
texto = "hola mundo desde python"
partes = texto.split()
print(partes)
# ['hola', 'mundo', 'desde', 'python']
# Con salto de línea:
temperatures = '''Daylight: 260 F
Nighttime: -280 F'''
print(temperatures.split())
['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']



# BUSCAR EN UNA CADENA
# Puedes usar el operador in para saber si un texto contiene otro.


# Ejemplos:
# 'Moon' in 'This text talks about space'    # False
# 'Moon' in 'This text talks about the Moon' # True



# MÉTODO find()
# Busca una palabra y devuelve el índice donde aparece.
# Si no la encuentra, devuelve -1.


temperatures = "Saturn has -170 and Mars has -28 Celsius"
print(temperatures.find("Mars"))  # Devuelve el índice
print(temperatures.find("Jupiter"))  # -1 (no encontrado)



# MÉTODO count()
# Devuelve cuantas veces aparece una palabra o letra.


temperatures = "Moon, Moon, Mars"
print(temperatures.count("Moon"))  # 2



# MÉTODO replace()
# Sirve para sustituir una palabra por otra.


texto = "Celsius is a temperature scale"
nuevo = texto.replace("Celsius", "C")
print(nuevo)



# MÉTODO join()
# Convierte una lista de cadenas en una sola cadena, uniendo con el carácter que elijas.


moon_facts = [
'The Moon is drifting away from Earth.',
'The Moon moves 4 cm every year.'
]
texto = '\n'.join(moon_facts)
print(texto)
# Salida:
# The Moon is drifting away from Earth.
# The Moon moves 4 cm every year.


# title()
# Primera letra en mayúsculas de cada palabra.

"hola mundo".title()

# capitalize()
# Primera letra en mayúsculas, el resto en minúsculas.

"hola MUNDO".capitalize()


# strip()
# Elimina espacios al principio y final.

" hola ".strip()

# lstrip() → quita a la izquierda

# rstrip() → quita a la derecha



# zfill()
# Rellena con ceros a la izquierda hasta el tamaño indicado.

"7".zfill(3) # 007

# center(), ljust(), rjust()
# Alinea texto rellenando con espacios o caracteres.

"hi".center(10)
"hi".ljust(10, '-')
"hi".rjust(10, '.')

# FORMATEADORES DE CADENA

# isalpha()
# Comprueba si solo hay letras.

"Hola".isalpha()

# a) f-strings (el más moderno):
nombre = "Juan"
edad = 25
print(f"Me llamo {nombre} y tengo {edad}")
# b) format():
print("Me llamo {} y tengo {}".format(nombre, edad))
# c) % (estilo antiguo):
print("Me llamo %s y tengo %d" % (nombre, edad))



# RESUMEN:D

# Las cadenas son inmutables → no se modifican, se crean nuevas.


# split() → divide texto en elementos de lista.


# in → comprobar si una palabra está en el texto.


# find() → posición donde aparece.


# count() → cuántas veces aparece.


# replace() → reemplaza palabras.


# join() → une lista en un texto.


# f-strings → la forma moderna de formatear.


