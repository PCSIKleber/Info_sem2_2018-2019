# Import de Numpy qui sert a lire le fichier
import numpy as np
# Lecture du fichier
t,u = np.loadtxt('inertie_p_PP.txt',unpack=True,skiprows=1)

# A vous de jouer en mettant dans la variable omega300 la valeur de la vitesse 
# angulaire lors du 300e passage par un trou et dans theta10 la valeur de 
# l'angle au plus proche de t=10s

omega300 = 'Pas cela, malheureusement...' # A changer...
theta10  = 'Ni cela'


# A la fin, on affiche les resultats a l'ecran
print(omega300,theta10)
