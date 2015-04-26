#propriete utile pour faire des cartes de manière basique

#pour extraire la carte du  fichier
import pickle

class CarteBasique:
	def __init__(self,filename):
		#initialise la carte a partir d'un fichier
		self.carte = list()
		with open(filename,'rb') as fichier:
			depickler = pickle.Unpickler(fichier)
			self.carte = depickler.load()
			
	def extract_sublist(self,x_min,x_max,y_min,y_max):
		#extrait une sous-liste de 'liste' de dimension
		#(x_max-x_min+1)x(y_max-y_min+1)
		sub = []
		for elem in self.carte[y_min:y_max+1]:
			sub.append(elem[x_min:x_max+1])
		return sub

if __name__ == '__main__':
	carte = CarteBasique('../../data/carte')
	for i in carte.carte:
		print(i)
	print()
	sub_list = carte.extract_sublist(1,3,1,3)
	for i in sub_list:
		print(i)
