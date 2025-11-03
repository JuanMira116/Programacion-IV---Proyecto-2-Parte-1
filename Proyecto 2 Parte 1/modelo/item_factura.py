
from decimal import Decimal, ROUND_HALF_UP
from .producto import Producto

class ItemFactura:
    def __init__(self, producto: Producto, cantidad: int):
        if not isinstance(producto, Producto):
            raise TypeError("El producto debe ser una instancia de Producto.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        self.producto = producto
        self.cantidad = cantidad
        self.total = (producto.precio * cantidad).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)