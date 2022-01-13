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
        if ( len(liste) == 0 ) :
            print ( "Pas d'obstacle dans la liste" )
        elif ( type(liste[0]) != type(Obstacle(0,0)) ) :
            print ( "L'obstacle n'est pas du bon type :", type(liste[0]) )
        else :
            for i in range ( len ( liste ) ) :
                o = ObstacleGUI ( liste[i] )
                o.affiche ( self )
                
    