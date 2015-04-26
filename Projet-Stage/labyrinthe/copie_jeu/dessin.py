from api import *
from constantes import *

def dessiner_carte(fenetre, jeu):
	for l, ligne in enumerate(jeu.cases):
		for c, case in enumerate(ligne):
			if case: rect_case = MUR
			else:    rect_case = SOL
			fenetre.dessiner(SOLS, (l * COTE_CASE, c * COTE_CASE), rect_case)
	fenetre.dessiner(SOLS, (jeu.arrivee.l * COTE_CASE, jeu.arrivee.c * COTE_CASE), FIN)

def dessiner_perso(fenetre, jeu):
	fenetre.dessiner(PERSONNAGE, (jeu.perso.l * COTE_CASE, jeu.perso.c * COTE_CASE),
			RECTS_PERSO[jeu.perso.dir][1])
	fenetre.afficher()

def dessiner_etape_mouvement(fenetre, jeu, etape):
	l, c = DECALAGE[jeu.perso.dir]
	fenetre.dessiner(PERSONNAGE,
			(jeu.perso.l * COTE_CASE + l * etape * 7,
			jeu.perso.c * COTE_CASE + c * etape * 7),
			RECTS_PERSO[jeu.perso.dir][(etape + 2) % 3])

def dessiner_mouvement(fenetre, jeu):
	for etape in range(7):
		dessiner_carte(fenetre, jeu)
		dessiner_etape_mouvement(fenetre, jeu, etape)
		fenetre.afficher()
		pause(DELAI)

def animation_fin(fenetre, jeu):
	for etape in range(10):
		jeu.perso.dir = etape % 4
		dessiner_carte(fenetre, jeu)
		dessiner_perso(fenetre, jeu)
		fenetre.ecrire("You win!")
		fenetre.afficher()
		pause(.05)
