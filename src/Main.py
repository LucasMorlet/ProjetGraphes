from core.Scene import *
from core.Graphe import *

from gui.MainWindow import *

#test = Tk()
#test.mainloop()

w = 800
h = 600
nb_obstacles = 5

nb_sommets = 200
dist_depart = 100

# La scène
s = Scene ( w, h, nb_obstacles )
s.genere_obstacles()

# Le graphe
g = Graphe ( s, nb_sommets )
g.genere_sommets()
g.genere_matrice ( dist_depart )
g.trouve_PCC ( Sommet(0,0), Sommet(w,h), dist_depart, 0.2 )

fenetre = MainWindow( s, g )
fenetre.loop()
