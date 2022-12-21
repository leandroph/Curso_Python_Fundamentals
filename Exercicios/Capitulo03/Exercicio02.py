'''
Escreva uma calculadora utilizando funções anônimas
'''

operações = {
    '1': lambda x, y: x + y, # Função que recebe dois números e retorna a soma
    '2': lambda x, y: x - y, # Função que recebe dois números e retorna a subtração
    '3': lambda x, y: x * y, # Função que recebe dois números e retorna a multiplicação
    '4': lambda x, y: x / y, # Função que recebe dois números e retorna a divisão
    '5': lambda x, y: x % y, # Função que recebe dois números e retorna o resto da divisão
    '6': lambda x, y: x ** y, # Função que recebe dois números e retorna a potência
    '7': lambda x, y: x ** (1 / y), # Função que recebe dois números e retorna a raiz quadrada
    '8': lambda x, y: x // y, # Função que recebe dois números e retorna a divisão inteira
    '9': lambda x, y: abs(x - y), # Função que recebe dois números e retorna o valor absoluto
    '10': lambda x, y: max(x, y), # Função que recebe dois números e retorna o maior valor
    '11': lambda x, y: min(x, y), # Função que recebe dois números e retorna o menor valor
    '12': lambda x, y: round(x, y), # Função que recebe dois números e retorna o valor arredondado
    '13': lambda x, y: round(x, y, 'DOWN'), # Função que recebe dois números e retorna o valor arredondado para baixo
    '14': lambda x, y: round(x, y, 'UP'), # Função que recebe dois números e retorna o valor arredondado para cima
}

def calculadora():
    while True:
        print('Escolha uma das operações abaixo:')
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Resto da divisão')
        print('6 - Potência')
        print('7 - Raiz quadrada')
        print('8 - Divisão inteira')
        print('9 - Valor absoluto')
        print('10 - Maior valor')
        print('11 - Menor valor')
        print('12 - Arredondamento')
        print('13 - Arredondamento para baixo')
        print('14 - Arredondamento para cima')
        operação = input('Digite o número da operação desejada: ')
        if operação in operações:
            x = float(input('Digite o primeiro número: '))
            y = float(input('Digite o segundo número: '))
            print(f'O resultado da operação é: {operações[operação](x, y)}')
        else:
            print('Operação inválida!')
        
        if input('Deseja realizar outra operação? (S/N) ').upper() == 'N':
            break
 
        
if __name__ == '__main__':
    calculadora()