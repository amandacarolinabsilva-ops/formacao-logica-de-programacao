# Pense em uma cor
# Um "truque de mágica" que tenta adivinhar a cor escolhida.

import os

os.system('cls')

print("Escolha uma cor na sua mente:")
print("🔴 Vermelho")
print("🔵 Azul")
print("🟢 Verde")
print("🟡 Amarelo")
input("Aperte Enter quando tiver escolhido...")

os.system('cls')
print("Concentre-se...")
input()

print("Você pensou na cor... 🔵 Azul!")
resposta = input("Acertei, né? (sim/não): ").lower()

if resposta == "sim":
    print("Eu sabia! Sou incrível!")
else:
    print("Ah, que pena! Da próxima vez eu acerto!")
