class Cliente:
    def __init__(self, nome, dataNascimento, endereco):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self.listaCarteiras = []
        