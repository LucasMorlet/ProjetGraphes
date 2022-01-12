from core.Sommet import *
from core.Arete import *
from core.Scene import *
from random import random

INF = 10**15

class Graphe :

	def __init__ ( self, s, nb ) :
		self.scene = s
		self.nb_sommets = nb
		self.liste_sommets = [0]*self.nb_sommets
		self.matrice = [0]*self.nb_sommets
		for i in range ( self.nb_sommets ) :
			self.matrice[i] = [0]*self.nb_sommets
			
		self.dist_debut = [INF] * self.nb_sommets   
		self.prec_debut = [-1] * self.nb_sommets   
		self.dist_fin   = [INF] * self.nb_sommets   
		self.prec_fin   = [-1] * self.nb_sommets  

	def getSommets ( self ) :
		return self.liste_sommets
		
	def getAretes ( self ) :
		liste = []
		for i in range ( self.nb_sommets ) :
			for j in range ( i+1, self.nb_sommets ) :
				if ( self.matrice[i][j] < INF ) :
					liste.append ( Arete ( self.liste_sommets[i], self.liste_sommets[j] ) )
		return liste
			
	def genere_sommets ( self ) :
		for i in range ( self.nb_sommets ) :
			self.liste_sommets[i] = self.scene.genere_sommet()
			
	def complete_sommets ( self, dist ) :
		sommets_valides = len ( self.liste_sommets )
		while ( len ( self.liste_sommets ) < self.nb_sommets ) :
			indice = int ( sommets_valides * random() )
			s = self.liste_sommets[indice].genere_voisin( dist )
			
			while ( not self.scene.est_un_sommet_valable ( s ) ) :
				indice = int ( sommets_valides * random() )
				s = self.liste_sommets[indice].genere_voisin( dist )
				
			self.liste_sommets.append ( s )
			
			
	def affiche_liste ( self ) :
		for i in range ( self.nb_sommets ) :
			self.liste_sommets[i].affiche()
			
	def setDebut ( self, d ) :
		self.liste_sommets[0] = d
		
	def setFin ( self, f ) :
		self.liste_sommets[1] = f
			
	def genere_matrice ( self, dist_max ) :
		for i in range ( self.nb_sommets ) :
			self.matrice[i][i] = 0
			for j in range ( i+1, self.nb_sommets ) :
				d = self.liste_sommets[i].distance ( self.liste_sommets[j] )
				if ( d > dist_max ) :
					d = INF
				self.matrice[i][j] = d
				self.matrice[j][i] = d
				
	def affiche_matrice ( self ) :
		for i in range ( self.nb_sommets ) :
			for j in range ( self.nb_sommets ) :
				if ( self.matrice[i][j] == INF ) :
					print ( "INF", end = " " )
				else :
					print ( int ( self.matrice[i][j] * 100 ) / 100, end = " " )
			print()
			
	def dijkstra ( self, indice_premier_sommet ) :
		distances = [ INF ] * self.nb_sommets
		precedents = [ -1 ] * self.nb_sommets
		dejaTraite = [ False ] * self.nb_sommets
		
		distances[indice_premier_sommet] = 0
		precedents[indice_premier_sommet] = indice_premier_sommet
		
		sommet_courant = indice_premier_sommet
		while ( sommet_courant >= 0 ) :
			# On trouve le sommet non-traité le plus près
			mini = INF
			sommet_courant = -1
			for i in range ( self.nb_sommets ) :
				if ( not dejaTraite[i] and distances[i] < mini ) :
					sommet_courant = i
					mini = distances[i]
			 
			# Si on a pas trouvé de sommet, on termine l'algo
			if ( sommet_courant < 0 ) :
				break
			
			dejaTraite[sommet_courant] = True
			# On met à jour toutes les distances nécessaires
			for i in range ( self.nb_sommets ) :
				if ( not dejaTraite[i] ) :
					dist = distances[sommet_courant] + self.matrice[sommet_courant][i]
					if ( dist < distances[i] ) :
						distances[i] = dist
						precedents[i] = sommet_courant
		
		if ( indice_premier_sommet == 0 ) :
			self.dist_debut = distances
			self.prec_debut = precedents
		elif ( indice_premier_sommet == 1 ) :
			self.dist_fin = distances
			self.prec_fin = precedents
			
		return ( distances, precedents )
		
	def raffine ( self, dist, ecart ) :
		dist_max = self.dist_debut[1] * ( 1 + ecart )
		nouvelle_liste = []
		for i in range ( self.nb_sommets ) :
			dist_somm = self.dist_debut[i] + self.dist_fin[i]
			if ( dist_somm < dist_max ) :
				nouvelle_liste.append ( self.liste_sommets[i] )
		self.liste_sommets = nouvelle_liste
		
	def regenere ( self ) :
		del self.liste_sommets[int(self.nb_sommets/2):]
		
	def trouve_PCC ( self, debut, fin, dist, ecart ) :
		self.genere_sommets()
		self.setDebut ( debut )
		self.setFin ( fin )
		self.genere_matrice( dist )
		self.dijkstra ( 0 ) 
		self.dijkstra ( 1 ) 
		
		echec = 0
		while ( echec < 5 ) :
			self.itere ( dist, ecart )
			
			if ( self.dist_debut[1] < INF ) :
				dist *= 0.9
				ecart *= 0.9
				echec = 0
			else :
				echec += 1
			
				
			self.affiche_PCC()
			
	def itere ( self, dist, ecart ) :	   
		# Si on a trouvé le PCC, on conserve chaque sommet qui n'en est pas trop écarté
		if ( self.dist_debut[1] < INF ) :
			self.raffine ( dist, ecart )
		   
		# Sinon on supprime la moitié des sommets (à vérifier)
		else :
			self.regenere ( )
			
		# Dans tous les cas on complète nos sommets
		self.complete_sommets ( dist )
		self.genere_matrice( dist )
			
		# On met à jour nos Dijkstra
		self.dijkstra ( 0 ) 
		self.dijkstra ( 1 ) 
		
	def affiche_PCC ( self ) :
		if ( self.dist_debut[1] >= INF ) :
			print ( "Pas de plus court chemin !" )
			
		else :
			print ( "Plus court chemin" )
		
			i = 1
			liste = [1]
			while ( i > 0 ) :
				i = self.prec_debut[i]
				liste.append ( i )
				
			while ( len ( liste ) > 0 ) :
				self.liste_sommets[liste.pop()].affiche()
		
		