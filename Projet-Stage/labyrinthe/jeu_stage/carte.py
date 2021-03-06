from position import *

class Carte:
	def __init__(self, cases, arrivee):
		self.cases = cases
		self.arrivee = Position(arrivee)
		for ligne in self.cases:
			ligne = map(bool, ligne)

	def est_arrive(self, perso):
		return perso.position == self.arrivee

	def peut_deplacer(self, pos):
		return not self.cases[pos.l][pos.c]
