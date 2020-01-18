# faça um programa que peça ao usuario um numero e imprima todos os numeros de
# um ateh o numero dado

numero = int(input('digite um numero: '))

lista = 0
resultado = []

while lista < numero:
    resultado.append(numero)
    numero = numero - 1

resultado.sort()

print(resultado)