import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pygame.display.init()
	
	fenetre = pygame.display.set_mode((640,480))
	
	fenetre.fill(pygame.Color(255,255,255))
	
	while True:
		pygame.display.flip()
	
		event = pygame.event.wait()
		
		if event.type == QUIT:
			pygame.display.quit()
			pygame.quit()
			sys.exit(0)
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.display.quit()
				pygame.quit()
				sys.exit(0)
			
main()
