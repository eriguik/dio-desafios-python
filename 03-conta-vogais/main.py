def conta_vogais(texto: str) -> int:
    """Conta quantas vogais (sem acentuação) existem na string, ignorando maiúsculas/minúsculas."""
    vogais = set("aeiouAEIOU")
    contador = 0

    for caractere in texto:
        if caractere in vogais:
            contador += 1

    return contador


def main() -> None:
    entrada = input()
    total = conta_vogais(entrada)
    print(f"O número de vogais na string '{entrada}' é: {total}")


if __name__ == "__main__":
    main()
