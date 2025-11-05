
import pytest
from decimal import Decimal
from datetime import date
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.antibiotico import Antibiotico
from modelo.producto import Producto
from modelo.control_plagas import ControlDePlagas

def test_cliente_con_factura_simple():
    c = Cliente("Mario", "999")
    f = Factura(date.today())
    c.agregar_factura(f)
    assert len(c.facturas) == 1

def test_factura_con_multiples_productos_y_total():
    f = Factura(date.today())
    p1 = Producto("Desparasitante", Decimal("15.00"))
    p2 = Producto("Vitaminas", Decimal("5.00"))
    f.agregar_producto(p1)
    f.agregar_producto(p2)
    assert f.valor_total == Decimal("20.00")

def test_factura_con_antibiotico():
    f = Factura(date.today())
    a = Antibiotico("Penicilina", 500, "Caprino", Decimal("30.00"))
    f.agregar_producto(a)
    assert f.valor_total == Decimal("30.00")

def test_cliente_con_multiples_facturas_y_totales():
    c = Cliente("Laura", "888")
    f1 = Factura(date.today())
    f2 = Factura(date.today())
    p = Producto("Vacuna Triple", Decimal("20.00"))
    f1.agregar_producto(p)
    f1.agregar_producto(p)
    f2.agregar_producto(p)
    c.agregar_factura(f1)
    c.agregar_factura(f2)
    total_cliente = sum(f.valor_total for f in c.facturas)
    assert total_cliente == Decimal("60.00")

def test_factura_con_producto_control():
    f = Factura(date.today())
    p = ControlDePlagas("ICA001", "PlagaStop", 15, 10, Decimal("50.00"))
    f.agregar_producto(p)
    f.agregar_producto(p)
    assert f.valor_total == Decimal("100.00")

def test_cliente_agrega_factura_invalida():
    c = Cliente("Mario", "999")
    with pytest.raises(TypeError):
        c.agregar_factura("no_factura")

def test_factura_agregar_producto_invalido():
    f = Factura(date.today())
    with pytest.raises(TypeError):
        f.agregar_producto("cadena")