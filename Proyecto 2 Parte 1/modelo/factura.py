
from decimal import Decimal
from datetime import date
from .item_factura import ItemFactura

class Factura:
    def __init__(self, fecha: date):
        if not isinstance(fecha, date):
            raise ValueError("La fecha es obligatoria.")
        self.fecha = fecha
        self._items = []
        self._total = Decimal("0.00")

    def agregar_item(self, item: ItemFactura):
        if not isinstance(item, ItemFactura):
            raise TypeError("Debe agregar un objeto de tipo ItemFactura.")
        self._items.append(item)
        self._recalcular_total()

    def _recalcular_total(self):
        self._total = sum((item.total for item in self._items), Decimal("0.00"))

    @property
    def total(self):
        return self._total

    @property
    def items(self):
        return list(self._items)