class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular       # Público
        self._tipo = "Ahorro"        # Protected (Convención, accesible pero no se debe)
        self.__saldo = saldo         # Private (Nombre modificado, inaccesible directo)

    # Getter para privado
    @property
    def saldo(self):
        return self.__saldo

    # Setter para privado con validación
    @saldo.setter
    def saldo(self, cantidad):
        if cantidad >= 0:
            self.__saldo = cantidad
        else:
            raise ValueError("El saldo no puede ser negativo")

    def __str__(self): # Para imprimir bonito
        return f"Cuenta de {self.titular}"