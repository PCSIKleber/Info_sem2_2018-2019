
TP09 Intégration et tirage aléatoire
====================================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.

Applications directes du cours
------------------------------

1. Intégration: Implémentez les fonctions `integration_rectangle(f,a,b,n)` et `integration_trapeze(f,a,b,n)` qui intègrent la fonction entre `a` et `b` sur `n` points d’échantillonnage par, respectivement, la méthode des rectangles et celle des trapèzes. Elle doit renvoyer la valeur de cette intégrale.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2. Recherche d’un zéro d’une fonction par dichotomie: Implémentez la fonction `zero_dichotomie(f,a,b)` qui cherche (par dichotomie...) un zéro de la fonction `f` entre `a` et `b`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Utilisation sur quelques distributions
--------------------------------------

### Ce qu’il va falloir faire

Voici en détaillé ce que vous allez devoir faire:

1.  Dans chacun des exemples suivants, il va falloir définir la fonction
    f correspondant à la densité de probabilité décrite de sorte que
    l’intégrale de cette fonction sur l’ensemble de définition vaille
    1 (sauf mention explicite du contraire).

2.  Une fois cette fonction définie, il faudra utiliser l’une de vos
    procédures d’intégration pour calculer la primitive
    F de f qui s'annule en x=xmin.

3.  Faire une boucle sur le nombre d’évènements à tirer de manière
    aléatoire et pour chacun

    1.  En utilisant la fonction `random.random()`, tirer aléatoirement un nombre compris entre 0 et 1.

    2.  Adapter (ou utiliser avec ruse) la procédure de recherche de
        zéro par dichotomie pour trouver l’antécédent du nombre
        aléatoire par la fonction F: c’est la valeur de l’évènement x
        cherché.

4.  Une fois les tirages terminés, faire un histogramme de la
    répartition des évènements tirés pour vérifier que la répartition correspond bien à ce que vous vouliez simuler. On redonne le code permettant de tracer un exemple de tel histogramme:

```Python
import random                        # Pour les tirages aléatoires
import matplotlib.pyplot as plt      # Pour les représentations graphiques
nb_tirages = 10000                   # Le nombre de tirages
sommes = [0]*nb_tirages              # Initialisation du stockage des sommes
for i in range(nb_tirages):          # Boucle sur les tirages
    for j in range(10):              # On choisit 10 nombres au hasard sur [0,1[
        sommes[i] += random.random() # en rajoutant à la somme
plt.hist(sommes,bins=16,range=(1,9)) # Dessin de l'histogramme
plt.hist(sommes,bins=32,range=(1,9)) # Le même en 32 bins
plt.xlabel("Valeur de la somme")     # Description de l'axe x
plt.ylabel("Nombre d'evenements")    # Description de l'axe y
plt.title("Somme de 10 nombres aleatoirement choisis entre 0 et 1")
plt.savefig('TP09_somme_10.png')     # Enregistrement de la figure
plt.clf()                            # Nettoyage
```


### Distribution triangulaire.

On considère une distribution triangulaire (affine par morceau avec f(2)=f(4)=0 et f(3)=1). Tirer 10000 évènements correspondant à cette distribution et représenter l’histogramme correspondant. Enregistrez le fichier sous le nom `TP09_tirage_triangle_VotreNom.png` (en remplaçant bien sûr la chaîne par votre vrai nom) et pilotez la génération du fichier par une procédure nommée `tirage_triangle()`

Remarquez que le calcul peut être assez long (selon comment vous l’avez
codé, cela peut représenter pas mal d’intégrales à calculer). Il pourra
être utile d’utiliser la fonction qui permet d’interpoler n’importe
quelle fonction y(x) à partir d’un échantillonnage des x. En outre, il est très facile d’établir la bijection réciproque d’une fonction: il suffit d’échanger les rôles de x et y (qui sont alors tous deux des tableaux triées). Voici un exemple d’utilisation:

```Python
import scipy as sp
import scipy.interpolate
X = sp.linspace(0,20,100)
fX= [Xi**2 - Xi + 2 for Xi in X]
# interp1d renvoie une fonction qui renvoie un array:
# il faut donc ruser et convertir au vol en flottant
f = lambda x: float(scipy.interpolate.interp1d(X,fX)(x))
print(f(12.321),12.321**2 - 12.321 + 2)
```

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


### Distribution gaussienne.

La distribution des notes dans une classe suit généralement une gaussienne, c’est-à-dire que l’on a f(x) = A exp[-(x-mu)^2)/2\sigma^2]$ où mu est la moyenne de la distribution et sigma son écart-type (sigma^2 est la variance). Faire un tirage pour une classe de 44 élèves en ajustant la constante A de sorte que xmin=0 et xmax=20 et en imposant une moyenne à 10 et un écart-type de 3. Comparer l’histogramme obtenu à celui généré pour un tirage de 44x3=132 notes correspondant aux trois PCSI rassemblées en un DS commun. Enregistrez le fichier sous le nom `TP09_tirage_gauss_VotreNom.png` et pilotez la génération du fichier par une procédure nommée `tirage_gauss()`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Vérifiez, en implémentant la fonction `moyenne_et_variance(liste)` que l’on retrouve bien aux environs de mu pour la moyenne et aux environs de sigma^2 pour la variance. Vérifiez ce que cela donne pour la distribution précédente.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


### IMF: Initial Mass Function

Lors de la naissance d’un amas stellaire, la distribution des masses m des étoiles (exprimées en masses solaires) suit ce que l’on appelle l’IMF (pour «Initial Mass Function») dont les astronomes pensent qu’elle est universelle, c’est-à-dire que quel que soit le coin de l’Univers observé, c’est cette distribution qui semble prévaloir. Celle-ci peut se modéliser de manière simple comme un raccordement par continuité de trois lois de puissance d'exposants alpha (pour m compris entre 0.1 et 1 masse solaire), beta (pour m compris entre 1 et 10 masses solaires) et gamma (pour m >= 10 masses solaires) où l’on prend généralement $\alpha=\nb{1,30}$, $\beta=\nb{2,35}$ et
$\gamma=\nb{4,0}$. Vous devez préparer des amas stellaires contenant
chacun $\nb{10000}$ étoiles pour lancer vos simulations de dynamique
stellaire. On vous impose de plus les masses minimale et maximale
admissibles pour vos étoiles qui sont respectivement
$m\e{min}=\nb{0,1}\U{M_\odot}$ et $m\e{max}=\nb{100}\U{M_\odot}$.

1.  Combien avez-vous, en moyenne, d’étoiles de plus de $1\U{M_\odot}$
    dans vos simulations ? de plus de $10\U{M_\odot}$ ?

2.  L’essentiel ($90\%$) de la lumière de l’amas est fourni, durant ses
    premiers millions d’années d’existence, par les étoiles de plus de
    $5\U{M_\odot}$: quelle fraction de la masse totale de l’amas
    représentent-elles ? En quoi cela peut-il être intéressant pour
    l’astrophysicien ?

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
