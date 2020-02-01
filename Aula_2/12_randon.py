import random

lista = []
cont = 0

while cont < 10:
    lista.append(random.randint(1,10))
    cont +=1
print('lista oficial:', lista)

#a) 
# print(lista[0:4])
# print(lista[:4])

# #b) 
# tamanho_lista = len(lista)
# print(lista[tamanho_lista - 5:])

#c e d)
# numeros_pares = []
# numeros_impares = []

# for elemento in lista:
#     if elemento % 2 ==0:
#         numeros_pares.append(elemento)
#     else:
#         numeros_impares.append(elemento)
# print('lista numeros pares: ', numeros_pares)
# print ('lista numeros impares: ', numeros_impares)


#e) lista inversa sem o reverse
# lista.reverse()
# print('lista reversa', lista)

lista_2 = lista.copy() #se nao colocar .copy() fica sempre vinculado
lista_reversa = []

for indice, elemento in enumerate(lista_2):
    lista_reversa.append(lista_2[- indice + 1])

print('lista reversa:', lista_reversa)

# f lista inversa dos 5 primeiros numeros da lista

lista_inversa_cinco = []
lista_i_5 = lista[:5].copy()

print('cinco numeros', lista_i_5)

for elementos in lista_i_5:
    lista_inversa_cinco.append(lista_i_5[-1])
    lista_i_5.pop()
print('lista reversa cinco primeiros', lista_inversa_cinco)

# basta fazer um contador ao contrario e usar como indice da lista;
# reverse == altera a lista :: soh exibicao






 