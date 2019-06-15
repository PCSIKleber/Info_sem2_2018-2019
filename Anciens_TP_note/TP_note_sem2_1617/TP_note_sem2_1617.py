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
if __name__ == '__main__': import test_TP_note_sem2_1617 as testeur


# ***************************************************************************
# Partie I: Lecture/Affichage du spectre RMN
# ***************************************************************************

def lecture_fichier(filename):
    """ Lecture du fichier RMN: 3 colonnes dont seulement les deux premieres 
    sont a renvoyer """
    return 

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('01_lecture')

import matplotlib.pyplot as plt

def visualise_spectre(delta,spectre):
    """ Fonction qui ne renvoie rien mais devrait creer une image nommee 
    mon_spectre_brut.png a partir des donnees fournies en argument."""
    # Ecrivez votre code entre cette ligne et le plt.clf() qui fait le menage
    
    
    #plt.clf() # Toujours penser a finir par un nettoyage de l'ecran
    # Pensez a decommenter la ligne precedente...

# ***************************************************************************
# Partie II: Integration du signal spectroscopique
# ***************************************************************************

def integration_trapeze_cumulee(x,fx):
    """ Renvoie l'integration cumulee par methode des trapezes pour la liste 
    de valeurs fx de la fonction evaluee aux points correspondant de la liste 
    x. La liste renvoyee doit avoir la meme taille que x et fx avec 
    obligatoirement 0 pour premiere valeur."""
    return []


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_integration')

def visualise_spectre_integre(delta,spectre):
    """ Fonction qui ne renvoie rien mais devrait creer une image nommee 
    mon_spectre_integre.png a partir des donnees fournies en argument."""
    # Ecrivez votre code entre cette ligne et le plt.clf() qui fait le menage
    
    
    #plt.clf() # Toujours penser a finir par un nettoyage de l'ecran
    # Pensez a decommenter la ligne precedente...


# ***************************************************************************
# Partie III: Detection des plateaux
# ***************************************************************************

def rabotage(signal):
    """ Fonction qui renvoie un np.array (ou une liste) identique au signal 
    donne en entree sauf pour les valeurs qui sont inferieure ou egales a 0.5% 
    de la valeur maximale qui sont mises (strictement) a 0 """
    return []

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_rabotage')

import copy

def filtre_median(x,fx,etendue):
    """ Filtre les valeurs fx du signal (obtenues en fonction de x) de sorte a 
    prendre la mediane des valeurs sur l'intervalle de demi-largeur 'etendue' 
    de part et d'autre du point considere. Doit renvoyer:
    * la liste des x amputee de ce qu'il faut ;
    * et la liste correspondant au signal apres filtration."""
    # Si jamais vous avez pour velleite de modifier les listes donnees en 
    # arguments, pensez a n'en modifier qu'une copie via la commande
    #FX = copy.deepcopy(fx)
    return   [[],[]]  
          
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('04_filtre_median')

def detection_plateaux(signal_propre):
    """ Renvoie la liste des positions des milieux des plateaux (zones ou le 
    signal donne en argument est nul). Les milieux sont definis par 
    (debut+fin)//2 ou 'debut' est la position de la premiere annulation sur le 
    plateau et 'fin' est la position de la derniere annulation sur le 
    plateau."""
    return []

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_plateaux')

def visualise_plateaux(delta,signal):
    """ Fonction qui ne renvoie rien mais devrait creer une image nommee 
    mon_spectre_plateau.png a partir des donnees fournies en argument (qu'il 
    faudra proprifier a partir des fonctions precedentes)."""
    # Ecrivez votre code entre cette ligne et le plt.clf() qui fait le menage
    
    
    #plt.clf() # Toujours penser a finir par un nettoyage de l'ecran
    # Pensez a decommenter la ligne precedente...


# ***************************************************************************
# Partie IV: Nombre d'hydrogenes
# ***************************************************************************

def trouve_pourcentages(valeurs_plateaux):
    """ Renvoie la liste des pourcentages de la hauteur de chaque marche 
    comparee a la hauteur totale a partir des hauteurs successives de chaque 
    plateau (liste strictement croissante). """
    return []

# Lignes suivantes a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('06_valeurs_plateaux')

def nombre_total_hydrogenes(pourcentages):
    """ A partir de la liste des pourcentages trouvee precedemment, determiner 
    le (plus petit) nombre total d'hydrogenes de la molecule compatible avec 
    les saut, c'est-a-dire que chaque saut correspond a un nombre 
    (approximativement) entier d'hydrogenes. On dira qu'un nombre est 
    approximativement entier si la difference relative avec sa prediction 
    entiere la plus proche est plus petite que 15%. 
    """
    return

# Lignes suivantes a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('07_nombre_total')


def analyse_molecule(delta,spectre):
    """ Renvoie un unique entier constitue du nombre (minimal) total 
    d'hydrogene de la molecule en utilisant les fonctions definies dans les 
    trois parties precedentes. Une etendue de 30 pour le filtrage est un bon 
    compromis. """

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('08_analyse')



# Calcul de la note finale (a ne commenter que si vous ne voulez pas etre 
# stresse par la note ou que vos algorithmes en chantier font que l'ensemble 
# tourne trop lentement).
if __name__ == '__main__': testeur.detaille_note()
