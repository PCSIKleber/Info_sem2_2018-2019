## unittest est le module permettant les tests
import unittest


## On importe les définitions du module créé par les élèves
from TP_note_sem2_1617 import *


import random
#random.seed(0)

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
## Degré et normalisation
##############

import numpy as np

DELTA,SIGNAL = np.loadtxt('spectrum.jdx',usecols=(0,1),unpack=True)

def setUp_global(val):
    import numpy as np
    import scipy as sp
    import scipy.integrate
    
    val.nom_fichier = 'spectrum.jdx'
    def lecture_fichier(filename):
        return np.loadtxt(filename,usecols=(0,1),unpack=True)
    val.lecture_fichier = lecture_fichier
    val.delta,val.signal = np.array(DELTA),np.array(SIGNAL) #lecture_fichier(val.nom_fichier)
    
    def integration_trapeze_cumulee(x,fx):
        return sp.integrate.cumtrapz(fx,x,initial=0)
    val.integration_trapeze_cumulee = integration_trapeze_cumulee
        
    def rabotage(signal):
        signal = np.array(signal)
        signal[signal < max(signal)*0.5e-2] = 0.0
        return signal
    val.rabotage = rabotage
        
    def filtre_median(x,fx,etendue):
        n = len(x)
        L = []
        for i in range(etendue,n-etendue):
            extrait = fx[i-etendue:i+etendue+1]
            L.append(np.median(extrait))
        return x[etendue:n-etendue],np.array(L)
    val.filtre_median = filtre_median
    
    def detection_plateaux(signal_propre):
        SUR_PLATEAU = False
        L = []
        for i in range(len(signal_propre)):
            if not(SUR_PLATEAU) and signal_propre[i] == 0:
                debut = i
                SUR_PLATEAU=True
            if SUR_PLATEAU and signal_propre[i] != 0:
                fin = i-1
                L.append((debut+fin)//2)
                SUR_PLATEAU = False
        if SUR_PLATEAU:
            fin = i
            L.append((debut+fin)//2)
        return L
    val.detection_plateaux = detection_plateaux
    
    def trouve_pourcentages(valeurs_plateaux):
        v = np.array(valeurs_plateaux)
        return (v[1:] - v[:-1]) / max(valeurs_plateaux)
    val.trouve_pourcentages = trouve_pourcentages
    
    def nombre_total_hydrogenes(pourcentages):
        pourcentages = np.array(pourcentages)
        min_H = min(pourcentages)
        for i in range(1,5):
            v = i * pourcentages / min_H
            rv= np.array([round(vi) for vi in v])
            modulo = abs((v - rv)/v)
            if max(modulo) < 0.15:
                return round(sum(v))
        v = 1 * pourcentages / min_H
        return round(sum(v))
    
    val.nombre_total_hydrogenes = nombre_total_hydrogenes
    
    val.analyse = 17

class LectureTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)
    
    def test_lecture_01(self):
        filename = self.nom_fichier
        data = lecture_fichier(filename)
        self.assertEqual(len(data),2)

    def test_lecture_02(self):
        filename = self.nom_fichier
        data = lecture_fichier(filename)
        self.assertEqual(len(data[0]),len(self.delta))

    def test_lecture_03(self):
        filename = self.nom_fichier
        data = lecture_fichier(filename)
        self.assertEqual(len(data[1]),len(self.signal))

    def test_lecture_04(self):
        filename = self.nom_fichier
        data = lecture_fichier(filename)
        i = random.randint(0,len(self.delta)-1)
        self.assertEqual(data[0][i],self.delta[i])

    def test_lecture_05(self):
        filename = self.nom_fichier
        data = lecture_fichier(filename)
        i = random.randint(0,len(self.signal)-1)
        self.assertEqual(data[1][i],self.signal[i])


class VisualiseTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)
    
    def test_visualise_spectre(self):
        visualise_spectre(self.delta,self.signal)

    def test_visualise_spectre_integre(self):
        visualise_spectre_integre(self.delta,self.signal)

    def test_visualise_plateaux(self):
        visualise_plateaux(self.delta,self.signal)


import numpy as np
import scipy as sp
import scipy.integrate

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)

    def test_integration_01(self):
        x = [i for i in range(5)]
        fx= [5]*5
        res = [i*5 for i in range(5)]
        self.assertEqual(list(integration_trapeze_cumulee(x,fx)),res)

    def test_integration_02(self):
        x = [i for i in range(5)]
        fx= [i for i in range(5)]
        res = [i*i/2 for i in range(5)]
        self.assertEqual(list(integration_trapeze_cumulee(x,fx)),res)
    

    def test_integration_03(self):
        x = [i for i in range(5)]
        fx= [i**2 for i in range(5)]
        res = [sum([(j**2+(j+1)**2)/2 for j in range(i)]) for i in range(5)]
        self.assertEqual(list(integration_trapeze_cumulee(x,fx)),res)

    def test_integration_04(self):
        x = np.linspace(0,2*np.pi,1000)
        fx= np.cos(x)
        res = sp.integrate.cumtrapz(fx,x,initial=0)
        comparaison = np.all(res == integration_trapeze_cumulee(x,fx))
        self.assertTrue(comparaison)
    
    def test_integration_05(self):
        x = np.linspace(0,2*np.pi,1000)
        fx= np.cos(x)**2
        res = sp.integrate.cumtrapz(fx,x,initial=0)
        comparaison = np.all(res == integration_trapeze_cumulee(x,fx))
        self.assertTrue(comparaison)

class RabotageTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)
    
    def test_rabotage_01(self):
        s = [(random.random()-0.5)*1e-2 for i in range(3)] + [1] + [random.random()*5e-3 for i in range(3)] 
        p = [0]*3 + [1] + [0]*3
        self.assertEqual(list(rabotage(s)),p)
    
    def test_rabotage_02(self):
        s = [(random.random()-0.5)*1e-1 for i in range(3)] + [10] + [random.random()*5e-2 for i in range(3)] 
        p = [0]*3 + [10] + [0]*3
        self.assertEqual(list(rabotage(s)),p)
    
    def test_rabotage_03(self):
        s = [0,10,0,-10,0]
        p = [0]*5
        p[1] = 10
        self.assertEqual(list(rabotage(s)),p)

    def test_rabotage_04(self):
        maxi = 23
        nb = 100
        x = np.linspace(0,np.pi,nb)
        s = [(random.random()-0.5)*0.5e-2*maxi for i in range(nb)] 
        s+= list(maxi*np.cos(x))
        p = self.rabotage(s)
        result = np.all(p == rabotage(s))
        self.assertTrue(result)

    def test_rabotage_05(self):
        maxi = 0.1
        nb = 100
        x = np.linspace(0,np.pi,nb)
        s = (np.random.random(3*nb)-0.5)*0.5e-2*maxi 
        s[nb:2*nb] = np.exp(-x)*maxi
        p = self.rabotage(s)
        result = np.all(p == rabotage(s))
        self.assertTrue(result)
    
    
     
class FiltreMedianTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)

    def test_filtre_01(self):
        s = [1,2,10,3,4,254,5]
        x = [i for i in range(len(s))]
        etendue = 1
        res = x[etendue:-etendue],[2,3,3,4,5]
        self.assertEqual(list(filtre_median(x,s,etendue)[0]),res[0])

    def test_filtre_02(self):
        s = [1,2,10,3,4,254,5]
        x = [i for i in range(len(s))]
        etendue = 1
        res = x[etendue:-etendue],[2,3,4,4,5]
        self.assertEqual(list(filtre_median(x,s,etendue)[1]),res[1])

    def test_filtre_03(self):
        s = [1,2,10,3,4,254,5]
        x = [i for i in range(len(s))]
        etendue = 2
        res = x[etendue:-etendue],[3,4,5]
        self.assertEqual(list(filtre_median(x,s,etendue)[1]),res[1])

    def test_filtre_04(self):
        n = 1000
        x = np.linspace(0,2*np.pi,n)
        s = 3*np.cos(x) + 2*np.sin(2*x) + np.random.random(n)*3
        etendue = n//10
        res = self.filtre_median(x,s,etendue)
        self.assertTrue(np.all(filtre_median(x,s,etendue)[1][:n//2] == res[1][:n//2]))

    def test_filtre_05(self):
        n = 1000
        x = np.linspace(0,2*np.pi,n)
        s = 3*np.cos(x) + 2*np.sin(2*x) + np.random.random(n)*3
        etendue = n//100
        res = self.filtre_median(x,s,etendue)
        self.assertTrue(np.all(filtre_median(x,s,etendue)[1][:n//2] == res[1][:n//2]))

    
class PlateauxTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)

    def test_plateaux_01(self):
        s = [0]*5 + [1,2,3] + [0]*9
        res = [2,12]
        self.assertEqual(list(detection_plateaux(s)),res)

    def test_plateaux_02(self):
        s = [0]*5 + [1,2,3] + [0]*9 + [1,2,3] + [0]*2
        res = [2,12,20]
        self.assertEqual(list(detection_plateaux(s)),res)

    def test_plateaux_03(self):
        s = [0]*9 + [1,2,3] + [0]*5 + [1,2,3] + [0]*2
        res = [4,14,20]
        self.assertEqual(list(detection_plateaux(s)),res)

    def test_plateaux_04(self):
        # Construction d'un signal avec plusieurs plateaux
        s = []
        while len(s) < 1000:
            nb = int(random.random()*100)
            if random.random() < 0.5:
                s.extend([0]*nb)
            else:
                s.extend([1]*nb)
        res = self.detection_plateaux(s)
        self.assertEqual(list(detection_plateaux(s)),res)
    
    def test_plateaux_05(self):
        maxi = 0.1
        nb = 100
        x = np.linspace(0,np.pi,nb)
        s = np.zeros(3*nb)
        s[nb:2*nb] = np.exp(-x)*maxi
        res = [(nb-1)//2, (2*nb+3*nb-1)//2]
        self.assertEqual(list(detection_plateaux(s)),res)
    

class ValeursPlateauxTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)
        
    def test_pourcentages_01(self):
        vp = [0,2.5,5,10]
        res = [0.25,0.25,0.5]
        self.assertEqual(list(trouve_pourcentages(vp)),res)

    def test_pourcentages_02(self):
        vp = [0,5,10,15,20]
        res = [0.25,0.25,0.25,0.25]
        self.assertEqual(list(trouve_pourcentages(vp)),res)

    def test_pourcentages_03(self):
        vp = [0,10,40,50]
        res = [0.2,0.6,0.2]
        self.assertEqual(list(trouve_pourcentages(vp)),res)

    def test_pourcentages_04(self):
        nb = 10
        vp = sorted(np.array(np.random.random(nb)*1000,dtype=int))
        res = self.trouve_pourcentages(vp)
        eleve = trouve_pourcentages(vp)
        erreur = np.sqrt(np.mean((np.array(eleve)-np.array(res))**2))
        self.assertTrue(erreur < 1e-6)

    def test_pourcentages_05(self):
        nb = 100
        vp = sorted(np.array(np.random.random(nb)*1000,dtype=int))
        res = self.trouve_pourcentages(vp)
        eleve = trouve_pourcentages(vp)
        erreur = np.sqrt(np.mean((np.array(eleve)-np.array(res))**2))
        self.assertTrue(erreur < 1e-6)

    
class NombreTotalTest(unittest.TestCase):
    def setUp(self):
        setUp_global(self)

    def test_nb_tot_01(self):
        pc = [0.25,0.25,0.5]
        res = 4
        self.assertEqual(nombre_total_hydrogenes(pc),res)

    def test_nb_tot_02(self):
        L = [2,2,3]
        pc = [i/sum(L) for i in L]
        res = sum(L)
        self.assertEqual(nombre_total_hydrogenes(pc),res)

    def test_nb_tot_03(self):
        L = [4,3,3]
        pc = [i/sum(L) for i in L]
        res = sum(L)
        self.assertEqual(nombre_total_hydrogenes(pc),res)


    def test_nb_tot_04(self):
        L = [5,2,3,4,3,2,1]
        pc = [i/sum(L) for i in L]
        res = sum(L)
        self.assertEqual(nombre_total_hydrogenes(pc),res)


    def test_nb_tot_05(self):
        L = [5,3,4,2,6]
        pc = [i/sum(L) for i in L]
        res = sum(L)
        self.assertEqual(nombre_total_hydrogenes(pc),res)


    
class AnalyseTest(unittest.TestCase):
    def setUp(self):
        REPONSES = [4,5,7,10,9]
        def teste_analyse(n):
            fichier = 'spectre0{}.jdx'.format(n)
            delta,spectre = np.loadtxt(fichier,unpack=True,usecols=(0,1))
            res = REPONSES[n-1]
            self.assertEqual(analyse_molecule(delta,spectre),res)
        self.teste_analyse = teste_analyse
    
    def test_analyse_01(self):
        self.teste_analyse(1)

    def test_analyse_02(self):
        self.teste_analyse(2)

    def test_analyse_03(self):
        self.teste_analyse(3)

    def test_analyse_04(self):
        self.teste_analyse(4)

    def test_analyse_05(self):
        self.teste_analyse(5)



##################################
## Procédure d'exécution des tests
##################################

DICO = {
        '01_lecture': LectureTest,
        '02_integration': IntegrationTest,
        '03_rabotage': RabotageTest,
        '04_filtre_median': FiltreMedianTest,
        '05_plateaux': PlateauxTest,
        '06_valeurs_plateaux': ValeursPlateauxTest,
        '07_nombre_total': NombreTotalTest,
        '08_analyse': AnalyseTest,
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

#    print("Verification de la bonne execution des procedures graphiques")
#    suite = unittest.TestLoader().loadTestsFromTestCase(VisualiseTest)
#    unittest.TextTestRunner(verbosity=2).run(suite)

    total_general  = 0
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
        print("{:02d}/{:02d}".format(success,total),k)
        total_general += total 
        success_general += success
    print('='*20)
    print('Globalement: {}/{}'.format(success_general,total_general))
    print('Note indicative: {}/20'.format(round(success_general/total_general*20,2)))
    print('Attention, il y a 15 points qui seront evalues "a l\'oeil" concernant les figures a produire.')
