"""
Faça um programa que pede para o usuário digitar 5 números e, ao final, 
imprime uma lista com os 5 números digitados pelo usuário (sem converter os 
números para int ou float).  Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, 
o programa deve imprimir a lista ['1','5','2','3','6']
"""

lista = []
questao = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']

for numero in range(len(questao)):
    valor = input ('informe o {} número: '.format(questao[numero]))
    lista.append(valor)

print('a lista de números digitadas foi: ',lista)
