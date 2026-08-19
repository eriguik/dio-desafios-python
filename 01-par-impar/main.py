def classificar_paridade(numero: int) -> str:
    """Retorna 'Par' ou 'Ímpar' de acordo com a paridade do número."""
    return "Par" if numero % 2 == 0 else "Ímpar"


def main() -> None:
    numero = int(input())
    print(classificar_paridade(numero))


if __name__ == "__main__":
    main()
