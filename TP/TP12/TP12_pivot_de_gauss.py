# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des
# tests automatiquement et sans effort: il suffira de decommenter la ligne #if
# #if __name__ == '__main__': testeur.fais_tests('...')
# presente apres chaque definition de fonction.
#
# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est
# ***absolument primordial*** de lancer l'execution dans le menu via
# "Executer  en tant que script" ou "Run file as script"
# c'est-a-dire avec le raccourci Ctrl-Sh#ift-E (et NON simplement Ctrl-E) sinon
# les mises a jour de votre fichier ne seront pas prises en compte.
# (NB: Si vous etes sous Mac, c'est Pomme-Sh#ift-E qu'il faut utiliser)
# ***************************************************************************


# On importe la batterie de tests uniquement a l'execution du fichier et non
# lors de l'import en tant que module:
if __name__ == '__main__': import test_TP12 as testeur


# ***************************************************************************
# Les fonctions gracieusement fournies par vos serviteurs
# ***************************************************************************

def affiche(M):
   '''Procedure simple d'affichage.'''
   for i in range(lignes(M)):
       print(M[i])

def matrice_nulle(n,p):
    '''Renvoie une matrice nulle a n lignes et p colonnes'''
    return [[0 for j in range(p)] for i in range(n)]

# ***************************************************************************
# Compter les lignes et les colonnes
# ***************************************************************************

def lignes(M):
    return []

def colonnes(M):
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_lignes_et_colonnes')

# ***************************************************************************
# Matrices identites et constantes
# ***************************************************************************

def identite(n):
    return []

def matrice_constante(n,p,v):
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('02_identite_et_constante')

# ***************************************************************************
# Trace et transposee
# ***************************************************************************

def trace(M):
    return []

def transpose(M):
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('03_trace_et_transposee')



# ***************************************************************************
# Somme, produit avec un scalaire, multiplication et puissance
# ***************************************************************************

def somme_matrices(M,N):
    return []

def produit_matrice_avec_scalaire(M,k):
    return []

def multiplication_matrices(M,N):
    return []

def puissance_matrice(M,k):
    return []


# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('04_somme_produit_multiplication_puissance')


# ***************************************************************************
# Fusion, separation
# ***************************************************************************

def fusion(A,B):
    '''NB: la fusion doit pouvoir traiter correctement le cas ou B est une
    matrice au bon nombre de lignes mais au nombre arbitraire de colonnes.'''
    return []

def separation(A_B):
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('05_fusion_separation')

# ***************************************************************************
# cherche_pivot, echange_de_ligne, transvection, dilatation
# ***************************************************************************

def cherche_pivot(A_B,i):
    return []

def echange_lignes(A_B,i,j):
    return []

def transvection(A_B,k,i,alpha):
    return []

def dilatation(M,i,alpha):
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('06_echange_pivot_transvection_dilatation')

# ***************************************************************************
# Pivot de Gauss complet
# ***************************************************************************

def pivot_de_gauss(A,B):
    '''NB: si B est une matrice a n lignes et p colonnes, la solution doit
    etre une matrice a n lignes et p colonnes (qui correspond a la resolution
    de p systemes differents dont on change a chaque fois le second membre).
    Cela permettra au return []age de traiter directement la procedure d'inversion
    (cas ou B est la matrice identite)'''
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('07_pivot_de_gauss')


# ***************************************************************************
# determinant
# ***************************************************************************

def determinant(M):
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('08_determinant')

# ***************************************************************************
# inversion
# ***************************************************************************
def inversion(M):
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('09_inversion')

# ***************************************************************************
# puissances relatives
# ***************************************************************************

def puissance_relative_matrice(M,k):
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('10_puissances_relatives')

# ***************************************************************************
# Reseau electrocinetique et poulie
# ***************************************************************************

def reseau_electrocinetique():
    return []

def poulie_a_deux_masses():
    return []

# Ligne suivante a decommenter pour tester (ce sont des tests de verite, le
# details n'est en fait pas tres utile... Faites vos propres tests !)
#if __name__ == '__main__': testeur.fais_tests('11_physique')



# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
