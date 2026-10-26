class Calculadora:
    """Encapsula as operações matemáticas básicas."""

    def soma(self, num1: int, num2: int) -> int:
        """Retorna a soma de dois números inteiros."""
        return num1 + num2


def main() -> None:
    num1 = int(input())
    num2 = int(input())

    calc = Calculadora()
    resultado = calc.soma(num1, num2)
    print(resultado)


if __name__ == "__main__":
    main()
