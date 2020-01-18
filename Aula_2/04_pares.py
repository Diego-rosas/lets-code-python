#Faça um programa que 
# olhe todos os itens de uma lista e diga quantos deles são pares.  

lista_qualquer = [1,2,3,4,5,6,7,8,9,10]
pares = []

for item in lista_qualquer:
    if item % 2 == 0:
        pares.append(item)

print('existem', len(pares), 'numeros pares na lista')

