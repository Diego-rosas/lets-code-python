'''
Faça um programa que pede para o usuário digitar 
uma palavra e cria uma nova string igual, porém com espaço 
entre cada letra, depois imprima a nova string: Exemplo: se o usuário
digitar "python" o programa deve imprimir  "p y t h o n "

'''

palavra = input('digite uma palavra: ')

nova_palavra = []
for letra in palavra:
    nova_palavra.append(letra)

print(' '.join(nova_palavra))