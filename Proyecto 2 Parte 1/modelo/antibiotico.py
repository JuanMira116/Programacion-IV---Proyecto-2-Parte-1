
from decimal import Decimal
from .producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, dosis: float, tipo_animal: str, precio: Decimal):
        super().__init__(nombre, precio)

        if not isinstance(dosis, (int, float)):
            raise ValueError("La dosis debe ser un número.")
        if dosis < 400 or dosis > 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")
        self._dosis = dosis

        if tipo_animal not in ["Bovino", "Caprino", "Porcino"]:
            raise ValueError("El tipo de animal debe ser 'Bovino', 'Caprino' o 'Porcino'.")
        self._tipo_animal = tipo_animal

    @property
    def dosis(self):
        return self._dosis

    @property
    def tipo_animal(self):
        return self._tipo_animal