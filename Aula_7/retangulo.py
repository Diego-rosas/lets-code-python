class Retangulo():
    
    def __init__(self, lado_menor, lado_maior):
        self.lado_menor = lado_menor
        self.lado_maior = lado_maior
    
    def calculo_area(self):
        return self.lado_menor * self.lado_maior

ret = Retangulo(5, 10)

print('A area é de: ', ret.calculo_area())

