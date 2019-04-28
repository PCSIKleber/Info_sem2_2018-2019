import unittest
EKxGC=Exception
EKxGf=int
EKxGn=range
EKxGW=len
EKxGj=AssertionError
EKxGP=None
EKxGt=list
from TP12_pivot_de_gauss import*
import random
random.seed(0)
import numpy as np
import time
import math
import signal
import copy
def signal_handler(signum,frame):
 raise EKxGC("Timed out!")
def chrono(test,ttot,f,*args):
 if EKxGf(ttot)!=ttot:
  return chrono2(test,ttot,f,*args)
 signal.signal(signal.SIGALRM,signal_handler)
 signal.alarm(ttot)
 try:
  EKxGJ=f(*args)
 except EKxGC:
  print("Votre algorithme dure plus que le temps autorise ({} s)".format(ttot))
  raise
 return EKxGJ
def chrono2(test,ttot,f,*args):
 t1=time.clock()
 EKxGJ=f(*args)
 t2=time.clock()
 try:test.assertTrue(t2-t1<ttot)
 except:
  print("Votre algorithme est trop long !")
  raise
 return EKxGJ
def chrono(test,ttot,f,*args):
 return chrono2(test,ttot,f,*args)
class LignesColonnesTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.B=[1,2,3]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.D=[[1],[2],[3],[4],[5]]
  EKxGM.E=[[j*i for j in EKxGn(12)]for i in EKxGn(234)]
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
 def test_lignes01(EKxGM):
  EKxGM.assertEqual(lignes(EKxGM.A),EKxGW(EKxGM.A))
 def test_lignes02(EKxGM):
  EKxGM.assertEqual(lignes(EKxGM.B),EKxGW(EKxGM.B))
 def test_lignes03(EKxGM):
  EKxGM.assertEqual(lignes(EKxGM.C),EKxGW(EKxGM.C))
 def test_lignes04(EKxGM):
  EKxGM.assertEqual(lignes(EKxGM.D),EKxGW(EKxGM.D))
 def test_lignes05(EKxGM):
  EKxGM.assertEqual(lignes(EKxGM.E),EKxGW(EKxGM.E))
 def test_colonnes01(EKxGM):
  EKxGM.assertEqual(colonnes(EKxGM.A),EKxGW(EKxGM.A[0]))
 def test_colonnes02(EKxGM):
  EKxGM.assertEqual(colonnes(EKxGM.F),EKxGW(EKxGM.F[0]))
 def test_colonnes03(EKxGM):
  EKxGM.assertEqual(colonnes(EKxGM.C),EKxGW(EKxGM.C[0]))
 def test_colonnes04(EKxGM):
  EKxGM.assertEqual(colonnes(EKxGM.D),EKxGW(EKxGM.D[0]))
 def test_colonnes05(EKxGM):
  EKxGM.assertEqual(colonnes(EKxGM.E),EKxGW(EKxGM.E[0]))
class IdentiteConstanteTest(unittest.TestCase):
 def test_identite01(EKxGM):
  n=1
  In=np.identity(n)
  EKxGM.assertTrue(np.all(np.array(identite(n))==In))
 def test_identite02(EKxGM):
  n=2
  In=np.identity(n)
  EKxGM.assertTrue(np.all(np.array(identite(n))==In))
 def test_identite03(EKxGM):
  n=3
  In=np.identity(n)
  EKxGM.assertTrue(np.all(np.array(identite(n))==In))
 def test_identite04(EKxGM):
  n=10
  In=np.identity(n)
  EKxGM.assertTrue(np.all(np.array(identite(n))==In))
 def test_identite05(EKxGM):
  n=100
  In=np.identity(n)
  EKxGM.assertTrue(np.all(np.array(identite(n))==In))
 def test_constante01(EKxGM):
  n,p,v=1,2,3
  M=np.ones((n,p))*v
  EKxGM.assertTrue(np.all(np.array(matrice_constante(n,p,v))==M))
 def test_constante02(EKxGM):
  n,p,v=2,2,42
  M=np.ones((n,p))*v
  EKxGM.assertTrue(np.all(np.array(matrice_constante(n,p,v))==M))
 def test_constante03(EKxGM):
  n,p,v=42,2,421
  M=np.ones((n,p))*v
  EKxGM.assertTrue(np.all(np.array(matrice_constante(n,p,v))==M))
 def test_constante04(EKxGM):
  n,p,v=10,12,-54.2
  M=np.ones((n,p))*v
  EKxGM.assertTrue(np.all(np.array(matrice_constante(n,p,v))==M))
 def test_constante05(EKxGM):
  n,p,v=41,42,43
  M=np.ones((n,p))*v
  EKxGM.assertTrue(np.all(np.array(matrice_constante(n,p,v))==M))
class TraceTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,4,5]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j/(i+1)for j in EKxGn(125)]for i in EKxGn(125)]
  EKxGM.G=[[j/(i+1)for j in EKxGn(125)]for i in EKxGn(234)]
 def test_trace01_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,trace,EKxGM.A)
 def test_trace02(EKxGM):
  M=EKxGM.C
  tr=np.trace(M)
  EKxGM.assertEqual(trace(M),tr)
 def test_trace03(EKxGM):
  M=EKxGM.B
  tr=np.trace(M)
  EKxGM.assertEqual(trace(M),tr)
 def test_trace04(EKxGM):
  M=EKxGM.D
  tr=np.trace(M)
  EKxGM.assertEqual(trace(M),tr)
 def test_trace05(EKxGM):
  M=EKxGM.F
  tr=np.trace(M)
  EKxGM.assertAlmostEqual(trace(M),tr)
 def test_transpose01(EKxGM):
  M=EKxGM.A
  tM=np.transpose(M)
  EKxGM.assertTrue(np.all(np.array(transpose(M))==tM))
 def test_transpose02(EKxGM):
  M=EKxGM.B
  tM=np.transpose(M)
  EKxGM.assertTrue(np.all(np.array(transpose(M))==tM))
 def test_transpose03(EKxGM):
  M=EKxGM.C
  tM=np.transpose(M)
  EKxGM.assertTrue(np.all(np.array(transpose(M))==tM))
 def test_transpose04(EKxGM):
  M=EKxGM.F
  tM=np.transpose(M)
  EKxGM.assertTrue(np.all(np.array(transpose(M))==tM))
 def test_transpose05(EKxGM):
  M=EKxGM.G
  tM=np.transpose(M)
  EKxGM.assertTrue(np.all(np.array(transpose(M))==tM))
class SommeTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,4,5]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
 def test_somme01_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,somme_matrices,EKxGM.A,EKxGM.B)
 def test_somme02_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,somme_matrices,EKxGM.A,EKxGM.C)
 def test_somme03(EKxGM):
  M=np.array(EKxGM.C)+np.array(EKxGM.D)
  EKxGM.assertTrue(np.all(np.array(somme_matrices(EKxGM.C,EKxGM.D))==M))
 def test_somme04(EKxGM):
  M=np.array(EKxGM.F)+np.array(EKxGM.F)
  EKxGM.assertTrue(np.all(np.array(somme_matrices(EKxGM.F,EKxGM.F))==M))
 def test_somme05_matrices_inchangees(EKxGM):
  M=np.array(EKxGM.C)+np.array(EKxGM.D)
  somme_matrices(EKxGM.D,EKxGM.D)
  EKxGM.assertTrue(np.all(np.array(EKxGM.D)==np.array(EKxGM.E)))
 def test_produit_avec_scalaire01(EKxGM):
  k=42
  M=EKxGM.A
  R=np.array(M)*k
  EKxGM.assertTrue(np.all(np.array(produit_matrice_avec_scalaire(M,k))==R))
 def test_produit_avec_scalaire02(EKxGM):
  k=1/42
  M=EKxGM.A
  R=np.array(M)*k
  EKxGM.assertTrue(np.all(np.array(produit_matrice_avec_scalaire(M,k))==R))
 def test_produit_avec_scalaire03(EKxGM):
  k=42
  M=EKxGM.F
  R=np.array(M)*k
  EKxGM.assertTrue(np.all(np.array(produit_matrice_avec_scalaire(M,k))==R))
 def test_produit_avec_scalaire04(EKxGM):
  k=0
  M=EKxGM.E
  R=np.array(M)*k
  EKxGM.assertTrue(np.all(np.array(produit_matrice_avec_scalaire(M,k))==R))
 def test_produit_avec_scalaire05_matrices_inchangees(EKxGM):
  k=1j
  M=EKxGM.D
  produit_matrice_avec_scalaire(M,k)
  EKxGM.assertTrue(np.all(np.array(M)==EKxGM.E))
 def test_multiplication01_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,multiplication_matrices,EKxGM.B,EKxGM.A)
 def test_multiplication02_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,multiplication_matrices,EKxGM.A,EKxGM.C)
 def test_multiplication03(EKxGM):
  R=np.matrix(EKxGM.C)*np.matrix(EKxGM.A)
  EKxGM.assertTrue(np.all(np.array(multiplication_matrices(EKxGM.C,EKxGM.A))==R))
 def test_multiplication04(EKxGM):
  R=np.matrix(EKxGM.A)*np.matrix(EKxGM.B)
  EKxGM.assertTrue(np.all(np.array(multiplication_matrices(EKxGM.A,EKxGM.B))==R))
 def test_multiplication05_matrices_inchangees(EKxGM):
  a=multiplication_matrices(EKxGM.D,EKxGM.D)
  EKxGM.assertTrue(np.all(np.array(EKxGM.D)==np.array(EKxGM.E)))
 def test_puissance01_assert(EKxGM):
  k=2
  EKxGM.assertRaises(EKxGj,puissance_matrice,EKxGM.A,k)
 def test_puissance02(EKxGM):
  k=0
  R=np.matrix(EKxGM.C)**k
  EKxGM.assertTrue(np.all(np.array(puissance_matrice(EKxGM.C,k))==R))
 def test_puissance03(EKxGM):
  k=2
  R=np.matrix(EKxGM.C)**k
  EKxGM.assertTrue(np.all(np.array(puissance_matrice(EKxGM.C,k))==R))
 def test_puissance04(EKxGM):
  k=5
  R=np.matrix(EKxGM.C)**k
  EKxGM.assertTrue(np.all(np.array(puissance_matrice(EKxGM.C,k))==R))
 def test_puissance05(EKxGM):
  k=10
  R=np.matrix(EKxGM.C)**k
  EKxGM.assertTrue(np.all(np.array(puissance_matrice(EKxGM.C,k))==R))
class FusionTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.BB=[[1,2,1,2],[3,4,3,4]]
  EKxGM.BBB=[[1,2,1,2,1,2],[3,4,3,4,3,4]]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.AC=[[5,3,1,1,1],[0,7,2,2,2],[4,1,3,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,4,5]]
  EKxGM.AD=[[5,3,1,2,3],[0,7,2,3,4],[4,1,3,4,5]]
  EKxGM.ADsep=[[5,3,1],[0,7,2],[4,1,3]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
 def test_fusion01_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,fusion,EKxGM.A,EKxGM.B)
 def test_fusion02(EKxGM):
  EKxGM.assertEqual(fusion(EKxGM.A,EKxGM.C),EKxGM.AC)
 def test_fusion03(EKxGM):
  EKxGM.assertEqual(fusion(EKxGM.A,EKxGM.D),EKxGM.AD)
 def test_fusion04(EKxGM):
  EKxGM.assertEqual(fusion(EKxGM.B,EKxGM.B),EKxGM.BB)
 def test_fusion05(EKxGM):
  EKxGM.assertEqual(fusion(EKxGM.BB,EKxGM.B),EKxGM.BBB)
 def test_separation01(EKxGM):
  B,BB=separation(EKxGM.BBB)
  EKxGM.assertEqual(B,EKxGM.B)
 def test_separation02(EKxGM):
  B,BB=separation(EKxGM.BBB)
  EKxGM.assertEqual(BB,EKxGM.BB)
 def test_separation03(EKxGM):
  B,B2=separation(EKxGM.BB)
  EKxGM.assertEqual(B,EKxGM.B)
 def test_separation04(EKxGM):
  B,B2=separation(EKxGM.BB)
  EKxGM.assertEqual(B2,EKxGM.B)
 def test_separation05(EKxGM):
  EKxGb,B2=separation(EKxGM.AD)
  EKxGM.assertEqual(EKxGb,EKxGM.ADsep)
class EchangeTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.Aech=[[0,7],[5,3],[4,1]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.Cech=[[2,2,2],[1,1,1],[3,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,4,5]]
  EKxGM.Dech=[[3,4,5],[2,3,4],[1,2,3]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
  EKxGM.Fech=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
  EKxGM.G=[[j*i*(-1)**i for j in EKxGn(125)]for i in EKxGn(234)]
 def test_echange01(EKxGM):
  a=echange_lignes(EKxGM.A,0,1)
  EKxGM.assertEqual(EKxGM.A,EKxGM.Aech)
 def test_echange02(EKxGM):
  a=echange_lignes(EKxGM.C,0,1)
  EKxGM.assertEqual(EKxGM.C,EKxGM.Cech)
 def test_echange03(EKxGM):
  a=echange_lignes(EKxGM.D,0,2)
  EKxGM.assertEqual(EKxGM.D,EKxGM.Dech)
 def test_echange04(EKxGM):
  a=echange_lignes(EKxGM.D,2,0)
  EKxGM.assertEqual(EKxGM.D,EKxGM.Dech)
 def test_echange05(EKxGM):
  a=echange_lignes(EKxGM.F,120,120)
  EKxGM.assertEqual(EKxGM.F,EKxGM.Fech)
 def test_cherche_pivot01(EKxGM):
  A=[[1,2,3,4],[3,2,1,4],[1,1,1,4]]
  j=cherche_pivot(A,0)
  EKxGJ=1
  EKxGM.assertEqual(j,EKxGJ)
 def test_cherche_pivot02(EKxGM):
  A=[[1,2,3],[3,2,1],[1,1,1]]
  j=cherche_pivot(A,1)
  EKxGJ=1
  EKxGM.assertEqual(j,EKxGJ)
 def test_cherche_pivot03(EKxGM):
  A=[[1,2,3],[3,2,1],[1,1,1]]
  j=cherche_pivot(A,2)
  EKxGJ=2
  EKxGM.assertEqual(j,EKxGJ)
 def test_cherche_pivot04(EKxGM):
  j=cherche_pivot(EKxGM.G,10)
  EKxGJ=lignes(EKxGM.G)-1
  EKxGM.assertEqual(j,EKxGJ)
 def test_cherche_pivot05(EKxGM):
  j=cherche_pivot(EKxGM.F,10)
  EKxGJ=lignes(EKxGM.F)-1
  EKxGM.assertEqual(j,EKxGJ)
 def test_transvection01(EKxGM):
  A=random_matrix(3,5)
  B=copy.deepcopy(A)
  k,i,alpha=2,1,0.1
  transvection(A,k,i,alpha)
  p_transvection(B,k,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_transvection02(EKxGM):
  A=random_matrix(3,5)
  B=copy.deepcopy(A)
  k,i,alpha=1,2,0.1
  transvection(A,k,i,alpha)
  p_transvection(B,k,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_transvection03(EKxGM):
  A=random_matrix(7,15)
  B=copy.deepcopy(A)
  k,i,alpha=5,0,0.1
  transvection(A,k,i,alpha)
  p_transvection(B,k,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_transvection04(EKxGM):
  A=random_matrix(3,5)
  B=copy.deepcopy(A)
  k,i,alpha=0,0,0.1
  transvection(A,k,i,alpha)
  p_transvection(B,k,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_transvection05(EKxGM):
  A=random_matrix(8,15)
  B=copy.deepcopy(A)
  k,i,alpha=7,7,0.1
  transvection(A,k,i,alpha)
  p_transvection(B,k,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_dilatation01(EKxGM):
  A=random_matrix(3,5)
  B=copy.deepcopy(A)
  i,alpha=1,0.1
  dilatation(A,i,alpha)
  p_dilatation(B,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_dilatation02(EKxGM):
  A=random_matrix(3,5)
  B=copy.deepcopy(A)
  i,alpha=2,0.1
  dilatation(A,i,alpha)
  p_dilatation(B,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_dilatation03(EKxGM):
  A=random_matrix(7,15)
  B=copy.deepcopy(A)
  i,alpha=0,0.1
  dilatation(A,i,alpha)
  p_dilatation(B,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_dilatation04(EKxGM):
  A=random_matrix(3,5)
  B=copy.deepcopy(A)
  i,alpha=0,0
  dilatation(A,i,alpha)
  p_dilatation(B,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
 def test_dilatation05(EKxGM):
  A=random_matrix(8,15)
  B=copy.deepcopy(A)
  i,alpha=7,7
  dilatation(A,i,alpha)
  p_dilatation(B,i,alpha)
  EKxGM.assertTrue(np.all(np.around(A,decimals=5)==np.around(B,decimals=5)))
def p_dilatation(M,i,alpha):
 for k in EKxGn(colonnes(M)):
  M[i][k]*=alpha
def p_transvection(EKxGF,k,i,alpha):
 for j in EKxGn(colonnes(EKxGF)):
  EKxGF[k][j]-=alpha*EKxGF[i][j]
def random_matrix(n,m=EKxGP):
 if m==EKxGP:m=n
 return[[random.random()for j in EKxGn(m)]for i in EKxGn(n)]
def random_col(n):
 return[[random.random()for j in EKxGn(1)]for i in EKxGn(n)]
class PivotTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,4,5]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
 def test_pivot01_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,pivot_de_gauss,EKxGM.A,[1,2,3])
 def test_pivot02_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,pivot_de_gauss,EKxGM.C,EKxGM.B)
 def test_pivot03(EKxGM):
  A=random_matrix(1)
  B=random_col(1)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot04(EKxGM):
  A=random_matrix(2)
  B=random_col(2)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot05(EKxGM):
  A=random_matrix(3)
  B=random_col(3)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot06(EKxGM):
  A=random_matrix(4)
  B=random_col(4)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot07(EKxGM):
  A=random_matrix(6)
  B=random_col(6)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot08(EKxGM):
  A=random_matrix(8)
  B=random_col(8)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot09(EKxGM):
  A=[[delta(i,j)for j in EKxGn(5)]for i in EKxGn(5)]
  B=random_col(5)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot10(EKxGM):
  A=[[delta(i,j)for j in EKxGn(3)]for i in EKxGn(3)]
  B=random_matrix(3)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5)
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5)
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot03(EKxGM):
  A=random_matrix(3)
  B=random_col(3)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
 def test_pivot03(EKxGM):
  A=random_matrix(3)
  B=random_col(3)
  X=np.around(np.matrix(A)**-1*np.matrix(B),decimals=5).reshape(EKxGW(B))
  EKxGJ=np.around(pivot_de_gauss(A,B),decimals=5).reshape(EKxGW(B))
  EKxGM.assertTrue(np.all(EKxGJ==X))
def p_matrice_nulle(n,p):
 return[[0 for j in EKxGn(p)]for i in EKxGn(n)]
def delta(i,j):
 if i==j:return 1
 else:return 0
import numpy.linalg
class DeterminantTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,0,5]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
  EKxGM.zero3=p_matrice_nulle(3,3)
  EKxGM.id=[[delta(i,j)for j in EKxGn(5)]for i in EKxGn(5)]
 def test_determinant01_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,determinant,EKxGM.A)
 def test_determinant02(EKxGM):
  EKxGM.assertEqual(determinant(EKxGM.zero3),0)
 def test_determinant03(EKxGM):
  EKxGM.assertEqual(determinant(EKxGM.id),1)
 def test_determinant04(EKxGM):
  EKxGM.assertEqual(determinant(EKxGM.C),0)
 def test_determinant05(EKxGM):
  EKxGN=np.linalg.det(EKxGM.D)
  EKxGM.assertAlmostEqual(determinant(EKxGM.D),EKxGN)
 def test_determinant06(EKxGM):
  M=random_matrix(3)
  EKxGN=np.linalg.det(M)
  EKxGM.assertAlmostEqual(determinant(M),EKxGN)
 def test_determinant07(EKxGM):
  M=random_matrix(4)
  EKxGN=np.linalg.det(M)
  EKxGM.assertAlmostEqual(determinant(M),EKxGN)
 def test_determinant08(EKxGM):
  M=random_matrix(5)
  EKxGN=np.linalg.det(M)
  EKxGM.assertAlmostEqual(determinant(M),EKxGN)
 def test_determinant09(EKxGM):
  M=random_matrix(8)
  EKxGN=np.linalg.det(M)
  EKxGM.assertAlmostEqual(determinant(M),EKxGN)
 def test_determinant10(EKxGM):
  M=random_matrix(10)
  EKxGN=np.linalg.det(M)
  EKxGM.assertAlmostEqual(determinant(M),EKxGN)
class InversionTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,100]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.C=[[1,1,1],[2,2,2],[3,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,4,50]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
 def test_inversion01_assert(EKxGM):
  EKxGM.assertRaises(EKxGj,inversion,EKxGM.A)
 def test_inversion02(EKxGM):
  M=EKxGM.B
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion03(EKxGM):
  M=EKxGM.D
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion04(EKxGM):
  M=random_matrix(1)
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion05(EKxGM):
  M=random_matrix(2)
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion06(EKxGM):
  M=random_matrix(3)
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion07(EKxGM):
  M=random_matrix(4)
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion08(EKxGM):
  M=random_matrix(5)
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion09(EKxGM):
  M=random_matrix(8)
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
 def test_inversion10(EKxGM):
  M=random_matrix(10)
  EKxGp=np.around(np.matrix(M)**(-1),decimals=4)
  EKxGi=np.around(inversion(M),decimals=4)
  EKxGM.assertTrue(np.all(EKxGi==EKxGp))
class PuissancesTest(unittest.TestCase):
 def setUp(EKxGM):
  EKxGM.A=[[5,3],[0,7],[4,1]]
  EKxGM.B=[[1,2],[3,4]]
  EKxGM.C=[[1,1,1],[2,20,2],[30,3,3]]
  EKxGM.D=[[1,2,3],[2,3,4],[3,4,5]]
  EKxGM.E=copy.deepcopy(EKxGM.D)
  EKxGM.F=[[j*i for j in EKxGn(125)]for i in EKxGn(234)]
 def test_puissance_relative01_assert(EKxGM):
  k=2
  EKxGM.assertRaises(EKxGj,puissance_relative_matrice,EKxGM.A,k)
 def test_puissance_relative02(EKxGM):
  k=0
  R=np.around(np.matrix(EKxGM.C)**k,decimals=5)
  E=np.around(puissance_relative_matrice(EKxGM.C,k),decimals=5)
  EKxGM.assertTrue(np.all(E==R))
 def test_puissance_relative03(EKxGM):
  k=-2
  R=np.around(np.matrix(EKxGM.C)**k,decimals=5)
  E=np.around(puissance_relative_matrice(EKxGM.C,k),decimals=5)
  EKxGM.assertTrue(np.all(E==R))
 def test_puissance_relative04(EKxGM):
  k=5
  R=np.around(np.matrix(EKxGM.C)**k,decimals=5)
  E=np.around(puissance_relative_matrice(EKxGM.C,k),decimals=5)
  EKxGM.assertTrue(np.all(E==R))
 def test_puissance_relative05(EKxGM):
  k=-10
  R=np.around(np.matrix(EKxGM.C)**k,decimals=5)
  E=np.around(puissance_relative_matrice(EKxGM.C,k),decimals=5)
  EKxGM.assertTrue(np.all(E==R))
def p_reseau_electrocinetique():
 R1,R4,R5,R6=[100]*4
 R2,R3=[220]*2
 E=5
 A=[[R1,R2,0,0,0],[0,-R2,R3,R4,0],[0,0,0,-R4,R5+R6],[-1,1,1,0,0],[0,0,-1,1,1]]
 B=[5,0,0,0,0]
 X=np.matrix(A)**-1*np.transpose(np.matrix(B))
 return[X[i]for i in EKxGn(5)]
def p_poulie_a_deux_masses():
 EKxGQ=5e-3
 m1=0.1
 m2=0.2
 R=0.1
 g=9.81
 A=[[EKxGQ,-R,R],[m1*R,1,0],[-m2*R,0,1]]
 B=[0,m1*g,m2*g]
 X=np.matrix(A)**-1*np.transpose(np.matrix(B))
 return[X[i]for i in EKxGn(3)]
EKxGs=EKxGt(np.around(p_reseau_electrocinetique(),decimals=6))
EKxGR=EKxGt(np.around(reseau_electrocinetique(),decimals=6))
EKxGO=EKxGt(np.around(p_poulie_a_deux_masses(),decimals=6))
EKxGD=EKxGt(np.around(poulie_a_deux_masses(),decimals=6))
class PhysiqueTest(unittest.TestCase):
 def test_elec01(EKxGM):
  EKxGM.assertEqual(EKxGR[0:2],EKxGs[0:2])
 def test_elec02(EKxGM):
  EKxGM.assertEqual(EKxGR[2:4],EKxGs[2:4])
 def test_elec03(EKxGM):
  EKxGM.assertEqual(EKxGR[4],EKxGs[4])
 def test_meca01(EKxGM):
  EKxGM.assertEqual(EKxGD[0:2],EKxGO[0:2])
 def test_meca02(EKxGM):
  EKxGM.assertEqual(EKxGD[2],EKxGO[2])
# Created by pyminifier (https://github.com/liftoff/pyminifier)
