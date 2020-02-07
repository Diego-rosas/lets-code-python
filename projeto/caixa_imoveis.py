# from selenium import webdriver

import requests
from bs4 import BeautifulSoup

# abrir a página do sistema
# driver = webdriver.Chrome()

# driver.get('https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?')

url = 'https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?'

r = requests.get(url)

soup = BeautifulSoup( r.text, 'html.parser' )

tabela_ximoveis = soup.find('table')


for imovel in tabela_ximoveis.find_all('tr'):
    detalhe     = imovel.find_all('td')[0].a
    endereco    = imovel.find_all('td')[1].text.strip()
    print(detalhe, endereco)    

        
        


# for team in league_table.find_all('tbody'):
#     rows = team.find_all('tr')
#     for row in rows:
#         pl_team = row.find('td', class_ ='standing-table__cell standing-table__cell--name')
#         pl_team = pl_team['data-long-name']
#         points = row.find_all('td', class_ = 'standing-table__cell')[9].text
#         print(pl_team, points)





# tabela = driver.find_element_by_xpath("/html/body/table")

# resultado = tabela.get_attribute("outerHTML")

# soup = BeautifulSoup(resultado, 'html.parser')

# print (resultado)


# table_data = [[cell.text for cell in row("td")]
#                          for row in BeautifulSoup(resultado)("tr")]

# import json
# print (json.dumps(dict(table_data)))




# import urllib
# import urllib.request
# from bs4 import BeautifulSoup

# def make_soup(url):
#     thepage = urllib.request.urlopen(url)
#     soupdata = BeautifulSoup(thepage, "html.parser")
#     return soupdata

# soup = make_soup("https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?43193352")

# for registros in soup.findAll("tr"):
#     for dados in registros.findAll("td"):
#         print(dados.text)
    