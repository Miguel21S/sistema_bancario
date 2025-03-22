from modelos.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados < self.limite_saques and valor <= self.limite and valor <= self._saldo:
            self._saldo -= valor
            self.saques_realizados += 1
            return True
        print("Saque não permitido: Limite excedido ou saldo insuficiente.")
        return False

