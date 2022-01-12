from random import *
from math import *

class Sommet :

	def __init__ ( self, x, y ) :
		self.abscisse = x
		self.ordonnee = y

	def getAbscisse ( self ) :
		return self.abscisse

	def getOrdonnee ( self ) :
		return self.ordonnee

	def affiche ( self ) :
		print ( "(", self.abscisse, ";", self.ordonnee, ")" )

	def distance ( self, autre ) :
		dx = self.abscisse - autre.getAbscisse()
		dy = self.ordonnee - autre.getOrdonnee()
		return sqrt ( dx*dx + dy*dy )

	def genere_voisin ( self, dist ) :
		r = random() * dist
		theta = random() * 2*pi

		x = self.abscisse + r*cos(theta)
		y = self.ordonnee + r*sin(theta)
		
		x = int(100*x)/100
		y = int(100*y)/100

		return Sommet ( x, y )