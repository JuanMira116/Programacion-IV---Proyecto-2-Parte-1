
from .factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: str):
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if not cedula:
            raise ValueError("La cédula es obligatoria.")
        self.nombre = nombre
        self.cedula = cedula
        self._facturas = []

    def agregar_factura(self, factura: 'Factura'):
        if not isinstance(factura, Factura):
            raise TypeError("Debe agregar un objeto de tipo Factura.")
        self._facturas.append(factura)

    @property
    def facturas(self):
        return list(self._facturas)