
from .factura import Factura

class Cliente:
    def __init__(self, nombre: str, cedula: str):
        if not nombre:
            raise ValueError("El nombre es obligatorio.")
        if not cedula:
            raise ValueError("La cédula es obligatoria.")
        self._nombre = nombre
        self._cedula = cedula
        self._facturas = []

    def agregar_factura(self, factura: Factura):
        if not isinstance(factura, Factura):
            raise TypeError("Debe agregar un objeto de tipo Factura.")
        self._facturas.append(factura)

    @property
    def nombre(self):
        return self._nombre

    @property
    def cedula(self):
        return self._cedula

    @property
    def facturas(self):
        return list(self._facturas)