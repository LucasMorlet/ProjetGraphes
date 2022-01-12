from core.Sommet import *

# type = "rectangle"
# type = "ovale"

class Obstacle :
	
	def __init__ ( self, t, x, y, w, h ) :
		self.type = t
		self.posX = x
		self.posY = y
		self.largeur = w
		self.hauteur = h
		
	def getType ( self ) :
		return self.type

	def getX ( self ) :
		return self.posX
		
	def getY ( self ) :
		return self.posY
		
	def getLargeur ( self ) :
		return self.largeur
		
	def getHauteur ( self ) :
		return self.hauteur
		
	def collision ( self, sommet ) :
		if ( self.type == "rectangle" ) :
			return self.collision_rectangle ( sommet )
		elif ( self.type == "ovale" ) :
			return self.collision_ovale ( sommet )
			
		print ( "Obstacle de type inconnu" )
		return False
		
	def collision_rectangle ( self, sommet ) :
		if ( sommet.getAbscisse() < self.posX ) :
			return False
		elif ( sommet.getAbscisse() > self.posX + self.largeur ) :
			return False
		elif ( sommet.getOrdonnee() < self.posY ) :
			return False
		elif ( sommet.getOrdonnee() > self.posY + self.hauteur ) :
			return False
		else :
			return True
		
	def collision_ovale ( self, sommet ) :
		return self.collision_rectangle ( sommet )