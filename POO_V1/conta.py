from historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("\nOperação falhou! Saldo insuficiente.")
            return False
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        else:
            print("\nOperação falhou! Valor inválido.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
            return True
        else:
            print("\nOperação falhou! Valor inválido.")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([
            transacao for transacao in self.historico.transacoes
            if transacao["tipo"] == "Saque"
        ])

        if valor > self.limite:
            print("\nOperação falhou! Valor excede o limite.")
            return False
        elif numero_saques >= self.limite_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
            return False
        else:
            return super().sacar(valor)

    def __str__(self):
        return f"Agência: {self.agencia} | Conta: {self.numero} | Titular: {self.cliente.nome}"

    