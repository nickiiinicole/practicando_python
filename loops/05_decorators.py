def mi_decorador(funcion_original):
    def envoltura(*args, **kwargs):
        print("--- Antes de ejecutar ---")
        resultado = funcion_original(*args, **kwargs)
        print("--- Después de ejecutar ---")
        return resultado
    return envoltura

@mi_decorador
def suma(a, b):
    return a + b