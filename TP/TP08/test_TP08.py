from test_TP08z import *



##################################
# Procédure d'exécution des tests
##################################

DICO  = {'01_pgcd': PGCDTest,
         '02_eratosthene': EratostheneTest,
         '03_amplitude': AmplitudeTest,
         '04_gain': GainTest,
         '05_gain_date': GainDateTest,
         '06_gain1': Gain1Test,
         '07_gain1_date': Gain1DateTest,
         '08_winner': WinnerTest,
         '09_tour1' : Tour1Test,
         '10_tour1_bis' : Tour1BisTest,
         '11_tour2' : Tour2Test,
         '12_tour2_bis' : Tour2BisTest,
         }


def fais_tests(choix):
    '''Fonction qui appelle les batteries de tests selon le choix de
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


def detaille_note():
    '''Pour calculer les notes à chaque sous-suite de tests.'''
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
