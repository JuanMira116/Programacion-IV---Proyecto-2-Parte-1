
from decimal import Decimal
from datetime import date
from .producto_control import ProductoDeControl

class ControlDeFertilizantes(ProductoDeControl):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: str, fecha_ultima_aplicacion: date, precio: Decimal):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, precio)
        if not isinstance(fecha_ultima_aplicacion, date):
            raise ValueError("La fecha de última aplicación debe ser un objeto tipo date.")
        self._fecha_ultima_aplicacion = fecha_ultima_aplicacion

    @property
    def fecha_ultima_aplicacion(self):
        return self._fecha_ultima_aplicacion