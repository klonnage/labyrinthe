import pygame
from constantes import *

class Fenetre:
	def __init__(self, edit):
		dimension = edit.carte.dimension.c * LARGEUR,\
			edit.carte.dimension.l * LARGEUR
		self.fenetre = pygame.display.set_mode(dimension)

	def dessine(self, image, position, portion = None):
		self.fenetre.blit(image,position,portion)

	def affiche(self):
		pygame.display.flip()
