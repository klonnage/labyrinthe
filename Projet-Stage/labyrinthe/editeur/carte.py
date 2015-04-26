from constantes import *
from api import *

class Perso:
	def __init__(self,c = 0,l = 0,direction = DROITE):
		self.position, self.dir = Position(c, l), direction

class Carte:
	def __init__(self, dimension = Dimension()):
		self.dimension = dimension
		self._carte =[[0 for i in range(self.dimension.c)] 
						for i in range(self.dimension.l)]
		self.fin = Position()
		self.perso = Perso()

	def poser_perso(self, position, direction):
		self.supprimer_tuile(position)
		self.perso.position = Position(position)
		self.perso.dir = direction

	def poser_tuile(self, position, identifiant_tuile):
		self.supprimer_tuile(position)
		if identifiant_tuile == ID_FIN:
			self.fin = Position(position)
		else:
			self._carte[position.l][position.c] =\
					identifiant_tuile

	def supprimer_tuile(self, position):
		if position == self.fin:
			self.fin.c, self.fin.l = -1, -1
		if position == self.perso.position:
			self.perso.position.c, self.perso.position.l = -1, -1
		self._carte[position.l][position.c] = ID_SOL
	
	@property
	def carte(self):
		return self._carte
		
	@carte.setter
	def carte(self, nouvelle_carte):
		print 'e'
		self._carte = nouvelle_carte
		self.dimension = Dimension(self._carte.c, self._carte.l)
