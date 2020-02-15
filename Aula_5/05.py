'''
Crie uma função que receba os valores do nome, idade e e-mail de 
uma pessoa e guarde-os em um dicionário com as chaves ‘nome’, ‘idade’  
e  ‘email’, 
respectivamente.  Sua  função  deve retornar  esse dicionário.
'''

def cadastro(nome, idade, mail):
    pessoa = {'nome': nome, 'idade': idade, 'email': mail}
    return pessoa

nome = input('nome: ')
idade = int(input ('idade: '))
email = input ('email: ')

pessoa = cadastro(nome, idade, email)

print(pessoa)
