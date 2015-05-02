#! /usr/bin/env python2


#Debut:
import pygame, os
from api import *
from fonctions import *
from pygame.locals import *
from constantes import *

#initialise l'api
initialiser()

#creer la police 'police_basique'
police_basique = creer_police(CHEMIN + 'police_basique.ttf', 55)

#initialise la carte
carte, perso, fin = creer_jeu()

#creer la fenetre
fenetre = creer_fenetre(len(carte[0]) * LARGEUR, len(carte) * LARGEUR)

#affiche la carte et le perso
dessiner_carte(fenetre,carte,fin)

#condition pour que le jeu continue
jeu_en_cours = True

#temps de depart pour le jeu
temps_debut = obtenir_temps()

#tant que le jeu est en cours
while jeu_en_cours:
	#calcul de la difference de temps a afficher
	temps_actuel = obtenir_temps()
	temps = temps_actuel - temps_debut
	
	#permet d'afficher le timer
	afficher_temps(temps, police_basique, bleu)
	
	#synchronise les actions (ex: touche enfoncee) avec l'ordinateur
	synchroniser_actions()
	
	#on regarde les touches sur lesquelles l'utilisateur appuient
	clavier = obtenir_touche()
	
	#indique que le personnage se deplace
	deplace = False
			
	#si l'utilisateur appuie sut la touche 'Droite'
	if touche_enfoncee(clavier, TOUCHE_DROITE):
		#fixe la direction du perso a la valeur de 'DROITE'
		perso[2] = DROITE
		#autorise le deplacement
		deplace = True
		
	#s'il appuie sur la touche 'Gauche'
	elif touche_enfoncee(clavier, TOUCHE_GAUCHE):
		#fixe la direction du perso a la valeur de 'GAUCHE'
		perso[2] = GAUCHE
		#autorise le deplacement
		deplace = True
		
	#s'il appuie sur la touche 'Bas'
	elif touche_enfoncee(clavier, TOUCHE_BAS):
		#fixe la direction du perso a la valeur de 'BAS'
		perso[2] = BAS
		#autorise le deplacement
		deplace = True
		
	#s'il appuie sur la touche 'Haut'
	elif touche_enfoncee(clavier, TOUCHE_HAUT):
		#fixe la direction du perso a la valeur de 'HAUT'
		perso[2] = HAUT
		#autorise le deplacement
		deplace = True
		
	elif touche_enfoncee(clavier, K_e):
		perso[:2] = list(fin)
		
	#s'il appuie sur la touche 'Echap'
	elif touche_enfoncee(clavier,TOUCHE_ECHAP):
		jeu_en_cours = False
		
	#si le perso peut se deplacer et qu'il n'y a rien devant lui
	if deplace and peut_deplacer(carte, perso):
		#regarde si le personnage va arrivee
		arrive = va_arriver(perso, fin)
		#deplace le perso a l'ecran
		dessiner_mouvement(fenetre, perso, arrive)
		#deplace le perso sur la carte
		deplacer_perso(perso)
		
	#si le perso est sur la case de fin
	if est_arrivee(perso,fin):
		#animation de fin du feu
		anim_fin(fenetre, perso)
		jeu_en_cours = False
		pause(.5)
		
	#si le temps depasse 20 secondes on dit que le joueur a perdu
	if temps >= 20:
		#recupere la taille du perso
		taille_fenetre = obtenir_taille(fenetre)
		#ecrit 'tu as perdu'
		ecrire_centre("Tu as perdu!", police_basique, rouge, taille_fenetre)
		#dessine et affiche tout a l'ecran
		dessiner_perso(fenetre, perso)
		#un dernier pour la route
		tout_dessiner(fenetre)
		#et on affiche!!
		afficher_ecran()

		#petite pause avant de quitter le jeu, pour que le joueur puisse voir le resultat
		pause(1)
		#pour qutter le jeu
		jeu_en_cours = False
		
		
	#dessine et affiche tout a l'ecran
	dessiner_perso(fenetre, perso)
	#tout_dessiner(fenetre)
	afficher_ecran()

#quitte le programme
quitter()
