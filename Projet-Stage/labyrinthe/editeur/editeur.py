from carte import *
from api import *
from constantes import *
from fenetre import *
from dessine import * 
from enregistreur import *

class Editeur:
	def __init__(self, *argument):
		if type(argument[0]) == type(Dimension()):
			self.carte = Carte(argument[0])
		else:
			self.carte = charger_carte(argument[0])
		self.dimension = self.carte.dimension
		self.curseur = Position(1, 1)
		self.tuile_courante = ID_SOL
		self.tuiles = None
	
	def __iter__(self):
		self.id_tuile = 0
		return self
		
	def next(self):
		if self.id_tuile == NOMBRE_TUILE:
			raise StopIteration
		self.id_tuile += 1
		return self.id_tuile
		
	def evoluer_curseur(self):
		if not self.tuiles:
			self.tuiles = iter(self)
		try:
			self.tuile_courante = next(self.tuiles)
		except StopIteration:
			self.tuiles = iter(self)
			self.tuile_courante = 0
	
	def poser_perso(self):
		self.carte.poser_perso(self.curseur, DROITE)
	
	def modifier_case(self):
		if self.tuile_courante <= ID_FIN:
			self.carte.poser_tuile(self.curseur,
					self.tuile_courante)
		else:
			self.carte.poser_perso(self.curseur,DROITE)

	def supprimer_case(self):
		self.carte.supprimer_tuile(self.curseur)

	def deplacer_curseur(self, direction):
		self.curseur.l = (self.curseur.l + direction.l - 1) % (self.dimension.l - 2) + 1
		self.curseur.c = ((self.curseur.c + direction.c - 1) % (self.dimension.c - 2)) + 1
