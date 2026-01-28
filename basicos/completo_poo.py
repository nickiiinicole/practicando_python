class Droid:
    def __init__(self, modelo, energia):
        self.modelo = modelo
        self._energia = energia

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if valor < 0:
            self._energia = 0
        else:
            self._energia = valor

    def usar(self):
        self.energia -= 10

    @staticmethod
    def es_funcional(energia):
        return energia > 0

    @classmethod
    def crear_estandar(cls, modelo):
        return cls(modelo, 100)
