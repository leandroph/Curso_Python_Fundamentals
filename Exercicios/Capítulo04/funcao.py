def definirCategoria(x):
    menor = {}
    adulto = {}
    idoso = {}

    n_menor = 0
    n_adulto = 0
    n_idoso = 0

    for chave, valor in x.items():
        if valor < 18:
            menor[chave] = valor
            n_menor += 1
        elif valor < 60:
            adulto[chave] = valor
            n_adulto += 1
        else:
            idoso[chave] = valor
            n_idoso += 1
    
    while True:
        escolha = int(input(f'''Voce digitou {len(x)} nomes, e eles podem ser divididos em:
        Menores: {n_menor}
        Adultos: {n_adulto}
        Idosos:  {n_idoso} 
        
        Voce gostaria de verificar os nomes das pessoas de alguma categoria?
        Digite 1 - Para ver os nomes dos menores.
        Digite 2 - Para ver os nomes dos adultos.
        Digite 3 - Para ver os nomes dos idosos.
        Digite 4 - Para fechar o programa
        '''))

        if escolha == 1:
            print(f'Os menores de idade adicionados foram: ')
            for name in menor.keys():
                print(name)

        if escolha == 2:
            print(f'Os adultos adicionados foram: ')
            for name in adulto.keys():
                print(name)

        if escolha == 3:
            print(f'Os idosos adicionados foram: ')
            for name in idoso.keys():
                print(name)

        if escolha == 4:
            break
