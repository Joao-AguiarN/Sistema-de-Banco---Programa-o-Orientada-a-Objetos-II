from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.limite = 2000