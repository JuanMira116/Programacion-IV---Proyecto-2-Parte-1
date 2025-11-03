
from decimal import Decimal
from datetime import date
from .producto_control import ProductoControl

class ControlFertilizante(ProductoControl):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_dias: int, fecha_ultima_aplicacion: date, precio: Decimal):
        super().__init__(registro_ica, nombre, frecuencia_dias, precio)
        if not isinstance(fecha_ultima_aplicacion, date):
            raise ValueError("La fecha de la última aplicación es obligatoria y debe ser un objeto tipo date.")
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion