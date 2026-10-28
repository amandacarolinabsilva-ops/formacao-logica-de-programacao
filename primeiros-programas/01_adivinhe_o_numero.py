# Adivinhe o número
# O programa tenta adivinhar o número que a pessoa pensou.

print('Quero que você adivinhe um número')
print('Você só pode pensar em um número de 0 a 10...')

print('Vamos lá, pensa aí, e quando pensar, clica em "Enter"')
input()

print('Você pensou no número 5? Se sim, digite "sim", se não, digite "não"')
resposta = input()

if resposta.lower() == 'sim':
    print('Uhul! Acertei :)')
else:
    print('Ahh, que pena! Eu não acertei :(')
