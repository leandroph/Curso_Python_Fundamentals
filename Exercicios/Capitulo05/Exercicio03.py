# Implemente uma função de consulta no programa do exercício 2

import csv

def consulta():
    with open('cadastro.csv', 'r', newline='') as arquivo:
        leitura = csv.reader(arquivo, delimiter=';')
        for linha in leitura:
            print(linha)

def main():
    consulta()
        

if __name__ == '__main__':
    main()