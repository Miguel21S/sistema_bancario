
from modelos.pessoa_fisica import PessoaFisica
from modelos.saque import Saque
from modelos.conta_corrente import ContaCorrente
from modelos.deposito import Deposito

cliente = PessoaFisica("João", "1990-01-01", "12345678900", "Rua A, 123")

# Criar conta
conta = ContaCorrente(1001, cliente)
cliente.adicionar_conta(conta)

# Realizar depósito
deposito = Deposito(1000)
cliente.realizar_transacao(conta, deposito)

# Realizar saque
saque = Saque(300)
cliente.realizar_transacao(conta, saque)

print(f"Saldo final: {conta.saldo}")