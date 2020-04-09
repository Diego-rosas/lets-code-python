class Retangulo():
    def __init__(self, lado, lado_maior):
         self.lado_menor = lado
         self.lado_maior = lado_maior
    
    def calculo_area(self):
        return self.lado_menor * self.lado_maior

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    

q = Quadrado.calculo_area(15)