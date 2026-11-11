# Lendo e depurando código

Exercício do nível 3 (Lendo, depurando e entendendo códigos) da formação de Lógica de Programação da Rocketseat.

A aula entrega um simulador de compra de supermercado que não roda. A tarefa é ler o código, achar os erros e corrigir.

| Arquivo | O que tem |
|---|---|
| [codigo_com_erros.py](./codigo_com_erros.py) | Código como veio na aula |
| [codigo_corrigido.py](./codigo_corrigido.py) | Minha versão corrigida |

## Erros que encontrei

| Linha | Erro | Correção |
|---|---|---|
| `valor_total = preco_unitário * quantidade` | A variável foi criada como `preco_unitario`, sem acento. Para o Python são nomes diferentes | Usar `preco_unitario` |
| `se quantidade > 2:` | `se` é pseudocódigo, não Python | Trocar por `if` |
| `valor_total * 0,9` | Python usa ponto como separador decimal. Com vírgula vira uma tupla | Trocar por `0.9` |
| `print("...R$", + valor_total)` | O `+` sobrando não faz sentido ali, e o valor sai com várias casas decimais | Usar f-string com `:.2f` |

Resultado depois da correção: `Valor total da compra: R$15.63`

## Aprendizados

- Ler a mensagem de erro antes de sair mexendo no código: ela diz o tipo do erro e a linha
- Acompanhar o código linha a linha no PythonTutor e no depurador do VS Code
- Alguns erros param o programa (sintaxe) e outros só aparecem quando a linha é executada (nome de variável errado)
