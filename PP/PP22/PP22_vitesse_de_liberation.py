import numpy as np
# Lecture des donnees
M,R = np.loadtxt('donnees.txt',unpack=True)

# Constante de gravitation universelle
G = 6.67e-11

# Acceleration de la pesanteur a la surface
g0 = G*M/R**2

# Temps jusqu'a l'apogee pour une pesanteur uniforme
def t_apogee(v0):
    return v0/g0
