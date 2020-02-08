'''
2) Leia do usuário uma frase e imprima na tela a frase com a
 primeira letra de cada palavra em caixa-alta (maiusculo)

'''
def caixa_alta(frase):

    nova_frase = []
    for palavras in frase.split():
        nova_frase.append(palavras.capitalize())

    return(' '.join(nova_frase))

frase = input('digite algo: ')
print(caixa_alta(frase))