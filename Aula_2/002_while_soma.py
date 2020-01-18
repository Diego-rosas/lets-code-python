numero = int(input('digite um numero: '))

lista = 0
resultado = []

while lista < numero:
    resultado.append(numero)
    numero = numero - 1

#resultado.sort()

print('O resultado eh: ', sum(resultado))