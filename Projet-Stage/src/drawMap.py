import pygame
from pygame.locals import *

#image
sols = pygame.image.load('../data/textures.png')
#rectangle correspondant a chaque rectangle dans la tileset
sol = pygame.Rect(0,0,50,50)
mur = pygame.Rect(50,0,50,50)
fin = pygame.Rect(100,0,50,50)

def draw(fenetre,carte,perso,fin):
	global sols
	#pour chaque ligne et chaque colone, on affiche la case 
	#correspondante
	for i,ligne in enumerate(carte):
		for j,colone in enumerate(ligne):
			if colone == 0:
				fenetre.blit(sols,(j*50,i*50),sol)
			elif colone == 1:
				fenetre.blit(sols,(j*50,i*50),mur)
			elif colone == 2:
				fenetre.blit(sols,(j*50,i*50),fin)
	pygame.display.flip()
				
if __name__ == '__main__':
	pygame.init()
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((10*50,15*50))
	
	carte = [[1,1,1,1,1,1,1,1,1,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,2,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,1,1,1,1,1,1,1,1,1]]
	draw(fenetre,carte)
	#pause d'une seconde
	pygame.time.wait(5000)
