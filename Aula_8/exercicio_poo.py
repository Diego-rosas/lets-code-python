
class Cliente():

    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

class Sistema():

    def __init__(self):
        self.lista_registros = []

    def cadastrar(self):
        cpf = input('cpf?')
        nome = input('nome?')
        idade = int(input('idade?'))
        email = input('email?')
        
        cliente = Cliente(nome, idade, email)
        
        registro = {cpf:cliente}
        
        database = open('banco_de_dados.csv', 'a')
        database.write(cpf+','+nome+','+str(idade)+','+email+'\n')
        database.close()
        
        self.lista_registros.append(registro)
        print('cadastro...')

    def buscar(self):
        print()
        cpf_busca = input('digite o cpf desejado:')
        nao_encontrado = True
        
        for registro in self.lista_registros:
            if cpf_busca in registro.keys():
                nao_encontrado = False
                exibir_msg_bonita(registro[cpf_busca])
                break # força a parada de um laço (for/while)
            
            if nao_encontrado: # igual a 'if nao_encontrado == True:'
                print('Esse cpf não está cadastrado')

    def listar(self):
        print()
        print(self.lista_registros) # arrumar essa parte com o que ele demonsrou na aula
    

    def sair_sistema(self):
        print('saindo do sistema')
    



# Exercício de agr: Gravar em um arquivo (usando open()) as info...
#...do cadastro (cpf, nome, idade e email) (um por linha)

sistema = Sistema() # cria o sistema

def exibir_msg_bonita(registro):
    print('nome:', registro.nome)
    print('idade:', registro.idade)
    print('e-mail:', registro.email)

resposta = int(input('Selecione o menu:\n1 - Cadastro\n2 - Listagem\n3 - Buscar CPF\n4 - Sair'))
while resposta != 4:
    print()
	# Exibe menu
    if resposta == 1:
        sistema.cadastrar()
    
    elif resposta == 2:
        sistema.listar()
    
    elif resposta == 3:
        sistema.buscar()
    
    print()
    resposta = int(input('Selecione o menu:\n1 - Cadastro\n2 - Listagem\n3 - Buscar CPF\n4 - Sair'))

if resposta == 4:
    sistema.sair_sistema()
		