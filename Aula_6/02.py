# Exercício de agr: Gravar em um arquivo (usando open()) as info...
#...do cadastro (cpf, nome, idade e email) (um por linha)

lista_registros = []

def exibir_msg_bonita(registro):
	for key, value in registro.items():
		print(key, value)

def gravar_no_arquivo(cpf, nome, idade, email):
    arquivo = open('base.txt', 'a')
    arquivo.write (cpf +',' + nome +',' +str(idade) +',' + email + '\n')
    arquivo.close()


resposta = int(input('Selecione o menu:\n1 - Cadastro\n2 - Listagem\n3 - Buscar CPF\n4 - Sair'))
while resposta != 4:
	print()
	# Exibe menu
	if resposta == 1:
		# Faz o cadastro
		print()
		cpf = input('cpf?')
		nome = input('nome?')
		idade = int(input('idade?'))
		email = input('email?')

		gravar_no_arquivo(cpf, nome, idade, email)
        

		registro = {cpf:{'nome':nome,
							'idade':idade,
							'email':email}}

		lista_registros.append(registro)

		print('cadastro...')
		
	elif resposta == 2:
		# Faz a listagem dos cadastros
		print()
		print(lista_registros)
		

	elif resposta == 3:
		# Faz a busca por CPF
		print()
		cpf_busca = input('digite o cpf desejado:')

		nao_encontrado = True

		# v1 - Só serve para lista de dicionários
		for registro in lista_registros:
			if cpf_busca in registro.keys():
				nao_encontrado = False
				exibir_msg_bonita(registro[cpf_busca])
				break # força a parada de um laço (for/while)

		# v2 - Só serve para dicionário de dicionários
		# registros = {'1':{...}, '2':{...}, '3':{...}, ...}
		'''if cpf_busca in registros.keys():
			print(registros[cpf_busca])
		else:
			print('Esse cpf não está cadastrado')'''

		if nao_encontrado: # igual a 'if nao_encontrado == True:'
			print('Esse cpf não está cadastrado')

	print()
	resposta = int(input('Selecione o menu:\n1 - Cadastro\n2 - Listagem\n3 - Buscar CPF\n4 - Sair'))

if resposta == 4:
	print('saindo do sistema')	
