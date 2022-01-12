from core.Graphe import *
from gui.SommetGUI import *
from gui.AreteGUI import *

class GrapheGUI :

	def __init__ ( self, g ) :
		self.graphe = g

	def affiche ( self, sc ) :
		self.affiche_aretes(sc)
		self.affiche_sommets(sc)
		
	def affiche_sommets ( self, sc ) :
		liste = self.graphe.getSommets()
		for i in range ( len ( liste ) ) :
			s = SommetGUI ( liste[i] )
			s.affiche ( sc )
			
	def affiche_aretes ( self, sc ) :
		liste = self.graphe.getAretes()
		for i in range ( len ( liste ) ) :
			s = AreteGUI ( liste[i] )
			s.affiche ( sc )