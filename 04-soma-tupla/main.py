def soma_tupla(tupla: tuple[int, ...]) -> int:
    """Retorna a soma de todos os elementos inteiros da tupla."""
    return sum(tupla)


def main() -> None:
    entrada = input()
    elementos: tuple[int, ...] = tuple(map(int, entrada.split()))
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")


if __name__ == "__main__":
    main()
