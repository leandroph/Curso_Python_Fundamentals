# Implemente uma função de exclusão no programa do exercício 2.

import csv

def excluir():
    with open('cadastro.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        cadastro = list(leitor)
    cpf = input('Digite o CPF: ')
    for indice in range(len(cadastro)):
        if cadastro[indice][0] == cpf:
            del cadastro[indice]
            break
    with open('cadastro.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerows(cadastro)

def main():
    while True:
        excluir()
        if input('Deseja continuar? (S/N) ').upper() == 'N':
            break
        
if __name__ == '__main__':
    main()

