'''
Reescreva o exercício da quitanda do capítulo 2 separando as operações em funções
'''

def menu():
    print('Quitanda :\n1: Ver cesta\n2: Adicionar frutas\n3: Checkout\n4: Sair')
    opcao = int(input('Digite a opção desejada: '))
    return opcao

def adicionar_fruta(cesta):
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
    return cesta

def checkout(cesta):
    preco = {'Banana': 3.50, 'Melancia': 7.50, 'Morango': 5.00}
    total = 0
    for i in cesta:
        total += preco[i]
    print('Total de compras: ', total)
    print('Cesta de compras: ', cesta)

def main():
    cesta = []
    opcao = menu()
    while opcao != 4:
        if opcao == 1:
            print('Cesta de compras: ', cesta)
        elif opcao == 2:
            cesta = adicionar_fruta(cesta)
        elif opcao == 3:
            checkout(cesta)
        else:
            print('Digite uma opção inválida')
        opcao = menu()
    print('Programa encerrado')

if __name__ == '__main__':
    main()