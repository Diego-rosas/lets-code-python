class ImoveisCaixa():

    def __init__(self):

        nuContrato       = imovel.find('a', href=True)
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