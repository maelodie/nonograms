from  methode_incomplete import est_coloriable_rec, est_coloriable_rec_2, colore_ligne_rec
from config import *

##################
# Test cases Q4
##################
M = 6
seq_1 = []
seq_2 = [1,2,1]
seq_3 = [2,2]
seq_4 = [6]
seq_5 = [4,2]
seq_6 = [3,2,1]
seq_7 = [1,1,1,1,1,1]


memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec(M-1, 0, seq_1, memo) == True
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec(M-1, 3, seq_2, memo) == True
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec(M-1, 2, seq_3, memo) == True
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec(M-1, 1, seq_4, memo) == True
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec(M-1, 2, seq_5, memo) == False
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec(M-1, 3, seq_6, memo) == False
memo = creer_tab(M, M+1,VIDE)
assert est_coloriable_rec(M-1, 6, seq_7, memo) == False

print("Tous les testes sont passés pour est_coloriable_rec !")
##################

##################
# Test cases Q5
##################
M = 4 


seq_1 = []
cases_colorees = [BLANC, BLANC, BLANC, BLANC]
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec_2(M-1, 0, seq_1, memo, cases_colorees) == True
cases_colorees = [BLANC, BLANC, NOIR, BLANC]
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec_2(M-1, 0, seq_1, memo, cases_colorees) == False

seq_2 = [6]
cases_colorees = [VIDE, BLANC, NOIR, BLANC]
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec_2(M-1, 1, seq_2, memo, cases_colorees) == False

seq_3 = [3]
cases_colorees = [BLANC, BLANC, NOIR, BLANC]
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec_2(M-1, 1, seq_3, memo, cases_colorees) == False

seq_4 = [2]
cases_colorees = [NOIR, NOIR, BLANC, VIDE]
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec_2(M-1, 1, seq_4, memo, cases_colorees) == True

seq_5 = [2, 1]
cases_colorees = [VIDE, VIDE, BLANC, NOIR]
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec_2(M-1, 2, seq_5, memo, cases_colorees) == True

seq_6 = [3]
cases_colorees = [BLANC, VIDE, VIDE, VIDE, VIDE]
memo = creer_tab(5, 5,VIDE)
assert est_coloriable_rec_2(4, 1, seq_6, memo, cases_colorees) == True

seq_7 = [3]
cases_colorees = [VIDE, VIDE, NOIR, BLANC]
memo = creer_tab(M, M,VIDE)
assert est_coloriable_rec_2(M-1, 1, seq_7, memo, cases_colorees) == True

print("Tous les testes sont passés pour est_coloriable_rec_2 !")
##################

##################
# Test cases for colore_ligne_rec
##################
fichier_instance = "instances/0.txt"
A = lire_instance(fichier_instance)
index = 0
cases_colorees = []
b, m, cases = colore_ligne_rec(A, 0, index, cases_colorees)
assert b == True
assert cases == [2]

A = lire_instance(fichier_instance)
index = 0
cases_colorees = []
b, m, cases = colore_ligne_rec(A, 1, index, cases_colorees)
assert b == True
assert cases == [0,1,2,3,4]

A = lire_instance(fichier_instance)
index = 0
cases_colorees = []
b, m, cases = colore_ligne_rec(A, 2, index, cases_colorees)
assert b == True
assert cases == [0,1,2,3,4]

A = lire_instance(fichier_instance)
index = 0
cases_colorees = []
b, m, cases = colore_ligne_rec(A, 3, index, cases_colorees)
assert b == True
assert cases == [2]

print("Tous les testes sont passés pour colore_ligne_rec !")
#################

