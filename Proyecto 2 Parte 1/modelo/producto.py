
from decimal import Decimal

class Producto:
    def __init__(self, nombre: str, precio: Decimal):
        if not nombre:
            raise ValueError("El nombre del producto es obligatorio.")
        if precio is None or precio < 0:
            raise ValueError("El precio debe ser mayor o igual a 0.")
        self._nombre = nombre
        self._precio = Decimal(precio)

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    def __repr__(self):
        return f"{self._nombre} (${self._precio:.2f})"