from gui.SceneGUI import *
from tkinter import *

class MainWindow :

	def __init__ ( self, s, g ) :
		self.fenetre = Tk()
		self.fenetre.title("Projet graphe")
		self.widget_scene = SceneGUI( s, g )	
		
	def loop ( self ) :
		self.widget_scene.affiche()
		self.widget_scene.pack()
		self.fenetre.mainloop()