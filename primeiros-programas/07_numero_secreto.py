# Número secreto
# O jogo repete até a pessoa acertar o número.

numero_secreto = 7
tentativas = 0

while True:
    try:
        chute = int(input("Adivinhe o número (entre 1 e 10): "))
    except ValueError:
        print("Digite só números, por favor!")
        continue

    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Tente novamente!")
