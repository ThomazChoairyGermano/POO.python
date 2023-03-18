class Computador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f'Ligando o {self.marca} modelo {self.modelo}')

computador_1 = Computador('Dell', 'xps')
computador_1.ligar()