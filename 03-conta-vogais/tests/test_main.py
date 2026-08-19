import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import conta_vogais


def test_python():
    assert conta_vogais("Python") == 1


def test_programacao():
    assert conta_vogais("Programação") == 4


def test_funcao():
    assert conta_vogais("Função") == 2


def test_sem_vogais():
    assert conta_vogais("xyz") == 0


def test_string_vazia():
    assert conta_vogais("") == 0


def test_maiusculas_e_minusculas():
    assert conta_vogais("AEIOUaeiou") == 10
