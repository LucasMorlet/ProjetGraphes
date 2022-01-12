from core.Arete import *
from tkinter import *

color = "#008800"

class AreteGUI :

	def __init__ ( self, a ) :
		self.arete = a
		
	def affiche ( self, sc ) :
		ax = self.arete.getAX()
		ay = self.arete.getAY()
		bx = self.arete.getBX()
		by = self.arete.getBY()
		
		sc.create_line ( ax, ay, bx, by, fill=color )