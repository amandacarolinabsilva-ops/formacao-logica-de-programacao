# Legibilidade e refatoração

Atividade prática do nível 4 (Boas práticas e legibilidade de código) da formação de Lógica de Programação da Rocketseat.

A aula começa com um código que até tem uma lógica, mas que ninguém consegue ler. A tarefa é refatorar: deixar o código claro sem mudar o que ele faz.

| Arquivo | O que tem |
|---|---|
| [antes.py](./antes.py) | Código do início da aula |
| [depois.py](./depois.py) | Código refatorado no fim da aula |

## O que mudou

- Nomes como `a`, `x`, `y`, `z`, `r`, `s` e `t` viraram nomes que dizem o que guardam: `lista`, `limite`, `multiplicador`
- Uma função que fazia tudo foi dividida em três, cada uma com uma tarefa: somar os maiores, multiplicar a lista e exibir o resultado
- Indentação e quebras de linha no padrão do Python, em vez de várias instruções na mesma linha com `;`
- O laço `for` com `append` virou compreensão de lista, e a soma passou a usar `sum()`

Saída do código refatorado:

```
soma: 90
lista: [20, 40, 60, 80, 100]
```

## Aprendizados

- Código é lido muito mais vezes do que é escrito
- Refatorar é melhorar a estrutura sem mudar o resultado, então vale conferir a saída antes e depois
- Uma função com nome claro dispensa comentário
