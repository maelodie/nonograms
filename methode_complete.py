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
    while len(lignes_a_voir) != 0 or len(colonnes_a_voir) != 0:
        for i in lignes_a_voir:
            possibility, A_prime, new_colonnes = colore_ligne_rec(A_prime, i, 0, [], {})
         
            if possibility == False:
                return False, (grille_vide(n, m), None, None)
            colonnes_a_voir = colonnes_a_voir + new_colonnes
            lignes_a_voir = [x for x in lignes_a_voir if x != i]

        for j in colonnes_a_voir:
            possibility, A_prime, new_lignes = colore_colonne_rec(A_prime, j, 0, [], {})
            if not possibility:
                return False, (grille_vide(n, m), None, None)
            lignes_a_voir = lignes_a_voir + new_lignes  
            colonnes_a_voir = [x for x in colonnes_a_voir if x!=j]

    for i in range(n):
        for j in range(m):
            if A_prime[0][i][j] == VIDE:
                return None, A_prime #parce qu'on ne sait pas : None = on ne sait pas
            
    return True, A_prime

def prochaine_case_indeterminee(grille,k) :
    """
    Determine k', le numéro de la premiere case VIDE tel que k' > k
    
    Parameters
    ----------
    - grille : La grille dans son état actuel
    - k : numero de la case ou on se trouve

    Returns
    -------
    - k' :
        numéro de la premiere case vide situé apres k
    """
    nb_lignes = len(grille)
    nb_colonnes= len(grille[0])

    i = k // nb_colonnes
    j = k % nb_colonnes

    for p in range(i,nb_lignes):
        for q in range(j,nb_colonnes):
            if (grille[p][q] == VIDE):
                return p*nb_colonnes+q
    return nb_lignes*nb_colonnes

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
    b, A:
        - True si le coloriage est possible, False sinon
        - A : La grille obtenue
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
    # k_prime = trouvek(A_prime, i,j,m,n)
    k_prime = prochaine_case_indeterminee(copy.deepcopy(A_prime[0]),k)
    return (enum_rec(A_prime, k_prime, BLANC) or enum_rec(A_prime, k_prime, NOIR))

def enumeration(A : list(list())) :
    """
    """
    possible, A_prime = coloration(A)

    if possible == True :
        return True, A_prime
    
    if possible == False :
        return False, A_prime
    
    # k = prochaine_case_indeterminee(A,A_prime, 0)
    n = len(A[0])
    m =  len(A[0][0])
    k = prochaine_case_indeterminee(copy.deepcopy(A_prime[0]),0)
    possible_b, A_prime_b = enum_rec(A_prime,k,BLANC)
    if possible_b :
        return possible_b, A_prime_b
    
    possible_n, A_prime_n = enum_rec(A_prime,k,NOIR)
    if possible_n:
        return possible_n, A_prime_n
    
    return False, A_prime

def propagation_complete(src) :
    """
    Affiche une visualisation de la grille apres la coloration selon une instance

    Parameters
    ----------
    - src : fichier source de l'instance a représenté
    """
    A =  lire_instance(src)
    ok,res = enumeration(A)
    filename = src + "complete.jpeg"
    if ok :
        print("Le puzzle " + src + " a une solution")
        dessin(res[0],filename)
    if ok == False :
        print("Le puzzle n'a pas de solution")
    if ok == None :
        print("Nous pouvons rien déduire")
