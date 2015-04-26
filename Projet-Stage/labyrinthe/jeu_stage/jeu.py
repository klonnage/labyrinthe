import json
from constantes import *
from perso import *
from position import *
from carte import *
from position import *

class Jeu:
	def __init__(self, nom_fichier):
		with open(nom_fichier) as fichier:
			donnees = json.load(fichier)
			self.carte = Carte(donnees['cases'], donnees['fin'])
			
			self.perso = Personnage(0, 0, 0)
			self.perso.position.l, self.perso.position.c, self.perso.dir = tuple(donnees['perso'])
			
	def est_arrive(self):
		return self.carte.est_arrive(self.perso)
		
	def tourner_perso(self, direction):
		self.perso.tourner(direction)
		
	def deplacer_perso(self):
		self.perso.deplacer()
		
	def peut_deplacer(self):
		pos = self.perso.position + POSITIONS[self.perso.dir]
		return self.carte.peut_deplacer(pos)
