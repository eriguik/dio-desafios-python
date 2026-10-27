import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import ConversorTemperatura


def test_exemplo_32():
    assert ConversorTemperatura().celsius_para_fahrenheit(32) == pytest.approx(89.6)


def test_exemplo_22():
    assert ConversorTemperatura().celsius_para_fahrenheit(22) == pytest.approx(71.6)


def test_exemplo_17():
    assert ConversorTemperatura().celsius_para_fahrenheit(17) == pytest.approx(62.6)


def test_ponto_de_congelamento():
    assert ConversorTemperatura().celsius_para_fahrenheit(0) == pytest.approx(32.0)


def test_ponto_de_ebulicao():
    assert ConversorTemperatura().celsius_para_fahrenheit(100) == pytest.approx(212.0)


def test_temperatura_negativa():
    # -40 é o ponto onde as duas escalas coincidem
    assert ConversorTemperatura().celsius_para_fahrenheit(-40) == pytest.approx(-40.0)
