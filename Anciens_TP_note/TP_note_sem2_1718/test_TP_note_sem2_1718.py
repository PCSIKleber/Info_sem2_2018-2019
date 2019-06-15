# coding: latin1

## unittest est le module permettant les tests
import unittest

## On importe les définitions du module créé par les élèves
from TP_note_sem2_1718 import *


import random
random.seed(0)

import time
# Pour tuer un appel trop long, cf http://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call-in-python
import signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")

def chrono(test,ttot,f,*args):
    '''Fonction qui sert à chronométrer les performances d'un algorithme. 
    Renvoie le résultat de la fonction si elle ne dépasse pas le temps limite'''
    if int(ttot) != ttot:  # alarm ne marche qu'avec des temps entiers
        # On refile le bébé à chrono2, en espérant qu'il n'y ait pas de boucle infinie...
        return chrono2(test,ttot,f,*args) 
    # Sinon, on utilise le module "signal"
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(ttot)   # ttot seconds
    try :
        res= f(*args)
    except Exception:
        print("Votre algorithme dure plus que le temps autorise ({} s)".format(ttot))
        raise
    signal.alarm(0)      # On enlève l'alarme
    return res


def chrono2(test,ttot,f,*args):
    '''Fonction qui sert à chronométrer les performances d'un algorithme. 
    Renvoie le résultat de la fonction'''
    t1 = time.clock()
    res= f(*args)
    t2 = time.clock()
    try: test.assertTrue(t2-t1 < ttot)
    except: 
        print("Votre algorithme est trop long !")
        raise
    return res

def chrono(test,ttot,f,*args): return chrono2(test,ttot,f,*args)

##############
## Chiffrage et Lettrage
##############

p_alphabet = list('abcdefghijklmnopqrstuvwxyz')

def p_chiffrage(c):
    for i in range(len(p_alphabet)):
        if p_alphabet[i] == c: return i
    return None

def p_lettrage(nb):
    return p_alphabet[nb]

class ChiffrageTest(unittest.TestCase):
    def test_chiffrage_01(self):
        self.assertEqual(chiffrage('e'),4)

    def test_chiffrage_02(self):
        self.assertEqual(chiffrage('z'),25)

    def test_chiffrage_03(self):
        self.assertEqual(chiffrage('a'),0)

    def test_chiffrage_04(self):
        self.assertEqual(chiffrage('u'),20)

    def test_chiffrage_05(self):
        self.assertEqual(chiffrage(';'),None)

    def test_lettrage_01(self):
        self.assertEqual(lettrage(4),'e')

    def test_lettrage_02(self):
        self.assertEqual(lettrage(25),'z')

    def test_lettrage_03(self):
        self.assertEqual(lettrage(0),'a')

    def test_lettrage_04(self):
        self.assertEqual(lettrage(20),'u')

##################################
## Test de mise en entiers et maitrecorbeau
##################################

def p_Mise_en_entier(s):
    L = []
    for c in s:
        chiffre = p_chiffrage(c)
        if chiffre != None: L.append(chiffre)
    return L

def p_codage_cesar(texte,d):
    L = p_Mise_en_entier(texte)
    L = [(x-d)%26 for x in L]
    return ''.join([p_lettrage(x) for x in L])

class MiseEnEntierTest(unittest.TestCase):
    def test_mise_en_entier_01(self):
    
        self.assertEqual(Mise_en_entier('hello world!'),[7,4,11,11,14,22,14,17,11,3])

    def test_mise_en_entier_02(self):
        self.assertEqual(Mise_en_entier('pcsi rocks !'),[15,2,18,8,17,14,2,10,18])

    def test_mise_en_entier_03(self):
        s = 'what do you mean by: "test de mise en entier" ?'
        prof = p_Mise_en_entier(s)
        self.assertEqual(Mise_en_entier(s),prof)

    def test_mise_en_entier_04(self):
        s = 'wu, ka et xenophobie sont des mots sympathiques pour gagner au scrabble...'
        prof = p_Mise_en_entier(s)
        self.assertEqual(Mise_en_entier(s),prof)
        
    def test_maitre_corbeau(self):
        result = (maitrecorbeau == p_codage_cesar('maitrecorbeau',5))
        self.assertTrue(result)


##################################
## Passons au codage/decodage
##################################


def p_decodage_cesar(texte,d):
    return p_codage_cesar(texte,-d)

class CodageCesarTest(unittest.TestCase):
    def test_codage_01(self):
        texte,d = 'maitrecorbeau',10
        prof = p_codage_cesar(texte,d)
        self.assertEqual(codage_cesar(texte,d),prof)

    def test_codage_02(self):
        texte,d = 'maitrecorbeau',33
        prof = p_codage_cesar(texte,d)
        self.assertEqual(codage_cesar(texte,d),prof)

    def test_codage_03(self):
        texte,d = 'maitrecorbeau',-10
        prof = p_codage_cesar(texte,d)
        self.assertEqual(codage_cesar(texte,d),prof)

    def test_codage_04(self):
        texte,d = 'wu, ka et xenophobie sont des mots sympathiques pour gagner au scrabble...',-210
        prof = p_codage_cesar(texte,d)
        self.assertEqual(codage_cesar(texte,d),prof)

    def test_codage_05(self):
        texte,d = 'wu, ka et xenophobie sont des mots sympathiques pour gagner au scrabble...',10**10
        prof = p_codage_cesar(texte,d)
        self.assertEqual(codage_cesar(texte,d),prof)

    def test_decodage_01(self):
        texte,d = 'voyons comment le decodage fonctionne.',10
        code = p_codage_cesar(texte,d)
        texte= p_codage_cesar(texte,0)
        self.assertEqual(decodage_cesar(code,d),texte)

    def test_decodage_02(self):
        texte,d = 'cela marche-t-il avec des indices negatifs ?',-10
        code = p_codage_cesar(texte,d)
        texte= p_codage_cesar(texte,0)
        self.assertEqual(decodage_cesar(code,d),texte)

    def test_decodage_03(self):
        texte,d = 'voire meme tout simplement trop grands...',100
        code = p_codage_cesar(texte,d)
        texte= p_codage_cesar(texte,0)
        self.assertEqual(decodage_cesar(code,d),texte)

    def test_decodage_04(self):
        texte,d = 'ou encore trop grands parmi les negatifs.',-1000
        code = p_codage_cesar(texte,d)
        texte= p_codage_cesar(texte,0)
        self.assertEqual(decodage_cesar(code,d),texte)


##################################
## Recherche de fréquence principale
##################################

def p_frequence(texte):
    L = [0]*26
    for c in texte:
        nb = p_chiffrage(c)
        if nb != None:
            L[nb] += 1
    return L

class FrequenceTest(unittest.TestCase):
    def test_frequence_01(self):
        L = [0]*26
        L[4] = 5
        texte = 'eeeee'
        self.assertEqual(frequence(texte),L)

    def test_frequence_02(self):
        L = [0]*26
        L[2],L[8],L[15],L[18] = 1,1,1,1
        texte = 'pcsi1'
        self.assertEqual(frequence(texte),L)

    def test_frequence_03(self):
        texte = 'pcsi rocks, what else could it be ?'
        L = p_frequence(texte)
        self.assertEqual(frequence(texte),L)

    def test_frequence_04(self):
        texte = 'rubbishtalkingwhateveryouwouldliketoknowisnotinhere'
        L = p_frequence(texte)
        self.assertEqual(frequence(texte),L)

    def test_frequence_05(self):
        texte = 'wedidnotinventthealgorithmthealgorithmconsistentlyfindsjesusthealgorithmkilledjeevesthealgorithmisbannedinChinathealgorithmisfromjerseythealgorithmconstantlyfindsjesusthisisnotthealgorithmthisisclose'
        L = p_frequence(texte)
        self.assertEqual(frequence(texte),L)

##################################
## Décodage automatique
##################################

def p_decodageauto_en_e_majeur(texte):
    L = p_frequence(texte)
    maximum = L[0]
    i_max   = 0
    for i in range(len(L)):
        if L[i] > maximum:
            maximum = L[i]
            i_max = i
    clef = 4 - i_max
    return p_decodage_cesar(texte,clef)

class DecodageAutoTest(unittest.TestCase):
    def test_decodageauto_01(self):
        texte = 'wedidnotinventthealgorithmthealgorithmconsistentlyfindsjesusthealgorithmkilledjeevesthealgorithmisbannedinchinathealgorithmisfromjerseythealgorithmconstantlyfindsjesusthisisnotthealgorithmthisisclosverycloseextremelyclose'
        coded_texte = p_codage_cesar(texte,0)
        self.assertEqual(decodageauto_en_e_majeur(coded_texte),texte)

    def test_decodageauto_02(self):
        texte = 'unefemmepassadunemainfastueusesoulevantbalancantlefestonetlourlet'
        coded_texte = 'bulmlttlwhzzhkbulthpumhzablbzlzvbslchuaihshujhuaslmlzavulasvbysla'
        self.assertEqual(decodageauto_en_e_majeur(coded_texte),texte)

    def test_decodageauto_03(self):
        texte = "pourpouvoirdecoderuntexteilfautconnaitrelavaleurdedecalagequelonappellelaclefunemanieredeladeterminerautomatiquementestdessayerdedevinercettevaleurlapprochelapluscourammentemployeeestderegarderlafrequencedapparitiondechaque"
        coded_texte = p_codage_cesar(texte,35)
        self.assertEqual(decodageauto_en_e_majeur(coded_texte),texte)

    def test_decodageauto_04(self):
        texte = "ecrireunefonctiondecodageautoenemajeurtextequiprendenargumentletextecryptesousformedechainedecaractereetquiretourneletextedorigineencalculantlaclefpourquelalettreesoitlaplusfrequentedansletextedecrypte"
        coded_texte = p_codage_cesar(texte,-13)
        self.assertEqual(decodageauto_en_e_majeur(coded_texte),texte)

    def test_decodageauto_05(self):
        texte = "ecrireunefonctiontopsecretquidecodelemessagedufichiersecrettxt"
        coded_texte = p_codage_cesar(texte,42)
        self.assertEqual(decodageauto_en_e_majeur(coded_texte),texte)

##################################
## Le message top_secret
##################################

def p_top_secret():
    f = open('secret.txt')
    for line in f:
        message = line
    return p_decodageauto_en_e_majeur(message)

try: result_top_secret = (top_secret() == p_top_secret())
except: result_top_secret = False

class TopSecretTest(unittest.TestCase):
    def test_top_secret_01(self):
        self.assertTrue(result_top_secret)

    def test_top_secret_02(self):
        self.assertTrue(result_top_secret)

    def test_top_secret_03(self):
        self.assertTrue(result_top_secret)

    def test_top_secret_04(self):
        self.assertTrue(result_top_secret)

    def test_top_secret_05(self):
        self.assertTrue(result_top_secret)


##################################
## Partie II: Système à N corps
##################################

def p_force2(m1,p1,m2,p2):
    P1P2 = [p2[i]-p1[i] for i in range(len(p1))]
    norme = (sum([x**2 for x in P1P2]))**0.5
    a = m1*m2/norme**3
    return [a*x for x in P1P2]

class Force2Test(unittest.TestCase):
    def test_force2_01(self):
        m1,p1,m2,p2 = 1,[1.0,0,0],1,[0,0,0]
        res = force2(m1,p1,m2,p2)
        self.assertEqual(res,[-1,0,0])

    def test_force2_02(self):
        m1,p1,m2,p2 = 2,[1.0,0,0],1,[0,0,0]
        res = force2(m1,p1,m2,p2)
        self.assertEqual(res,[-2,0,0])

    def test_force2_03(self):
        m1,p1,m2,p2 = 1,[0,0,0],2,[0,1.0,0]
        res = force2(m1,p1,m2,p2)
        self.assertEqual(res,[0,2,0])

    def test_force2_04(self):
        m1,p1,m2,p2 = 1,[0,0,1],1,[0,1.0,0]
        res = force2(m1,p1,m2,p2)
        prof= [0,1/2**1.5,-1/2**1.5]
        rtol= 1e-5
        np.testing.assert_allclose(res,prof,rtol)

    def test_force2_05(self):
        m1,p1,m2,p2 = 1,[0,-1,1],1,[0,1.0,0]
        res = force2(m1,p1,m2,p2)
        prof= [0,2/5**1.5,-1/5**1.5]
        rtol= 1e-5
        np.testing.assert_allclose(res,prof,rtol)

    def test_force2_06(self):
        m1,m2 = [random.random() for i in range(2)]
        p1,p2 = [[random.random() for j in range(3)] for i in range(2)]
        prof= p_force2(m1,p1,m2,p2)
        res = force2(m1,p1,m2,p2)
        rtol= 1e-5
        np.testing.assert_allclose(res,prof,rtol)

    def test_force2_07(self):
        m1,m2 = [random.random() for i in range(2)]
        p1,p2 = [[random.random() for j in range(3)] for i in range(2)]
        prof= p_force2(m1,p1,m2,p2)
        res = force2(m1,p1,m2,p2)
        rtol= 1e-5
        np.testing.assert_allclose(res,prof,rtol)

    def test_force2_08(self):
        m1,m2 = [random.random() for i in range(2)]
        p1,p2 = [[random.random() for j in range(3)] for i in range(2)]
        prof= p_force2(m1,p1,m2,p2)
        res = force2(m1,p1,m2,p2)
        rtol= 1e-5
        np.testing.assert_allclose(res,prof,rtol)

##################################
## Force totale sur le corps j
##################################

import numpy as np

def produit_amas(nb):
    m = []
    pos=[]
    vit=[]
    for i in range(nb):
        m.append(random.random())
        pos.append([random.random() for j in range(3)])
        vit.append([random.random() for j in range(3)])
    return m,pos,vit

def p_forceN(j,m,pos):
    force = [0]*3
    for k in range(len(m)):
        if k != j:
            f_k_sur_j = p_force2(m[j],pos[j],m[k],pos[k])
            force = [force[i] + f_k_sur_j[i] for i in range(3)]
    return force

class ForceNTest(unittest.TestCase):
    def test_forceN_01(self):
        j,m,pos = 0,[1],[[1,1,1]]
        res = forceN(j,m,pos)
        self.assertEqual(res,[0]*3)

    def test_forceN_02(self):
        j,m,pos = 0,[1,2],[[1,1,1],[3,3,3]]
        prof = p_force2(m[0],pos[0],m[1],pos[1])
        rtol = 1e-5
        res = forceN(j,m,pos)
        np.testing.assert_allclose(res,prof,rtol)

    def test_forceN_03(self):
        N = 3
        m,pos,vit = produit_amas(N)
        rtol = 1e-5
        prof = p_forceN(N//2,m,pos)
        res = forceN(N//2,m,pos)
        np.testing.assert_allclose(res,prof,rtol)

    def test_forceN_04(self):
        N = 10
        m,pos,vit = produit_amas(N)
        rtol = 1e-5
        prof = p_forceN(N//2,m,pos)
        res = forceN(N//2,m,pos)
        np.testing.assert_allclose(res,prof,rtol)


    def test_forceN_05(self):
        N = 100
        m,pos,vit = produit_amas(N)
        rtol = 1e-5
        prof = p_forceN(N//2,m,pos)
        res = forceN(N//2,m,pos)
        np.testing.assert_allclose(res,prof,rtol)

##################################
## Positions suivantes
##################################

def p_positions_suivantes(m,pos,vit,h):
    """ Calcul de la position suivante connaissant les positions et vitesses à 
    l'instant t_i ainsi que le pas de temps h voulu.
    Version où l'on parcourt manuellement les trois dimensions d'espace. 
    Attention, l'accélération vaut la force divisée par la masse (on aurait 
    mieux fait de calculer les accélérations directement pour économiser 
    quelques calculs...). """
    L = []                   # Initialisation des nouvelles positions
    for j in range(len(m)):  # On parcourt les particules une à une
        mj,pj,vj = m[j], pos[j], vit[j]  # Des raccourcis pour la lisibilité
        force = p_forceN(j,m,pos)        # Vecteur force totale sur j
        next_pj = [0]*3                  # Initialisation nouvelle position pour j
        for k in range(len(pj)):         # Boucle sur les dimensions d'espace
            next_pj[k] = pj[k] + vj[k]*h + h**2/2 * force[k]/mj  # et Verlet
        L.append(next_pj)    # Ajout du résultat à la liste
    return L                 # et renvoi final une fois complètement remplie

class PositionsSuivantesTest(unittest.TestCase):
    def test_positions_suivantes_01(self):
        N = 2
        m,pos,vit = produit_amas(N)
        dt = 1.0
        rtol=1e-4
        prof = p_positions_suivantes(m,pos,vit,dt)
        res  = positions_suivantes(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof,rtol)

    def test_positions_suivantes_02(self):
        N = 5
        m,pos,vit = produit_amas(N)
        dt = 1.0
        rtol=1e-4
        prof = p_positions_suivantes(m,pos,vit,dt)
        res  = positions_suivantes(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof,rtol)

    def test_positions_suivantes_03(self):
        N = 10
        m,pos,vit = produit_amas(N)
        dt = 4.0
        rtol=1e-4
        prof = p_positions_suivantes(m,pos,vit,dt)
        res  = positions_suivantes(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof,rtol)

    def test_positions_suivantes_04(self):
        N = 20
        m,pos,vit = produit_amas(N)
        dt = 1e-1
        rtol=1e-4
        prof = p_positions_suivantes(m,pos,vit,dt)
        res  = positions_suivantes(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof,rtol)

    def test_positions_suivantes_05(self):
        N = 100
        m,pos,vit = produit_amas(N)
        dt = 2
        rtol=1e-4
        prof = p_positions_suivantes(m,pos,vit,dt)
        res  = positions_suivantes(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof,rtol)

##################################
## Etats suivants
##################################

def p_etats_suivants(m,pos,vit,h):
    """ Calcul de l'état suivant (position et vitesse) pour toutes les 
    particules connaissant ces valeurs à la date t_i. """
    new_pos = p_positions_suivantes(m,pos,vit,h) # On calcule tout de suite les nouvelles positions
    new_vit = []                    # Liste vide pour les nouvelles vitesses
    for j in range(len(m)):         # Les particules, une à une
        mj,vj= m[j],vit[j]          # Raccourcis
        fi   = [f/mj for f in p_forceN(j,m,pos)]# Accélération à t_i
        fip1 = [f/mj for f in p_forceN(j,m,new_pos)]# Accélération à t_{i+1}
        next_vj = [0]*3        # Initialisation à la vitesse nulle pour la taille
        for k in range(len(vj)):    # Boucle sur les dimensions d'espace
            next_vj[k] = vj[k] + h/2 * (fi[k] + fip1[k]) # Application de Verlet
        new_vit.append(next_vj)     # Ajout à la liste des vitesses
    return new_pos,new_vit          # Renvoi des nouvelles positions et nouvelles vitesses

class EtatsSuivantsTest(unittest.TestCase):
    def test_etats_suivants_01(self):
        N = 2
        m,pos,vit = produit_amas(N)
        dt = 1.0
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = etats_suivants(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_02(self):
        N = 4
        m,pos,vit = produit_amas(N)
        dt = 0.1
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = etats_suivants(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_03(self):
        N = 10
        m,pos,vit = produit_amas(N)
        dt = 0.01
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = etats_suivants(m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_04(self):
        N = 20
        m,pos,vit = produit_amas(N)
        dt = 2
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = chrono(self,1,etats_suivants,m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_05(self):
        N = 30
        m,pos,vit = produit_amas(N)
        dt = 2
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = chrono(self,1,etats_suivants,m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_06(self):
        N = 50
        m,pos,vit = produit_amas(N)
        dt = 2
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = chrono(self,1,etats_suivants,m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_07(self):
        N = 80
        m,pos,vit = produit_amas(N)
        dt = 2
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = chrono(self,1,etats_suivants,m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_08(self):
        N = 100
        m,pos,vit = produit_amas(N)
        dt = 2
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = chrono(self,1,etats_suivants,m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_09(self):
        N = 150
        m,pos,vit = produit_amas(N)
        dt = 2
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = chrono(self,1,etats_suivants,m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)

    def test_etats_suivants_10(self):
        N = 200
        m,pos,vit = produit_amas(N)
        dt = 2
        prof = p_etats_suivants(m,pos,vit,dt)
        res  = chrono(self,1,etats_suivants,m,pos,vit,dt)
        np.testing.assert_allclose(res,prof)



##################################
## Procédure d'exécution des tests
##################################

DICO = {
        '01_chiffrage_lettrage': ChiffrageTest,
        '02_Mise_en_entier_maitrecorbeau': MiseEnEntierTest,
        '03_codage_decodage': CodageCesarTest,
        '04_frequence': FrequenceTest,
        '05_decodage_auto': DecodageAutoTest,
        '06_top_secret': TopSecretTest,
        '07_force2': Force2Test,
        '08_forceN': ForceNTest,
        '09_positions_suivantes': PositionsSuivantesTest,
        '10_etats_suivants': EtatsSuivantsTest
        }

def fais_tests(choix):
    '''Fonction qui appelle les batteries de test selon le choix de 
    l'utilisateur.'''
    try: 
        suite = unittest.TestLoader().loadTestsFromTestCase(DICO[choix])    
    except:
        print('='*70)
        print('Le choix "%s" ne fait pas partie des possibilites suivantes:' % choix)
        s = '\n  * '
        print(s[1:] + s.join(sorted(list(DICO.keys()))))
        print('='*70)
        exit()
    unittest.TextTestRunner(verbosity=2).run(suite)
    

def calcule_note():
    '''Fonction qui calcule automatiquement la note de l'élève au prorata du 
    nombre de tests passés avec succès.'''
    liste_testcases = ['test_TP_note_sem1.' + elem.__name__ for elem in DICO.values()]
    suite = unittest.TestLoader().loadTestsFromNames(liste_testcases)
    f = open('erreurs.txt','w')
    res = unittest.TextTestRunner(stream=f,verbosity=1).run(suite)
    f.close()
    f = open('erreurs.txt','r')
    explications = '''Resultats des tests: E = Error, F = Failure, . = Success'''
    s_ex = '\n' + '*'*len(explications) + '\n' + explications + '\n' + '*'*len(explications)
    print(s_ex)
    print(f.readline())
    f.close()
    total = res.testsRun  
    failed= len(res.failures)
    errors= len(res.errors)
    success = total - failed - errors
    print("Vous avez reussi {} tests sur un total de {}.".format(success,total))
    print("Note indicative: {}/20 (sans compter la penalite 'commentaires')".format(int(success/total*20)))

def detaille_note():
    '''Pour calculer les notes à chaque sous-suite de tests.'''
    total_general  = 10
    success_general= 0
    for k in sorted(DICO.keys()):
        s = unittest.TestLoader().loadTestsFromTestCase(DICO[k])
        f = open('erreurs.txt','w')
        res = unittest.TextTestRunner(stream=f,verbosity=1).run(s)
        f.close()
        total = res.testsRun  
        failed= len(res.failures)
        errors= len(res.errors)
        success = total - failed - errors
        print("{}/{}".format(success,total),k)
        total_general += total
        success_general += success
    print('='*20)
    print('Globalement: {}/{}'.format(success_general,total_general))
    print('Note indicative: {}/20'.format(round(success_general/total_general*20,2)))
    print('Attention, il y a 10 points qui seront evalues "a l\'oeil" concernant la figure a produire.')
