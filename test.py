from coloriage import est_coloriable_rec
from config import *

##################
# Test cases Q4
##################

M = 6
memo = creer_memo(M,M-1,VIDE) # matrice de mémoisation

# j = 5, l = 0, s = []
assert est_coloriable_rec(M-1, 0, [], memo) == True

# j = 3, l = 2, s = [2, 1]
assert est_coloriable_rec(3, 2, [2, 1], memo) == False

# # j = 2, l = 2, s = [3, 2, 1]
assert est_coloriable_rec(2, 2, [3, 2, 1], memo) == False

# # j = 3, l = 2, s = [3, 2, 1]
assert est_coloriable_rec(3, 2, [3, 2, 1], memo) == False

# # j = 5, l = 3, s = [1, 1, 1]
assert est_coloriable_rec(5, 3, [1, 1, 1], memo) == True

# # j = 3, l = 1, s = [3]
assert est_coloriable_rec(3, 1, [3], memo) == True

# # j = 5, l = 2, s = [3, 2, 1]
assert est_coloriable_rec(5, 2, [3, 2, 1], memo) == False

print("Tous les testes sont passés !")
# ##################
