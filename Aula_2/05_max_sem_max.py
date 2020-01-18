#Faça um programa que imprima o maior número de uma lista, sem usar o método max().

lista = [1,2,3,4,5,6,7,8,9,10]

maior = lista[0]

for elemento in lista:
    if elemento > maior:
        maior = elemento

print (elemento)

    