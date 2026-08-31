import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import soma_tupla


def test_exemplo_1():
    assert soma_tupla((2, 5, 6, 7, 9)) == 29


def test_exemplo_2():
    assert soma_tupla((9, 8, 7, 6, 5)) == 35


def test_exemplo_3():
    assert soma_tupla((50, 50, 50, 50)) == 200


def test_tupla_vazia():
    assert soma_tupla(()) == 0


def test_tupla_com_um_elemento():
    assert soma_tupla((7,)) == 7


def test_tupla_com_negativos():
    assert soma_tupla((-5, 5, 10)) == 10
