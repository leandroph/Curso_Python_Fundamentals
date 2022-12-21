class Fila:

    def __init__(self):
        self.fila = []
        self.prioridade = []

    def adicionar(self, nome:str, idade:int):
        if idade >= 65:
            self.prioridade.append(nome)
            self.fila.append(nome)
            print(f'{nome} entrou na fila prioritária')
        else:
            self.fila.append(nome)
            print(f'{nome} entrou na fila')

    def atender(self):
        if len(self.prioridade) > 0:
            print(f'{self.prioridade.pop(0)} foi atendido')
            self.fila.pop(0)
        elif len(self.fila) > 0:
            print(f'{self.fila.pop(0)} foi atendido')
        else:
            print('Não há ninguém na fila')

   
fila = Fila()
fila.adicionar('João', 20)
fila.adicionar('Maria', 65)
fila.adicionar('José', 20)
fila.adicionar('Ana', 65)
fila.adicionar('Pedro', 20)
fila.atender()
fila.atender()
fila.atender()
fila.atender()