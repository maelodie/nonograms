from config import *

def is_case_possible(j : int, l: int, s: list):
    """
    j : Nombre de colonnes de la ligne testée
    l : Nombre de cases actuel dans le bloc de la sequence
    s : séquence à vérifier (si elle est coloriable)
    """
    if l == 0:
        return True
    
    if l >= 1:
        if j < s[l-1]:
            return False
        
        if j == s[l-1]:
            if l == 1:
                return True
            else:
                return False
        
        if j > s[l-1]:
            return is_case_possible(j-1, l, s) or is_case_possible(j-s[l-1]-1, l-1, s)
    
##### TEST CASES #####

#j = 5, l = 0, s = []
assert(is_case_possible(5, 0, []) == True) 

#j = 2, l = 2, s = [3, 2, 1]
assert(is_case_possible(2, 2, [3, 2, 1]) == False)

#j = 3, l = 2, s = [3, 2, 1]
assert(is_case_possible(3, 2, [3, 2, 1]) == False)

#j = 5, l = 3, s = [1, 1, 1]
assert(is_case_possible(5, 3, [1, 1, 1]) == True)

#j = 3, l = 1, s = [3]
assert(is_case_possible(3, 1, [3]) == True)

#j = 5, l = 2, s = [3, 2, 1]
assert(is_case_possible(5, 2, [3, 2, 1]) == False)
