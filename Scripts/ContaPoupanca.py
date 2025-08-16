from Conta import Conta
class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, rendimento):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento
    
    def acaoRendimento(self):
        None
        # Precisa por "Return None" ou só "None" já está certo?