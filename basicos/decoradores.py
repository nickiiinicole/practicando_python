import functools
import time

print("--- GUÍA MAESTRA DE DECORADORES PARA EXAMEN ---\n")

# ==============================================================================
# NIVEL 1: EL DECORADOR BÁSICO (La Plantilla Estándar)
# ==============================================================================
# Estructura: Una función que envuelve a otra.
# Uso: Logs, medir tiempo, validar cosas simples.

def mi_decorador_simple(funcion_original):
    """Este es el decorador (el papel de regalo)."""
    
    def wrapper(*args, **kwargs):
        """Este es el envoltorio (lo que se ejecuta realmente)."""
        print("1️⃣  NIVEL 1: Antes de ejecutar la función.")
        
        # AQUÍ ejecutamos la función original.
        # Usamos *args y **kwargs para que sirva con CUALQUIER función
        resultado = funcion_original(*args, **kwargs)
        
        print("1️⃣  NIVEL 1: Después de ejecutar la función.")
        
        # IMPORTANTE: Hay que devolver el resultado o se pierde.
        return resultado

    return wrapper

@mi_decorador_simple
def suma(a, b):
    print(f"   -> Ejecutando suma de {a} + {b}")
    return a + b

# Prueba Nivel 1
print(">>> Probando Decorador Básico:")
res = suma(5, 3)
print(f"   -> Resultado final: {res}\n")


# ==============================================================================
# NIVEL 2: DECORADORES CON PARÁMETROS (La Fábrica)
# ==============================================================================
# Estructura: 3 niveles de funciones (Inception).
# 1. La Fábrica (recibe el parámetro del decorador: veces=3).
# 2. El Decorador (recibe la función).
# 3. El Wrapper (recibe los argumentos de la función).

def repetir(veces):
    """NIVEL 1: La Fábrica. Recibe la configuración."""
    
    def decorador_real(funcion_original):
        """NIVEL 2: El Decorador. Recibe la función."""
        
        @functools.wraps(funcion_original) # Buena práctica: conserva el nombre original
        def wrapper(*args, **kwargs):
            """NIVEL 3: El Wrapper. Ejecuta la lógica."""
            print(f"2️⃣  NIVEL 2: Voy a repetir esto {veces} veces.")
            
            resultado = None
            for i in range(veces):
                print(f"   -> Repetición {i+1}")
                resultado = funcion_original(*args, **kwargs)
            
            return resultado
            
        return wrapper
    
    return decorador_real

@repetir(veces=3)
def saludar(nombre):
    print(f"   -> Hola {nombre}!")

# Prueba Nivel 2
print(">>> Probando Decorador con Parámetros:")
saludar("Ana")
print("\n")


# ==============================================================================
# NIVEL 3: DECORADORES BASADOS EN CLASES
# ==============================================================================
# Estructura: Usamos una clase en lugar de una función.
# __init__: Recibe la función a decorar.
# __call__: Hace el trabajo del 'wrapper'.

class DecoradorClase:
    def __init__(self, funcion_original):
        self.funcion_original = funcion_original
        self.llamadas = 0  # Podemos guardar estado (memoria) fácilmente

    def __call__(self, *args, **kwargs):
        self.llamadas += 1
        print(f"3️⃣  NIVEL 3: Llamada número {self.llamadas} a la clase decoradora.")
        return self.funcion_original(*args, **kwargs)

@DecoradorClase
def resta(a, b):
    return a - b

# Prueba Nivel 3
print(">>> Probando Decorador de Clase:")
resta(10, 5)
resta(20, 5)
print("\n")


# ==============================================================================
# NIVEL 4: EJEMPLO REAL DE EXAMEN (Validación)
# ==============================================================================
# Decorador que impide que una función reciba números negativos.

def validar_positivos(func):
    def wrapper(*args, **kwargs):
        # Revisamos los argumentos ANTES de llamar a la función
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"❌ Error: No se permiten negativos ({arg})")
        
        return func(*args, **kwargs)
    return wrapper

@validar_positivos
def calcular_area_cuadrado(lado):
    return lado * lado

# Prueba Nivel 4
print(">>> Probando Decorador de Validación:")
try:
    print(f"   -> Área de 5: {calcular_area_cuadrado(5)}")
    print("   -> Intentando con -5...")
    calcular_area_cuadrado(-5)
except ValueError as e:
    print(f"   -> Excepción capturada: {e}")