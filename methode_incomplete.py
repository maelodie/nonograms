import copy
from config import *

def est_coloriable_rec(j: int, l: int, sequence: list, memo: np.array):
    """
    Vérifie récursivement si une séquence peut être coloriée jusqu'à la colonne j dans la ligne l, avec mémoisation .

    Parameters
    ----------
    - j : Nombre de colonnes de la ligne en cours de test. (j = M-1)
    - l : Nombre actuel de cases dans le bloc de la séquence. (l premiers bloques de la ligne l ?)
    - sequence : Séquence à vérifier pour la colorabilité.
    - memo : Matrice de mémoisation, memo[j][l] = T(j,l)

    Returns
    -------
    - True si la ligne est coloriable jusqu'à la colonne j, False sinon.
    """
    if memo[j][l] != VIDE :
        return memo[j][l] # On connaît déja la valeur grâce a la mémoisation
    
    # Cas de base : la séquence est vide, donc la coloration est toujours possible
    if l == 0:
        memo[j][l] = True
        return True
    
    # Cas où il y a au moins un bloc dans la séquence
    if l >= 1:
        # Cas 2a : la séquence dépasse le nombre de colonnes j
        if j < sequence[l-1] - 1:
            memo[j][l] = False
            return False
        
        # Cas 2b :
        if j == sequence[l-1] - 1:
            if(l==1) :          # nb_colonnes == sequence[l-1]
                memo[j][l] = True
                return True
            else :
                memo[j][l] = False
                return False
        
        # Cas 2c : relation de récurrence
        memo[j][l] = est_coloriable_rec(j-1, l, sequence, memo) or est_coloriable_rec(j-sequence[l-1]-1, l-1, sequence, memo)
        return memo[j][l]
    
def check_bloc(i,j,etat,cases_colorees):
    """
    Verifie si les cases entre les colonnes i et j sont du même etat .
    Parameters
    ----------
    - i : Numéro de colonne de début
    - j : Numéro de colonne de fin
    - etat : etat de case qu'on souhaite vérifier
    - cases_colorees : liste des cases deja coloriées en blanc ou en noir

    Returns
    -------
    - True s'il existe au moins une case etat entre les colonnes i et j, False sinon.
    """
    return all(cases_colorees[k] == etat for k in range(i,j+1))

def est_coloriable_rec_2(j: int, l: int, sequence: list, memo: np.array, cases_colorees : list):
    """
    Vérifie récursivement si une séquence peut être coloriée jusqu'à la colonne j dans la ligne l, avec mémoisation.
    Avec certaines cases déja coloriées en blanc ou en noir.

    Parameters
    ----------
    - j : Nombre de colonnes de la ligne en cours de test.
    - l : Nombre actuel de cases dans le bloc de la séquence.
    - sequence : Séquence à vérifier pour la colorabilité.
    - memo : Matrice de mémoisation, memo[j][l] = T(j,l)
    - cases_colorees : liste des cases deja coloriées en blanc ou en noir

    Returns
    -------
    - True si la ligne est coloriable jusqu'à la colonne j, False sinon.
    """
    if memo[j][l] != VIDE :
        return memo[j][l] # on connaît déja la valeur grâce a la mémoisation
    
    # Cas de base : la séquence est vide, donc la ligne ne doit pas contenir case noire
    if l == 0:
        memo[j][l] = (check_bloc(0, j, BLANC, cases_colorees) or check_bloc(0,j,VIDE,cases_colorees))
        return memo[j][l]
    
    # Cas où il y a au moins un bloc dans la séquence
    if l >= 1:
        # Cas 2a : la séquence dépasse le nombre de colonnes j, toujous faux
        if j < sequence[l-1] - 1:
            memo[j][l] = False
            return False
        
        # Cas 2b : 
        if j == sequence[l-1] - 1 :
            if(l==1) :
                memo[j][l] = (check_bloc(0, j, NOIR, cases_colorees) or check_bloc(0, j, VIDE, cases_colorees))
                return memo[j][l]
        
        # Cas 2c : relation de récurrence
        # Ici il faut couvrir tous les cas :
        # 1) la premiere case traitée, aka la derniere, cases_colorées[j] peut être blanche, on traite récursivement pour verifier si colorable sur les j-1 colonnes
        # 2) si elle est noire, on a deja colorié dernier bloque de la sequénce.
            # a) il faut s'assurer que il ya une suite de cases noires qui correspondent a s[l-1]
            # b) il faut verifier qu'au moins la case avant le début de dernier bloque est blanche donc la case j - s[l-1] -1
            # c) si c'est bon, verifier que la sequence est coloriable sur les colonnes entre 0 et j - s[l-1] -1
        else:
            if cases_colorees[j] == BLANC or cases_colorees[j] == VIDE:                   # cas 1
                possible = est_coloriable_rec_2(j-1, l, sequence, memo, cases_colorees)
                memo[j][l] = possible
                return memo[j][l]
            else :                                                                  # cas 2 la case j est noire
                if check_bloc(j-sequence[l-1]+1, j, NOIR, cases_colorees) :         # cas 2.a)
                    if cases_colorees[j - sequence[l-1]] == BLANC or cases_colorees[j - sequence[l-1]] == VIDE:                 # cas 2.b)
                            possible = est_coloriable_rec_2(j - sequence[l-1]-1, l-1, sequence, memo, cases_colorees)
                            memo[j][l] = possible
                            return memo[j][l]
                else :
                    memo[j][l] = False
                    return False

                    return False

def colore_ligne(A: list(list()), i: int, index):
    """
    Colorie par récurrence un max de cases de la ligne i de A
    A : La grille dans son état actuelle. A = grille, sequences_lignes, sequences_colonnes
    i : la ligne a colorié
    index : index de la case avec laquelle on commence
    """
    ligne = copy.deepcopy(A[0][i])
    sequence = A[1][i]
    j = len(ligne[i]) - 1 # nb_colonnes de la ligne a coloriée
    l = len(sequence)     # nombre de blocs dans la séquence da la ligne i
    cases_colorees = []   # liste des indices des cases colorées de la ligne i
    memoisation = creer_tab(j,l, VIDE)

    if memoisation[j][l] != VIDE :
        return memo[j][l]
    
    # Cas de base : # il ne reste  aucune case vide a coloré
    if not(check_bloc(index, j, VIDE)) :
        possible = est_coloriable_rec_2(j, l, sequence, memo, ligne)
        return possible, A, cases_colorees

    # La case ne doit pas être encore coloriée
    if ligne[index] == VIDE :
        # Tester si elle peut être coloriée en blanc (la colorier en blanc, et tester si la ligne i a une réponse positive) :
        ligne[index] = BLANC
        memo =  creer_tab(j,l,VIDE)
        reponse_b  = est_coloriable_rec_2(j, l, sequence, memo, ligne)

        # Tester de même si elle peut être coloriée en noir :
        ligne[index] = NOIR
        memo =  creer_tab(j,l,VIDE)
        reponse_n  = est_coloriable_rec_2(j, len(sequence), sequence, memo, ligne)

        if reponse_b and not(reponse_n) :   # le test blanc réussit mais le test noir échoue
            A[0][i][index] =  BLANC
            cases_colorees.append(index)      # mis a jour des indices des cases colorées
            memoisation[j][l] = colore_ligne(A,i,index+1)
            
        if reponse_n and not(reponse_b) :   # le test noir réussit mais le test blanc échoue
            A[0][i][index] =  NOIR
            cases_colorees.append(index)
            memoisation[j][l] = colore_ligne(A,i,index+1)

        if reponse_b and reponse_n :        # les 2 tests reussissent, on peut rien déduire sur cette case
            A[0][i][index] =  VIDE
            cases_colorees.append(index)
            memoisation[j][l] = colore_ligne(A,i,index+1)


        if not(reponse_b) and not(reponse_n):   # les 2 tests echouent
            print("Le puzzle n'a pas de solution")
            return False,A,[]

        return True,A,cases_colorees
    
    # Cas ou la case est deja colorée
    else :
        colore_ligne(A,i,index+1)


def colore_colonne(A: list(list()), index: int):
    """
        Détermine si la colonne d'indice index est coloriable et renvoie la grille augmentée de ce nouveau coloriage
    """
    new_A = A
    new_lignes = []
    return False, new_A , new_lignes


def coloration(A: list(list())):
    n = len(A)
    m = len(A[0])
    A_prime = copy.deepcopy(A) #O(nm) parce qu'il faut parcourir chaque élément de A pour créer une nouvelle copie
    lignes_a_voir = [i for i in range(n)]
    colonnes_a_voir = [i for i in range(m)]#en supposant que les lignes ont toutes le même nombre de colonnes

    while len(lignes_a_voir) != 0 and len(colonnes_a_voir) != 0:
        for i in lignes_a_voir:
            possibility, A_prime, new_colonnes = colore_ligne(A_prime, i)
            if not possibility:
                return False, empty_grille(n, m)
            colonnes_a_voir = colonnes_a_voir + new_colonnes
            lignes_a_voir.remove(i)

        for j in colonnes_a_voir:
            possibility, A_prime, new_lignes = colore_colonne(A_prime, j)
            if not possibility:
                return False, empty_grille(n, m)
            lignes_a_voir = lignes_a_voir + new_lignes
            colonnes_a_voir.remove(j)
    
    for i in range(n):
        for j in range(m):
            if A_prime[i][j] == VIDE:
                return None, A_prime #parce qu'on ne sait pas : None = on ne sait pas

    return True, A_prime

