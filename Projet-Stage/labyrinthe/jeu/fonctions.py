from api import *
from constantes import *
import pygame, json

#initialise le jeu
def creer_jeu():
	#ligne a modifier pour chaner la carte
	nom_fichier = 'carte.json'
	with open(CHEMIN + nom_fichier, "r") as fichier:
		donnees = json.load(fichier)
		carte = donnees["cases"]
		fin = donnees["fin"]
		perso = donnees["perso"]
	return carte, perso, fin
	
#deplace le perso sur la carte si le deplacement est possible
def deplacer_perso(perso):
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
				ajouter_dessin(SOLS,(j*LARGEUR,i*LARGEUR),SOL)
			#si la case a dessiner est un mur
			elif colone == 1:
				ajouter_dessin(SOLS,(j*LARGEUR,i*LARGEUR),MUR)
				
	#dessine la fin du niveau
	ajouter_dessin(SOLS, (fin[1]*LARGEUR, fin[0]*LARGEUR), FIN)

#dessine la carte, le personnage et la case de fin
def dessiner_perso(fenetre, perso):
	#stock temporairement la position du personnage
	position = (perso[1]*LARGEUR, perso[0]*LARGEUR)

	#dessine le personnage dans la bonne position sur la fenetre
	ajouter_dessin(PERSONNAGE, position, obtenir_portion(perso))
	
	#dessine du sol a l'endroit ou est le personnage
	ajouter_dessin(SOLS, position, SOL)
	
	#dessine tout
	tout_dessiner(fenetre)

#Verifie si le personnage est sur la case de fin		
def est_arrivee(perso,fin):
	return perso[0] == fin[0] and perso[1] == fin[1]

#dessine une petite animation pour la fin du niveau
def anim_fin(fenetre, perso):
	#fait tourner le personnage sur lui meme et affiche
	#'Tu as gagne'
	
	#affiche le message
	#la police de caractere
	police = creer_police(CHEMIN + 'police.ttf', 50)
	#Le message a afficher
	message = creer_message('You win!', police)
	#La taille de la fenetre
	taille_fenetre = obtenir_taille(fenetre)
	#La taille du message
	taille_message = obtenir_taille(message)
	#La position pour que le message soit centre
	centre = (taille_fenetre[0]-taille_message[0])/2, (taille_fenetre[1]-taille_message[1])/2
	for etape in range(10):
		#l'effet pour que le personnage tourne sur lui-meme
		perso[2] = etape % (HAUT + 1)
		#dessine le perso et la fin
		position = (perso[1] * LARGEUR, perso[0] * LARGEUR)
		ajouter_dessin(SOLS, position, FIN)
		
		ajouter_dessin(PERSONNAGE, position, obtenir_portion(perso))
		
		#affiche le message
		ajouter_dessin(message, centre)
		#dessine et affiche a l'ecran pour que
		#l'utilisateur puisse voir le rendu
		tout_dessiner(fenetre)
		afficher_ecran()
		#fait une pause pour laisser le temps a l'utilisateur
		#de voir le resultat
		pause(.05)

#dessine le personnage en mouvement
def dessiner_etape_mouvement(fenetre, perso, arrive, etape):
	#on stock la position de la case sur laquelle est le perso
	position = (perso[1] * LARGEUR, perso[0] * LARGEUR)
	#ajoute le sol a la liste des cases a affichee
	ajouter_dessin(SOLS, position, SOL)
	if perso[2] == DROITE:
		#position de la case a droite
		position = ((perso[1] + 1) * LARGEUR, perso[0] * LARGEUR)
		#indique la position du personnage
		deplacement_colone = 1
		deplacement_ligne = 0
	elif perso[2] == GAUCHE:
		#position de la case a droite
		position = ((perso[1] - 1) * LARGEUR, perso[0] * LARGEUR)
		#indique la position du personnage
		deplacement_colone = -1
		deplacement_ligne = 0
	elif perso[2] == BAS:
		#position de la case a droite
		position = (perso[1] * LARGEUR, (perso[0] + 1) * LARGEUR)
		#indique la position du personnage
		deplacement_colone = 0
		deplacement_ligne = 1
	elif perso[2] == HAUT:
		#position de la case a droite
		position = (perso[1] * LARGEUR, (perso[0] - 1) * LARGEUR)
		#indique la position du personnage
		deplacement_colone = 0
		deplacement_ligne = -1
		
	#calcule la position du personnage
	position_perso = (perso[1] * LARGEUR + deplacement_colone * etape * 25,perso[0] * LARGEUR + deplacement_ligne * etape * 25)
	#ajoute le personnage dans la liste des images a afficher
	ajouter_dessin(PERSONNAGE,position_perso,obtenir_portion(perso,(etape + 2) % 3))
	
	#si le personnage va arriver
	if arrive:
		#ajoute le sol a la liste des images a affichee
		ajouter_dessin(SOLS, position, FIN)
	else:
		#ajoute le sol a la liste des images a affichee
		ajouter_dessin(SOLS, position, SOL)

#dessine le mouvement du personnage
def dessiner_mouvement(fenetre, perso, arrive):
	for etape in range(2):
		dessiner_etape_mouvement(fenetre, perso, arrive, etape)
		tout_dessiner(fenetre)
		afficher_ecran()
		pause(.01)
	#dessine un carre de sol a l'acienne position du personnage
	#qui n'a pas encore ete change
	position = (perso[1] * LARGEUR, perso[0] * LARGEUR)
	if arrive:
		ajouter_dessin(SOLS, position, FIN)
	else:
		ajouter_dessin(SOLS, position, SOL)
		
#verifie si il y a quelque chose dans la case la plus proche
#de 'perso' en direction de 'perso[2]'
def peut_deplacer(carte,perso):
	if perso[2] == DROITE:
		return carte[perso[0]][perso[1] + 1] != 1
	elif perso[2] == GAUCHE:
		return carte[perso[0]][perso[1] - 1] != 1
	elif perso[2] == BAS:
		return carte[perso[0] + 1][perso[1]] != 1
	elif perso[2] == HAUT:
		return carte[perso[0] - 1][perso[1]] != 1
		
#indique si le personnage va arriver sur la case d'arrive
def va_arriver(perso, fin):
	if perso[2] == DROITE:
		return perso[1] == fin[1] and perso[0] + 1 == fin[0]
	elif perso[2] == GAUCHE:
		return perso[1] == fin[1] and perso[0] - 1 == fin[0]
	elif perso[2] == BAS:
		return perso[1] + 1 == fin[1] and perso[0] == fin[0]
	elif perso[2] == HAUT:
		return perso[1] - 1 == fin[1] and perso[0] == fin[0]
		
#affiche le timer
def afficher_temps(temps, police, couleur):
	#creer le message contenant le temps a afficher
	temps_message = creer_message(str(temps), police, couleur)
	#affiche deux murs pour afficher le timer par dessus
	#ajouter_dessin(SOLS, (0, 0), MUR)
	#ajouter_dessin(SOLS, (0, 50), MUR)
	
	#cree le fond
	fond = creer_surface(100, 50)
	dessiner_surface(fond, SOLS, (0,0), MUR)
	dessiner_surface(fond, SOLS, (50,0), MUR)
	dessiner_surface(fond, temps_message, (10 , 2))
	
	#affiche le timer en heut a gauche
	ajouter_dessin(fond, (0, 0))
