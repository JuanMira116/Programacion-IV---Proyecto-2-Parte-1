
import pytest
from decimal import Decimal
from datetime import date
from modelo.factura import Factura
from modelo.producto import Producto

def test_creacion_factura_valida():
    f = Factura(date.today())
    assert f.valor_total == Decimal("0.00")
    assert f.productos == []

def test_agregar_producto_valido():
    f = Factura(date.today())
    p = Producto("Vacuna", Decimal("10.00"))
    f.agregar_producto(p)
    assert len(f.productos) == 1
    assert f.valor_total == Decimal("10.00")

def test_fecha_invalida():
    with pytest.raises(ValueError):
        Factura("2025-01-01")

def test_agregar_producto_invalido():
    f = Factura(date.today())
    with pytest.raises(TypeError):
        f.agregar_producto("no_producto")