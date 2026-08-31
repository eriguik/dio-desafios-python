import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import elementos_comuns


def test_exemplo_1():
    assert sorted(elementos_comuns(["1", "2", "3", "4"], ["3", "4", "5", "6"])) == [3, 4]


def test_exemplo_2():
    assert sorted(elementos_comuns(["9", "8", "7", "6", "5"], ["5", "2", "3", "7"])) == [5, 7]


def test_sem_elementos_comuns():
    assert elementos_comuns(["1", "2"], ["3", "4"]) == []


def test_remove_duplicatas():
    assert sorted(elementos_comuns(["1", "1", "2"], ["1", "2", "2"])) == [1, 2]


def test_listas_identicas():
    assert sorted(elementos_comuns(["1", "2", "3"], ["1", "2", "3"])) == [1, 2, 3]
