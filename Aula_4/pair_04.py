''' 
 4) Leia uma frase do usuário e informe as letras 
 e a quantidade de aparições
 '''

def conta_letras_frase(frase):
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
        
        if letra != ' ':
            print (letra, x)
            tupla = (letra , x) # aqui eu poderia só dar um print, mas vou seguir com tuplas;
        lista_final.append(tupla)

    
    return lista_final

frase = input('digite algo: ')

print('resultado da expressão', frase, ':', conta_letras_frase(frase))