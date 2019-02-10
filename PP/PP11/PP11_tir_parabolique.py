import numpy as np

# Recuperation des donnees
data = np.loadtxt('donnees.txt')
# v0: vitesse initiale de lancement
# h: altitude initiale
# d: portee recherchee
v0,h,d = [float(x) for x in data]

# ATTENTION: bien ecrire 9.81 et pas 9,81 qui renvoie un message d'erreur sybillin !
g = 9.81 

# Equation de la trajectoire
def trajectoire(x,alpha):
    '''Renvoie l'altitude, en fonction de la position horizontale x et de 
    l'angle alpha de lancement (exprime en radians)''' 
    return h + np.tan(alpha)*x - g*(x/(v0*np.cos(alpha)))**2 / 2

# A vous de trouver un moyen d'atteindre les angles de tir correspondants
alpha1,alpha2 = "Pas","ca"


# Affichage
print(alpha1,alpha2)
