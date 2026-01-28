import pytest

# =========================
# FUNCIONES A TESTEAR
# =========================

def sumar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def multiplicar(a, b):
    return a * b

def lista_valores():
    return [1, 2, 3, 4]

# =========================
# CLASES A TESTEAR
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
            raise ValueError("Edad inválida")
        self._edad = valor

    def es_mayor(self):
        return self.edad >= 18

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
# FIXTURES
# =========================

@pytest.fixture
def persona_adulta():
    return Persona(30)

@pytest.fixture
def numeros():
    return [1, 2, 3]

@pytest.fixture(scope="module")
def calc():
    return Calculadora()

# =========================
# TESTS DE FUNCIONES
# =========================

def test_sumar():
    assert sumar(2, 3) == 5

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_lista():
    datos = lista_valores()
    assert len(datos) == 4
    assert 1 in datos
    assert datos[-1] == 4

# =========================
# TESTS DE CLASES Y POO
# =========================

def test_persona_es_mayor(persona_adulta):
    assert persona_adulta.es_mayor() is True

def test_property_edad():
    p = Persona(25)
    assert p.edad == 25

def test_setter_edad_negativa():
    p = Persona(10)
    with pytest.raises(ValueError):
        p.edad = -5

def test_calc_sumar(calc):
    assert calc.sumar(2, 3) == 5

def test_calc_multiplicar(calc):
    assert calc.multiplicar(3, 4) == 12

def test_contador():
    Contador.total = 0
    Contador.incrementar()
    Contador.incrementar()
    assert Contador.total == 2

# =========================
# TEST PARAMETRIZADOS
# =========================

@pytest.mark.parametrize(
    "a,b,resultado",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
    ]
)
def test_sumar_parametrizado(a, b, resultado):
    assert sumar(a, b) == resultado

# =========================
# TESTS CON LISTAS Y FIXTURES
# =========================

def test_suma_lista(numeros):
    assert sum(numeros) == 6

# =========================
# TESTS DE MÉTODOS DE CLASE
# =========================

class TestPersona:

    def setup_method(self):
        self.persona = Persona(20)

    def test_es_mayor(self):
        assert self.persona.es_mayor() is True

    def test_cambiar_edad(self):
        self.persona.edad = 15
        assert self.persona.es_mayor() is False

# =========================
# FIN DEL ARCHIVO
# =========================
