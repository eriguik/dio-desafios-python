def elementos_comuns(lista1: list[str], lista2: list[str]) -> list[int]:
    """Retorna, em uma lista, os elementos inteiros comuns às duas listas, sem duplicatas."""
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))


def main() -> None:
    lista1 = input().split()
    lista2 = input().split()

    if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
        comuns = elementos_comuns(lista1, lista2)
        print(f"Elementos comuns às duas listas: {comuns}")
    else:
        print("Entrada inválida.")


if __name__ == "__main__":
    main()
