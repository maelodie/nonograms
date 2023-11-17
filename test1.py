from coloriage import est_coloriable_rec
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


memo = creer_memo(M, M,VIDE)
assert est_coloriable_rec(M-1, 0, seq_1, memo) == True
memo = creer_memo(M, M,VIDE)
assert est_coloriable_rec(M-1, 3, seq_2, memo) == True
memo = creer_memo(M, M,VIDE)
assert est_coloriable_rec(M-1, 2, seq_3, memo) == True
memo = creer_memo(M, M,VIDE)
assert est_coloriable_rec(M-1, 1, seq_4, memo) == True
memo = creer_memo(M, M,VIDE)
assert est_coloriable_rec(M-1, 2, seq_5, memo) == False
memo = creer_memo(M, M,VIDE)
assert est_coloriable_rec(M-1, 3, seq_6, memo) == False
memo = creer_memo(M, M+1,VIDE)
assert est_coloriable_rec(M-1, 6, seq_7, memo) == False

print("Tous les testes sont passés !")
# ##################