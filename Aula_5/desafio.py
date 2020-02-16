clientes_v1 = [{'nome':'Ana', 'idade':54, 'salario': 1220}, 
			{'nome':'João', 'idade':48, 'salario': 5020},
			{'nome':'Fernando', 'idade':31, 'salario': 1500},
			{'nome':'Silva', 'idade':23, 'salario': 1890},
			{'nome':'William', 'idade':34, 'salario': 7000},
			{'nome':'Beatriz', 'idade':24, 'salario': 2000},
			{'nome':'Cássia', 'idade':40, 'salario': 1220},
			{'nome':'Maria', 'idade':35, 'salario': 1220}]

clientes_v2 = {'nomes':['Ana', 'João', 'Fernando', 'Silva', 'William', 'Beatriz', 'Cássia', 'Maria'],
			'idades':[54, 48, 31, 23, 34, 24, 40, 35],
			'salario':[1220, 5020, 1500, 1890, 7000, 2000, 1220, 1220]}

# Qual a média de idade?
# Qual a média de salário?

soma_idades = 0
soma_salarios = 0
for indice, item in enumerate(clientes_v1):
    soma_idades += clientes_v1[indice]['idade']
    soma_salarios += clientes_v1[indice]['salario']
print ('a media de idade é de: ', soma_idades/len(clientes_v1))
print ('a soma dos salarios é de: ', soma_salarios)

# Qual o mais jovem/velho?
mais_jovem = clientes_v1[0]['idade']
mais_velho = clientes_v1[0]['idade']
maior_salario = clientes_v1[0]['salario']

rico = 0
for indice, pessoa in enumerate(clientes_v1):
    
    if mais_jovem > clientes_v1[indice]['idade']:
        mais_jovem = clientes_v1[indice]['idade']
    
    if mais_velho < clientes_v1[indice]['idade']:
        mais_velho = clientes_v1[indice]['idade']

    if maior_salario < clientes_v1[indice]['salario']:
        maior_salario = clientes_v1[indice]['salario']
        nome_rico = clientes_v1[indice]['nome']
        idade_rico = clientes_v1[indice]['idade']
       
print('O mais jovem tem: {} e o mais velho tem {}'.format(
    mais_jovem, mais_velho))

print('o maior salario é de {} quem ganha é {} e tem {} anos'.format(
    maior_salario,
    nome_rico,
    idade_rico ))
# Quem ganha o maior salario? (o nome e idade)
