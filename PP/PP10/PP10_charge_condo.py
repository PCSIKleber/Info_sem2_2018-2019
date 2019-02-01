# Import de Numpy qui sert a lire le fichier
import numpy as np
# Lecture du fichier
MESURES = np.loadtxt('mesures_i.txt',unpack=True)

# A vous de jouer en mettant dans la variable 'charge' la charge accumulee sur 
# le condensateur, sachant que MESURES contient l'intensite du courant 
# traversant le condensateur echantillonne toutes les millisecondes.

charge = 'Pas cela, malheureusement...' # A changer...



# A la fin, on affiche le resultat a l'ecran
print(charge)
