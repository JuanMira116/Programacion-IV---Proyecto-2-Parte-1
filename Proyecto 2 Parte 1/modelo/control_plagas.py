
from decimal import Decimal
from .producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_dias: int, periodo_carencia: int, precio: Decimal):
        super().__init__(registro_ica, nombre, frecuencia_dias, precio)
        if periodo_carencia < 0:
            raise ValueError("El periodo de carencia no puede ser negativo.")
        self.periodo_carencia = periodo_carencia