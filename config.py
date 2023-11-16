BLANC = 1
VIDE = 0
NOIR = -1

import numpy as np
def creer_memo(n, m, etat) :
    """
    Créer une matrice pour la mémoisastion

    Parameteres
    -----------
    - n : nombre de lignes
    - m : nombre de colonnes
    - etat : état d'une case (VIDE, BLANC OU NOIR)

    Returns
    -------
    Une matrice nxm initialisé a v
    """
    return np.full((n,m), etat)