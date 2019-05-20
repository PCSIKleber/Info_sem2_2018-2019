# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent 
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des 
# tests automatiquement et sans effort: il suffira de decommenter la ligne #if 
# #if __name__ == '__main__': testeur.fais_tests('...') 
# presente apres chaque definition de fonction.
#
# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est 
# ***absolument primordial*** de lancer l'execution dans le menu via 
# "Executer  en tant que script" ou "Run file as script"
# c'est-a-dire avec le raccourci Ctrl-Shift-E (et NON simplement Ctrl-E) sinon 
# les mises a jour de votre fichier ne seront pas prises en compte.
# (NB: Si vous etes sous Mac, c'est Pomme-Shift-E qu'il faut utiliser)
# ***************************************************************************


# On importe la batterie de tests uniquement a l'execution du fichier et non 
# lors de l'import en tant que module:
if __name__ == '__main__': import test_TP_eclipse as testeur

# ***************************************************************************
# Premiere partie: K-means algorithm
# ***************************************************************************
        
def distribue_selon_centroides(donnees,centroides):
    """ 
    Associe a chaque point de donnees le centroide le plus proche.
    
    Parametres:
    * 'donnees' est un np.array de dimensions (m,p) contenant m points definis 
    par p coordonnees.
    * 'centroides' est un np.array de dimensions (k,p) contenant les k 
    centroides auxquels associer chaque point des donnees
    
    La fonction doit renvoyer un np.array de dimension m contenant le numero 
    du centroide le plus proche en norme euclidienne.    
    """
    return []             

# Ligne suivante a decommenter pour tester 
if __name__ == '__main__': testeur.fais_tests('01_distribution')

def recalcule_centroides(donnees,classes,centroides):
    """ 
    Recalcule la positions des centroides comme barycentre des points qui 
    appartiennent a leur groupe d'influence. Si un centroides n'a aucun point 
    associe, il reste par defaut en place.
    
    Parametres:
    * 'donnees' est un np.array de dimensions (m,p) contenant m points definis 
    par p coordonnees.
    * 'classes' est un np.array de dimension m contenant le numero du 
    centroide le plus proche en norme euclidienne.
    * 'centroides' est un np.array de dimensions (k,p) contenant les k 
    centroides auxquels sont associes chaque point des donnees.
    
    La fonction doit renvoyer un np.array de dimensions (k,p) contenant les k 
    nouveaux centroides.
    """
    return []

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_calcul_centroides')

def algo_kmeans(donnees,depart_centroides):
    """ 
    Algorithme k-means complet.
    
    Parametres:
    * 'donnees' est un np.array de dimensions (m,p) contenant m points definis 
    par p coordonnees.
    * 'depart_centroides' est un np.array de dimensions (k,p) contenant les k 
    points de departs pour les centroides de l'algorithme.
    
    L'algorithme doit renvoyer un couple constitue d'un np.array de dimensions 
    (k,p) contenant les centroides finalement trouves ainsi qu'un np.array de 
    dimension m associant a chaque point le numero de son centroide et 
    permettant donc de partitionner des donnees en differents groupes.
    """
    return [],[]

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_algo_kmeans')

def enveloppe(chemin_image):
    """ 
    Fonction determinant l'enveloppe de l'image du Soleil sur l'image dont 
    on donne le chemin (par exemple 'telescope/Eclipse1.jpg'). Pour que tout 
    le monde trouve les memes coordonnees, on pourra parcourir l'image ligne 
    par ligne et determiner l'enveloppe comme le point juste exterieur au 
    Soleil avant (ou apres selon le cote) que l'on ait franchi l'interface. 
    Par exemple, avec une image qui se represente sous la forme

    000000                             000000
    001100                             0x11x0
    011110  les points a prendre sont  x1111x
    011110  representes par des 'x':   x1111x
    001100                             0x11x0
    000000                             000000
    
    Renvoie une liste de doublets (x,y) des coordonnees des points dans 
    l'image ou x represente le numero de ligne et y le numero de la colonne.
    """
    return [(1,1),(2,1)]

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('04_enveloppe')

# ***************************************************************************
# Deuxieme partie: Regression lineaire
# ***************************************************************************

def ajustement(X,Y):
    """ 
    Fonction d'ajustement generique pour une regression "lineaire".

    Parametres:
    * X est une np.matrix de dimensions (m,p) ou m est le nombre de points de 
    donnees disponibles et p est le nombre de parametres d'ajustement choisis. 
    Par exemple, pour l'ajustement d'une parabole y=ax**2+bx+c, X devra 
    contenir une colonne de x**2, une colonne de x et une colonne de 1, soit 3 
    colonnes en tout.
    * Y est une np.matrix de dimensions (m,1) qui contient le resultat attendu 
    pour chaque point. Dans le meilleur des mondes, si Theta est le vecteur 
    colonne contenant les p parametres recherches, alors on devrait avoir sous 
    forme matricielle Y = X*Theta
    
    La fonction doit renvoyer la np.matrix Theta de dimension (p,1) contenant 
    les parametres optimaux d'ajustement. 
    """
    return np.matrix(0)

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_ajustement')


def regression_circulaire(couples):
    """ 
    Fonction permettant d'ajuster l'equation d'un cercle a un ensemble de 
    points. On donne en entree une liste 'couples' contenant les coordonnees 
    (x,y) des points pour lesquels il faut trouver le cercle optimal d'equation
    
    (x-a)**2 + (y-b)**2 = R**2
    
    La fonction doit renvoyer un triplet avec les valeurs a, b et R trouvees
    """
    return a,b,R

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('06_cercles')

# Les lignes suivantes permettent d'effectuer (recentrage = True) ou non 
# (recentrage=False) le recentrage des images du repertoire telescope/
recentrage = False
if recentrage and __name__ == '__main__':
     # Mettre ici le code necessaire pour effectuer les operations de 
     # recentrage. N'oubliez pas de mettre la bascule 'recentrage' a True pour 
     # voir les resultats et de la remettre a False une fois que vous voudrez 
     # passer a la suite et que tous les calculs ne se fassent pas a chaque 
     # fois.
     pass


def regression_elliptique(couples):
    """ 
    Fonction permettant d'ajuster l'equation d'une ellipse a un ensemble de 
    points. On donne en entree une liste 'couples' contenant les coordonnees 
    (x,y) des points pour lesquels il faut trouver l'ellipse optimale 
    d'equation
    
    x**2 + A*x*y + B*y**2 + C*x + D*y + E = 0
    
    La fonction doit renvoyer un quintuplet des valeurs A a E trouvees.
    """
    return A,B,C,D,E

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('07_ellipses')

# Les lignes suivantes permettent d'effectuer (recircularisation = True) ou 
# non (recircularisation=False) le recentrage des images du repertoire 
# telescope/
recircularisation = False
if recircularisation and __name__ == '__main__':
     # Mettre ici le code necessaire pour effectuer les operations de 
     # recentrage. N'oubliez pas de mettre la bascule 'recircularisation' a 
     # True pour voir les resultats 
     pass


# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
