####
#
####
# 1. MANEJO DE ERRORES EN PYTHON

# try – except
# Sirve para evitar que el programa se cierre cuando ocurre un error.

# Ejemplo:
try:
    x = 10 / 0
except:
    print("Ha ocurrido un error")


# 2. Detectar tipos de error específicos

try:
    x = int("hola")
except ValueError:
    print("Error: No es un número")

# Principales errores frecuentes:

# ValueError

# TypeError

# ZeroDivisionError

# FileNotFoundError

# IndexError

# 3. Multiples except

try:
    
    x = 10 / 0
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
except Exception:
    print("Error desconocido")

# else
# Se ejecuta solo si NO hubo errores. ?¿finally

try:
    x = 5 / 1
except ZeroDivisionError:
    print("Error")
else:
    print("Todo salió bien")

# finally
# Se ejecuta siempre, haya error o no.
# Útil para cerrar archivos, conexiones, etc.

try:
    x = 5 / 0
except:
    print("Error")
finally:
    print("Fin del programa")

# Capturar el error dentro de una variable

try:
    x = 10 / 0
except Exception as e:
    print("Error:", e)

# Lanzar errores manualmente (raise)

edad = -1

if edad < 0:
    raise ValueError("La edad no puede ser negativa")
    # como el throw

# EJEMPLITO COMPLETICO :D

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except TypeError:
        print("Debes introducir números")
    else:
        print("Resultado:", resultado)
    finally:
        print("Operación finalizada")

dividir(10, 2)
dividir(10, 0)
dividir("a", 5)

