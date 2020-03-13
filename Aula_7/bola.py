class Bola():
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
        self.area = self.area_bola(raio)
        self.volume = self.volume_bola(raio)
    
    def area_bola(self, raio):
        return 4*3.14*raio*raio/3;
    
    def volume_bola(self, raio):
        return 3.14*raio*raio*raio
    
    def imprime_atributos(self):
        print('A bola tem cor:', self.cor, 'area:', self.area, 'e raio', self.raio)

nova_bola = Bola('vermelha', 2)
nova_bola.imprime_atributos()

