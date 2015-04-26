import pygame

#Chemin permettant d'acceder a la carte
CHEMIN = '../../data/'

#Delai d'attente entre chaque affichage
DELAI = 40

#Directions:
DROITE = 0
GAUCHE = 1
BAS = 2
HAUT = 3

#Images
SOLS = pygame.image.load(CHEMIN + 'textures.png')
PERSONNAGE = pygame.image.load(CHEMIN + 'spritesPerso.png')

#Dimension d'une tuile
LARGEUR = 50

#Rectangles pour l'affichage des textures
SOL = pygame.Rect(0,0,50,50)
MUR = pygame.Rect(50,0,50,50)
FIN = pygame.Rect(100,0,50,50)

#Listes des rectangles pour l'affichage des personnages
#Le personnage en position statique est dans chaque liste
# la case du milieu
P_BAS = [pygame.Rect(0,0,50,50),
		pygame.Rect(50,0,50,50),
		pygame.Rect(100,0,50,50)]
		
P_GAUCHE = [pygame.Rect(0,50,50,50),
			pygame.Rect(50,50,50,50),
			pygame.Rect(100,50,50,50)]
			
P_DROITE = [pygame.Rect(0,100,50,50),
			pygame.Rect(50,100,50,50),
			pygame.Rect(100,100,50,50)]

P_HAUT = [pygame.Rect(0,150,50,50),
			pygame.Rect(50,150,50,50),
			pygame.Rect(100,150,50,50)]
			
PERSO_RECT = [P_DROITE,P_GAUCHE,P_BAS,P_HAUT]
