from core.Scene import *
from core.Graphe import *

w = 400
h = 300

s = Scene ( w, h )
g = Graphe ( s, 1000 )
g.trouve_PCC ( Sommet ( 0, 0 ), Sommet ( w, h ), 50, 0.2 )