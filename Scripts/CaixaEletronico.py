from Carteira import Carteira
from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica
# Fazer de um jeito melhor essa parte acima

import os
def limpar():
    os.system('cls')
    
listaClientes = []

while True:
    limpar()
    print('''
        BEM VINDO AO BANCO JAUM
        
        1- Cadastrar Novo Cliente
        2- Pesquisar Por Cliente
        3- sair
        
        ''')
    x = input()
    if x == "1":
        #Cadastrar Cliente
        limpar()
        nome = input("Informe o nome do cliente: ")
        limpar()
        dataNascimento = input("Insira a data de nascimento do cliente: ")
        limpar()
        endereco = input("Insira o endereço do cliente: ")
        limpar()
        while True:
            limpar()
            print('''
                Informe o tipo de pessoa:
                1- Física
                2- Jurídica
                ''')
            x = input()
            if x == "1":
                limpar()
                cpf = input("Informe o cpf do cliente: ")
                objCliente = PessoaFisica(nome, dataNascimento, endereco, cpf)
                break
            elif x == "2":
                limpar()
                cnpj = input("Informe o cnpj do cliente: ")
                objCliente = PessoaJuridica(nome, dataNascimento, endereco, cnpj)
                break
            else:
                continue
                
        listaClientes.append(objCliente)
            
        
        
    elif x == "2":
        limpar()
        #Pesquisar cliente
        # Preciso saber como fazer polimorfismo nessa
        None
        
    elif x == "3":
        limpar()
        break
    
    
    else:
        continue