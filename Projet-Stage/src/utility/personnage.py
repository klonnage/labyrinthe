class BasiquePersonnage:
	def __init__(self,coordonnees):
		#liste des coordonnees du personnage su la carte
		self.coordonnees = coordonnees
	
	#deplacement de personnage
	def move_right(self):
		self.coordonnees[1] +=1
		
	def move_left(self):
		self.coordonnees[1] -=1
		
	def move_up(self):
		self.coordonnees[0] -=1
		
	def move_down(self):
		self.coordonnees[0] +=1
