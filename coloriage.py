import numpy as np
from config import *

def est_coloriable_rec(j: int, l: int, sequence: list, memo: np.array):
    """
    Vérifie récursivement si une séquence peut être coloriée jusqu'à la colonne j dans la ligne l, avec mémoisation .

    Parameters
    ----------
    - j : Nombre de colonnes de la ligne en cours de test.
    - l : Nombre actuel de cases dans le bloc de la séquence.
    - sequence : Séquence à vérifier pour la colorabilité.
    - memo : Matrice de mémoisation

    Returns
    -------
    - True si la ligne est coloriable jusqu'à la colonne j, False sinon.
    """
    if memo[j,l] != VIDE :
        return memo[j,l] # on connaît déja la valeur grâce a la mémoisation
    
    # Cas de base : la séquence est vide, donc la coloration est toujours possible
    if l == 0:
        memo[j,l] = True
        return True
    
    # Cas où il y a au moins un bloc dans la séquence
    if l >= 1:
        # Cas 2a : la séquence dépasse le nombre de colonnes j
        if j < sequence[l-1]:
            memo[j,l] = False
            return False
        
        # Cas 2b : il ne reste qu'une seule case disponible sur la ligne
        if j == sequence[l-1]:
            if(l==1) :
                memo[j,l] = True
                return True
            else :
                memo[j,l] = False
                return False
        
        # Cas 2c : relation de récurrence
        memo[j,l] = est_coloriable_rec(j-1, l, sequence, memo) or est_coloriable_rec(j-sequence[l-1]-1, l-1, sequence, memo)
        return memo[j,l]

