class Pessoa:
    """Representa uma pessoa com nome e idade."""

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def obter_informacoes(self) -> str:
        """Retorna os dados da pessoa no formato 'Nome: <nome>, Idade: <idade>'."""
        return f"Nome: {self.nome}, Idade: {self.idade}"


def main() -> None:
    nome = input()
    idade = int(input())

    pessoa = Pessoa(nome, idade)
    print(pessoa.obter_informacoes())


if __name__ == "__main__":
    main()
