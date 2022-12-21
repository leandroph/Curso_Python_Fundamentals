'''Crie um programa que pergunte para o usuario um numero de pessoas a participarem de um sorteio (0-20),
e o numero de pessoas a serem sorteadas, e depois sorteie esse numero de pessoas da lista.
O programa deverá pegar o numero de pessoas a participar aleatoriamente desta lista:'''

import random

def sortear_participante(lista):
    participantes = int(input('Digite o numero de participantes a serem sorteados: '))
    if participantes > len(lista):
        print('Não é possível sortear mais pessoas do que as que estão na lista')
    else:
        for i in range(participantes):
            print('Participante sorteado: ', random.choice(lista))

def main():
    lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", 
    "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", 
    "Benedito", "Tereza", "Valmir", "Joaquim"]
    sortear_participante(lista)
        

if __name__ == '__main__':
    main() 