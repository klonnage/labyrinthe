#! /usr/bin/env python2

from api import *
from jeu import Jeu
from dessin import *
from constantes import *

def lancement(nom_fichier = 'carte.json'):
	initialiser()
	jeu = Jeu(DOSSIER + nom_fichier)
	fenetre = Fenetre(jeu.cases)

	def deplacer_perso(fenetre, jeu):
		if jeu.peut_deplacer():
			dessiner_mouvement(fenetre, jeu)
			jeu.deplacer()

	jeu_continue = True
	while jeu_continue:
		dessiner_carte(fenetre, jeu)
		dessiner_perso(fenetre, jeu)

		action = obtenir_action()
		if action.type == ACTION_QUITTER:
			jeu_continue = False
		elif action.type == ACTION_CLAVIER:
			if action.key == TOUCHE_HAUT:
				jeu.perso.dir = Direction.HAUT
				deplacer_perso(fenetre, jeu)
			elif action.key == TOUCHE_BAS:
				jeu.perso.dir = Direction.BAS
				deplacer_perso(fenetre, jeu)
			elif action.key == TOUCHE_GAUCHE:
				jeu.perso.dir = Direction.GAUCHE
				deplacer_perso(fenetre, jeu)
			elif action.key == TOUCHE_DROITE:
				jeu.perso.dir = Direction.DROITE
				deplacer_perso(fenetre, jeu)
			elif action.key == TOUCHE_ECHAP:
				jeu_continue = False

		if jeu.est_arrive():
			animation_fin(fenetre, jeu)
			pause(.5)
			jeu_continue = False

	quitter()

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		lancement(sys.argv[1])
	else:
		lancement()
