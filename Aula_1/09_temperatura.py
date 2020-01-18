# Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C).  °C = (5 * (F-32) / 9) 
# Obs: Tente também fazer um programa que faça o inverso: peça a temperatura em graus Celsius e a transforme em graus Fahrenheit

temperatura = int(input('digite uma temperatura em Fahrenheit: '))
celsius = (5 * (temperatura -32) / 9 )

print('A temperatura em Celsius é de: ', round(celsius, 2), 'ºC' )