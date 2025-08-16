from Cliente import Cliente

class PessoaJuridica(Cliente):
    def __init__(self, nome, dataNascimento, endereco, cnpj):
        super().__init__(nome, dataNascimento, endereco)
        self.cnpj = cnpj
        
    def tipoSociedade(self):
        None
        # Programar depois! Return str