from fenetre import *
from constantes import *

class Dessinateur:
	def __init__(self, fenetre):
		self.fenetre = fenetre

	def dessine_carte(self, carte):
		for l, ligne in enumerate(carte.carte):
			for c, case in enumerate(ligne):
				position = (c * LARGEUR, l * LARGEUR)

				if case == ID_MUR: portion = MUR.rect
				else: portion = SOL.rect

				self.fenetre.dessine(SOLS, position, portion)

		position_fin = (carte.fin.c * LARGEUR, carte.fin.l * LARGEUR)
		self.fenetre.dessine(SOLS, position_fin, FIN.rect)

		self.fenetre.affiche()

	def dessine_perso(self, carte):
		rectangle_perso = PERSO_RECT[carte.perso.dir].rect
		position_perso = carte.perso.position.c * LARGEUR, carte.perso.position.l * LARGEUR
		self.fenetre.dessine(PERSONNAGE, position_perso, rectangle_perso)
		self.fenetre.affiche()

	def dessine_curseur(self, curseur, id_tuile = ID_SOL):
		surface = pygame.Surface((LARGEUR, LARGEUR))
		position_curseur = curseur.c * LARGEUR, curseur.l * LARGEUR
		surface.fill(pygame.Color(125,50,0,0))
		surface.set_alpha(125)

		tuile = pygame.Surface((LARGEUR, LARGEUR))		
		tuile_rect = TUILES_AFFICHABLES[id_tuile].rect
		if id_tuile <= ID_FIN:
			image = SOLS
		else:
			image = PERSONNAGE
			tuile.blit(SOLS, (0, 0), SOL)
		tuile.blit(image, (0, 0), tuile_rect)
		tuile.blit(surface, (0, 0))
		
		self.fenetre.dessine(tuile, position_curseur)

		self.fenetre.affiche()
