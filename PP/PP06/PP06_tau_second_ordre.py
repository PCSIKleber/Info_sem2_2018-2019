# Pour la lecture
import numpy as np
# Lecture des donnees
donnees_t,donnees_u = np.loadtxt('Uc_41.txt',unpack=True)

# A l'aide du PythonPhysique sur la detection des maximas, trouvez-les puis 
# appliquez le logarithme sur les valeurs de tension avant de faire un ajustement
def temps_et_maxima(t,u):
    liste_t,liste_u = [],[]
    return liste_t,liste_u

# Des valeurs bidons pour illustrer la suite (ne pas oublier de convertir en 
# np.array pour la suite)
max_u = np.array([10,5,3,1.5,1])
max_t = np.array([ 1,2,3,4  ,5])

# Application du log 
lnU = np.log(max_u)
    
# Import de ce qu'il faut pour l'ajustement et la visualisation
import matplotlib.pyplot as plt
import scipy as sp
import scipy.optimize

# Visualisation des points de mesure
plt.plot(max_t,lnU,'o')
plt.grid()
plt.savefig('visualisation.png')

# A vous de definir la bonne fonction
def f(t,A,tau):
    return t*A - tau  # expression a changer...

# Ajustez l'option 'p0=...' pour donner des valeurs plausibles pour A et tau
p,pcov = sp.optimize.curve_fit(f,max_t,lnU,p0=[1,1])

# Recuperation des valeurs ajustees
A,tau = p    

# Verification graphique
fit = f(max_t,A,tau)
plt.plot(max_t,fit)
plt.savefig('verification.png')
plt.clf()
    
# Ne reste plus qu'a afficher le resultat
print(tau)
