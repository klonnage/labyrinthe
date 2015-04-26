from constantes import *
from api import *

class Perso:
	def __init__(self,c = 0,l = 0,direction = DROITE):
		self.position, self.dir = Position(c, l), direction

class Carte:
	def __init__(self, dimension = Dimension()):
		self.dimension = dimension
		self.carte = [[0 for i in range(self.dimension.c)] 
						for i in range(self.dimension.l)]
		self.fixer_bord()
		self.fin = Position(1, 1)
		self.perso = Perso(1, 1)

	def poser_perso(self, position, direction):
		self.supprimer_tuile(position)
		self.perso.position = Position(position)
		self.perso.dir = direction

	def poser_tuile(self, position, identifiant_tuile):
		self.supprimer_tuile(position)
		if identifiant_tuile == ID_FIN:
			self.fin = Position(position)
		else:
			self.carte[position.l][position.c] =\
					identifiant_tuile

	def supprimer_tuile(self, position):
		if position == self.fin:
			self.fin.c, self.fin.l = -1, -1
		if position == self.perso.position:
			self.perso.position.c, self.perso.position.l = -1, -1
		self.carte[position.l][position.c] = ID_SOL
		
	def fixer_bord(self):
		self.carte[0] = [1 for i in self.carte[0]]
		fin = len(self.carte) - 1
		self.carte[fin] = [1 for i in self.carte[0]]
		fin_colone = len(self.carte[0]) - 1
		for ligne in self.carte:
			ligne[0], ligne[fin_colone] = 1, 1
