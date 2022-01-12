from core.Obstacle import *
from tkinter import *

color = "#333333"

class ObstacleGUI :

	def __init__ ( self, obst ) :
		self.obstacle = obst
		
	def affiche ( self, sc ) :
		if ( self.obstacle.getType() == "rectangle" ) :
			self.affiche_rectangle ( sc )
			
		elif ( self.obstacle.getType() == "ovale" ) :
			self.affiche_ovale ( sc )
			
	def affiche_rectangle ( self, sc ) :
		x1 = self.obstacle.getX()
		y1 = self.obstacle.getY()
		x2 = x1 + self.obstacle.getLargeur()
		y2 = y1 + self.obstacle.getHauteur()
		sc.create_rectangle ( x1, y1, x2, y2, fill=color, outline=color )
		
	def affiche_ovale ( self, sc ) :
		x1 = self.obstacle.getX()
		y1 = self.obstacle.getY()
		x2 = x1 + self.obstacle.getLargeur()
		y2 = y1 + self.obstacle.getHauteur()
		sc.create_oval ( x1, y1, x2, y2, fill=color, outline=color )