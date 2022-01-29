from core.Graphe import *
from gui.SommetGUI import *
from gui.AreteGUI import *

class GrapheGUI :

    def __init__ ( self, g ) :
        self.graphe = g

    def affiche ( self, sc ) :
        if ( self.graphe == 0 ) :
            print ( "Pas de graphe attribué" )
        else :
            self.affiche_aretes(sc)
            self.affiche_sommets(sc)
            self.affiche_PCC(sc)
        
    def affiche_sommets ( self, sc ) :
        liste = self.graphe.getSommets()
        if ( len(liste) == 0 ) :
            print ( "Pas de sommets dans le graphe" )
        elif ( type(liste[0]) != type(Sommet(0,0)) ) :
            print ( "Le sommet n'est pas du bon type :", type(liste[0]) )
        else :
            for i in range ( len ( liste ) ) :
                s = SommetGUI ( liste[i] )
                s.affiche ( sc )
            
    def affiche_aretes ( self, sc ) :
        liste = self.graphe.getAretes()
        if ( len(liste) == 0 ) :
            print ( "Pas d'arêtes dans le graphe" )
        elif ( type(liste[0]) != type(Arete(Sommet(0,0),Sommet(0,0))) ) :
            print ( "L'arête n'est pas du bon type :", type(liste[0]) )
        elif ( type(liste[0].sommetA) != type(Sommet(0,0)) ) :
            print ( "L'arête ne contient pas un sommet :", type(liste[0].sommetA) )
        else :
            for i in range ( len ( liste ) ) :
                s = AreteGUI ( liste[i] )
                s.affiche ( sc )
                
    def affiche_PCC ( self, sc ) :
        liste = self.graphe.get_PCC()
        for i in range ( len(liste)-1 ) :
            arete = AreteGUI ( Arete ( liste[i], liste[i+1] ) )
            arete.affiche_PCC ( sc )
            
        for i in range ( len(liste) ) :
            sommet = SommetGUI ( liste[i] )
            sommet.affiche ( sc )