# La complexité temporelle pourrait être optimisée en rendant les fonctions colore_ligne et colore_colonne itératives. 
# Dans le pseudo-code fourni, il est indiqué que ces deux fonctions sont réalisées par récurrence. 
# Par conséquent, nous avons conservé cette version dans le fichier 'methode_incomplete.py'. 

from methode_incomplete import est_coloriable_rec_2
from config import *
import copy

def colore_ligne_rec(A: list(list()), i: int, index : int, cases_colorees : list(), memoisation):
    """
    Colorie un max de cases de la ligne i de A
    A : La grille dans son état actuelle. A = grille, sequences_lignes, sequences_colonnes
    i : la ligne a colorié
    index : index de la case avec laquelle on commence
    cases_colorees : liste des indices des cases qu'on colorie
    memoisation : on garde pour la coherence avec le reste du code en cas de testage
    """
    ligne = copy.deepcopy(A[0][i])
    sequence = copy.deepcopy(A[1][i])
    j = len(ligne) - 1    # nb_colonnes de la ligne a coloriée
    l = len(sequence)     # nombre de blocs dans la séquence da la ligne i
    cases_colorees = []    # liste des indices des cases colorees    
      
    for index in range(j+1):
        # La case ne doit pas être encore coloriée
        if ligne[index] == VIDE :
            # Tester si elle peut être coloriée en blanc (la colorier en blanc, et tester si la ligne i a une réponse positive) :
            ligne[index] = BLANC
            memo =  grille_vide(j+1,l+1)
            reponse_b  = est_coloriable_rec_2(j, l, sequence, memo, ligne)

            # Tester de même si elle peut être coloriée en noir :
            ligne[index] = NOIR
            memo =  grille_vide(j+1,l+1)
            reponse_n  = est_coloriable_rec_2(j, l, sequence, memo, ligne)

            if reponse_b and not(reponse_n) :   # le test blanc réussit mais le test noir échoue
                ligne[index] = BLANC
                A[0][i][index] =  BLANC
                cases_colorees.append(index)      # mis a jour des indices des cases colorées
            
            if reponse_n and not(reponse_b) :   # le test noir réussit mais le test blanc échoue
                ligne[index] = NOIR
                A[0][i][index] =  NOIR
                cases_colorees.append(index)
 
            if reponse_b and reponse_n :        # les 2 tests reussissent, on peut rien déduire sur cette case
                ligne[index] = VIDE
                A[0][i][index] = VIDE

            if not(reponse_b) and not(reponse_n):   # les 2 tests echouent
                print("Le puzzle n'a pas de solution")
                return False,A,[]

    return True,A,cases_colorees

def colore_colonne_rec(A: list(list()), j : int, index : int, cases_colorees : list(), memoisation):
    """
    Colorie un max de cases de la colonne j de A
    A : grille dans son état actuel. A = grille, sequences_lignes, sequencees_colonne
    j : indice de la colonne a colorier
    index : index de la case avec laquelle on commence
    cases_colorees : liste des indices des cases qu'on colorie
    memoisation : on garde pour la coherence avec le reste du code en cas de testage
    """
    colonne = [colonne[j] for colonne in A[0]]
    sequence = A[2][j]
    l = len(sequence)
    i = len(colonne) #indice à partir duquel on commence à colorier la ligne
    cases_colorees = []

    for index in range(i):
        if colonne[index] == VIDE:
            #Test si elle peut être coloriée en blanc
            colonne[index] = BLANC
            memo = grille_vide(i, l+1)
            reponse_b = est_coloriable_rec_2(i - 1, l, sequence, memo, colonne)

            #Test si elle peut être coloriée en noir
            colonne[index] = NOIR
            memo = grille_vide(i, l+1)
            reponse_n = est_coloriable_rec_2(i - 1 , l, sequence, memo, colonne)

            #réussite du test blanc et pas du test noir
            if reponse_b and not(reponse_n) : 
                colonne[index] = BLANC
                A[0][index][j] =  BLANC
                cases_colorees.append(index)      
            
            #réussite du test noir et pas du test blanc
            if reponse_n and not(reponse_b) :   
                colonne[index] = NOIR
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

