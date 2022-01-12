from core.Sommet import *
from tkinter import *

rayon_sommet = 1
color = "#FF0000"

class SommetGUI :

	def __init__ ( self, s ) :
		self.sommet = s
		
	def affiche ( self, sc ) :
		x1 = self.sommet.getAbscisse() - rayon_sommet
		y1 = self.sommet.getOrdonnee() - rayon_sommet
		x2 = self.sommet.getAbscisse() + rayon_sommet
		y2 = self.sommet.getOrdonnee() + rayon_sommet
		
		sc.create_oval ( x1, y1, x2, y2, fill=color, outline=color )