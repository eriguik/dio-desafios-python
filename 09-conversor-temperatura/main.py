class ConversorTemperatura:
    """Converte temperaturas entre escalas."""

    def celsius_para_fahrenheit(self, celsius: float) -> float:
        """Converte graus Celsius para Fahrenheit: F = (C * 9/5) + 32."""
        return celsius * 9 / 5 + 32


def main() -> None:
    celsius = float(input())

    conversor = ConversorTemperatura()
    fahrenheit = conversor.celsius_para_fahrenheit(celsius)
    print(fahrenheit)


if __name__ == "__main__":
    main()
