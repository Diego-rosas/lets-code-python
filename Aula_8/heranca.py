# Herança
class Pet:
	def __init__(self, nome, raca, cor, idade):
		self.nome = nome
		self.raca = raca
		self.cor = cor
		self.idade = idade

	def comer(self):
		print( self.nome, 'esta comendo')

	def correr(self):
		print( self.nome, 'esta correndo')

	def morder(self):
		print( self.nome, 'esta mordendo')

class Cachorro(Pet):
	def __init__(self, nome, raca, cor, idade, porte):
		super().__init__(nome, raca, cor, idade)
		self.porte = porte

	def latir(self):
		print( self.nome, 'esta latindo')

class Gato(Pet):
	def __init__(self, nome, raca, cor, idade, peso):
		super().__init__(nome, raca, cor, idade)
		self.peso = peso

ming = Gato('ming', 'viralata', 'verde', 3, 3)
cadu = Cachorro('Cadu', 'beagle', 'tricolor', 4, 'medio')

ming.comer()
cadu.comer()
