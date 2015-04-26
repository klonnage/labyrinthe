from position import *
from constantes import *

class Personnage:
	def __init__(self, c, l, direction):
		self.position, self.dir = Position(c, l), direction
		
	def deplacer(self):
		self.position += POSITIONS[self.dir]
			
	def tourner(self, nouvelle_direction):
		self.dir = nouvelle_direction
