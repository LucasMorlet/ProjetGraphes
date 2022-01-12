from core.Sommet import *

class Arete :

	def __init__ ( self, a, b ) :
		self.sommetA = a
		self.sommetB = b
		
	def getAX ( self ) :
		return self.sommetA.getAbscisse()
		
	def getAY ( self ) :
		return self.sommetA.getOrdonnee()
		
	def getBX ( self ) :
		return self.sommetB.getAbscisse()
		
	def getBY ( self ) :
		return self.sommetB.getOrdonnee()