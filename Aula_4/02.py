palavra = input('digite uma palavra: ')

def maiusculas(palavra):
    nova_palavra = ''
    for letra in palavra:
        nova_palavra += letra.upper()
    
    return nova_palavra

print(maiusculas(palavra))