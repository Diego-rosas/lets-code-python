'''
 Faça um programa que peça 2 números inteiros e um número real, calcule e mostre: 

 a)o produto do dobro do primeiro com metade do segundo. 
 b)a soma do triplo do primeiro com o terceiro. 
 c)o terceiro elevado ao cubo.
'''


primeiro_numero = int(input('digite um número inteiro: '))
segundo_numero = int(input('digite um número inteiro: '))
terceiro_numero = float(input('digite um número real: '))


print ('o produto do dobro do primeiro com metade do segundo', (primeiro_numero*2) * (segundo_numero / 2) )
print ('a soma do triplo do primeiro com o terceiro: ', (primeiro_numero * 3) + terceiro_numero)
print ('o terceiro elevado ao cubo: ', terceiro_numero **3)
