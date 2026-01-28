from dataclasses import dataclass

# =========================
# 1️⃣ CLASE BASICA CON METODOS
# =========================
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 10 if self.velocidad >= 10 else 0


# =========================
# 2️⃣ ATRIBUTO PRIVADO + PROPERTY
# =========================
class Persona:
    def __init__(self, edad):
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("Edad no puede ser negativa")
        self._edad = valor

    def es_mayor(self):
        return self.edad >= 18


# =========================
# 3️⃣ STATICMETHOD Y CLASSMETHOD
# =========================
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def multiplicar(a, b):
        return a * b


class Contador:
    total = 0

    @classmethod
    def incrementar(cls):
        cls.total += 1


# =========================
# 4️⃣ HERENCIA Y POLIMORFISMO
# =========================
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hace un sonido")


class Perro(Animal):
    def hablar(self):
        print("Guau")


# =========================
# 5️⃣ METODOS ESPECIALES (__str__)
# =========================
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.precio}€"


# =========================
# 6️⃣ COMPOSICION
# =========================
class Motor:
    def encender(self):
        print("Motor encendido")


class CocheConMotor:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()


# =========================
# 7️⃣ VALIDACION DE METODOS
# =========================
class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad


# =========================
# 8️⃣ LISTAS DE OBJETOS + FILTRO
# =========================
@dataclass
class Droid:
    nombre: str
    energia: int

    def activo(self):
        return self.energia > 0


# Crear droides y filtrar
droides = [
    Droid("R2", 80),
    Droid("C3", 0),
    Droid("BB8", 50),
    Droid("K2", 0),
]

droides_activos = [d for d in droides if d.activo()]


# =========================
# 9️⃣ DECORADOR DENTRO DE POO
# =========================
def log_metodo(func):
    def wrapper(self, *args, **kwargs):
        print(f"Ejecutando {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper


class DroidConRecarga:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

    @log_metodo
    def recargar(self, cantidad):
        self.energia += cantidad


# =========================
# 10️⃣ DATACLASS + FILTRO CON LIST COMPREHENSION
# =========================
@dataclass
class DroidData:
    id: int
    modelo: str
    energia: int

droides_data = [
    DroidData(1, "R2", 80),
    DroidData(2, "C3", 40),
    DroidData(3, "BB8", 20),
    DroidData(4, "K2", 100),
]

droides_mayor_50 = [d for d in droides_data if d.energia > 50]


# =========================
# EJEMPLOS DE USO / PRUEBA
# =========================
if __name__ == "__main__":
    # Coche
    coche = Coche("Toyota", "Corolla")
    coche.acelerar()
    coche.frenar()
    print(coche.velocidad)

    # Persona
    p = Persona(20)
    print(p.es_mayor())

    # Contador
    Contador.total = 0
    Contador.incrementar()
    Contador.incrementar()
    print(Contador.total)

    # Animal
    perro = Perro("Firulais")
    perro.hablar()

    # Producto
    prod = Producto("Libro", 20)
    print(prod)

    # Coche con motor
    coche_m = CocheConMotor()
    coche_m.arrancar()

    # Cuenta bancaria
    cuenta = CuentaBancaria(100)
    try:
        cuenta.retirar(50)
        cuenta.retirar(100)
    except ValueError as e:
        print(e)

    # Droid recarga
    droid = DroidConRecarga("R2", 50)
    droid.recargar(20)
    print(droid.energia)

    # Filtrado droides data
    for d in droides_mayor_50:
        print(d.modelo, d.energia)
