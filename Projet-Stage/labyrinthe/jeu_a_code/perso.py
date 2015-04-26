from position import *
from constantes import *

class Personnage:
	def __init__(self, c, l, direction):
		self.position = Position(c, l)
		self.dir = direction
		
	def deplacer(self):
		pass
			
	def tourner(self, nouvelle_direction):
		pass
