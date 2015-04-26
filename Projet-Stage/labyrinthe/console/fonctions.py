from constantes import *

def print_map(carte):
	for i in carte:
		print(i)

def print_jeu(carte,perso):
	carte_jeu = []
	for ligne in carte:
		carte_jeu.append(list(ligne))
	carte_jeu[perso[0]][perso[1]] = 2
	print_map(carte_jeu)
	
def move(carte,perso,direction):
	if direction == DROITE and carte[perso[0]][perso[1] + 1] == 0:
		perso[1] += 1
	elif direction == GAUCHE and carte[perso[0]][perso[1] - 1] == 0:
		perso[1] -= 1
	elif direction == BAS and carte[perso[0] + 1][perso[1]] == 0:
		perso[0] += 1
	elif direction == HAUT and carte[perso[0] - 1][perso[1]] == 0:
		perso[0] -= 1
		
if __name__ == '__main__':
	carte = [[0,0,1],[1,0,1],[1,0,0]]
	perso = [0,0,1]
	print_jeu(carte,perso)
	print()
	move(carte,perso,DROITE)
	print_jeu(carte,perso)
	print('droite')
	move(carte,perso,BAS)
	print_jeu(carte,perso)
	print('bas')
	move(carte,perso,GAUCHE)
	print_jeu(carte,perso)
	print('gauche')
