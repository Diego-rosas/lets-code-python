import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?43193352")

for registros in soup.findAll("tr"):
    for dados in registros.findAll("td"):
        print(dados.text)
    