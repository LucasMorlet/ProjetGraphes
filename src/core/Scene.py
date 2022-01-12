from core.Sommet import *

class Scene :

	def __init__ ( self, l, h ) :
		self.largeur = l
		self.hauteur = h

	def getLargeur ( self ) :
		return self.largeur

	def getHauteur ( self ) :
		return self.hauteur

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
		return True