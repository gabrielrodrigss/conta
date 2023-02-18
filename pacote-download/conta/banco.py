class Banco:
    def __init__(self, contas, numero):
        self.contas = contas
        self.numero = numero

    def armazenar_conta(self):
        for conta in self.contas:
            print(f"Lista de contas: {conta}")



