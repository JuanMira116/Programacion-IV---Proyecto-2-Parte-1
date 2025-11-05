
from decimal import Decimal
from .producto_control import ProductoDeControl

class ControlDePlagas(ProductoDeControl):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: str, periodo_carencia: int, precio: Decimal):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, precio)
        if periodo_carencia < 0:
            raise ValueError("El periodo de carencia no puede ser negativo.")
        self._periodo_carencia = periodo_carencia

    @property
    def periodo_carencia(self):
        return self._periodo_carencia