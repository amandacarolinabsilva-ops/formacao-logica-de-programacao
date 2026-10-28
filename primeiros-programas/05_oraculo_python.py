# Oráculo da sabedoria Python
# A pessoa escolhe um assunto de Python e o oráculo explica.

print('Olá, seja bem-vindo(a) ao Oráculo da Sabedoria Python! Escolha um assunto de Python e o oráculo vai te explicar!')

nome = input('Digite o seu nome: ')
print(f'\nOlá {nome}, vamos começar a brincadeira!')

print('\nAssuntos disponíveis:')
print('Arrays, Funções, Classes, Loops, Condicionais, Listas, Dicionários, Tuplas, Módulos, Exceções, Decoradores, Geradores')
pergunta = input('Sobre qual assunto você quer saber? ').lower()

match pergunta:
    case 'arrays':
        print('Arrays são estruturas de dados que armazenam elementos do mesmo tipo em uma sequência contínua. Eles são úteis para organizar e acessar dados de forma eficiente.')
    case 'funções' | 'funcoes':
        print('Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a organizar o código e a evitar repetição.')
    case 'classes':
        print('Classes são modelos para criar objetos em programação orientada a objetos. Elas definem atributos e métodos que os objetos terão, permitindo a criação de instâncias com comportamentos específicos.')
    case 'loops':
        print('Loops são estruturas de controle que permitem repetir um bloco de código várias vezes. Eles são úteis para iterar sobre coleções de dados ou executar tarefas repetitivas.')
    case 'condicionais':
        print('Condicionais são estruturas de controle que permitem executar diferentes blocos de código com base em condições específicas. Elas ajudam a tomar decisões no fluxo do programa.')
    case 'listas':
        print('Listas são estruturas de dados que armazenam uma coleção de elementos em uma ordem específica. Elas são mutáveis e permitem adicionar, remover e acessar elementos facilmente.')
    case 'dicionários' | 'dicionarios':
        print('Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles permitem acessar valores rapidamente usando suas chaves, tornando-os úteis para organizar e buscar informações.')
    case 'tuplas':
        print('Tuplas são estruturas de dados imutáveis que armazenam uma coleção de elementos em uma ordem específica. Elas são úteis quando você deseja garantir que os dados não sejam alterados após a criação.')
    case 'módulos' | 'modulos':
        print('Módulos são arquivos que contêm código Python reutilizável, como funções, classes e variáveis. Eles ajudam a organizar o código em partes menores e facilitam a manutenção e o compartilhamento de funcionalidades.')
    case 'exceções' | 'excecoes':
        print('Exceções são eventos que ocorrem durante a execução de um programa e indicam que algo inesperado aconteceu. Elas permitem tratar erros de forma controlada, evitando que o programa seja interrompido abruptamente.')
    case 'decoradores':
        print('Decoradores são funções que modificam o comportamento de outras funções ou métodos. Eles permitem adicionar funcionalidades extras sem alterar o código original, tornando o código mais modular e reutilizável.')
    case 'geradores':
        print('Geradores são funções que produzem uma sequência de valores sob demanda, em vez de armazená-los todos na memória. Eles são úteis para trabalhar com grandes conjuntos de dados ou fluxos de dados infinitos, economizando recursos do sistema.')
    case _:
        print('Hmm, o oráculo ainda não conhece esse assunto. Tente outro da lista!')
