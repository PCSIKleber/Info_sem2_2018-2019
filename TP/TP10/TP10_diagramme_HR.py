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
if __name__ == '__main__': import test_TP10 as testeur


# ***************************************************************************
# Determination des dates de transition
# ***************************************************************************

def date_transitions():
    return "Not good..."

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('01_transitions')

# ***************************************************************************
# Les valeurs de temperature et de luminosite
# ***************************************************************************

def obtiens_valeurs_T_L(transitions):
    return "Not good...."

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_echantillonnage')

# ***************************************************************************
# Fabrication du diagramme HR
# ***************************************************************************

def diagramme_HR(T,L):
    print("Aucun diagramme en vue pour le moment")

# Ligne suivante a decommenter pour fabrication effective (n'oubliez pas de definir T et L...)
#if __name__ == '__main__': diagramme_HR(T,L)


# ***************************************************************************
# Lecture du fichier EZ
# ***************************************************************************

def lis_EZ(file='EZ_summary.txt'):
    return "Not good...."

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_lecture')

# ***************************************************************************
# Fabrication du diagramme HR total
# ***************************************************************************

def diagramme_HR_total():
    print("Aucun diagramme total en vue pour le moment")

# Ligne suivante a decommenter pour fabrication effective (n'oubliez pas de definir T et L...)
#if __name__ == '__main__': diagramme_HR_total()




# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
