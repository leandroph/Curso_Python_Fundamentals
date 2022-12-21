# Exercícios - Aula 06


## Exercício 1:

Crie uma classe que represente um ônibus. O ônibus deverá conter os seguintes atributos:

- capacidade total
- capacidade atual
- velocidade
- placa
- modelo

Os comportamentos esperados para um Ônibus são:

- Acelerar
- Frear
- Embarcar
- Desembarcar

Lembre-se que a capacidade total do ônibus é de 45 pessoas - não será possível admitir superlotação.
Além disso, quando o ônibus ficar vazio, não será permitido efetuar o desembarque de pessoas.

## Exercício 2:

Implemente um programa que represente uma fila. O contexto do programa é uma
agência de banco. Cada cliente ao chegar deverá respeitar a seguinte regra: o primeiro
a chegar deverá ser o primeiro a sair. Você poderá representar pessoas na fila a partir
de números os quais representam a idade. A sua fila deverá conter os seguintes comportamentos:

- Adicionar pessoa na fila: adicionar uma pessoa na fila.
- Atender Fila: atender a pessoa respeitando a ordem de chegada
- Dar prioridade: colocar uma pessoa maior de 65 anos como o primeiro da fila

Lembre-se que a capacidade da fila é de 10 pessoas. E quando um lugar fica vago na fila, este
automaticamente fica disponível para o próximo - o que torna a fila uma estrutura circular.
