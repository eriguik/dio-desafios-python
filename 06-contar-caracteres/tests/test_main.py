import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import contar_caracteres


def test_exemplo_collections():
    assert contar_caracteres("collections") == {
        "c": 2, "o": 2, "l": 2, "e": 1, "t": 1, "i": 1, "n": 1, "s": 1
    }


def test_exemplo_numpy():
    assert contar_caracteres("numpy") == {"n": 1, "u": 1, "m": 1, "p": 1, "y": 1}


def test_exemplo_datetime():
    assert contar_caracteres("datetime") == {
        "d": 1, "a": 1, "t": 2, "e": 2, "i": 1, "m": 1
    }


def test_string_vazia():
    assert contar_caracteres("") == {}


def test_caracteres_repetidos():
    assert contar_caracteres("aaa") == {"a": 3}


def test_preserva_ordem_de_insercao():
    assert list(contar_caracteres("collections").keys()) == [
        "c", "o", "l", "e", "t", "i", "n", "s"
    ]
