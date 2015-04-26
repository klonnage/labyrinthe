import pygame
from pygame.locals import *
from constantes import *

ACTION_QUITTER = QUIT
ACTION_TOUCHE_ENFONCEE = KEYDOWN
ACTION_TOUCHE_RELACHEE = KEYUP
ACTION_BOUGER_SOURIE = MOUSEMOTION
ACTION_CLIQUE_ENFONCEE = MOUSEBUTTONDOWN
ACTION_CLIQUE_RELACHEE = MOUSEBUTTONUP

TOUCHE_HAUT = K_UP
TOUCHE_BAS = K_DOWN
TOUCHE_GAUCHE = K_LEFT
TOUCHE_DROITE = K_RIGHT
TOUCHE_ECHAP = K_ESCAPE
TOUCHE_SUPPR = K_DELETE
TOUCHE_ENTRER = K_RETURN
TOUCHE_TABULATION = K_TAB
TOUCHE_PLUS = K_PLUS
TOUCHE_MOINS = K_MINUS
TOUCHE_CONTROLE_DROIT = K_RCTRL
TOUCHE_CONTROLE_GAUCHE = K_LCTRL
TOUCHE_S = K_s

class Dimension:
	def __init__(self, c = 0, l = 0):
		self.c, self.l = c, l

class Position:
	def __init__(self,*argument):
		if len(argument) == 2:
			self.c ,self.l = argument
		elif len(argument) == 0:
			self.c, self.l = 0, 0
		else:
			self.c, self.l = argument[0].c, argument[0].l
			
	def __eq__(self, pos):
		return (self.c, self.l) == (pos.c, pos.l)

class Rectangle:
	def __init__(self,rect):
		self.rect = rect

def initialiser():
	pygame.init()
	pygame.display.init()
	pygame.font.init()

	pygame.key.set_repeat(100,100)

def quitter():
	pygame.font.quit()
	pygame.display.quit()
	pygame.quit()

def attendre_action():
	return pygame.event.wait()

def lire_dimension():
	dimension = Dimension()
	dimension.c, dimension.l = tuple(map(int,raw_input('Entrez les dimensions de la carte :').split()))
	return dimension

def afficher_carte(carte):
	for ligne in carte:
			print ligne

def afficher_curseur(curseur):
	print curseur.c , curseur.l

def debug(a_afficher,pour_afficher):
	pour_afficher(a_afficher)
	
def obtenir_mode():
	return pygame.key.get_mods()
