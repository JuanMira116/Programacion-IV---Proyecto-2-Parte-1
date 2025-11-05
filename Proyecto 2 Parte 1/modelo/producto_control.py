
from decimal import Decimal
from .producto import Producto

class ProductoDeControl(Producto):
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: str, precio: Decimal):
        super().__init__(nombre, precio)
        if not registro_ica:
            raise ValueError("El registro ICA es obligatorio.")
        if not frecuencia_aplicacion:
            raise ValueError("La frecuencia de aplicación es obligatoria.")
        self._registro_ica = registro_ica
        self._frecuencia_aplicacion = frecuencia_aplicacion

    @property
    def registro_ica(self):
        return self._registro_ica

    @property
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion