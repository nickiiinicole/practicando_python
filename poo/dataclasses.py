from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0  # Valor por defecto

    def valor_total(self) -> float:
        return self.precio * self.stock