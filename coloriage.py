import numpy as np
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

def colore_ligne(A: list(list()), index: int):
    """
        Détermine si la ligne d'indice index est coloriable et renvoie la grille augmentée de ce nouveau coloriage
    """
    new_A = A

    return False, new_A 
def coloration(A: list(list())):
    A_prime = A.copy(A) #O(nm) parce qu'il faut parcourir chaque élément de A pour créer une nouvelle copie
    ligne_a_voir = [0 for i in range(len(A))]
    colonnes_a_voir = [0 for i in range(len(A[0]))]#en supposant que les lignes ont toutes le même nombre de colonnes

    while len(ligne_a_voir) != 0 and len(colonnes_a_voir) != 0:
        for i in ligne_a_voir:
            possibility, A_prime = colore_ligne(A_prime, i)
            if not possibility:
                return False, empty_grille()