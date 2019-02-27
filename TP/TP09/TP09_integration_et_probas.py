# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des
# tests automatiquement et sans effort: il suffira de decommenter la ligne if
# if __name__ == '__main__': testeur.fais_tests('...')
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
if __name__ == '__main__': import test_TP09 as testeur


# ***************************************************************************
# Integration par methode des rectangles
# ***************************************************************************

def integration_rectangle(f,a,b,n):
    pas=(b-a)/n
    return sum([f(a+k*pas) for k in range(n)])*pas

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_rectangle')


# ***************************************************************************
# Integration par methode des trapezes
# ***************************************************************************

def integration_trapeze(f,a,b,n):
    pas=(b-a)/n
    return sum([(f(a+k*pas)+f(a+(k+1)*pas)) for k in range(n)])*pas/2

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_trapeze')


# ***************************************************************************
# Recherche d'un zero par dichotomie
# ***************************************************************************

def zero_dichotomie(f,a,b,epsilon=1e-6):
    d=a
    g=b
    while abs(g-d)>epsilon:
        m=(d+g)/2
        if f(m)*f(d)<=0:
            g=m
        else:
            d=m
    return m

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_dichotomie')


# ***************************************************************************
# La distribution triangulaire a definir
# ***************************************************************************

def triangle(x):
    if 1<=x<=2: return 0
    elif 2<=x<=3: return x-2
    elif 3<=x<=4: return 4-x
    else: return 0

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_triangle')

# ***************************************************************************
# Pour produire le graphique demande, mettez vos calculs et commandes dans
# cette fonction.
# ***************************************************************************

def repartition_triangle(x):
    if 1<=x<=2: return 0
    elif 2<=x<=3: return ((x-2)**2)/2
    elif 3<=x<=4: return 1-(0.5)*(4-x)**2
    else: return 1
    
    
import math    
    
def repartition_triangle_inv(y):
    if 0<=y<=0.5: return 2+math.sqrt(2*y)
    elif 0.5<=y<=1: return 4-math.sqrt(2)*math.sqrt(1-y)  
    
import random
import matplotlib.pyplot as plt


def tirage_triangle(nb_tirage=10):
    liste=[0]*nb_tirage
    for i in range(nb_tirage):
        liste[i]=repartition_triangle_inv(random.random())
    plt.hist(liste,bins=32,range=(2,4))
    plt.show()



# Ligne suivante a decommenter uniquement quand vous voulez faire votre tirage
# et effectivement produire votre graphique (les calculs sont longs...)
#if __name__ == '__main__': tirage_triangle()



# ***************************************************************************
# La distribution gaussienne de moyenne 10 et d'ecart-type 3 a definir aussi
# pour utilisation ulterieure. Attention, on s'attend a ce qu'elle soit
# normalisee de sorte que son integrale de 0 a 20 ait pour valeur 1
# ***************************************************************************


f=lambda x: math.exp(-(x-10)**2/18)

integrale_gauss=integration_trapeze(f,0,20,1000)



def gauss_normalisee(x):
    return f(x)/integrale_gauss
    
repartition_gauss = lambda x: integration_trapeze(gauss_normalisee,0,x,100)

def repartition_gauss_inv(y):
    h=lambda x: repartition_gauss(x)-y
    return zero_dichotomie(h,0,20,epsilon=1e-6)
    
    


# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('05_gauss')


# ***************************************************************************
# Pour produire le graphique demande, mettez vos calculs et commandes dans
# cette fonction.
# ***************************************************************************

def tirage_gauss(nb_tirage=1000):
    liste=[0]*nb_tirage
    for i in range(nb_tirage):
        liste[i]=repartition_gauss_inv(random.random())
    plt.hist(liste,bins=32,range=(0,20))
    plt.show()

# Ligne suivante a decommenter uniquement quand vous voulez faire votre tirage
# et effectivement produire votre graphique (les calculs sont longs, mais on
# ne demande pas trop pour la gaussienne).
#if __name__ == '__main__': tirage_gauss()

# ***************************************************************************
# Calcul de la moyenne et de la variance d'une liste de nombres
# ***************************************************************************

def moyenne_et_variance(liste):
    return moyenne,variance

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('06_moyenne_variance')

# ***************************************************************************
# L'IMF (Initial Mass Function) d'abord definie de sorte que imf(1) = 1 (a
# vous de vous debrouiller pour que ce soit bien continu)
# ***************************************************************************

def imf(x):
    return "Pas cela en tous cas..."

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('07_imf')

# Il reste a determiner les valeurs demandees (stockez-les bien dans ces
# variables si vous voulez tous les points)

etoiles_de_plus_de_une_masse_solaire  = "Beaucoup"
etoiles_de_plus_de_dix_masses_solaires= "Beaucoup moins"
fraction_masse_totale_en_etoiles_de_plus_de_cinq_masses_solaires = "Diantre !"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('08_etoiles')




# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
