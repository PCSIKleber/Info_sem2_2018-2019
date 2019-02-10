import numpy as np

# Recuperation des donnees
data = np.loadtxt('donnees.txt')
# v0: vitesse initiale de lancement
# h: altitude initiale
# d: portee recherchee
# gamma: constante intervenant dans les frottements
v0,h,d,gamma = [float(x) for x in data]

# ATTENTION: bien ecrire 9.81 et pas 9,81 qui renvoie un message d'erreur sybillin !
g = 9.81 

# A present, vous etes assez grands pour vous debrouiller tout seul.

alpha1,alpha2 = "Pas","ca"


# Affichage
print(alpha1,alpha2)
