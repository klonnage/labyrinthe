import json

def read(filename):
	with open(filename,"r") as fichier:
		dico = json.load(fichier)
		carte = dico['carte']
		perso = dico['perso']
		fin = dico['fin']
		for i in carte:
			print i
		print perso
		print fin
	
if __name__ == '__main__':
	read('carte')
