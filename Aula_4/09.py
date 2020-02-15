palavra  = input('? ')

alfabeto = 'abcdefghijlmnopqrstuvwxyz'
digitos = '0123456789'

lista_letras =[]
lista_digitos = []

for caracter in palavra:
    if caracter in alfabeto:
        lista_letras.append(caracter)
    elif caracter in digitos:
        lista_digitos.append(caracter)

print(lista_digitos)
print(lista_letras)
