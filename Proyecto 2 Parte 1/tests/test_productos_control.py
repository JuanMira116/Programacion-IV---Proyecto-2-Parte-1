
import pytest
from decimal import Decimal
from datetime import date
from modelo.control_fertilizantes import ControlFertilizante
from modelo.control_plagas import ControlPlagas

def test_control_fertilizante_valido():
    f = ControlFertilizante("ICA123", "FertiMax", 30, date.today(), Decimal("40.00"))
    assert f.registro_ica == "ICA123"
    assert f.frecuencia_dias == 30

def test_control_plagas_valido():
    p = ControlPlagas("ICA777", "PlagaKill", 15, 5, Decimal("30.00"))
    assert p.periodo_carencia == 5

def test_control_fertilizante_fecha_invalida():
    with pytest.raises(ValueError):
        ControlFertilizante("ICA123", "FertiMax", 30, "ayer", Decimal("40.00"))

def test_control_fertilizante_frecuencia_invalida():
    from modelo.producto_control import ProductoControl
    with pytest.raises(ValueError):
        ProductoControl("ICA000", "ControlX", 0, Decimal("20.00"))

def test_control_plagas_periodo_negativo():
    with pytest.raises(ValueError):
        ControlPlagas("ICA777", "PlagaKill", 15, -1, Decimal("30.00"))