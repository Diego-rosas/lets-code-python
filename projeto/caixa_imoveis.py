import requests
from bs4 import BeautifulSoup


url = 'https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?'

r = requests.get(url)

soup = BeautifulSoup( r.text, 'html.parser' )

print(soup)

tabela_ximoveis = soup.find('table')

for imovel in tabela_ximoveis.find_all('a', href=True):
    detalhe = imovel['href']
    print(detalhe)

for imovel in tabela_ximoveis.find_all('tr'):
    detalhe         = imovel.find_all('a', href=True)
    # detalhe2          = imovel.find_all('td')[0].text.strip()
    endereco         = imovel.find_all('td')[1].text.strip()
    Bairro           = imovel.find_all('td')[2].text.strip()
    descricao        = imovel.find_all('td')[3].text.strip()
    preco            = imovel.find_all('td')[4].text.strip()
    valor_avaliado   = imovel.find_all('td')[5].text.strip() 
    desconto         = imovel.find_all('td')[6].text.strip()
    modalidade_venda = imovel.find_all('td')[7].text.strip()
    foto             = imovel.find_all('td')[8].text.strip()
    cidade           = imovel.find_all('td')[9].text.strip()
    estado           = imovel.find_all('td')[10].text.strip()
    print(detalhe)    
      
    