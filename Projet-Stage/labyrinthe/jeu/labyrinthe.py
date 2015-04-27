#! /usr/bin/env python2

#Variables:

carte = list()
fin = list()
perso = list()
perso_graphique = list()
fenetre = None
game_continue = bool()
event = None

#Debut:
import pygame, os
from api import *
from fonctions import *
from pygame.locals import *
from constantes import *

#initialise l'api
initialiser()

#creer la fenetre
fenetre = creer_fenetre(6 * LARGEUR, 7 * LARGEUR)

#initialise la carte
carte = creer_carte()

#creer le perso
perso = creer_perso()

#creer la fin
fin = creer_fin()

#condition pour que le jeu continue
game_continue = True

#tant que le jeu est en cours
while game_continue:
	#affiche la carte et le perso
	dessiner_tout(fenetre,carte,perso,fin)
	
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
			
			#deplace le perso sur la carte
			deplacer_perso(carte,perso)
		#s'il appuie sur la touche 'Gauche'
		elif event.key == K_LEFT:
			#fixe la direction du perso a la valeur de 'GAUCHE'
			perso[2] = GAUCHE
			
			#deplace le perso sur la carte
			deplacer_perso(carte,perso)
		#s'il appuie sur la touche 'Bas'
		elif event.key == K_DOWN:
			#fixe la direction du perso a la valeur de 'BAS'
			perso[2] = BAS
			
			#deplace le perso sur la carte
			deplacer_perso(carte,perso)
		#s'il appuie sur la touche 'Haut'
		elif event.key == K_UP:
			#fixe la direction du perso a la valeur de 'HAUT'
			perso[2] = HAUT
			
			#deplace le perso sur la carte
			deplacer_perso(carte,perso)
		#s'il appuie sur la touche 'Echape'
		elif event.key == K_ESCAPE:
			game_continue = False
	#si le perso est sur la case de fin
	if est_arrivee(perso,fin):
		#animation de fin du feu
		anim_fin(fenetre,carte,perso,fin)
		game_continue = False
		pause(.5)
		
#quitte le programme
quitter()
