from Cliente import Cliente
from datetime import date

class PessoaFisica(Cliente):
    def __init__(self, nome, dataNascimento, endereco, cpf):
        super().__init__(nome, dataNascimento, endereco)
        self.cpf = cpf
        
    def maiorLegal(self, data):
        Data = data
        Data = Data.split("/")
        dia, mes, ano = Data[0], Data[1], Data[2]
        
        dataAtual = date.today
        dataAtual = dataAtual.split("-")
        diaAtual, mesAtual, anoAtual = dataAtual[0], dataAtual[1], dataAtual[2]
        
        if anoAtual
        