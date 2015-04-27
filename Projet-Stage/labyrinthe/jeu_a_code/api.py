import pygame
from pygame.locals import *
from constantes import *

#creer la fenetre
def creer_fenetre(colone, ligne):
	return pygame.display.set_mode((colone, ligne))
	
#creer une police de caractere
def creer_police(nom_police, taille):
	return pygame.font.Font(nom_police, taille)
	
#renvoie la portion correspondant au personnage
#dans sa direction de deplacement
def obtenir_portion_perso(direction):
	return PERSO_RECT[direction]
	
#creer un message a afficher a l'ecran
def creer_message(message, police):
	return police.render(message, True, pygame.Color(0, 0, 0))
	
#dessine a l'ecran
def dessiner_ecran(fenetre, image, position, portion):
	fenetre.blit(image, position, portion)
	
#fait une pause
def pause(temps):
	pygame.time.wait(int(temps * 100))
	
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
