# Faça um programa que peça o peso e altura de uma pessoa e calcule seu IMC 
# (Índice de Massa Corporal). Obs: IMC = Peso/Altura2

peso = float(input('informe seu peso: '))
altura = float(input('informe sua altura: '))

imc = peso / altura ** 2

print('seu IMC eh de: ', imc)