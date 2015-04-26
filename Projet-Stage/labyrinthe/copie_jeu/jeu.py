import json
from constantes import *

class Objet: pass

class Jeu:
	def __init__(self, nom_fichier):
		with open(nom_fichier) as fichier:
			donnees = json.load(fichier)
			self.cases = donnees['cases']
			for ligne in self.cases:
				ligne = map(bool, ligne)
			self.perso = Objet()
			self.perso.l, self.perso.c, self.perso.dir = tuple(donnees['perso'])
			self.arrivee = Objet()
			self.arrivee.l, self.arrivee.c = tuple(donnees['fin'])

	def est_arrive(self):
		return (self.perso.l, self.perso.c) == (self.arrivee.l, self.arrivee.c)

	def peut_deplacer(self):
		l, c = DECALAGE[self.perso.dir]
		return not self.cases[self.perso.l + l][self.perso.c + c]

	def deplacer(self):
		l, c = DECALAGE[self.perso.dir]
		if not self.cases[self.perso.l + l][self.perso.c + c]:
			self.perso.l += l
			self.perso.c += c
