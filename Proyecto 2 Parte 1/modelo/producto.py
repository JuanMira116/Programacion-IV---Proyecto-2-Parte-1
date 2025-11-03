
from decimal import Decimal

class Producto:
    def __init__(self, nombre: str, precio: Decimal):
        if not nombre:
            raise ValueError("El nombre del producto es obligatorio.")
        if precio is None or precio < 0:
            raise ValueError("El precio debe ser mayor o igual a 0.")
        self.nombre = nombre
        self.precio = Decimal(precio)

    def __repr__(self):
        return f"{self.nombre} (${self.precio})"