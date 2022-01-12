from core.Sommet import *
from core.Obstacle import *
from random import random

class Scene :

	def __init__ ( self, l, h, n ) :
		self.largeur = l
		self.hauteur = h
		self.nb_obstacles = n
		self.liste_obstacles = [0] * self.nb_obstacles
		self.genere_obstacles()

	def getLargeur ( self ) :
		return self.largeur

	def getHauteur ( self ) :
		return self.hauteur
		
	def getObstacles ( self ) :
		return self.liste_obstacles
		
	def genere_obstacles ( self ) :
		for i in range ( self.nb_obstacles ) :
			x = int ( random() * self.largeur )
			y = int ( random() * self.hauteur )
			l = int ( random() * ( self.largeur - x ) )
			h = int ( random() * ( self.hauteur - y ) )
			if ( random() < 0.5 ) :
				type = "rectangle"
			else :
				type = "ovale"
				
			self.liste_obstacles[i] = Obstacle ( type, x, y, l, h )

	def genere_sommet ( self ) :
		x = int ( random() * self.largeur * 100 ) / 100
		y = int ( random() * self.hauteur * 100 ) / 100
		s = Sommet ( x, y )
		while ( not self.est_un_sommet_valable( s ) ) :
			x = int ( random() * self.largeur * 100 ) / 100
			y = int ( random() * self.hauteur * 100 ) / 100
			s = Sommet ( x, y )
		return s 

	def est_un_sommet_valable ( self, s ) :
		if ( s.getAbscisse() < 0 or s.getAbscisse() > self.largeur ) :
			return False
		if ( s.getOrdonnee() < 0 or s.getOrdonnee() > self.hauteur ) :
			return False   

		for i in range ( self.nb_obstacles ) :
			if ( self.liste_obstacles[i].collision ( s ) ) :
				return False
			
		return True