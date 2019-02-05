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
    return "Not good..."

# Ligne suivante a decommenter pour tester
if __name__ == '__main__': testeur.fais_tests('01_rectangle')


# ***************************************************************************
# Integration par methode des trapezes
# ***************************************************************************

def integration_trapeze(f,a,b,n):
    return "Not good..."

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_trapeze')


# ***************************************************************************
# Recherche d'un zero par dichotomie
# ***************************************************************************

def zero_dichotomie(f,a,b,epsilon=1e-6):
    return "Not good..."

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_dichotomie')


# ***************************************************************************
# La distribution triangulaire a definir
# ***************************************************************************

def triangle(x):
    return "Pas cela en tous cas..."

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_triangle')

# ***************************************************************************
# Pour produire le graphique demande, mettez vos calculs et commandes dans
# cette fonction.
# ***************************************************************************

def tirage_triangle():
    pass

# Ligne suivante a decommenter uniquement quand vous voulez faire votre tirage
# et effectivement produire votre graphique (les calculs sont longs...)
#if __name__ == '__main__': tirage_triangle()



# ***************************************************************************
# La distribution gaussienne de moyenne 10 et d'ecart-type 3 a definir aussi
# pour utilisation ulterieure. Attention, on s'attend a ce qu'elle soit
# normalisee de sorte que son integrale de 0 a 20 ait pour valeur 1
# ***************************************************************************

def gauss_normalisee(x):
    return "Pas cela en tous cas..."

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('05_gauss')


# ***************************************************************************
# Pour produire le graphique demande, mettez vos calculs et commandes dans
# cette fonction.
# ***************************************************************************

def tirage_gauss():
    pass

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
