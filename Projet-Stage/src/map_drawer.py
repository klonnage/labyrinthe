import carte, pygame
from pygame.locals import *

#Couleurs Utiles
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)

#dessine la carte a l'ecran
def draw(game_map):
	""" dessine la carte a l'ecran """
	#la carte
	data_map = game_map.get_map()
	
	#fixe la taille de la fentre par rapport a 
	#la taille de la carte
	window = pygame.display.set_mode((len(data_map[0])*50,len(data_map)*50))
	
	#remplit l'ecran en blanc
	window.fill(white)
	
	#un rectangle de dimension 50x50 pour aficher la valeur
	#de chaque case de la carte
	case = pygame.Rect(0,0,50,50)
	#parcourt chaque case du tableau
	for line in data_map:
		for colone in line:
			#affiche un carre noir si c'est un obstcacle
			if colone == 1:
				pygame.draw.rect(window,black,case)
			#sinon si c'est un espace vide affiche un carre blanc
			elif colone == 0:
				pygame.draw.rect(window,white,case)
			#sinon affiche un carre rouge
			else:
				pygame.draw.rect(window,red,case)
			case.move_ip(50,0)
		case.x = 0
		case.move_ip(0,50)
	
	#actualise la fenetre
	pygame.display.update()
		
if __name__ == "__main__":
	#initialise pygame
	pygame.init()
	pygame.display.init()
	
	#charge et affiche la carte
	level_map = carte.Map('../data/carte')
	draw(level_map)
	
	#fait une pause
	pygame.time.wait(1000)
