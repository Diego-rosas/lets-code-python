import random

sorteio = []
qtde_numeros = 10

while qtde_numeros:
    sorteio.append(random.randint(0,100))
    qtde_numeros -= 1

print('dez numeros sorteados:', sorteio, '\n')

maior50 = 0
for numero in sorteio:
    if numero > 50:
        maior50 += 1
print('existem', maior50, 'numeros maiores que 50. \n')

#14 
maior = sorteio[0]
for numero in sorteio:
    if numero > maior:
        maior = numero
print(maior, 'eh o maior numero da lista \n')


menor = sorteio[0]
for numero in sorteio:
    if numero < menor:
        menor = numero
print('o menor numero da lista eh', menor)

soma = 0

for numero in sorteio:
    soma = soma + numero
media = soma / len(sorteio)
print('a soma deu isso:', soma)
print(media, 'é a media')
