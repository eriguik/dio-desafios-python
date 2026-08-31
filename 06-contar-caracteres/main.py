def contar_caracteres(string: str) -> dict[str, int]:
    """Retorna um dicionário com a contagem de ocorrências de cada caractere na string."""
    contador: dict[str, int] = {}

    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1

    return contador


def main() -> None:
    entrada = input()
    resultado = contar_caracteres(entrada)
    print(resultado)


if __name__ == "__main__":
    main()
