# Import pour lecture et utilisation de la mediane
import numpy as np
# Lecture des donnees
t,u = np.loadtxt('ouverture_appareil_photo.txt',unpack=True,skiprows=1)

# Pour que le dessin donne quelque chose
t_propre = [1,2,3]
u_propre = [1,3,1]


# Avant de pouvoir appliquer le meme principe que pour le flash, il faut 
# proprifier votre signal (stocker les valeurs correspondantes dans les listes 
# t_propre et u_propre).




# Le code suivant vous permet de visualiser si votre procede de nettoyage 
# marche correctement. Vous aurez dans le dossier un fichier image 
# ouverture_propre.png qui devrait se creer.

import matplotlib.pyplot as plt

plt.plot(t_propre,u_propre)
plt.savefig('ouverture_propre.png')

# Ne reste plus qu'a proceder comme pour le flash pour obtenir le temps total 
# d'ouverture

temps_ouverture = 'pas ca...'

# Affichage du resultat
print(temps_ouverture)
