import pygame
from api import *

CHEMIN = '../../data/'

DELAI = 40

DROITE = 0
GAUCHE = 1
BAS = 2
HAUT = 3

SOLS = pygame.image.load(CHEMIN + 'textures.png')
PERSONNAGE = pygame.image.load(CHEMIN + 'red.png')

LARGEUR = 50

ID_SOL = 0
ID_MUR = 1
ID_FIN = 2
ID_PERSO = 3

NOMBRE_TUILE = ID_PERSO

SOL = Rectangle(pygame.Rect(0,0,50,50))
MUR = Rectangle(pygame.Rect(50,0,50,50))
FIN = Rectangle(pygame.Rect(100,0,50,50))

TEXTURES = [SOL, MUR, FIN]

class Direction:
	DROITE = Position(1, 0)
	GAUCHE = Position(-1, 0)
	BAS = Position(0, 1)
	HAUT = Position(0, -1)

PERSO_BAS = Rectangle(pygame.Rect(50,0,50,50))
	
PERSO_GAUCHE = Rectangle(pygame.Rect(50,50,50,50))
		
PERSO_DROITE = Rectangle(pygame.Rect(50,100,50,50))

PERSO_HAUT = Rectangle(pygame.Rect(50,150,50,50))
			
PERSO_RECT = [PERSO_DROITE, PERSO_GAUCHE, PERSO_BAS, PERSO_HAUT]

TUILES_AFFICHABLES = TEXTURES + PERSO_RECT

POS_INTERDITE = Position(-1, -1)
