import pygame
from pygame.locals import *
from constantes import *

#touches
TOUCHE_HAUT = K_UP
TOUCHE_BAS = K_DOWN
TOUCHE_GAUCHE = K_LEFT
TOUCHE_DROITE = K_RIGHT
TOUCHE_ECHAP = K_ESCAPE

#liste des objets a afficher
a_afficher = []

#creer la fenetre
def creer_fenetre(colone, ligne):
	return pygame.display.set_mode((colone, ligne))
	
#renvoie la taille de la fenetre
def obtenir_taille(fenetre):
	return fenetre.get_size()
	
#creer une police de caractere
def creer_police(nom_police, taille):
	return pygame.font.Font(nom_police, taille)
	
#renvoie la portion correspondant au personnage
#dans sa direction de deplacement, a l'etape de son mouvement
def obtenir_portion(perso, etape = 1):
	return PERSO_RECT[perso[2]][etape]

#renvoie le temps ecoulee depuis la creation de la fenetre
def obtenir_temps():
	return int(pygame.time.get_ticks() / 1000)

#synchronise les actions (ex: touche enfoncee) avec l'ordinateur
def synchroniser_actions():
	pygame.event.pump()

#renvoie le tableau de toute les touches enfoncees
def obtenir_touche():
	return pygame.key.get_pressed()
	
#verifie si une touche est enfoncee
def touche_enfoncee(clavier, touche):
	return clavier[touche]
	
#creer un message a afficher a l'ecran
def creer_message(message, police, couleur=pygame.Color(0,0,0)):
	return police.render(message, True, couleur)

#creer une couleur
def creer_couleur(rouge, vert, bleu, transparence = 0):
	return pygame.Color(rouge, vert, bleur, transparence)

#ecrit un message a l'ecran
def ecrire_mesage(message, police, position, couleur):
	msg = creer_message(message, police, couleur)
	ajouter_dessin(msg, position)
	
#ecrit un message au centre de l'ecran
def ecrire_centre(message, police, couleur, taille_fenetre):
	#cree le message
	msg = creer_message(message, police, couleur)
	#calcul sa taille
	taille_message = obtenir_taille(msg)
	#calcul la position du centre
	position = ((taille_fenetre[0] - taille_message[0])/2, (taille_fenetre[1] - taille_message[1])/2)
	#ajoute l'image correspondant au texte
	ajouter_dessin(msg, position)

#ajoute quelque chose a afficher dans la liste a afficher
#PS : le 'portion = None' signifie que si l'on veut on n'est
#pas obliger de mettre quelque chose pour 'portion'
def ajouter_dessin(image, position, portion = None):
	a_afficher.append([image, position, portion])
	
#dessine a l'ecran
def dessiner_ecran(fenetre, image, position, portion):
	fenetre.blit(image, position, portion)

#creer une surface
def creer_surface(colone, ligne):
	return pygame.Surface((colone, ligne))
	
#dessine sur la surface
def dessiner_surface(surface, image, position, portion = None):
	return surface.blit(image, position, portion)

#dessine tout ce que l'on a mis dans la liste des choses a afficher
def tout_dessiner(fenetre):
	for information_image in a_afficher:
		fenetre.blit(information_image[0], information_image[1], information_image[2])
		a_afficher.remove(information_image)

#fait une pause
def pause(temps):
	pygame.time.wait(int(temps * 1000))
	
#affiche la fenetre
def afficher_ecran():
	pygame.display.flip()
	
#initialise pygame
def initialiser():
	#initialise le module pygame
	pygame.init()
	pygame.display.init()
	pygame.font.init()
	#fixe le delay entre chaque appuie sur une touche
	pygame.key.set_repeat(100,10)
	
#quitte pygame
def quitter():
	#quitte pygame
	pygame.font.quit()
	pygame.display.quit()
	pygame.quit()
