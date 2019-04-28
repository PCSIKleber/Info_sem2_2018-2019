from test_TP12z import *

##################################
# Procédure d'exécution des tests
##################################

DICO  = {'01_lignes_et_colonnes': LignesColonnesTest,
         '02_identite_et_constante': IdentiteConstanteTest,
         '03_trace_et_transposee': TraceTest,
         '04_somme_produit_multiplication_puissance': SommeTest,
         '05_fusion_separation': FusionTest,
         '06_echange_pivot_transvection_dilatation': EchangeTest,
         '07_pivot_de_gauss': PivotTest,
         '08_determinant': DeterminantTest,
         '09_inversion': InversionTest,
         '10_puissances_relatives': PuissancesTest,
         '11_physique': PhysiqueTest,
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
        print("{:2d}/{:2d}".format(success,total),k)
        total_general += total
        success_general += success
    print('='*20)
    print('Globalement: {}/{}'.format(success_general,total_general))
    print('Note indicative: {}/20'.format(round(success_general/total_general*20,2)))
#    print('Attention, il y a 10 points qui seront evalues "a l\'oeil" concernant les graphiques a produire')
#    print('a raison de 5 points par graphique correctement fait.')
