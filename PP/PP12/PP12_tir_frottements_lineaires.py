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

# Portee du tir
def portee(alpha):
    """
    Renvoie la portee atteinte (distance x necessaire pour que l'altitude
    s'annulle) connaissant l'angle alpha de lancement (exprime en radians)
    """
    # Initialisations diverses
    dt = 1e-3
    t = 0
    z = h
    x = 0
    vz= v0*np.sin(alpha)
    vx= v0*np.cos(alpha)
    # Boucle tant qu'on est au-dessus du sol
    while z > 0:
        dvx = - gamma*vx*dt       # Variation des vitesses
        dvz = (-g - gamma*vz)*dt
        dx  = vx*dt               # Variation des positions
        dz  = vz*dt
        # Incrementation des valeurs
        x = x+dx
        z = z+dz
        vx=vx+dvx
        vz=vz+dvz
    return x


alpha1,alpha2 = "Pas","ca"


# Affichage
print(alpha1,alpha2)
