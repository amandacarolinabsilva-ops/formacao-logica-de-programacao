# Primeiros Programas

Desafio prático do **Nível 2 — Escrevendo o seu primeiro programa** da formação de Lógica de Programação da Rocketseat.

Oito programas em Python para praticar entrada e saída de dados, variáveis, condicionais, laços de repetição, listas e funções.

---

## Exercícios

| # | Programa | Conceitos praticados | Arquivo |
|---|---|---|---|
| 1 | Adivinhe o número | `input`, `if`/`else`, `.lower()` | [01_adivinhe_o_numero.py](./01_adivinhe_o_numero.py) |
| 2 | Pense em uma cor | limpar a tela com `os`, `input` com mensagem | [02_pense_em_uma_cor.py](./02_pense_em_uma_cor.py) |
| 3 | História maluca | várias variáveis, f-strings | [03_historia_maluca.py](./03_historia_maluca.py) |
| 4 | Crachá de programador(a) | f-strings, alinhamento `:^30`, multiplicação de texto | [04_cracha_dev.py](./04_cracha_dev.py) |
| 5 | Oráculo da sabedoria Python | `match`/`case`, `case _`, padrões com `\|` | [05_oraculo_python.py](./05_oraculo_python.py) |
| 6 | Quiz de perguntas e respostas | lista de listas, `for`, contador `+= 1` | [06_quiz.py](./06_quiz.py) |
| 7 | Número secreto | `while True`, `break`, `continue`, `try`/`except` | [07_numero_secreto.py](./07_numero_secreto.py) |
| 8 | Caça ao tesouro espacial | tabuleiro com listas, função, `for`/`else` | [08_caca_ao_tesouro.py](./08_caca_ao_tesouro.py) |

---

## Como rodar

Com o Python instalado, abra o terminal na pasta e rode:

```bash
python 01_adivinhe_o_numero.py
```

Troque o nome do arquivo para rodar os outros. O `match`/`case` do oráculo precisa do Python 3.10 ou mais novo.

---

## Aprendizados

- **Primeiro pergunta, depois guarda a resposta:** `resposta = input("pergunta")`
- **`.lower()`** transforma o texto em minúscula; o outro lado da comparação também precisa estar em minúscula
- **`for item in lista`:** o `for` cria a variável e entrega um item de cada vez
- **`+= 1` conta**, **`+= valor` soma**
- **`break`** sai do laço; **`continue`** pula para a próxima volta
- **`try`/`except`** é uma rede de segurança para erros, como letra no lugar de número
- **`for`/`else`:** o `else` só roda se o laço terminar sem `break`
- Nomes de variável claros deixam o código mais fácil de ler
