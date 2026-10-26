import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import Calculadora


def test_soma_numeros_iguais():
    assert Calculadora().soma(5, 5) == 10


def test_soma_exemplo_2():
    assert Calculadora().soma(8, 8) == 16


def test_soma_exemplo_3():
    assert Calculadora().soma(20, 10) == 30


def test_soma_com_zero():
    assert Calculadora().soma(0, 7) == 7


def test_soma_com_negativos():
    assert Calculadora().soma(-3, -4) == -7


def test_soma_positivo_e_negativo():
    assert Calculadora().soma(10, -4) == 6
