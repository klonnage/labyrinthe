from constantes import *
import pygame, json

#initialise le jeu
def create_map(filename):
	#ouvre le fichier 'carte' contenue dans '../data'
	#ps: ce mode d'ouverture est plus sur car il garantit que 
	#le fichier va se fermer quoi qu'il se passe
	with open(filename) as fichier:
		#stock le contenu du fichier dans un dictionnaire
		#pour faciliter l'extraction des donnees
		dico = json.load(fichier)
		#extrait les donnees
		carte = dico['carte']
		perso = dico['perso']
		fin = dico['fin']
		return carte, perso, fin

#deplace le perso sur la carte si le deplacement est possible
def move(carte,perso):
	#si on peut se deplacer
	if not(have_something(carte,perso)):
		if perso[2] == DROITE:
			perso[1] += 1
		elif perso[2] == GAUCHE:
			perso[1] -= 1
		elif perso[2] == HAUT:
			perso[0] -= 1
		elif perso[2] == BAS:
			perso[0] += 1

#extrait une liste de dimension rect dans carte		
def extract_sublist(carte,x_min,x_max,y_min,y_max):
	sub = []
	#on parcourt chaque ligne en partant de la ligne 'x_min' a 
	#'x_max'
	#cette 'for' permet d'extraire la sous liste de la liste
	#principale
	for elem in carte[y_min:y_max+1]:
		sub.append(list(elem[x_min:x_max+1]))
	return sub

#dessine simplement la carte
def draw_map(fenetre,carte,fin):
	#pour chaque ligne et chaque colone, on affiche la case 
	#correspondante
	for i,ligne in enumerate(carte):
		for j,colone in enumerate(ligne):
			#si la case a dessiner est un sol
			if colone == 0:
				fenetre.blit(SOLS,(j*LARGEUR,i*LARGEUR),SOL)
			#si la case a dessiner est un mur
			elif colone == 1:
				fenetre.blit(SOLS,(j*LARGEUR,i*LARGEUR),MUR)
				
	#dessine la fin du niveau
	fenetre.blit(SOLS,(fin[1]*LARGEUR,fin[0]*LARGEUR),FIN)

#dessine la carte, le personnage et la case de fin
def draw(fenetre,carte,perso,fin):
	#dessine la carte et la fin a l'ecran
	draw_map(fenetre,carte,fin)
	
	#dessine le personnage dans la bonne position sur la fenetre
	fenetre.blit(PERSONNAGE,(perso[1]*LARGEUR,perso[0]*LARGEUR),
					PERSO_RECT[perso[2]][1])
					
	#actualise la fenetre pour que l'utilisateur puisse voir 
	#l'image
	pygame.display.flip()

#dessine le personnage a une certaine etape
def draw_perso_move(fenetre,perso,etape):
	if perso[2] == DROITE:
		fenetre.blit(PERSONNAGE,(perso[1]*LARGEUR + etape * 7,
				perso[0]*LARGEUR),P_DROITE[(etape+2)%3])
	elif perso[2] == GAUCHE:
		fenetre.blit(PERSONNAGE,(perso[1]*LARGEUR - etape * 7,
				perso[0]*LARGEUR),P_GAUCHE[(etape+2)%3])
	elif perso[2] == HAUT:
		fenetre.blit(PERSONNAGE,(perso[1]*LARGEUR,
			perso[0]*LARGEUR - etape * 7),P_HAUT[(etape+2)%3])
	elif perso[2] == BAS:
		fenetre.blit(PERSONNAGE,(perso[1]*LARGEUR,
			perso[0]*LARGEUR + etape * 7),P_BAS[(etape+2)%3])
				
#dessine la carte, la fin  et le personnage en mouvement	
def draw_move(fenetre,carte,perso,fin):
	#dessine le mouvement en trois images
	for i in range(7):
		#dessine la carte
		draw_map(fenetre,carte,fin)
		#dessine le personnage a l'etape 'i'
		draw_perso_move(fenetre,perso,i)
		#actualise l'image pour que l'utilisateur puisse la voir
		pygame.display.flip()
		#fait une pause de 50 miliseconde pour que l'utilisateur
		#puisse observer le changement d'image 
		pygame.time.wait(DELAI)

#Verifie si le personnage est sur la case de fin		
def finish(perso,fin):
	return perso[0] == fin[0] and perso[1] == fin[1]

#dessine une petite animation pour la fin du niveau
def anim_fin(fenetre,carte,perso,fin):
	#fait tourner le personnage sur lui meme et affiche
	#'Tu as gagne'
	for i in range(10):
		#l'effet pour que le personnage tourne sur lui-meme
		perso[2] = i % (HAUT + 1)
		#affiche la carte, le personnage et la fin
		draw(fenetre,carte,perso,fin)
		#affiche le message
		#la police de caractere
		font = pygame.font.Font(CHEMIN + 'Lighthouse_PersonalUse.ttf',50)
		#Le message a afficher
		message = font.render('You win!',True,
					pygame.Color(0,0,0))
		#affiche le message
		fenetre.blit(message,(150,300))
		#actualise l'ecran pour que l'utilisateur puisse voir
		#le rendu
		pygame.display.flip()
		#fait une pause pour laisser le temps a l'utilisateur
		#de voir le resultat
		pygame.time.wait(50)
		
#verifie si il y a quelque chose dans la case la plus proche
#de 'perso' en direction de 'perso[2]'
def have_something(carte,perso):
	if perso[2] == DROITE:
		return carte[perso[0]][perso[1] + 1] == 1
	elif perso[2] == GAUCHE:
		return carte[perso[0]][perso[1] - 1] == 1
	elif perso[2] == BAS:
		return carte[perso[0] + 1][perso[1]] == 1
	elif perso[2] == HAUT:
		return carte[perso[0] - 1][perso[1]] == 1
