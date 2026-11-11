# Raciocínio lógico

Exercício do nível 5 (Desafios com raciocínio lógico) da formação de Lógica de Programação da Rocketseat.

Pergunta da aula: quantos números de 4 dígitos dá para formar com os algarismos de 0 a 9?

| Arquivo | O que tem | Resultado |
|---|---|---|
| [combinacoes_com_repeticao.py](./combinacoes_com_repeticao.py) | Conta todas as combinações, com algarismos repetidos | 10000 |
| [combinacoes_sem_repeticao.py](./combinacoes_sem_repeticao.py) | Conta só as combinações sem nenhum algarismo repetido | 5040 |

## Como funciona

A primeira versão usa quatro `for` aninhados, um para cada dígito. Cada um passa pelos 10 algarismos, então são 10 × 10 × 10 × 10 = 10000 combinações.

Na segunda versão, o `continue` pula a volta sempre que o algarismo já foi usado em uma posição anterior. Sobram 10 × 9 × 8 × 7 = 5040 combinações. É a mesma conta de arranjo da matemática, só que feita pelo computador testando uma por uma.

## Outros temas do nível

- Pensar como um algoritmo
- Torre de Hanói e recursividade
- Sapo na Lagoa: decisões e possibilidades
- Percorrer e sair de um labirinto
