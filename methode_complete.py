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
    A[0][i][j] = c       # on colorie la case (i,j) avec la couleur c
    lignes_a_voir = [i]  # comme dans le pseudo-code
    colonnes_a_voir = [j] 

    while len(lignes_a_voir) != 0 and len(colonnes_a_voir) != 0:
        for i in lignes_a_voir:
            possibility, A_prime, new_colonnes = colore_ligne_rec(A_prime, i, 0, [])
            if not possibility:
                return False, (grille_vide(n, m), None, None)
            colonnes_a_voir = list(set(colonnes_a_voir + new_colonnes))
            lignes_a_voir.remove(i)
        
        for j in colonnes_a_voir:
            possibility, A_prime, new_lignes = colore_colonne_rec(A_prime, j, 0, [])
            #possibility, A_prime, new_lignes = colore_colonne(A_prime, j)
            if not possibility:
                return False, (grille_vide(n, m), None, None)
            lignes_a_voir = list(set(lignes_a_voir + new_lignes))
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
    

def trouvek(A,i,j,M,N):
    for i2 in range(i,N):
        for j2 in range(j,M):
            if (A[0][i2][j2] == VIDE):
                return M*i2+j2
    return M*N

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

    possible, A_prime = colorier_et_propager(A, i,j,c)
  
    if possible :
        return True,A_prime
    if possible == False:
        return False, (grille_vide(n,m), None, None)
  
    k_prime = trouvek(A_prime, i, j, m , n)
    print(k_prime)
    return enum_rec(A_prime, k_prime, BLANC) or enum_rec(A_prime, k_prime, NOIR)

def enumeration(A : list(list())) :
    possible, A_prime = coloration(A)

    if possible == False :
        n = len(A[0])               # nb_lignes 
        m = len(A[0][0])            # nb_colonnes
        return False, (grille_vide(n,m), None, None)
    
    return enum_rec(A_prime,0, BLANC) or enum_rec(A_prime,0, BLANC)
