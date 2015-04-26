import pygame
from pygame.locals import *
import sys,os

def dessine_image(fenetre,x,y,a_afficher):
	#dessine 'a_afficher' sur la fenetre 'fenetre' a la position
	#x, y.
	fenetre.blit(a_afficher,(x,y))
	
def dessine_rectangle(fenetre,x,y,longueur,hauteur,couleur):
	#dessine un rectangle de dimension 'longueur'x'hauteur' 
	pygame.draw.rect(fenetre,couleur,Rect(x,y,longueur,hauteur))
	
def actualise_fenetre():
	#actualise la fenetre
	pygame.display.update()
	
#Permet de tester les fonctions que l'on a code au dessus
if __name__ == "__main__":
	#initialise pygame
	pygame.init()
	pygame.display.init()
	
	#creer la fenetre
	fenetre = pygame.display.set_mode((640,480))
	
	#colorie la fentre en blanc
	fenetre.fill(pygame.Color(255,255,255))
	
	#affiche une petite image
	
	#dessine un rectangle rouge a (50,50)
	dessine_rectangle(fenetre,50,50,50,50,pygame.Color(255,0,0))
	
	#actualise la fenetre
	actualise_fenetre()
	
	#pause de 1s
	pygame.time.wait(1000)
	
	#quitte pygame
	pygame.display.quit()
	pygame.quit()
