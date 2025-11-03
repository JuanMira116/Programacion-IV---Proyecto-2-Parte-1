
from decimal import Decimal
from .producto import Producto

class ProductoControl(Producto):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_dias: int, precio: Decimal):
        super().__init__(nombre, precio)
        if not registro_ica:
            raise ValueError("El registro ICA es obligatorio.")
        if frecuencia_dias <= 0:
            raise ValueError("La frecuencia de aplicación debe ser mayor que 0.")
        self.registro_ica = registro_ica
        self.frecuencia_dias = frecuencia_dias