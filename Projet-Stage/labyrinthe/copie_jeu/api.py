import pygame
from pygame.locals import *
from constantes import *

ACTION_QUITTER = QUIT
ACTION_CLAVIER = KEYDOWN

TOUCHE_HAUT = K_UP
TOUCHE_BAS = K_DOWN
TOUCHE_GAUCHE = K_LEFT
TOUCHE_DROITE = K_RIGHT
TOUCHE_ECHAP = K_ESCAPE

def initialiser():
	pygame.init()
	pygame.display.init()
	pygame.font.init()
	pygame.key.set_repeat(100, 10)

def quitter():
	pygame.font.quit()
	pygame.display.quit()
	pygame.quit()

class Fenetre:
	def __init__(self, cases):
		self.display = pygame.display.set_mode(
				(len(cases[0]) * COTE_CASE,
				len(cases) * COTE_CASE))
		self.font = pygame.font.Font(DOSSIER + 'Lighthouse_PersonalUse.ttf', 50)
	def dessiner(self, image, position, portion):
		y, x = position
		position = x, y
		self.display.blit(image, position, portion)
	def ecrire(self, message):
		self.display.blit(self.font.render(message, True, pygame.Color(0, 0, 0)),
				(150, 300))
	def afficher(self):
		pygame.display.flip()

def obtenir_action():
	return pygame.event.wait()

def pause(duree):
	pygame.time.wait(int(duree * 1000))
