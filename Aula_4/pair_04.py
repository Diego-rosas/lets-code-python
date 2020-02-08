''' 
 4) Leia uma frase do usuário e informe as letras 
 e a quantidade de apariçõest
 '''

frase = input('digite algo: ')

letras = []
for palavra in frase:
    if palavra not in letras:
        letras.append(palavra)

# letras.remove(' ')

lista_final = []

for letra in letras:
    for x in frase:
        print(letra, x)
      




    



    
print(letras)


