import pytest
import math

# Úsalo cuando el enunciado diga: "La función debe lanzar un error si..."
def test_prueba_error_especifico():
    # Contexto: "Espero que lo siguiente falle"
    with pytest.raises(ValueError) as info_error:
        # Aquí llamas a la función que debe fallar
        tu_funcion(-1) 
    
    # Opcional: Verificar el mensaje del error
    assert "no puede ser negativo" in str(info_error.value)

# IMPORTANTE: Nunca uses == con floats (decimales). Usa pytest.approx.
def test_calculos_matematicos():
    resultado = math.sqrt(2) # 1.414213...
    
    # Incorrecto: assert resultado == 1.414 
    # Correcto:
    assert resultado == pytest.approx(1.4142, rel=1e-3)



# Para probar 5 casos distintos sin escribir 5 funciones. 
# Estructura: "nombre_input1, nombre_input2, esperado"
@pytest.mark.parametrize("entrada_a, entrada_b, esperado", [
    (2, 3, 5),      # Caso 1: Positivos
    (-1, 1, 0),     # Caso 2: Negativos
    (0, 0, 0),      # Caso 3: Ceros
    (100, -100, 0)  # Caso 4: Grandes
])
def test_suma_varios_casos(entrada_a, entrada_b, esperado):
    assert (entrada_a + entrada_b) == esperado