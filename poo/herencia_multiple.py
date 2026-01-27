class Animal:
    
    def __init__(self):
        pass

    def comer(self):
        pass


class Mamifero(Animal): 
    def __init__(self):
        pass       
    
    def amamantar(self):
        pass

    
class Ave(Animal): 
    def __init__(self):
        pass

    def volar(self):
        pass

class Murcielago(Mamifero,Ave):
    def __init__(self):
        super().__init__()
        
murcielago = Murcielago()
murcielago.comer()
murcielago.volar()

