from config import *

def is_case_possible(j : int, l: int, s: list):
    """
    j : Nombre de colonnes de la ligne testée
    l : Nombre de cases actuel dans le bloc de la sequence
    s : séquence à vérifier (si elle est coloriable)
    """
    if l == 0: # cas 1 : la séquence est vide donc T(j, l) est toujours vraie
        return True
    
    if l >= 1:
        if j < s[l-1]: # cas 2a : la séquence dépasse le nombre de colonnes de j
            return False
        
        if j == s[l-1]: # cas 2b : il ne reste plus qu'une seule case disponible sur la ligne
            if l == 1:
                return True
            else:
                return False
        
        if j > s[l-1]: # cas 2c : relation de récurrence
            return is_case_possible(j-1, l, s) or is_case_possible(j-s[l-1]-1, l-1, s)

def is_case_possible2(C: list, j : int, l: int, s: list): 
    """
    C : liste contenant la ligne primitive (ligne déjà coloriée) pour déterminer la possibilité de la séquence
    j : Nombre de colonnes de la ligne testée
    l : Nombre de cases actuel dans le bloc de la sequence
    s : séquence à vérifier (si elle est coloriable)
    """
    if l == 0: # cas 1 : la séquence est vide donc T(j, l) est toujours vraie
        return True
    
    if l >= 1:
        if j < s[l-1]: # cas 2a : la séquence dépasse le nombre de colonnes de j
            return False
        
        if j == s[l-1]: # cas 2b : il ne reste plus qu'une seule case disponible sur la ligne
            if l == 1 and C[j-1] != NOIR:
                return True
            else:
                return False
        
        if j > s[l-1]: # cas 2c : relation de récurrence
            return is_case_possible2(C, j-1, l, s) or is_case_possible2(C, j-s[l-1]-1, l-1, s)

##### TEST CASES Q4 #####

    #j = 5, l = 0, s = []
    assert(is_case_possible(5, 0, []) == True) 

    #j = 3, l = 2, s = [2, 1]
    assert(is_case_possible(3, 2, [2, 1]) == False)

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

##### TEST CASES Q5 #####

#Easy test cases

assert(is_case_possible2([BLANC, BLANC, NOIR, NOIR, BLANC, BLANC], 6, 2, [3, 1]) == False)

assert(is_case_possible2([BLANC, BLANC, NOIR, NOIR, BLANC, BLANC], 6, 2, [1, 1]) == True)