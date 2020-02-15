'''
crie um dicionario cujas chaves 
sao os meses do ano e os valores sao a duracao em dias de cada mes
'''

dicionario = { 
    'janeiro':31,
    'fevereiro':28,
    'marco': 30,
    'abril': 31,
    'maio': 30,
    'junho': 30,
    'julho': 31,
    'agosto': 31,
    'setembro': 30,
    'outubro': 30,
    'novembro': 30,
    'dezembro': 31 
    }

''' imprima cada resultado '''

print(dicionario)

for mes in dicionario.items():
    print (mes)

for mes in dicionario.items():
    print(mes[0], '-', mes[1])

for mes, dias in dicionario.items():
    print(mes, dias)