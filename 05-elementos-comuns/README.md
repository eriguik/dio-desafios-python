# 05 - Elementos Comuns

## 📋 Descrição

Recebe duas listas de números inteiros separados por espaço e retorna uma lista com os elementos comuns às duas, sem duplicatas. Se alguma entrada não for numérica, retorna `Entrada inválida.`.

📚 Documentação oficial usada como referência: [Listas em Python](https://docs.python.org/pt-br/3/tutorial/introduction.html#lists)

## ⬇️ Entrada

Duas listas de inteiros separadas apenas por espaço, uma por linha.

## ⬆️ Saída

Uma lista com os elementos comuns, ou `Entrada inválida.` se a entrada não for numérica.

## 🧪 Exemplos

| Entrada           | Saída                                       |
|--------------------|----------------------------------------------|
| 1 2 3 4<br>3 4 5 6 | Elementos comuns às duas listas: [3, 4]      |
| 9 8 7 6 5<br>5 2 3 7 | Elementos comuns às duas listas: [5, 7]    |
| a b c d<br>a e i o u | Entrada inválida.                          |

## ▶️ Como executar

```bash
python main.py
```

## ✅ Como rodar os testes

```bash
pip install pytest
pytest
```
