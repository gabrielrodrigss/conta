from banco import Banco
from cliente import Cliente
from conta import Conta

cliente1 = Cliente(123, "João", "Rua 1")
cliente2 = Cliente(123, "Maria", "Rua 2")
conta1 = Conta([cliente1, cliente2], 1, 2000)
# Criando novos objetos Cliente
cliente3 = Cliente(456, "Ana", "Rua 3")
cliente4 = Cliente(456, "José", "Rua 4")
# Criando uma nova conta com os novos clientes
conta2 = Conta([cliente3, cliente4], 2, 0)
conta1.transfereValor(conta2, 2000)
conta1.extrato.extrato(conta1.numero)
conta2.extrato.extrato(conta2.numero)
conta1.gerarsaldo()
conta2.gerarsaldo()
banco = Banco([conta1, conta2])
banco.armazenar_conta()



# #conta1.gerarsaldo()
# conta1.depositar(1000)
# conta1.sacar(1500)
# conta1.extrato.extrato(conta1.numero)
# #conta1.gerarsaldo()
# # conta1.imprimir_enderecos_clientes()
#
#
#
# conta2.gerarsaldo()
# conta2.depositar(2000)
# conta2.sacar(500)
# conta2.gerarsaldo()
# #conta2.imprimir_enderecos_clientes()







