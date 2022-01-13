from core.Sommet import *
from random import *

# type = "rectangle"
# type = "ovale"

class Obstacle :
    
    def __init__ ( self, w, h ) :
        self.posX = int ( random() * w )
        self.posY = int ( random() * h )
        self.largeur = 1 + int ( random() * ( w - self.posX ) )
        self.hauteur = 1 + int ( random() * ( h - self.posY ) )
        if ( random() < 0.5 ) :
            self.type = "rectangle"
        else :
            self.type = "ovale"
            
        
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
        x = sommet.getAbscisse()
        y = sommet.getOrdonnee()
        x -= self.posX
        y -= self.posY
        x /= self.largeur
        y /= self.hauteur
        return ( ( 0 < x < 1 ) and ( 0 < y < 1 ) )
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