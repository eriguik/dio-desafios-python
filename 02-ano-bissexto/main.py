def eh_bissexto(ano: int) -> bool:
    """Retorna True se o ano for bissexto, seguindo a regra gregoriana."""
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0


def main() -> None:
    ano = int(input())
    print("SIM" if eh_bissexto(ano) else "NÃO")


if __name__ == "__main__":
    main()
