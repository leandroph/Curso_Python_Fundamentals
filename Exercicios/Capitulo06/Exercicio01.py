class Onibus:
    def __init__(self):
        self.capacidade_total = 45
        self.capacidade_atual = 0
        self.velocidade = 0
        self.placa = 'ABC-1234'
        self.modelo = 'Mercedes'

    def acelerar(self):
        self.velocidade += 10
        print('O ônibus está acelerando!')

    def frear(self):
        while self.velocidade > 0:
            self.velocidade -= 10
            print('O ônibus está freando!')
        else:
            print('O ônibus está parado!')

    def embarcar(self):
        if self.capacidade_atual < self.capacidade_total:
            self.capacidade_atual += 1
            print(f"Um passageiro embarcou no onibus, há {self.capacidade_atual}/45 passageiros no total agora")
        else:
            print('O ônibus está cheio!')

    def desembarcar(self):
        if self.capacidade_atual > 0:
            self.capacidade_atual -= 1
            print(f"Um passageiro desembarcou do onibus, há {self.capacidade_atual}/45 passageiros no total agora")
        else:
            print('O ônibus está vazio!')

    def imprimir(self):
        print(f'''
        Capacidade total: {self.capacidade_total}
        Capacidade atual: {self.capacidade_atual}
        Velocidade: {self.velocidade}
        Placa: {self.placa}
        Modelo: {self.modelo}
        ''')

onibus = Onibus()
onibus.imprimir()
onibus.embarcar()
onibus.embarcar()
onibus.embarcar()
onibus.embarcar()
onibus.embarcar()
onibus.embarcar()
onibus.embarcar()
onibus.acelerar()
onibus.frear()

onibus.imprimir()