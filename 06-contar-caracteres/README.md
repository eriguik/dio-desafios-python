# 06 - Contar Caracteres

## 📋 Descrição

Recebe uma string e retorna um dicionário onde cada chave é um caractere presente na string e o valor é a quantidade de vezes que esse caractere aparece.

📚 Documentação oficial usada como referência: [Dicionários em Python](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries)

## ⬇️ Entrada

Uma única string textual.

## ⬆️ Saída

Um dicionário `{caractere: quantidade}`.

## 🧪 Exemplos

| Entrada    | Saída                                                          |
|------------|-----------------------------------------------------------------|
| collections | {'c': 2, 'o': 2, 'l': 2, 'e': 1, 't': 1, 'i': 1, 'n': 1, 's': 1} |
| numpy      | {'n': 1, 'u': 1, 'm': 1, 'p': 1, 'y': 1}                         |
| datetime   | {'d': 1, 'a': 1, 't': 2, 'e': 2, 'i': 1, 'm': 1}                 |

## ▶️ Como executar

```bash
python main.py
```

## ✅ Como rodar os testes

```bash
pip install pytest
pytest
```
