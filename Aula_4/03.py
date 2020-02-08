palavra = input('digite uma palavra: ')

def alternadas(palavra):
    
    nova_palavra = ''
    for indice, letra in enumerate(palavra):
        if indice % 2 == 0:
            nova_palavra += letra.upper()
        else:
            nova_palavra += letra.lower()
    
    return nova_palavra

print(alternadas(palavra))