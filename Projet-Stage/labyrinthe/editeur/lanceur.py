from carte import *
from api import *
from constantes import *
from fenetre import *
from dessine import * 
from editeur import *
from enregistreur import *

def lancer_editeur(nom_fichier = None):
	initialiser()
	
	if not nom_fichier:
		dimension = lire_dimension()
		editeur = Editeur(dimension)
	else:
		editeur = Editeur(nom_fichier)
	fenetre = Fenetre(editeur)
	dessinateur = Dessinateur(fenetre)

	jeu_continue = True
	while jeu_continue:
		dessinateur.dessine_carte(editeur.carte)
		dessinateur.dessine_perso(editeur.carte)
		dessinateur.dessine_curseur(editeur.curseur,
				editeur.tuile_courante)

		evenement = attendre_action()

		if evenement.type == ACTION_QUITTER:
			jeu_continue = False
		elif evenement.type == ACTION_TOUCHE_ENFONCEE:
			if evenement.key == TOUCHE_ECHAP:
				jeu_continue = False
			elif evenement.key == TOUCHE_HAUT:
				editeur.deplacer_curseur(Direction.HAUT)

			elif evenement.key == TOUCHE_BAS:
				editeur.deplacer_curseur(Direction.BAS)

			elif evenement.key == TOUCHE_GAUCHE:
				editeur.deplacer_curseur(Direction.GAUCHE)

			elif evenement.key == TOUCHE_DROITE:
				editeur.deplacer_curseur(Direction.DROITE)

			elif evenement.key == TOUCHE_ENTRER:
				editeur.modifier_case()

			elif evenement.key == TOUCHE_SUPPR:
				editeur.supprimer_case()

			elif evenement.key == TOUCHE_MOINS:
				editeur.evoluer_curseur()

			elif evenement.key == TOUCHE_TABULATION:
				debug(editeur.curseur, afficher_curseur)
			
			elif evenement.key == TOUCHE_S and obtenir_mode() &\
										KMOD_CTRL:
				if editeur.carte.fin == POS_INTERDITE or\
				editeur.carte.perso.position == POS_INTERDITE:
					print 'erreur : il manque le personnage ou\
la carte.'
				else:
					enregistrer_carte(editeur.carte,\
						raw_input('fichier :'))
	
	quitter()
	
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		lancer_editeur(sys.argv[1])
	else:
		lancer_editeur()
