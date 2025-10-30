#Las tuplas son como listas pero no se pueden cambiar construida
#Se escriben con ()
# LA USAMOS CUANDO LOS DATOS NO VAYAN A CAMBIAR
#     COORDENADAS X,Y
    
point = (10, 20)  # no queremos que cambie

# Cuando queremos garantizar integridad
# Si pasas datos a una función y no quieres que se 
# modifiquen:

def process(data):
    # data no cambiará
    print(data)

process((1, 2, 3))

#Cuando quieres usarlas como claves en diccionarios
# Las listas no pueden ser claves (porque son mutables), 
# las tuplas sí:
my_dict = {(1, 2): "valor"}
print(my_dict[(1, 2)])  # "valor"
