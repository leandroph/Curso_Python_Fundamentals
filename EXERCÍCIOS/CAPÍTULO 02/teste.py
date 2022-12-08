'''
1) Escreva um programa em Python que simule uma dança das cadeiras. Você deverá
importar o pacote random e iniciar uma lista com nomes de pessoas que participariam da
brincadeira. O jogo deverá iniciar com 9 cadeiras e 10 participantes. A cada rodada,
uma cadeira deverá ser retirada e um dos jogadores, de forma aleatória, ser eliminado. O
jogo deverá terminar quando apenas restar uma cadeira e ao final de todas as rodadas,
deverá ser apresentado vencedor.
Dica: Você poderá utilizar o pacote time para simular um tempo de a cada rodada para criar
um efeito mais interessante
'''
import random
import time
lista = ['João', 'Maria', 'José', 'Pedro', 'Paulo', 'Ana', 'Carla', 'Marcos', 'Mariana', 'Rafael']
cadeiras = 9
while cadeiras > 1:
    lista.reverse()
    cadeiras -= 1
    print('Cadeiras restantes: ', cadeiras)
    lista.pop(random.randint(0, len(lista) - 1))
    print('Participantes: ', lista)
    time.sleep(1)
print('Vencedor: ', lista[0])
