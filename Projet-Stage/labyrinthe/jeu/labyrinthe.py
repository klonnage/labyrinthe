#Variables:

carte = list()
fin = list()
perso = list()
perso_graphique = list()
fenetre = None
game_continue = bool()
event = None

#Debut:
import pygame, os, fonctions
from pygame.locals import *
from constantes import *

#condition pour que le jeu continue
game_continue = True

#initialise le module pygame
pygame.init()
pygame.display.init()
pygame.font.init()

#creer la fenetre
fenetre = pygame.display.set_mode((10*LARGEUR,15*LARGEUR))

#initialise la carte
carte, perso, fin = fonctions.create_map(CHEMIN + 'carte')

#fixe le delay entre chaque appuie sur une touche
pygame.key.set_repeat(100,10)
#tant que le jeu est en cours
while game_continue:
	#affiche la carte et le perso
	fonctions.draw(fenetre,carte,perso,fin)
	
	#on attend un evenement
	event = pygame.event.wait()
	
	#On regarde le type de l'evenement
	#si l'utilisateur a demande de fermer la fenetre
	if event.type == QUIT:
		game_continue = False
	#si l'utilisateur appuie sur une touche
	elif event.type == KEYDOWN:
		#s'il appuie sur la touche 'Droite'
		if event.key == K_RIGHT:
			#fixe la direction du perso a la valeur de 'DROITE'
			perso[2] = DROITE
			
			#on verifie qu'il n'y a rien pour pouvoir se
			#deplacer
			if not(fonctions.have_something(carte,perso)):
				#deplace le perso sur la fenetre
				fonctions.draw_move(fenetre,carte,perso,fin)
				#deplace le perso sur la carte
				fonctions.move(carte,perso)
		#s'il appuie sur la touche 'Gauche'
		elif event.key == K_LEFT:
			#fixe la direction du perso a la valeur de 'GAUCHE'
			perso[2] = GAUCHE
			
			#on verifie qu'il n'y a rien pour pouvoir se
			#deplacer
			if not(fonctions.have_something(carte,perso)):
				#deplace le perso sur la fenetre
				fonctions.draw_move(fenetre,carte,perso,fin)
				#deplace le perso sur la carte
				fonctions.move(carte,perso)
		#s'il appuie sur la touche 'Bas'
		elif event.key == K_DOWN:
			#fixe la direction du perso a la valeur de 'BAS'
			perso[2] = BAS
			
			#on verifie qu'il n'y a rien pour pouvoir se
			#deplacer
			if not(fonctions.have_something(carte,perso)):
				#deplace le perso sur la fenetre
				fonctions.draw_move(fenetre,carte,perso,fin)
				#deplace le perso sur la carte
				fonctions.move(carte,perso)
		#s'il appuie sur la touche 'Haut'
		elif event.key == K_UP:
			#fixe la direction du perso a la valeur de 'HAUT'
			perso[2] = HAUT
			
			#on verifie qu'il n'y a rien pour pouvoir se
			#deplacer
			if not(fonctions.have_something(carte,perso)):
				#deplace le perso sur la fenetre
				fonctions.draw_move(fenetre,carte,perso,fin)
				#deplace le perso sur la carte
				fonctions.move(carte,perso)
		#s'il appuie sur la touche 'Echape'
		elif event.key == K_ESCAPE:
			game_continue = False
	#si le perso est sur la case de fin
	if fonctions.finish(perso,fin):
		#animation de fin du feu
		fonctions.anim_fin(fenetre,carte,perso,fin)
		game_continue = False
		pygame.time.wait(500)
		
#quitte pygame
pygame.font.quit()
pygame.display.quit()
pygame.quit()
