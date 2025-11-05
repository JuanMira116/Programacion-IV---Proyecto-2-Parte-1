
import pytest
from decimal import Decimal
from modelo.antibiotico import Antibiotico


def test_creacion_antibiotico_valido():
    a = Antibiotico("Amoxicilina", 500, "Bovino", Decimal("25.5"))
    assert a.nombre == "Amoxicilina"
    assert a.dosis == 500
    assert a.tipo_animal == "Bovino"
    assert a.precio == Decimal("25.5")


def test_dosis_fuera_de_rango_baja():
    with pytest.raises(ValueError):
        Antibiotico("Amoxi", 300, "Bovino", Decimal("10.0"))


def test_dosis_fuera_de_rango_alta():
    with pytest.raises(ValueError):
        Antibiotico("Amoxi", 700, "Bovino", Decimal("10.0"))


def test_tipo_animal_invalido():
    with pytest.raises(ValueError):
        Antibiotico("Amoxi", 500, "Gato", Decimal("10.0"))