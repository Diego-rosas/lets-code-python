'''
3) Leia uma frase do usuário 
e informe qual é a maior palavra encontrada na frase
'''
def comp_maior(frase):
    lista_tamanhos = []
    lista_frase = []
    for palavras in frase.split():
        lista_tamanhos.append(len(palavras))
        lista_frase.append(palavras)
        
    maior = lista_tamanhos[0]
    for indice, item in enumerate(lista_tamanhos):
        if item > maior:
            maior = item
            maior_palavra = lista_frase[indice]

    print (' a maior palavra é, ', maior_palavra , 'e tem ', maior , ' letras')
        

frase = input('digite algo: ')
comp_maior(frase)

    