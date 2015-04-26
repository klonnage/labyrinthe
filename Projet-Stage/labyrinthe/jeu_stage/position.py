class Position:
	def __init__(self, *position):
		if len(position) == 1:
			if type(position[0]) == type([]):
				self.c, self.l = tuple(position[0])
			else:
				self.c, self.l = position[0].c, position[0].l
		else: self.c, self.l = tuple(position)
		
	def __eq__(self, pos):
		return (self.c, self.l) == (pos.c, pos.l)
		
	def __add__(self, pos):
		return Position(self.c + pos.c, self.l + pos.l)
		
POSITIONS = [Position(0, -1),
			Position(0, 1),
			Position(-1, 0),
			Position(1, 0)]
	
if __name__ == '__main__':
	def print_pos(pos):
		print pos.l, pos.c
	pos = Position(1,1)
	droite = Position(pos)
	p = Position([1, 2])
	print_pos(pos)
	print_pos(droite)
	print_pos(p)
	print pos is droite
