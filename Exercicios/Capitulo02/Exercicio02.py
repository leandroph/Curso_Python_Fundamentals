'''
2) Escreva um script em python que represente uma quitanda. O seu programa deverá
apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
deverá ser adicionada a uma cesta de compras.
Menu principal:
Quitanda:
1: Ver cesta
2: Adicionar frutas
3: Sair
Digite a opção desejada:
Menu de frutas:
Escolha fruta desejada:
1 - Banana
2 - Melancia
3 - Morango
Digite à opção desejada: 2
Melancia adicionada com sucesso!
Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.

Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem
Digite uma opção inválida)
O programa deverá ser encerrado apenas se o usuário digitar a opção 3.
'''

print('Quitanda :\n1: Ver cesta\n2: Adicionar frutas\n3: Sair')
opcao = int(input('Digite a opção desejada: '))
cesta = []
while opcao != 3:
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
    else:
        print('Digite uma opção inválida')
    print('Quitanda :\n1: Ver cesta\n2: Adicionar frutas\n3: Sair')
    opcao = int(input('Digite a opção desejada: '))

print('Programa encerrado')
