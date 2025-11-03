
from decimal import Decimal
from .producto import Producto
from .tipo_animal import TipoAnimal

class Antibiotico(Producto):
    def __init__(self, nombre: str, dosis_kg: int, tipo_animal: TipoAnimal, precio: Decimal):
        super().__init__(nombre, precio)
        if dosis_kg < 400 or dosis_kg > 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")
        if not isinstance(tipo_animal, TipoAnimal):
            raise ValueError("El tipo de animal debe ser un valor del enum TipoAnimal.")
        self.dosis_kg = dosis_kg
        self.tipo_animal = tipo_animal