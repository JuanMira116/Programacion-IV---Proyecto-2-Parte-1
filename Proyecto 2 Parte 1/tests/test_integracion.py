
import pytest
from decimal import Decimal
from datetime import date
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.item_factura import ItemFactura
from modelo.antibiotico import Antibiotico
from modelo.producto import Producto
from modelo.tipo_animal import TipoAnimal
from modelo.control_plagas import ControlPlagas

def test_cliente_con_factura_simple():
    c = Cliente("Mario", "999")
    f = Factura(date.today())
    c.agregar_factura(f)
    assert len(c.facturas) == 1

def test_factura_con_multiples_items_y_totales():
    f = Factura(date.today())
    p1 = Producto("Desparasitante", Decimal("15.00"))
    p2 = Producto("Vitaminas", Decimal("5.00"))
    f.agregar_item(ItemFactura(p1, 2))
    f.agregar_item(ItemFactura(p2, 3))
    assert f.total == Decimal("45.00")

def test_factura_con_antibiotico():
    f = Factura(date.today())
    a = Antibiotico("Penicilina", 500, TipoAnimal.CAPRINO, Decimal("30.00"))
    f.agregar_item(ItemFactura(a, 1))
    assert f.total == Decimal("30.00")

def test_cliente_con_multiples_facturas_y_totales():
    c = Cliente("Laura", "888")
    f1 = Factura(date.today())
    f2 = Factura(date.today())
    p = Producto("Vacuna Triple", Decimal("20.00"))
    f1.agregar_item(ItemFactura(p, 2))
    f2.agregar_item(ItemFactura(p, 1))
    c.agregar_factura(f1)
    c.agregar_factura(f2)
    total_cliente = sum(f.total for f in c.facturas)
    assert total_cliente == Decimal("60.00")

def test_factura_con_producto_control():
    f = Factura(date.today())
    p = ControlPlagas("ICA001", "PlagaStop", 15, 10, Decimal("50.00"))
    f.agregar_item(ItemFactura(p, 2))
    assert f.total == Decimal("100.00")

def test_cliente_agrega_factura_invalida():
    c = Cliente("Mario", "999")
    with pytest.raises(TypeError):
        c.agregar_factura("no_factura")

def test_factura_con_item_invalido():
    f = Factura(date.today())
    with pytest.raises(TypeError):
        f.agregar_item("cadena")

def test_item_factura_con_producto_invalido():
    from modelo.item_factura import ItemFactura
    with pytest.raises(TypeError):
        ItemFactura("no_producto", 2)

def test_item_factura_con_cantidad_invalida():
    from modelo.item_factura import ItemFactura
    from modelo.producto import Producto
    p = Producto("Antipulgas", Decimal("12.00"))
    with pytest.raises(ValueError):
        ItemFactura(p, 0)