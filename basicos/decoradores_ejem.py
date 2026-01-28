# Crear un decorador que muestre un mensaje antes y después de ejecutar una función.
def log(func):
    def wrapper():
        print("Antes")
        func()
        print("Después")
    return wrapper


@log
def saludar():
    print("Hola")

# El decorador debe funcionar con cualquier número de parámetros y devolver el resultado.
def log(func):
    def wrapper(*args, **kwargs):
        print("Ejecutando función")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper


@log
def sumar(a, b):
    return a + b

# Crear un decorador que muestre los argumentos recibidos.
def debug(func):
    def wrapper(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper

# Crear un decorador que ejecute la función N veces.
@debug
def saludar(nombre, saludo="Hola"):
    return f"{saludo} {nombre}"

def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador


@repetir(3)
def beep():
    print("Beep")

# Aplicar un decorador a un método de una clase.
def log_metodo(func):
    def wrapper(self, *args, **kwargs):
        print("Llamando al método")
        return func(self, *args, **kwargs)
    return wrapper


class Robot:
    @log_metodo
    def encender(self):
        print("Robot encendido")

# Crear un decorador que solo permita argumentos enteros.

def validar_ints(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Solo se permiten enteros")
        return func(*args, **kwargs)
    return wrapper


@validar_ints
def suma(a, b):
    return a + b

