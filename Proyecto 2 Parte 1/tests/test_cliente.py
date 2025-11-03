
import pytest
from modelo.cliente import Cliente
from modelo.factura import Factura

def test_creacion_cliente_valido():
    c = Cliente("Juan Perez", "123")
    assert c.nombre == "Juan Perez"
    assert c.cedula == "123"
    assert c.facturas == []

def test_agregar_factura_valida():
    c = Cliente("Ana", "321")
    f = Factura.__new__(Factura)  
    c.agregar_factura(f)
    assert len(c.facturas) == 1

def test_nombre_obligatorio():
    with pytest.raises(ValueError):
        Cliente("", "123")

def test_cedula_obligatoria():
    with pytest.raises(ValueError):
        Cliente("Juan", "")

def test_agregar_factura_invalida():
    c = Cliente("Carlos", "555")
    with pytest.raises(TypeError):
        c.agregar_factura("no es factura")

def test_facturas_es_lista_copiada():
    c = Cliente("Laura", "111")
    facturas1 = c.facturas
    facturas1.append("falsa")
    assert len(c.facturas) == 0 