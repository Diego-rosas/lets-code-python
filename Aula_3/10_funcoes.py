

def soma_listas(lista1, lista2):
    nova_lista = []
    
    for valor1, valor2 in zip(lista1, lista2):
        nova_lista.append(valor1 + valor2)
    
    return nova_lista

lista1 = [1,4,3]
lista2 = [3,5,1]

print ('a soma das listas é: ', soma_listas(lista1, lista2))
