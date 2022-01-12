from tkinter import *
from core.Scene import *
from gui.GrapheGUI import *
from gui.ObstacleGUI import *

class SceneGUI (Canvas) :

	def __init__ ( self, s, g ) :
		super().__init__()
		
		self.scene = s
		self.graphe = GrapheGUI ( g )
		
		self.config(width=self.scene.getLargeur(), height=self.scene.getHauteur())
		
	def affiche ( self ) :
		self.affiche_obstacles()
		self.graphe.affiche ( self )
		
	def affiche_obstacles ( self ) :
		liste = self.scene.getObstacles()
		for i in range ( len ( liste ) ) :
			o = ObstacleGUI ( liste[i] )
			o.affiche ( self )