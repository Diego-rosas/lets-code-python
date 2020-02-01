def imprime_dobro(numero):
    return numero * 2    
  
num = int(input('digite um numero: '))

print('O dobro é', imprime_dobro(num), '\n')

'''
Faça uma função que recebe o valor do raio de um círculo e 
retorna o valor do comprimento de sua circunferência: C = 2*pi*r. 
'''

def circunferencia(raio):
    return 2 * 3.14 * raio

raio = float(input('Digite o Raio: '))
print ('A circunferencia é de ', round(circunferencia(raio),2))

def comprimentar(nome):
    print ('Olá {} beleza?'. format(nome), '\n')

comprimentar(input('digite seu nome: \n'))

def calculadora (operacao, numeros):
    if operacao == 1:
        return sum(numeros)
    

operacao = int(input('Digite 1 para soma, 2 multiplica, 3 divide ou 4 subtrai \n'))

operacoes = ['soma', 'multiplicação', 'divide', 'subtraçāo']

n1 = int(input('digite o primeiro valor: '))
n2 = int (input('digite o segundo valor: '))

numeros = [n1, n2]
print ('o resultado da operaçāo de {} foi de'.format(operacoes[operacao - 1]), calculadora(operacao, numeros))

