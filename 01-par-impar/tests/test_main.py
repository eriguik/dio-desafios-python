import sys
from pathlib import Path

# Garante que o main.py (na raiz do projeto) seja importável
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import classificar_paridade


def test_numero_par():
    assert classificar_paridade(2) == "Par"


def test_numero_impar():
    assert classificar_paridade(5) == "Ímpar"


def test_zero_e_par():
    assert classificar_paridade(0) == "Par"


def test_numero_negativo_par():
    assert classificar_paridade(-6) == "Par"


def test_numero_negativo_impar():
    assert classificar_paridade(-7) == "Ímpar"
