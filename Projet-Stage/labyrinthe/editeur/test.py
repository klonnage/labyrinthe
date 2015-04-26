from constantes import *
from api import *
#from carte import *
from enregistreur import *
from editeur import *
import sys

class Exemple:
	def __init__(self, value = 1):
		self._x = value

	def getX(self):
		return self._x

	@property
	def x(self):
		return self._x

	@x.setter
	def _x(self, value):
		self._x = value - 1

if __name__ == '__main__':
	g = Exemple()
	g._x = 3 
	print g.x
