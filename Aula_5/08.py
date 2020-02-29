'''
Faça um programa que fique pedindo uma resposta do usuário, 
entre 1, 2 e 3. Se o usuário digitar 1, o programa deve cadastrar um novo 
usuário nos moldes do exercício 5 e guardar esse cadastro num dicionário cuja
chave será o CPF da pessoa. Quando o usuário digitar 2, o programa deve
 imprimir os usuários cadastrados; e se o usuário digitar 3, o programa 
 deve fechar.    
 Exemplo do dicionário:   
 ‘987.654.321-00’: 
 {‘nome’: Maria, ‘idade’: 20, ‘email’ :maria@ig.com}
 ''' 

def cadastro(cpf, nome, idade, mail):
     return { cpf: {'nome': nome, 'idade': idade, 'email': mail}}
     
## print (cadastro('333', 'vlad', 36, 'vlad@teste.com'))

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
        respostas.update(cadastro(cpf, nome, idade, email))

    elif resposta == '2':
        print('vc digitou 2 - exibe cadastro')
        print(respostas)
    
    elif resposta == '3':
        cpf_busca = input('digite o cpf desejado: ')

        # for registros in respostas:
        #     if registros == cpf_busca:
        #         print(respostas[registros])
        
        # v1 serve para lista de dicionarios
        # for registros in respostas:
        #     if cpf_busca in respostas.keys():
        #         print(respostas[cpf_busca])

        
        #v2 serve para dicionarios de dicionarios
        # {cpf:{}}
        if cpf_busca in respostas.keys():
            print(respostas[cpf_busca])
        else:
            print('Esse CPF nao está cadastrado')

    
    else:
        print('Tchau!')
        resposta = '4'

