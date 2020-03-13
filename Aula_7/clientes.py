class Cliente():

    def __init__(self, nome, idade, email, cpf):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf
    
    def imprime_cliente(self):
        print('\n Nome Cliente: {}\n Idade: {} \n E-mail: {} \n'.format(self.nome, 
        self.idade, self.email))

    def retorna_dicionario(self):
        return { self.cpf: {'nome': self.nome, 'idade': self.idade, 'email': self.email}}

    
cliente = Cliente('Fulano de Tal', 40, 'fulano@email.com', '666.666.171-00')
cliente.imprime_cliente()

class Sistema():

    def iniciar_sistema(self):
        # perguntar ao user
        pass

    def cadastrar_cliente(self, nome, idade, email, cpf):
        return novo_cliente = Cliente(nome, idade, email, cpf)
    
    def exibir_clientes_cadastrados(self):
        pass

    def buscar_cliente(self):
        pass

    def sair(self):
        pass



        


    resposta = ''
    respostas = {}
    while resposta != '4':
        
        resposta = input('digite 1 para cadastro, 2 para exibir e 3 para buscar, 4 para sair: ')
        
        if resposta == '1':
            print('vc digitou 1 - cadastro')
            cpf = input('digite CPF: ')
            nome = input('digite o nome: ')
            idade = input('digite a idade: ')
            email = input ('digite o email: ')
            cliente = Cliente(nome, idade, email, cpf)

        elif resposta == '2':
            print('vc digitou 2 - exibe cadastro')
            print(respostas)
        
        elif resposta == '3':
            cpf_busca = input('digite o cpf desejado: ')

            if cpf_busca in respostas.keys():
                print(respostas[cpf_busca])
            else:
                print('Esse CPF nao está cadastrado')

        else:
            print('Tchau!')
            resposta = '4'



