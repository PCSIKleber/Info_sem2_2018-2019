from test_TP11z import *

##################################
## Procédure d'exécution des tests
##################################

DICO = {
        '01_force2': Force2Test,
        '02_forceN': ForceNTest,
        '03_etats_suivants_euler_court': EtatsSuivantsEulerCourtTest,
        '04_etats_suivants_euler_long' : EtatsSuivantsEulerLongTest,
        '05_positions_suivantes_verlet_court': PositionsSuivantesVerletCourtTest,
        '06_positions_suivantes_verlet_long' : PositionsSuivantesVerletLongTest,
        '07_etats_suivants_verlet_court': EtatsSuivantsVerletCourtTest,
        '08_etats_suivants_verlet_long' : EtatsSuivantsVerletLongTest
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
    print('Attention, il y a 10 points qui seront evalues "a l\'oeil" concernant les figures a produire.')

