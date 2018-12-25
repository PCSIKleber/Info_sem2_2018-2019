TP08 Petits jeux électoraux
===========================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.


Algorithme d’Euclide
--------------------

Programmer une procédure `pgcd(a,b)` s’appliquant à deux entiers naturels `a` et `b` renvoyant le plus grand commun diviseur de a et b.

On rappelle l'algorithme d'Euclide:
  - On pose r{0} = a.
  - On pose r{1} = b.
  - Pour tout n>=1, si r{n} est non nul on note r{n+1} le reste de
    la division euclidienne de r{n-1} par $r{n}.
  - Si r{n} est nul, alors le pgcd recherché est r{n-1}.

Rappelons à toute fins utiles qu’en particulier le pgcd de 0 et 0 vaut 0.


**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Crible d’Ératostène
-------------------

Implémenter une procédure qui renvoie la liste des nombres
premiers inférieurs ou égaux à n en respectant l’algorithme du crible d'Érathostène. On utilisera une liste annexe pour stocker l'état (premier ou non) d'un nombre donné sous forme d'un booléen et éviter ainsi de barrer les multiples d'un nombre qui n'est déjà plus premier.
Pour visualiser concrètement ce qu’il se passe, on pourra consulter la
page suivante : http://commons.wikimedia.org/wiki/File:New_Animation_Sieve_of_Eratosthenes.gif

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Wall-Street
-----------

Ce problème s’inspire d’une épreuve d’informatique de l’École
Polytechnique. Vous ne devez pas utiliser les fonctions `min` et `max` 
appliquées à des listes.

On cherche à calculer le gain maximum possible (à la bourse) sur une
action pendant une période de n jours. Vous ne faites qu’une opération
d’achat et de vente d’une seule action pendant la période étudiée. On
suppose que les cours quotidiens de cette action sont enregistrés dans
un tableau d’entiers naturels contenant n éléments (0 <= i <= n-1).

On définit l’*amplitude* de la variation du cours comme le maximum de la
valeur absolue de la variation de ce cours pendant la période observée.

1.  Écrire une fonction `amplitude(cot)` qui renvoie comme
    résultat l’amplitude de la variation du cours représenté par la
    liste `cot`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Le *gain maximum* est le gain maximum possible sur la période observée,
c’est-à-dire le maximum de cot{j}-cot{i} pour i <= j.

2.  Donner un exemple où l’amplitude est différente du gain maximum. Que
    représente l’amplitude en terme de gain ou de perte ?

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  En suivant textuellement la définition du gain, écrire une fonction
    `gain(cot)` qui renvoie, en temps quadratique par rapport à
    n, le gain maximal possible sur le cours représenté par la liste `cot`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


4.  Construire une procédure `gain_date(cot)` en modifiant la procédure précédente afin de renvoyer la *liste* des *couples* formés des deux dates `da` et `dv` d’achat et de vente de l’action permettant d’obtenir le gain maximum sur la liste `cot` avec `dv - da` minimum.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Pour tout i de l'intervalle [0,n-1], définissons le gain courant maximum comme
le gain maximum possible obtenu en vendant son action au temps $i$.

5.  En calculant progressivement le gain courant maximum, écrire une
    procédure que l’on nommera `gain1(cot)` qui renvoie, en temps
    linéaire par rapport à n, le gain maximum possible sur le cours
    représenté par la liste `cot`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


6.  Construire une procédure `gain1_date` en modifiant la procédure précédente afin de renvoyer la liste des couples formés des deux dates `da` et `dv` d’achat et de vente de l’action permettant d’obtenir le gain maximum sur la liste `cot` avec `dv - da` minimum.


**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Dépouillement d’élections
-------------------------

Le problème suivant — inspiré d’un sujet d’écrit de l’École
polytechnique — consiste à faire le décompte du résultat des élections
dans le pays JJ-Boubou. La règle électorale y est très laxiste, puisque
l’on peut être élu sans s’être présenté. Plus prosaïquement, chaque
votant (portant un numéro i d'électeur compris entre 0 et n) vote pour `vote[i]`, où `vote[i]` est un
entier positif caractéristique de la personne pour qui on vote (les habitants du pays JJ-Boubou sont identifiés par un
entier réprésentant leur numéro de sécurité sociale qui peut être très grand et est notamment différent de leur numéro d'électeur). On dispose de la
liste qui contient les votes des $n$ habitants du pays des JJ-Boubou.

1.  Dans le pays JJ-Boubou, le seul candidat ayant obtenu strictement
    plus de 50% des voix exprimées est élu au premier tour des
    élections.

    1.  Écrire une fonction `winner(vote,k)` qui renvoie `True` si le candidat possède la majorité absolu et `False` sinon.

    **STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


    2.  Écrire la fonction `gagnant_tour1(vote)` qui renvoie le gagnant du premier tour s’il existe. S’il n’existe pas, on renvera `None`. On pourra utiliser la fonction de la question précédente. On se contentera d’une fonction faisant le calcul en temps quadratique par rapport à n.

    **STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2.  Supposons le tableau trié dans l’ordre croissant, vérifiant `vote[0]<=vote[1]<=...<=vote[n-1]`. Écrire une fonction `gagnant_tour1_bis(vote)` qui renvoie en temps linéaire par rapport à n le gagnant du premier tour s’il existe et `None` dans le cas contraire.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  Au second tour des élections, le candidat ayant obtenu le plus de
    voix est élu. S’il y a égalité de voix, tous les candidats ayant
    obtenu le plus de voix sont élus (ex æquo).

    1.  Écrire la fonction `gagnant_tour2(vote)`  qui renvoie dans un tableau les gagnants du second tour. On prendra garde à ne faire apparaître qu’une seule fois le nom des gagnants dans la liste finale (par exemple en utilisant un ensemble python (`set`)). On se contentera d’une fonction faisant le calcul en temps quadratique par rapport à n.

    **STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

    2.  Supposons le tableau trié en ordre croissant, vérifiant
        `vote[0]<=vote[1]<=...<=vote[n-1]`. Écrire une fonction `gagnant_tour2_bis(vote)` qui renvoie en temps linéaire par rapport à n le gagnant du second tour.

    **STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
