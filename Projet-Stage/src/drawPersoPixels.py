import pygame
from pygame.locals import *

def main():
	pygame.init()
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((150,200))
	
	fenetre.fill(pygame.Color(0,0,0))
	
	pygame.display.flip()
	
	sprites = pygame.image.load('../data/spritesPerso.png')
	
	fenetre.blit(sprites,[0,0])
	
	pygame.display.flip()
	
	pygame.time.wait(1000)
	
	fenetre.fill(pygame.Color(0,0,0))
	
	pygame.display.flip()
	
	pygame.time.wait(500)
	
main()
