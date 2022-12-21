'''
Escreva um programa em python que realize um cadastro. Deverão ser coletadas as
seguintes informações:

- CPF
- Nome
- Idade
- Sexo
- Endereço

Os registros deverão ser armazenados em um arquivo CSV. Caso desejar manter o padrão brasileiro, o CSV será separado pelo caractere ;.'''


import csv

def cadastrar():
    cpf = input('Digite o seu CPF: ')
    nome = input('Digite o seu nome: ')
    idade = input('Digite a sua idade: ')
    sexo = input('Digite o seu sexo: ').upper()
    endereco = input('Digite o seu endereco: ').upper()

    with open('cadastro.csv', 'a', newline='') as arquivo:
        escrever = csv.writer(arquivo, delimiter=';')
        escrever.writerow([cpf, nome, idade, sexo, endereco])

def main():
    while True:
        cadastrar()
        if input('Deseja continuar? (S/N) ').upper() == 'N':
            break

if __name__ == '__main__':
    main()