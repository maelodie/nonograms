import copy 
from config import *
from methode_incomplete import est_coloriable_rec_2

def colore_ligne(A: list(list()), j : int, index : int):
    """
        A : grille dans son état actuel. A = grille, sequences_lignes, sequencees_colonne
        j : indice de la colonne a colorier
    """
    colonne = [colonne[j] for colonne in A[0]]
    sequence = A[2][j]
    l = len(sequence)
    i = len(colonne) -1 #indice à partir duquel on commence à colorier la ligne
    cases_colorees = []

    for index in range(i+1):
        if colonne[index] == VIDE:
            #Test si elle peut être coloriée en blanc
            colonne[index] = BLANC
            memo = empty_grille(i+1, l+1)
            reponse_b = est_coloriable_rec_2(j, l, sequence, memo, colonne)

            #Test si elle peut être coloriée en noir
            colonne[index] = NOIR
            memo = empty_grille(i+1, l+1)
            reponse_n = est_coloriable_rec_2(j, l, sequence, memo, colonne)

            #réussite du test blanc et pas du test noir
            if reponse_b and not(reponse_n) : 
                colonne[index] = BLANC
                A[0][index][j] =  BLANC
                cases_colorees.append(index)      
            
            #réussite du test noir et pas du test blanc
            if reponse_n and not(reponse_b) :   
                colore_ligne[index] = NOIR
                A[0][index][j] =  NOIR
                cases_colorees.append(index)

            #réussite des deux tests
            if reponse_b and reponse_n :       
                colonne[index] = VIDE
                A[0][index][j] = VIDE
            
            #echec des deux tests
            if not(reponse_b) and not(reponse_n):   
                print("Le puzzle n'a pas de solution")
                return False,A,[]

    return True, A, cases_colorees
