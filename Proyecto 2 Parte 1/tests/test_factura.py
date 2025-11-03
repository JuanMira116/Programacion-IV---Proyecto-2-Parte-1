
import pytest
from decimal import Decimal
from datetime import date
from modelo.factura import Factura
from modelo.item_factura import ItemFactura
from modelo.producto import Producto

def test_creacion_factura_valida():
    f = Factura(date.today())
    assert f.total == Decimal("0.00")
    assert f.items == []

def test_agregar_item_valido():
    f = Factura(date.today())
    p = Producto("Vacuna", Decimal("10.00"))
    item = ItemFactura(p, 3)
    f.agregar_item(item)
    assert f.total == Decimal("30.00")
    assert len(f.items) == 1

def test_fecha_invalida():
    with pytest.raises(ValueError):
        Factura("2025-01-01") 

def test_agregar_item_invalido():
    f = Factura(date.today())
    with pytest.raises(TypeError):
        f.agregar_item("no_item")