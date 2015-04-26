import pygame, pickle

class Map:
	""" Map permet de gerer la carte et le personange.
	Elle contient le fond de la carte et les informations
	du personnage."""
	background = list()
	position_perso = list()

	#initialise la carte
	def __init__(self,filename=""):
		""" Recupere la carte dans le fichier 
		'filename',ainsi que les coordonnees du 
		personnage a sa position d'origine
		et les charge en memoire."""
		with open(filename,'rb') as map_file:
			depickler = pickle.Unpickler(map_file)
			#recupere la carte et la stock 
			#dans background
			self.background = depickler.load()
			#recupere les coordonnees du personnage
			#et les stock dans position_perso
			self.position_perso = depickler.load()

	#deplace le personnage 
	def move_personnage(self,movement):
		""" deplace le personnage et retourne vrai si le
		deplacement est possible"""
		if self.background[self.position_perso[0]][self.position_perso[1]] == 1:
			return False
		self.background[self.position_perso[0]][self.position_perso[1]] = 0
		self.position_perso[0] += movement[0]
		self.position_perso[1] += movement[1]
		self.background[self.position_perso[0]][self.position_perso[1]] = 2
		return True
		
	#recupere la carte
	def get_map(self):
		return self.background
		
if __name__ == '__main__':
	carte = Map('../data/carte')
	liste_carte = carte.get_map()
	for ligne in liste_carte:
		print ligne
	print
	carte.move_personnage([1,1])
	for ligne in liste_carte:
		print ligne
