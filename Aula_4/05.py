'''
Faça uma função que receba uma string e retorne uma 
nova string substituindo: 
'a' por '4' 
'e' por '3' 
'I' por '1' 
't' por '7'

'''

palavra = input('digite uma palavra: ')

def codificar(palavra):
    nova_palavra = []
    for letra in palavra:
        if letra == 'a':
            nova_palavra.append('4')
        elif letra == 'e':
            nova_palavra.append('3')
        elif letra == 'I':
            nova_palavra.append('1')
        elif letra == 't':
            nova_palavra.append('7')
        else:
            nova_palavra.append(letra)
    return ''.join(nova_palavra)

print(codificar(palavra))