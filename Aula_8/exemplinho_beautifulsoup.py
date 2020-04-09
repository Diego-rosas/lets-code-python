import requests
from bs4 import BeautifulSoup

f = open('index_exemplo.html', 'rb') # lê o arquivo local na máquina

page = BeautifulSoup(f, 'lxml')

# print(page)


# Acessar as tags
# print(page.title) # Navegando por tags

# Buscar tag específica
#div_retornado = page.find('div')
#print(div_retornado.h1.text)


# Encontrando um link
link = page.find('div', class_='conteudo')


link_uol = link.find('a')['href'] # acesso a tag
print(link_uol) 
print(link_uol['href']) # acesso um atributo da tag

'''
lista_divs = page.find_all('div') # retorna uma lista com as tags
for div in lista_divs:
    print(div)
    print()

# Encontrando todos os links
link = page.find('div', class_='conteudo')
links = link.find_all('a') # acesso a tag

for l in links:
    print(l['href'])

'''