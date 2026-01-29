def log_accion(function):
    def wrapper(*args,**kwargs):

        print("--- LOG DEL SISTEMA: Ejecutando acción... ---")
        result = function(*args, **kwargs)
        return result
    return wrapper


def verificar_espacio(function):
    def wrapper(*args,**kwargs):
        print("Verificando espacio de la mochila")
        result = function(*args, **kwargs)
        return result
    return wrapper


class Item:

    def __init__(self, nombre:str, tipo:str, valor:int):
        self.nombre = nombre
        self.tipo = tipo

class Mochila:
    def __init__(self, capacidad_max:int,contenido=[], oro=0):
        self.capacidad = capacidad_max
        self.contenido = contenido
        self.oro = oro

    @log_accion
    @verificar_espacio
    def agregar_item(self, item:Item):
        self.contenido.append(item)
        print(f"{item.nombre} agregado a la mochila")
    
    def mostrar_inventario(self):
        print("Inventario de la mochila:")
        for i, item in enumerate(self.contenido):
            print(f"{i}. {item.nombre} ({item.tipo} - Valor {item.valor})")
        