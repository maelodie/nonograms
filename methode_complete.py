import copy
from config import *
from methode_incomplete import colore_ligne_rec, colore_colonne_rec, coloration

def colorier_et_propager(A: list(list()), i : int, j : int, c):
    """
    Colorie une grille partiellement coloriée, en prenant en compte les séquences des lignes, et celles des colonnes.

    Parameters
    ----------
    A : La grille dans son état actuelle. A = grille, sequences_lignes, sequences_colonnes
    i : ligne de la case par laquelle on commence a colorié
    j : colonne de la case par laquelle on commence a colorié
    c : la couleur avec laquelle on colorie la case (i,j)

    Returns
    -------
    (b, A_prime)
    -  b : 
        True si la grille est coloriable, None si nous pouvons rien déduire, False sinon
    - A_prime :
        La grille apres la coloration, grille vide sinon.
    """
    A_prime = copy.deepcopy(A) #O(nm) parce qu'il faut parcourir chaque élément de A pour créer une nouvelle copie
    n = len(A[0])
    m = len(A[0][0])
    A_prime[0][i][j] = c       # on colorie la case (i,j) avec la couleur c
    lignes_a_voir = [i]  # comme dans le pseudo-code
    colonnes_a_voir = [j] 
    while len(lignes_a_voir) != 0 and len(colonnes_a_voir) != 0:
        for i in lignes_a_voir:
            possibility, A_prime, new_colonnes = colore_ligne_rec(A_prime, i, 0, [], {})
            print("check")
            if possibility == False:
                return False, (grille_vide(n, m), None, None)
            colonnes_a_voir = colonnes_a_voir + new_colonnes
            lignes_a_voir.remove(i)
        print("fin")
        for j in colonnes_a_voir:
            possibility, A_prime, new_lignes = colore_colonne_rec(A_prime, j, 0, [], {})
            if not possibility:
                return False, (grille_vide(n, m), None, None)
            lignes_a_voir = lignes_a_voir + new_lignes
            colonnes_a_voir.remove(j)  
   
    for i in range(n):
        for j in range(m):
            if A_prime[0][i][j] == VIDE:
                return None, A_prime #parce qu'on ne sait pas : None = on ne sait pas
            
    return True, A_prime

def prochaine_case_indeterminee(grille, k):
    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])

    for i in range(k + 1, nb_lignes * nb_colonnes):
        ligne = i // nb_colonnes
        colonne = i % nb_colonnes

        if grille[ligne][colonne] == VIDE:
            return i
    
    return nb_colonnes * nb_lignes

def enum_rec(A : list(list()), k : int, c) :
    """
    Enumere les coloriages potentiels de la grille A si la case k est de couleur c.
    
    Parameters 
    ---------
    A : La grille dans son état actuelle. A = grille, sequences_lignes, sequences_colonnes
    k : indice de la case a colorié
    c : couleur avec laquelle colorié la case k

    Returns 
    -------

    """
    n = len(A[0])               # nb_lignes 
    m = len(A[0][0])            # nb_colonnes 

    # cas de base
    if k == n*m :
        return True, A
    
    i  = k // m      # indice de la ligne de la case k
    j = k % m       # indice de la colonne de la case k

    possible, A_prime = colorier_et_propager(A, i, j, c)
    
    if possible == True:
        return True, A_prime
    
    if possible == False:
        return False, (grille_vide(n,m), None, None)
        
    #détermination de la prochaine case
    k_prime = prochaine_case_indeterminee(A_prime[0], k)
    print(k_prime)

    return enum_rec(A_prime, k_prime, BLANC) or enum_rec(A_prime, k_prime, NOIR)

def enumeration(A : list(list())) :
    possible, A_prime = coloration(A)
    if possible == False:
        return False, A
    
    essai_blanc, A_prime2 = enum_rec(A_prime, 0, NOIR)
    if essai_blanc:
        return True, A_prime2
    
    essai_noir, A_prime3 = enum_rec(A_prime, 0, NOIR)
    if essai_noir:
        return True, A_prime3

    return False, A
