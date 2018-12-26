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
if __name__ == '__main__': import test_TP_note_sem1_1718 as testeur

# ***************************************************************************
# La PREMIERE des choses a faire: remplir le numero du TP
# ***************************************************************************

numero_du_TP = 0


# ***************************************************************************
# Partie I: Construction d'une liste a partir d'un (normalement) entier n
# ***************************************************************************

def construction_de_liste(n):
    return "Mauvaise reponse..."

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('01_liste')

# ***************************************************************************
# Partie II: Recherche de l'element le plus proche d'une valeur donnee dans une liste
# ***************************************************************************

def recherche_dans(liste):
    return "Mauvaise reponse..."

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_recherche')


# ***************************************************************************
# Partie III: Une petite partie d'echecs ?
# ***************************************************************************

from echiquier import *

def detection_cavaliers(echiquier):
    return "Mauvaise reponse..."

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_detection_cavaliers')

def deplacements_possibles(position_initiale):
    return ['non', 'pas', 'ca...']

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('04_deplacements_possibles')

def prise_possible(echiquier):
    return "Mauvaise reponse..."

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_prise_possible')


# ***************************************************************************
# Partie IV: Un peu de PythonPhysique.
# ***************************************************************************

import numpy as np # Pour avoir par exemple acces a l'exponentielle via np.exp()

def determine_tau(t,u):
    return 0

#if __name__ == '__main__': testeur.fais_tests('06_PP_simple')
#if __name__ == '__main__': testeur.fais_tests('07_PP_simple_non_t0')
#if __name__ == '__main__': testeur.fais_tests('08_PP_decalage')
#if __name__ == '__main__': testeur.fais_tests('09_PP_bruit')


# Calcul de la note finale (a ne commenter que si vous ne voulez pas etre 
# stresse par la note ou que vos algorithmes en chantier font que l'ensemble 
# tourne trop lentement).
if __name__ == '__main__': testeur.detaille_note()
