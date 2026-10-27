import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import Pessoa


def test_exemplo_mary_silva():
    assert Pessoa("Mary Silva", 32).obter_informacoes() == "Nome: Mary Silva, Idade: 32"


def test_exemplo_john_soares():
    assert Pessoa("John Soares", 20).obter_informacoes() == "Nome: John Soares, Idade: 20"


def test_exemplo_marcelly_reis():
    assert Pessoa("Marcelly Reis", 40).obter_informacoes() == "Nome: Marcelly Reis, Idade: 40"


def test_atributos_sao_guardados_na_instancia():
    pessoa = Pessoa("Ana", 25)
    assert pessoa.nome == "Ana"
    assert pessoa.idade == 25


def test_instancias_sao_independentes():
    p1 = Pessoa("Ana", 25)
    p2 = Pessoa("Bruno", 30)
    assert p1.obter_informacoes() != p2.obter_informacoes()
