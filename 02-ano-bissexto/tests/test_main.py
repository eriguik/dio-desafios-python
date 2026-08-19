import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import eh_bissexto


def test_nao_divisivel_por_4():
    assert eh_bissexto(1975) is False


def test_divisivel_por_100_mas_nao_por_400():
    assert eh_bissexto(1986) is False  # não divisível por 4, controle
    assert eh_bissexto(1900) is False  # divisível por 100, não por 400


def test_divisivel_por_4_e_nao_por_100():
    assert eh_bissexto(1992) is True


def test_divisivel_por_400():
    assert eh_bissexto(2000) is True


def test_ano_2024():
    assert eh_bissexto(2024) is True
