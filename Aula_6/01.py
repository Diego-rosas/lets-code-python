# arquivos
# persistir dados

'''
open() serve para manipular arquivos, modos de acesso:
Escrita = w (cria arquivos do zero)
Leitura = r (le arquivos existentes)
Adicionar = a (cria qdo nao existe, ou acresce qdo existe)
'''

arquivo = open('meu_primeiro_arquivo.txt', 'w')
arquivo.write('minha primeira mensagem em arquivo \n')
arquivo.close()

arquivo = open('meu_primeiro_arquivo.txt', 'r')
print (arquivo.readlines())
arquivo.close()

arquivo = open('meu_primeiro_arquivo.txt', 'a')
arquivo.write('Teste se vai pro Final')
arquivo.close()



# POO

