# Quiz de perguntas e respostas
# Cada item da lista é uma pergunta e a resposta certa.

perguntas = [
    ["Quanto é 2 + 2?", "4"],
    ["Qual linguagem estamos aprendendo?", "python"],
    ["Qual animal é famoso por rir? (dica: aparece no Rei Leão)", "hiena"],
    ["Qual fruta rima com limão e é amarela?", "mamão"],
    ["Qual o nome do robô do Star Wars que parece um latão?", "r2d2"]
]

acertos = 0

for pergunta in perguntas:
    texto_pergunta = pergunta[0]
    resposta_certa = pergunta[1]

    resposta_digitada = input(texto_pergunta + " ")

    if resposta_digitada.lower() == resposta_certa:
        acertos += 1

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")
