import datetime

from banco import Banco
from extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return ("Transferencia Realizada")

    def gerarsaldo(self):
        print(f"\n ----------------- \n numero: {self.numero}\n saldo: {self.saldo}")

    # def imprimir_enderecos_clientes(self):
    #     for cliente in self.clientes:
    #         print(f"Endereço do cliente {cliente.nome}: {cliente.endereco}")
