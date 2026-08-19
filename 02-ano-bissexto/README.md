# 02 - Ano Bissexto

## 📋 Descrição

Informa se um determinado ano é bissexto, seguindo a regra gregoriana:

1. É divisível por 4 e não é divisível por 100, **ou**
2. É divisível por 400.

📚 Documentação oficial usada como referência: [Controle de Fluxo em Python](https://docs.python.org/pt-br/3/tutorial/controlflow.html)

## ⬇️ Entrada

Um único número inteiro representando o ano.

## ⬆️ Saída

Uma string: `SIM` ou `NÃO`.

## 🧪 Exemplos

| Entrada | Saída |
|---------|-------|
| 1975    | NÃO   |
| 1986    | NÃO   |
| 1992    | SIM   |

## ▶️ Como executar

```bash
python main.py
```

## ✅ Como rodar os testes

```bash
pip install pytest
pytest
```
