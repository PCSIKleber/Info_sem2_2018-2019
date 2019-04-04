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
# **NB**: Ne PAS commenter cette ligne car c'est elle qui charge le fichier de test...
if __name__ == '__main__': import test_TP11 as testeur

# ***************************************************************************
# Partie I: Préparatifs
# ***************************************************************************

def force2(m1,p1,m2,p2):
    """ Calcule la force gravitationnelle que la particule 2 exerce sur la
    particule 1. """
    f = [0]*3
    r2 = 0
    for i in range(3):
        r2 = r2 + (p1[i]-p2[i])**2
    r = r2**0.5
    for i in range(3):
        f[i] = -m1*m2 / r**3 * (p1[i]-p2[i])
    return f

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('01_force2')

def forceN(j,m,pos):
    """ Calcule la force gravitationnelle totale que les N-1 autres particules
    exercent sur la particule j. """
    mj = m[j]
    pj = pos[j]
    F = [0]*3
    for i in range(len(pos)):
        if i != j :
            f = force2(mj,pj,m[i],pos[i])
            for k in range(3):
                F[k] += f[k]
    return F

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_forceN')

def etats_suivants_euler(m,pos,vit,dt):
    """ Doit renvoyer les listes des positions et vitesses suivantes de chaque 
    particule (dans le meme ordre) apres un pas dt d'integration. Attention a 
    la complexite de votre algorithme si vous voulez obtenir tous les 
    points."""
    N = len(pos)
    new_pos = [[0,0,0] for i in range(N)] # On fournit gracieusement l'initialisation
    new_vit = [[0,0,0] for i in range(N)] # On fournit gracieusement l'initialisation
    for i in range(N):   #boucle sur le nombre de particules
         force=forceN(i,m,pos)
         for j in range(3): #boucle sur les coordonnées
            new_pos[i][j]=pos[i][j]+dt*vit[i][j]
            new_vit[i][j]=vit[i][j]+dt*force[j]/m[i]

    return(new_pos,new_vit)

if __name__ == '__main__': testeur.fais_tests('03_etats_suivants_euler_court') 
#if __name__ == '__main__': testeur.fais_tests('04_etats_suivants_euler_long')

def positions_suivantes_verlet(m,pos,vit,dt):
    """ Doit renvoyer la liste des positions suivantes de chaque particule 
    (dans le meme ordre) apres un pas dt d'integration. """
    N = len(pos)
    new_pos = [[0,0,0] for i in range(N)] # On fournit gracieusement l'initialisation
    return new_pos

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_positions_suivantes_verlet_court') 
#if __name__ == '__main__': testeur.fais_tests('06_positions_suivantes_verlet_long')

def etats_suivants_verlet(m,pos,vit,dt):
    """ Doit renvoyer les listes des positions et vitesses suivantes de chaque 
    particule (dans le meme ordre) apres un pas dt d'integration. Attention a 
    la complexite de votre algorithme si vous voulez obtenir tous les 
    points."""
    return [[]],[[]]

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('07_etats_suivants_verlet_court') 
#if __name__ == '__main__': testeur.fais_tests('08_etats_suivants_verlet_long')


# Ne vous restera plus qu'a generer le graphe demande et le stocker sous le 
# nom 'integration_verlet_VotreNom.png' et 'integration_verlet_VotreNom.png' 
# (ou bien entendu la chaîne 'VotreNom' est à remplacer par votre propre nom). 
# Attention cependant a ne *pas* laisser la procedure de generation active 
# pour eviter que l'ordinateur du correcteur ne tourne indefiniment...

import matplotlib.pyplot as plt

generer_graphe = False # A mettre a True pour lancer la generation

if __name__ == '__main__':
    if generer_graphe:
        print('''Une fois la figure generee, la variable 'generer_graphe' a False tu mettras...''')
        m = [3.0,4.0,5.0]  # Les masses des trois points
        v0= [[0,0,0] for i in range(3)]    # Les particules sont au repos
        p0= [[1.0,3,0], [-2,-1,0], [1,-1,0]] # Les trois sommets du triangle
        dt= 1e-4           # Le pas de temps demande
        # Mettez ici votre code pour generer les graphes demandes.



# Calcul de la note finale (a ne decommenter que si vous ne voulez pas etre 
# stresse par la note ou que vos algorithmes en chantier font que l'ensemble 
# tourne trop lentement).
if __name__ == '__main__': testeur.detaille_note()
