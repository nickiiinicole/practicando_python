import math
res = math.factorial(5) 

# def pedir_numero(mensaje, tipo=float):
#     """
#     Pide un dato repetidamente hasta que el usuario 
#     introduce el tipo correcto (int o float).
#     """
#     while True:
#         try:
#             valor = tipo(input(mensaje))
#             return valor
#         except ValueError:
#             print(f"Error: Por favor, introduce un número válido ({tipo.__name__}).")

# Uso:
# edad = pedir_numero("Dime tu edad: ", int)
# precio = pedir_numero("Dime el precio: ", float)

def pedir_numero(mensaje):
    valido = False      # Inicializamos la bandera en Falso
    numero = 0          # Variable para guardar el resultado
    
    while not valido:   # "Mientras NO sea válido, repite"
        entrada = input(mensaje)
        try:
            numero = float(entrada) # O int(entrada)
            valido = True           # ¡Éxito! Cambiamos la bandera para salir
        except ValueError:
            print("Error: Tienes que introducir un número.")
            
    return numero

def pedir_nota_rango(mensaje, minimo, maximo):
    valido = False
    numero = 0
    
    while not valido:
        entrada = input(mensaje)
        try:
            numero = float(entrada)
            # Aquí añadimos la lógica del rango
            if minimo <= numero <= maximo:
                valido = True  # Es número Y está en rango -> Salimos
            else:
                print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Eso no es un número.")
            
    return numero


def eliminar_duplicados(lista):
    nueva = []
    vistos = set()
    for item in lista:
        if item not in vistos:
            nueva.append(item)
            vistos.add(item)
    return nueva

# Aplanar lista de listas (Flatten): Convertir [[1,2], [3,4]] en [1,2,3,4].
lista_sucia = [[1, 2], [3, 4], [5]]
lista_plana = [item for sublista in lista_sucia for item in sublista]

# OPCIÓN B: 
def factorial_manual(n):
    if n < 0: raise ValueError("No existe factorial de negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def es_primo(n):
    if n < 2: return False
    # Solo comprobamos hasta la raíz cuadrada
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False # Encontramos un divisor, no es primo
    return True

def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        # El siguiente es la suma de los dos anteriores
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n] # Devuelve la lista cortada

# MCD
mcd = math.gcd(12, 18) # Da 6

# MCM (En Python 3.9+ existe math.lcm, si es viejo usa esto:)
def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Palíndromo (Capicúa): Detectar si se lee igual al revés (ignorando espacios y minúsculas).
def es_palindromo(texto):
    # Limpiamos: todo a minusculas y sin espacios
    texto_limpio = texto.lower().replace(" ", "")
    # Comparamos con su inversa
    return texto_limpio == texto_limpio[::-1]


# nagrama: Si dos palabras tienen las mismas letras.
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    # List comprehension + sum: Nivel Pro
    return sum(1 for letra in texto.lower() if letra in vocales)

# . El Decorador "Cronómetro"
# Si te piden "medir cuánto tarda una función", copia y pega esto. Es un decorador clásico.
import time

def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función '{funcion.__name__}' tardó {fin - inicio:.4f} segundos.")
        return resultado
    return envoltura

# Uso:
# @medir_tiempo
# def proceso_largo(): ...