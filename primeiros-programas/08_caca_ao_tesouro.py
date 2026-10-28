# Caça ao tesouro espacial
# Encontre o tesouro escondido num tabuleiro 3x3 em até 5 tentativas.

# Tabuleiro 3x3 vazio
tabuleiro = [
    [' ', ' ', ' '],  # linha 0
    [' ', ' ', ' '],  # linha 1
    [' ', ' ', ' ']   # linha 2
]

# Posição fixa do tesouro (linha 1, coluna 2)
linha_tesouro = 1
coluna_tesouro = 2


# Função para exibir o tabuleiro
def exibe_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)


tentativas = 5

print("🚀 Caça ao Tesouro Espacial")
print("Encontre o 💎 escondido no tabuleiro 3x3.")
print("Use números de 0 a 2 para linha e coluna.")
print("Exemplo: linha 1, coluna 2")

for i in range(tentativas):
    print(f"\nTentativa {i+1} de {tentativas}")

    linha = int(input("Digite a linha (0 a 2): "))
    coluna = int(input("Digite a coluna (0 a 2): "))

    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("❌ Posição inválida! Tente valores entre 0 e 2.")
        continue

    if linha == linha_tesouro and coluna == coluna_tesouro:
        tabuleiro[linha][coluna] = '💎'
        print("\n🎉 Parabéns! Você encontrou o tesouro!")
        exibe_tabuleiro()
        break
    else:
        if tabuleiro[linha][coluna] != ' ':
            print("⚠️ Você já tentou aqui!")
        else:
            tabuleiro[linha][coluna] = 'X'
            print("Nada aqui... continue tentando!")
        exibe_tabuleiro()

else:
    # Só roda se o for terminar sem nenhum break (tesouro não encontrado)
    print("\n⛔ Suas tentativas acabaram!")
    tabuleiro[linha_tesouro][coluna_tesouro] = '💎'
    print("O tesouro estava aqui:")
    exibe_tabuleiro()
