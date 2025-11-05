
import pytest
from decimal import Decimal
from datetime import date
from modelo.producto_control import ProductoDeControl
from modelo.control_fertilizantes import ControlDeFertilizantes
from modelo.control_plagas import ControlDePlagas

def test_control_fertilizante_valido():
    f = ControlDeFertilizantes("ICA123", "FertiMax", "30 días", date.today(), Decimal("40.00"))
    assert f.registro_ica == "ICA123"
    assert f.frecuencia_aplicacion == "30 días"
    assert isinstance(f.fecha_ultima_aplicacion, date)

def test_control_plagas_valido():
    p = ControlDePlagas("ICA777", "PlagaKill", "15 días", 5, Decimal("30.00"))
    assert p.registro_ica == "ICA777"
    assert p.frecuencia_aplicacion == "15 días"
    assert p.periodo_carencia == 5

def test_control_fertilizante_fecha_invalida():
    with pytest.raises(ValueError):
        ControlDeFertilizantes("ICA123", "FertiMax", "30 días", "ayer", Decimal("40.00"))

def test_producto_control_frecuencia_invalida():
    with pytest.raises(ValueError):
        ProductoDeControl("ICA000", "ControlX", "", Decimal("20.00"))

def test_control_plagas_periodo_negativo():
    with pytest.raises(ValueError):
        ControlDePlagas("ICA777", "PlagaKill", "15 días", -1, Decimal("30.00"))