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
		pass
		
	def tourner_perso(self, direction):
		pass
		
	def deplacer_perso(self):
		pass
		
	def peut_deplacer(self):
		pass
