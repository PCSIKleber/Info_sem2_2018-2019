Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.

Angle d’attaque
===============

Pour explorer les routines d'évolution stellaire fournies, vous disposez du module `sse` stocké sous forme
compilé dans le répertoire `TP10/` et plus particulièrement de la
fonction `sse.get_evolution(t)` qui donne les informations sur l’état de l’étoile à la date `t`,
sa luminosité et sa température de surface. Par exemple, vous pouvez
utiliser

```Python
import sse                   # Import du module
help(sse.get_evolution)      # Obtenir l’aide correspondant à la fonction appelée
t = 10                       # On regarde à t = 10Myr
s,L,T = sse.get_evolution(t) # Qu’obtient-on ?
print(“À t= {} Myr, état {} avec log10(L)={} et log10(T)={}”.format(t,s,L,T))
```

La durée de vie totale de l’étoile à 7 masses solaires que vous désirez
étudier est d’environ 60 Myr. Le but du TP est, dans un premier
temps, de dessiner le diagramme HR de l’étoile en plaçant 50 points
régulièrement espacés en temps sur chacune des phases (donc 300 points
au final vu qu’il y aura 6 phases, les formules d’interpolations
n’allant, dans notre cas, que jusqu’à l’état de géante rouge pulsante
sur la branche asymptotique des géantes). Pour ce faire, voici la marche
à suivre:

1.  Écrire une fonction `date_transitions()` qui renvoie une liste à 6 valeurs où chaque
    valeur représente l’âge de transition de l’étape `i` à l’étape `i+1`
    (la dernière valeur étant l’âge limite pour lequel les formules
    d’interpolation renvoient une valeur sensée [et non `None`]). On pourra
    s’inspirer des techniques développées en cours concernant la
    recherche par dichotomie d’une valeur dans une liste ou du zéro
    d’une fonction.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2.  Écrire une fonction `obtiens_valeurs_T_L(transitions)` qui prend en entrée la liste à 6 valeurs
    précédemment calculée et renvoie deux tableaux de 300 éléments
    chacun contenant les valeurs en log T et log L correctement
    échantillonnées à raison de 50 points sur chaque phase,
    c’est-à-dire que les points de 0 à 49 appartiennent à la phase 1,
    les points de 50 à 99 à la phase 2, etc. Pour les tests, la liste de
    transitions donnée est telle que si t_{i,i+1} correspond à la date
    de transition de l’état `i` à l’état `i+1`, alors l’état de l’étoile
    en t_{i,i+1} est l’état `i+1`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  Enfin, écrire une fonction `diagramme_HR(T,L)` qui prend en entrée les deux listes
    calculées précédemment et qui dessine en sortie le diagramme HR
    proprement dit à sauvegarder dans le fichier `HR_sse_VotreNom.png` (mettez bien sûr votre
    propre nom sans accent ni espace).

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Comparaison avec EZ-web
=======================

Dessiner un diagramme HR n’est pas tout. Encore faut-il comparer le
résultat avec un code qui aura pris un soin tout particulier à inclure
tout ce que l’on sait sur les mécanismes physiques à l’origine de
l’évolution stellaire. Vous avez récupéré une telle simulation dans le
fichier `TP10/EZ_summary.txt` qui contient énormément d’informations (29
colonnes en tout). Il faut à présent le lire, en extraire ce qui vous
intéresse (colonnes 4 pour $\log L$ et 6 pour $\log T$) et superposer le
diagramme HR correspondant à votre précédent diagramme. On procèdera
donc comme suit:

1.  Écrire une fonction `lis_EZ()` qui lit le fichier `TP10/EZ_summary.txt` et
    renvoie un triplet `(t,L,T)` :

    -   `t` est une liste contenant tous les âges présents dans la
        simulation (2ième colonne du fichier).

    -   `L` est une liste contenant les valeurs de log L (les valeurs du fichiers sont déjà les logarithme) en
        correspondance avec les âges contenus dans `t` (4ième colonne du
        fichier).

    -   `T` est une liste contenant les valeurs de log T en
        correspondance avec les âges contenus dans (6ième colonne du
        fichier).

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2.  Écrire une fonction `diagramme_HR_total()` qui va superposer sur un même diagramme les
    résultats des formules d’interpolation et ceux de la simulation EZ.
    Sauvegarder le résultat dans le fichier `HR_EZ_VotreNom.png` (mettez bien sûr votre
    propre nom sans accent ni espace).

On pourra terminer en comparant les âges de transition dans les deux
modèles, c’est-à-dire en regardant la position dans le diagramme HR de
EZ à l’âge correspondant à chaque transition tiré des formules
d’interpolation.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
