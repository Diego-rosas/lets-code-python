''' 
 4) Leia uma frase do usuário e informe as letras 
 e a quantidade de aparições
 '''

frase = input('digite algo: ')

letras = []
for palavra in frase:
    if palavra not in letras:
        letras.append(palavra)

# letras.remove(' ')

lista_final = []

for letra in letras:
    x = 0
    for repeticoes in frase:
        if repeticoes == letra:
            x = x + 1
    print('A letra:', letra ,'aparece', x , 'vezes')

