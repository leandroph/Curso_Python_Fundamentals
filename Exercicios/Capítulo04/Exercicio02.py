''' Crie um programa utilizando dois arquivos, onde um deles possui todas as funçoes utilizadas na aplicação.
 Onde o programa deverá perguntar ao usuario nome/idade de uma pessoa, e armazenar esses 
 valores em um dicionario,
 e repetir essa ação até que a pessoa não queira mais adicionar nomes, em seguida, 
 o programa deverá mostrar o numero
 de pessoas em categorias de acordo com a idade:
 0-17 anos: Menor de idade
 18-59 anos: Adulto
 60+ anos: Idoso
 E deverá perguntar para o usuario se ele gostaria de exibir na tela uma lista com os nomes 
 das pessoas de cada grupo,
 ou se o usuario deseja finalizar o programa.'''


from funcao import definirCategoria


dicionario = {}

while True:
    resposta = int(input('''Voce deseja adicionar um valor ao dicionario?
    1 - Adicionar um valor
    2 - Finalizar o dicionario
    '''))
    if resposta == 2:
        break

    nome = input('Qual o nome da pessoa a ser adicionada? ')
    idade = int(input('Qual a idade dessa pessoa? '))

    dicionario[nome] = idade

definirCategoria(dicionario)

