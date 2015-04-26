import pygame
from position import *

DOSSIER = '../../data/'

DELAI = .04

class Direction:
	HAUT = 0
	BAS = 1
	GAUCHE = 2
	DROITE = 3

DECALAGE = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]

SOLS = pygame.image.load(DOSSIER + 'textures.png')
PERSONNAGE = pygame.image.load(DOSSIER + 'foxy.png')


COTE_CASE = 50

SOL = pygame.Rect(0, 0, 50, 50)
MUR = pygame.Rect(50, 0, 50, 50)
FIN = pygame.Rect(100, 0, 50, 50)

RECTS_PERSO = [
	[
		pygame.Rect(0, 150, 50, 50),
		pygame.Rect(50, 150, 50, 50),
		pygame.Rect(100, 150, 50, 50)
	],
	[
		pygame.Rect(0, 0, 50, 50),
		pygame.Rect(50, 0, 50, 50),
		pygame.Rect(100, 0, 50, 50)
	],
	[
		pygame.Rect(0, 50, 50, 50),
		pygame.Rect(50, 50, 50, 50),
		pygame.Rect(100, 50, 50, 50)
	],
	[
		pygame.Rect(0, 100, 50, 50),
		pygame.Rect(50, 100, 50, 50),
		pygame.Rect(100, 100, 50, 50)
	]
]
