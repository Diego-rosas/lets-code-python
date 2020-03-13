carro = ['marca', 'ano', 'modelo', 'cor', 'potencia']
jogador = ['time', 'nome', 'numero_camisa', 'posicao', 'salario']
computador = ['marca', 'modelo', 'processador', 'memoria', 'preco']
cachorro = ['nome', 'raca', 'cor', 'tamanho', 'peso']

class Jogador():
    
    def __init__(self, nome_param, time_param, camisa_param, pos_param, salario_param):
        self.nome = nome_param
        self.time = time_param
        self.camisa = camisa_param
        self.posicao = pos_param
        self.salario = salario_param
            
pass

# tevez = Jogador('Tevez', 'Boca', 10, 'Atacante', 1000.00)

# print(tevez.nome)


class Carro():

    

    def __init__(self, marca, modelo, ano, versao, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.versao = versao
        self.cor = cor
        self.vendido = False
    
    def acelerar(self):
        print ('Aumentando a velocidade...')
    
    def frear(self):
        print ('reduzindo a velocidade...')

pass

corolla = Carro('Toyota', 'Sedan', 2010, 'xei', 'cinza')

print(corolla.ano)
corolla.acelerar()

class Cachorro():
    nome =''
    raca = ''
    porte = ''
    idade = 10
    manso = False
pass

pitty = Cachorro()

pitty.nome = 'Pitty'
pitty.raca = 'PitBull'
pitty.porte = 'medio'
pitty.idade = 16
pitty.manso = True


# print(pitty.nome)
