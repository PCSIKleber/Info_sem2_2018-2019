import numpy as np
# Recuperation de la fonction d'energie potentielle
from Ep import Ep
# Recuperation des donnees (position et vitesse initiales ainsi que masse)
x0,v0,m = np.loadtxt('data.txt',unpack=True)

# A vous de determiner les positions extremes
xmin,xmax = 'not','this'

# Affichage
print(xmin,xmax)
