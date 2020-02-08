'''
1) Dada uma lista, peça para o usuário digitar duas posições 
cujos elementos serão trocados de lugar
'''
import random

def trocaLugar(pos1, pos2):
    lista = []

    for indice in range(10):
        lista.append(random.randint(0,100))

    print(lista)


    valor1 = lista[pos1]
    valor2 = lista[pos2]

    lista[pos1] = valor2
    lista[pos2] = valor1

    return(lista)


pos1 = int(input('digite a primeira posicao: '))
pos2 = int(input('digite a segunda posicao: '))

print(trocaLugar(pos1, pos2))