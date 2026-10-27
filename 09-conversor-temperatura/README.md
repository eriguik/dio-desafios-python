# 09 - Conversor de Temperatura (POO)

## 📋 Descrição

Classe `ConversorTemperatura` que converte temperaturas de Celsius para Fahrenheit, com o método `celsius_para_fahrenheit` realizando o cálculo:

```
Fahrenheit = (Celsius × 9/5) + 32
```

O programa também cria uma instância do conversor e a utiliza para realizar a conversão.

📚 Documentação oficial usada como referência:
- [Classes em Python](https://docs.python.org/pt-br/3/tutorial/classes.html)
- [Métodos](https://docs.python.org/pt-br/3/library/stdtypes.html#methods)

## ⬇️ Entrada

Uma temperatura em graus Celsius (número decimal).

## ⬆️ Saída

A temperatura convertida para Fahrenheit.

## 🧪 Exemplos

| Entrada | Saída |
|---------|-------|
| 32      | 89.6  |
| 22      | 71.6  |
| 17      | 62.6  |

## ▶️ Como executar

```bash
python main.py
```

## ✅ Como rodar os testes

```bash
pip install pytest
pytest
```
