'''
3) Aproveitando o exercício anterior, incremente a sua quitanda para consolidar o valor
total de sua cesta de compras. Deverá ser adicionado ao seu menu inicial a opção
checkout e esta deverá listar os produtos de sua cesta bem como o valor total:
Menu:
1: Ver cesta
2: Adicionar Frutas
3: Checkout
4: Sair
Digite a opção desejada:
A saída do checkout deverá ser da seguinte maneira:
Total de compras: 15,00
Cesta de compras: Banana, Morango, Melancia
Considere os seguintes preços:
Banana: 3.50 Melancia: 7.50 Morango: 5.00
Dica: Você pode armazenar os dados de frutas e seus respectivos preços em um dicionário.
'''

print('Quitanda :\n1: Ver cesta\n2: Adicionar frutas\n3: Checkout\n4: Sair')
opcao = int(input('Digite a opção desejada: '))
cesta = []
preco = {'Banana': 3.50, 'Melancia': 7.50, 'Morango': 5.00}
total = 0
while opcao != 4:
    if opcao == 1:
        print('Cesta de compras: ', cesta)
    elif opcao == 2:
        print('Menu de frutas:\nEscolha fruta desejada:\n1 - Banana\n2 - Melancia\n3 - Morango')
        fruta = int(input('Digite à opção desejada: '))
        if fruta == 1:
            cesta.append('Banana')
            print('Banana adicionada com sucesso!')
        elif fruta == 2:
            cesta.append('Melancia')
            print('Melancia adicionada com sucesso!')
        elif fruta == 3:
            cesta.append('Morango')
            print('Morango adicionada com sucesso!')
        else:
            print('Digite uma opção inválida')
    elif opcao == 3:
        for i in cesta:
            total += preco[i]
        print('Total de compras: ', total)
        print('Cesta de compras: ', cesta)
    else:
        print('Digite uma opção inválida')
    print('Quitanda :\n1: Ver cesta\n2: Adicionar frutas\n3: Checkout\n4: Sair')
    opcao = int(input('Digite a opção desejada: '))

print('Programa encerrado')