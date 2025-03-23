from cliente import PessoaFisica
from conta import ContaCorrente
from transacao import Saque, Deposito

def main():
    cliente = PessoaFisica("Miguel", "1990-10-10", "46849148", "Rua A, 1234")
    conta = ContaCorrente.nova_conta(cliente, 1001)
    cliente.adicionar_conta(conta)

    print(conta)

    # Realizar depósito
    deposito = Deposito(1000)
    cliente.realizar_transacao(conta, deposito)

    # Realizar saques
    saque1 = Saque(200)
    cliente.realizar_transacao(conta, saque1)

    saque2 = Saque(600)  # Excede limite
    cliente.realizar_transacao(conta, saque2)

    saque3 = Saque(300)  # Dentro do limite
    cliente.realizar_transacao(conta, saque3)

    print(f"Saldo final: {conta.saldo}")

if __name__ == "__main__":
    main()
