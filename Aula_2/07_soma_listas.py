"""
Faça um programa que, dadas duas listas de mesmo tamanho,
crie uma nova lista com cada elemento igual a soma dos elementos da lista 1 
com os da lista 2, na mesma posição.  Exemplo: dadas lista1 = [1, 4, 5] e 
lista2 = [2, 2, 3], então lista3 = [1+2, 4+2, 5+3] = [3, 6, 8]
"""

lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
lista3 = []

for indice, elemento in enumerate(lista1):
    lista3.append(elemento + lista2[indice])

print(lista3)

lista4 = []
for valor1, valor2 in zip(lista1, lista2):
    lista4.append(valor1 + valor2)

print(lista4)


# um programa enquanto o numero for par

num = int(input('digite um numero: '))

while num % 2 == 0:
    num = int(input('digite um numero: '))

