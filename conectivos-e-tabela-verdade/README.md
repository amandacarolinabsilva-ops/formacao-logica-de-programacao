# Conectivos e Tabela-Verdade

Desafio prático de **Lógica de Programação** da Rocketseat.

Neste repositório resolvo exercícios de lógica proposicional: transformar frases em fórmulas com conectivos e montar a tabela-verdade de cada uma.

---

## Cola dos conectivos

| Conectivo | Símbolo | Regra |
|---|---|---|
| E (conjunção) | `^` | Só é **V** quando **tudo** é V |
| OU (disjunção) | `v` | Só é **F** quando **tudo** é F |
| NÃO (negação) | `~` | Inverte o valor |
| SE... ENTÃO (condicional) | `→` | Só é **F** quando é **V → F** |
| SE E SOMENTE SE (bicondicional) | `↔` | **V** quando os dois são iguais, **F** quando são diferentes |

**Número de linhas da tabela:** 2 elevado ao número de proposições (2 letras = 4 linhas, 3 letras = 8 linhas).

**No código:**

| Lógica | Python | C# |
|---|---|---|
| E | `and` | `&&` |
| OU | `or` | `\|\|` |
| NÃO | `not` | `!` |

---

## Exercício 1 — Conjunção (E)

> Eu estudei para a prova e fiz todos os exercícios.

- **A** = estudou para a prova
- **B** = fez todos os exercícios

**Fórmula:** `A ^ B`

| A | B | A ^ B |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

---

## Exercício 2 — Disjunção (OU)

> Eu vou ao cinema ou fico em casa assistindo séries.

- **A** = vou ao cinema
- **B** = fico em casa assistindo séries

**Fórmula:** `A v B`

| A | B | A v B |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

---

## Exercício 3 — Condicional (SE... ENTÃO)

> Se eu acordar cedo, então conseguirei pegar o ônibus.

- **A** = acordar cedo
- **B** = conseguir pegar o ônibus

**Fórmula:** `A → B`

| A | B | A → B |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

---

## Exercício 4 — Condicional com conjunção

> Se eu estudar muito, então passarei na prova e ganharei um presente.

- **A** = estudar muito
- **B** = passar na prova
- **C** = ganhar um presente

**Fórmula:** `A → (B ^ C)`

| A | B | C | B ^ C | A → (B ^ C) |
|---|---|---|---|---|
| V | V | V | V | V |
| V | V | F | F | F |
| V | F | V | F | F |
| V | F | F | F | F |
| F | V | V | V | V |
| F | V | F | F | V |
| F | F | V | F | V |
| F | F | F | F | V |

---

## Exercício 5 — Disjunção (OU)

> Eu vou jogar videogame ou vou estudar lógica de programação.

- **A** = jogar videogame
- **B** = estudar lógica de programação

**Fórmula:** `A v B`

| A | B | A v B |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

---

## Exercício 6 — Conjunção (E)

> Eu comi pizza e tomei refrigerante.

- **A** = comeu pizza
- **B** = tomou refrigerante

**Fórmula:** `A ^ B`

| A | B | A ^ B |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

---

## Exercício 7 — Condicional (SE... ENTÃO)

> Se eu tiver dinheiro, então viajarei nas férias.

- **A** = ter dinheiro
- **B** = viajar nas férias

**Fórmula:** `A → B`

| A | B | A → B |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

---

## Exercício 8 — Bicondicional (SE E SOMENTE SE)

> Eu lerei um livro se e somente se terminar meu trabalho.

- **A** = ler um livro
- **B** = terminar o trabalho

**Fórmula:** `A ↔ B`

| A | B | A ↔ B |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

---

## Exercício 9 — Condicional com disjunção

> Se estiver sol, então irei à praia ou ao parque.

- **A** = estar sol
- **B** = ir à praia
- **C** = ir ao parque

**Fórmula:** `A → (B v C)`

| A | B | C | B v C | A → (B v C) |
|---|---|---|---|---|
| V | V | V | V | V |
| V | V | F | V | V |
| V | F | V | V | V |
| V | F | F | F | F |
| F | V | V | V | V |
| F | V | F | V | V |
| F | F | V | V | V |
| F | F | F | F | V |

---

## Exercício 10 — Bicondicional (SE E SOMENTE SE)

> Eu farei um bolo se e somente se comprar os ingredientes.

- **A** = fazer o bolo
- **B** = comprar os ingredientes

**Fórmula:** `A ↔ B`

| A | B | A ↔ B |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

---

## Exercícios extras

Situações do dia a dia transformadas em fórmulas, já pensando no `if` do código.

| Situação | Fórmula | Em Python |
|---|---|---|
| O alarme dispara se estiver ligado e houver movimento ou a porta abrir | `L ^ (M v P)` | `ligado and (movimento or porta)` |
| Frete grátis para cliente cadastrado com compra acima de R$ 100, ou com cupom | `(A ^ B) v C` | `(cadastrado and acima_100) or cupom` |
| Entra na piscina quem é sócio com mensalidade e exame em dia, ou convidado com pulseira | `(A ^ B ^ C) v (D ^ E)` | `(socio and mensalidade and exame) or (convidado and pulseira)` |
| Aluno aprovado com frequência mínima e nota acima de 7 ou recuperação | `A ^ (B v C)` | `frequencia and (nota or recuperacao)` |
| Motorista liberado com carteira, vistoria e sem multa grave | `A ^ B ^ ~C` | `carteira and vistoria and not multa` |
| Empréstimo aprovado com renda e nome limpo, ou com fiador | `(A ^ ~B) v C` | `(renda and not nome_sujo) or fiador` |
