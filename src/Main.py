from core.Scene import *
from core.Graphe import *

from gui.MainWindow import *

test = Tk()
test.mainloop()

w = 800
h = 600
nb_obstacles = 5

nb_sommets = 200
dist_depart = 100

# La scène
#s = Scene ( w, h, nb_obstacles )
#s.genere_obstacles()
#fenetre = MainWindow( s, 0 )
#fenetre.loop()

# Le graphe
#g = Graphe ( s, nb_sommets )
#g.genere_sommets()
#g.genere_matrice ( dist_depart )

#fenetre = MainWindow( s, g )
#fenetre.loop()

#g.trouve_PCC ( Sommet ( 0, 0 ), Sommet ( w, h ), 50, 0.2 )