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
if __name__ == '__main__': import test_TP_note_sem2_1718 as testeur

# ***************************************************************************
# Partie I: Codage Cesar
# ***************************************************************************

# Ne pas modifier cette ligne sinon vos programmes risquent de ne pas marcher...
Alphabet = list('abcdefghijklmnopqrstuvwxyz')

def chiffrage(c):
    """ Prend en entree une lettre sous forme de chaine de caractere et 
    renvoie sa position dans la liste alphabetique 'Alphabet' fournie plus 
    haut. Si le caractere ne fait pas parti de la liste, on doit renvoyer 
    None. """
    return []

def lettrage(nb):
    """ Renvoie la caractere associe au nombre nb """
    return []

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('01_chiffrage_lettrage')

def Mise_en_entier(texte):
    """ Transforme la chaine de caractere donnee en entree en une liste 
    d'entiers correspondants aux positions de chaque lettre dans la liste 
    Alphabet. Si un caractere "louche" est trouve, il est simplement ignore et 
    n'apparaitra pas dans la liste a renvoyer. """
    return []

# Coder (a la main si vous voulez) la chaine de caractere 'maitrecorbeau' avec 
# un decalage de 5 caracteres vers la gauche.
maitrecorbeau = 'Pas cela...'

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_Mise_en_entier_maitrecorbeau')

def codage_cesar(texte,d):
    """ Renvoie une chaine de caractere correspondant au codage du texte 
    d'entree avec un decalage de d caracteres vers la gauche. """
    return 'mauvaisereponse'

def decodage_cesar(texte,d):
    """ Renvoie une chaine de caractere correspondant au decodage du texte 
    d'entree qui est suppose avoir ete code avec un decalage de d caracteres 
    vers la gauche. """
    return 'mauvaisereponse'

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_codage_decodage')

def frequence(texte):
    """ Renvoie une liste (de taille 26) qui a chaque lettre associe le nombre 
    d'occurences de cette lettre dans le texte donne en entree. """
    return []

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('04_frequence')

def decodageauto_en_e_majeur(texte):
    """ Se debrouille pour decoder automatiquement le texte en entree en 
    utilisant une analyse frequentielle."""
    return 'mauvaisereponse'

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_decodage_auto')


def top_secret():
    """ Se debrouille pour decoder automatiquement le texte stocke dans le 
    fichier 'secret.txt' du repertoire courant. ATTENTION: le fichier 
    'secret.txt' sera change lors des "tests profs" pour s'assurer que vous 
    avez effectivement implemente une procedure de lecture du fichier... """
    return 'mauvaisereponse'

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('06_top_secret')


# ***************************************************************************
# Partie II: Integrateur a N corps
# ***************************************************************************

def force2(m1,p1,m2,p2):
    """ Calcule la force gravitationnelle que la particule 2 exerce sur la 
    particule 1. """
    return []

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('07_force2')

def forceN(j,m,pos):
    """ Calcule la force gravitationnelle totale que les N-1 autres particules 
    exercent sur la particule j. """
    return []

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('08_forceN')

def positions_suivantes(m,pos,vit,dt):
    """ Doit renvoyer la liste des positions suivantes de chaque particule 
    (dans le meme ordre) apres un pas dt d'integration. """
    N = len(pos)
    new_pos = [[0,0,0] for i in range(N)] # On fournit gracieusement l'initialisation
    return new_pos

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('09_positions_suivantes')

def etats_suivants(m,pos,vit,dt):
    """ Doit renvoyer les listes des positions et vitesses suivantes de chaque 
    particule (dans le meme ordre) apres un pas dt d'integration. Attention a 
    la complexite de votre algorithme si vous voulez obtenir tous les 
    points."""
    return [[]],[[]]

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('10_etats_suivants')


# Ne vous restera plus qu'a generer le graphe demande et le stocker sous le 
# nom 'integration_verlet.png'. Attention cependant a ne *pas* laisser la 
# procedure de generation active pour eviter que l'ordinateur du correcteur ne 
# tourne indefiniment...

import matplotlib.pyplot as plt

generer_graphe = False # A mettre a True pour lancer la generation

if __name__ == '__main__':
    if generer_graphe:
        print('''Une fois la figure generee, la variable 'generer_graphe' a False tu mettras...''')
        m = [3.0,4.0,5.0]  # Les masses des trois points
        v0= [[0,0,0] for i in range(3)]    # Les particules sont au repos
        p0= [[1.0,3,0], [-2,-1,0], [1,-1,0]] # Les trois sommets du triangle
        dt= 1e-4           # Le pas de temps demande
        # Mettez ici votre code pour generer le graphe demande.


        # A la fin, on sauvegarde le fichier
        plt.savefig('integration_verlet.png')

# Calcul de la note finale (a ne decommenter que si vous ne voulez pas etre 
# stresse par la note ou que vos algorithmes en chantier font que l'ensemble 
# tourne trop lentement).
if __name__ == '__main__': testeur.detaille_note()
