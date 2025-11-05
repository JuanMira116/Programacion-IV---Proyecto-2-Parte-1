
from decimal import Decimal
from datetime import date
from .producto import Producto

class Factura:
    def __init__(self, fecha: date):
        if not isinstance(fecha, date):
            raise ValueError("La fecha es obligatoria y debe ser un objeto tipo date.")
        self._fecha = fecha
        self._productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Debe agregar un objeto de tipo Producto.")
        self._productos.append(producto)

    @property
    def fecha(self):
        return self._fecha

    @property
    def productos(self):
        return list(self._productos)

    @property
    def valor_total(self):
        return sum((p.precio for p in self._productos), Decimal("0.00"))

    def __repr__(self):
        return f"Factura ({self._fecha}) - Total: ${self.valor_total:.2f}"