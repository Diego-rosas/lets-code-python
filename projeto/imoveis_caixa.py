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



class ExtrairImoveis():

    pass

