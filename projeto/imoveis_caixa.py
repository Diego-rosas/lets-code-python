class ImoveisCaixa():
    def __init__(self, link, endereco, bairro, descricao, preco, avaliacao, desconto, modalidade_venda, foto, cidade, estado):
        self.link_imovel = link
        self.endereco = endereco
        self.bairro = bairro
        self.descricao = descricao
        self.preco = preco
        self.avaliacao = avaliacao
        self.desconto = desconto
        self.modalidade_venda = modalidade_venda
        self.foto = foto
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return self.descricao
    
    def exibir_imovel(self):
        pass


#teste de classe
imovel_caixa = ImoveisCaixa ('<link>', 'rua', 'bixiga', 'centroVelho', 15000, 250000,'20%','leilão','#','Guarulhos','SP')


import requests
from bs4 import BeautifulSoup

class ExtrairImoveis():

    def acessa_ximoveis(self, url):
        response = requests.get(url)

        if response.status_code == requests.codes.ok:
            soup = BeautifulSoup (response.text, 'html.parser')
            tabela = soup.find('table')
            return tabela
        else:
            raise TypeError ("site fora do ar, código http:", response.status_code)
            

        
 
url = 'https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_SP.htm?'
rotina = ExtrairImoveis()

tabela = rotina.acessa_ximoveis(url)

print(tabela)

try: 
    print(tabela.find('tr'))
except:
    print("site fora do ar")



# for imovel in tabela.find_all('tr'):
#     detalhe = imovel.find('a', href=True)
#     print(detalhe)


        
            


