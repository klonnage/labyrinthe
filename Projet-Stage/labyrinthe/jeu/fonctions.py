from api import *
from constantes import *
import pygame, json

#initialise le jeu
def creer_carte():
	carte = [[1, 1, 1, 1, 1, 1],
			 [1, 0, 0, 0, 0, 1],
			 [1, 1, 1, 1, 0, 1],
			 [1, 0, 0, 0, 0, 1],
			 [1, 0, 1, 1, 1, 1],
			 [1, 0, 0, 0, 0, 1],
			 [1, 1, 1, 1, 1, 1]]
	return carte
			 
#initialise le perso
def creer_perso():
	perso = [1, 1, DROITE]
	return perso
	
#initialise la fin	
def creer_fin():
	fin = [5, 4]
	return fin
	
#deplace le perso sur la carte si le deplacement est possible
def deplacer_perso(carte, perso):
	#si on peut se deplacer
	if not peut_deplacer(carte,perso):
		if perso[2] == DROITE:
			perso[1] += 1
		elif perso[2] == GAUCHE:
			perso[1] -= 1
		elif perso[2] == HAUT:
			perso[0] -= 1
		elif perso[2] == BAS:
			perso[0] += 1

#dessine simplement la carte
def dessiner_carte(fenetre,carte,fin):
	#pour chaque ligne et chaque colone, on affiche la case 
	#correspondante
	for i,ligne in enumerate(carte):
		for j,colone in enumerate(ligne):
			#si la case a dessiner est un sol
			if colone == 0:
				dessiner_ecran(fenetre, SOLS,(j*LARGEUR,i*LARGEUR),SOL)
			#si la case a dessiner est un mur
			elif colone == 1:
				dessiner_ecran(fenetre, SOLS,(j*LARGEUR,i*LARGEUR),MUR)
				
	#dessine la fin du niveau
	dessiner_ecran(fenetre, SOLS, (fin[1]*LARGEUR, fin[0]*LARGEUR), FIN)

#dessine la carte, le personnage et la case de fin
def dessiner_tout(fenetre,carte,perso,fin):
	#dessine la carte et la fin a l'ecran
	dessiner_carte(fenetre,carte,fin)
	
	#dessine le personnage dans la bonne position sur la fenetre
	dessiner_ecran(fenetre, PERSONNAGE, (perso[1]*LARGEUR, perso[0]*LARGEUR), obtenir_portion_perso(perso[2]))
					
	#affiche la fenetre pour que l'utilisateur puisse voir 
	#l'image
	afficher_ecran()

#Verifie si le personnage est sur la case de fin		
def est_arrivee(perso,fin):
	return perso[0] == fin[0] and perso[1] == fin[1]

#dessine une petite animation pour la fin du niveau
def anim_fin(fenetre,carte,perso,fin):
	#fait tourner le personnage sur lui meme et affiche
	#'Tu as gagne'
	
	#affiche le message
	#la police de caractere
	police = creer_police(CHEMIN + 'police.ttf', 50)
	#Le message a afficher
	message = creer_message('You win!', police)
	#affiche la carte
	dessiner_tout(fenetre, carte, perso, fin)
	afficher_ecran()
	for i in range(10):
		#l'effet pour que le personnage tourne sur lui-meme
		perso[2] = i % (HAUT + 1)
		#dessine le perso et la fin
		position = (perso[1] * LARGEUR, perso[0] * LARGEUR)
		dessiner_ecran(fenetre, SOLS, position, FIN)
		
		dessiner_ecran(fenetre, PERSONNAGE, position, obtenir_portion_perso(perso[2]))
		
		#affiche le message
		fenetre.blit(message, (75, 150))
		#actualise l'ecran pour que l'utilisateur puisse voir
		#le rendu
		afficher_ecran()
		#fait une pause pour laisser le temps a l'utilisateur
		#de voir le resultat
		pause(.1)
		
#verifie si il y a quelque chose dans la case la plus proche
#de 'perso' en direction de 'perso[2]'
def peut_deplacer(carte,perso):
	if perso[2] == DROITE:
		return carte[perso[0]][perso[1] + 1] == 1
	elif perso[2] == GAUCHE:
		return carte[perso[0]][perso[1] - 1] == 1
	elif perso[2] == BAS:
		return carte[perso[0] + 1][perso[1]] == 1
	elif perso[2] == HAUT:
		return carte[perso[0] - 1][perso[1]] == 1
