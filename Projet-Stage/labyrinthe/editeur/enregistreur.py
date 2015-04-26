import json
from carte import *
from constantes import *

def enregistrer_carte(carte, nom_fichier = ''):
	if not nom_fichier:
		raise IOError('Entrez un nom de fichier.')
	else:
		with open(CHEMIN + nom_fichier,'w') as fichier:
			informations = {'cases':carte.carte,
						'perso':[carte.perso.position.c,
						 carte.perso.position.l,
						 carte.perso.dir],
						'fin':[carte.fin.c,
						 carte.fin.l]}
			json.dump(informations, fichier)
			
def charger_carte(nom_fichier = ''):
	if not nom_fichier:
		raise IOError('Entrez un nom de fichier.')
	else:
		try:
			carte = Carte(Dimension(1, 1))
			fichier = open(CHEMIN + nom_fichier, 'r')
			informations = json.load(fichier)
			carte.carte = informations['cases']
			carte.perso.position.c, carte.perso.position.l,\
				carte.perso.dir = tuple(informations['perso'])
			carte.fin.c, carte.fin.l = tuple(informations['fin'])
			fichier.close()
			return carte
		except IOError:
			print '{} : fichier \
introuvable.'.format(nom_fichier)
			import sys
			quitter()
			sys.exit()
