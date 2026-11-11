def somar_maiores(lista, limite):
    return sum(elemento for elemento in lista if elemento > limite)

def multiplicar_lista(lista, multiplicador):
    return [elemento * multiplicador for elemento in lista]

def exibir_resposta(lista, limite, multiplicador):
    resultado = multiplicar_lista(lista, multiplicador)
    soma_maiores = somar_maiores(lista, limite)

    print("soma:", soma_maiores)
    print("lista:", resultado)

exibir_resposta([10, 20, 30, 40, 50], 35, 2)
