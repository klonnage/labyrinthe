#! /usr/bin/env python2

from api import *
from jeu import Jeu
from dessin import *
from constantes import *
from position import *


def lancement(nom_fichier = 'carte.json'):
	initialiser()

	quitter()

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 2:
		lancement(sys.argv[1])
	else:
		lancement()
