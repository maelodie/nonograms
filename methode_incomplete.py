import copy
from config import *

def est_coloriable_rec(j: int, l: int, sequence: list, memo: list):
    """
    Vérifie récursivement si les l premieres bloques d'une séquence peuvent être coloriées jusqu'à la colonne j dans la ligne, avec mémoisation .

    Parameters
    ----------
    - j : Nombre de colonnes de la ligne en cours de test. (j = M-1)
    - l : Nombre actuel de bloques de la séquence. 
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
    
def est_coloriable_rec_2(j: int, l: int, sequence: list, memo: list, cases_colorees : list):
    """
    Vérifie récursivement si les l premieres bloques d'une séquence peuvent être coloriées jusqu'à la colonne j dans la ligne, avec mémoisation.
    Avec certaines cases déja coloriées en blanc ou en noir.

    Parameters
    ----------
    - j : Nombre de colonnes de la ligne en cours de test.
    - l : Nombre actuel de bloques de la séquence. s
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
        memo[j][l] = (NOIR not in cases_colorees[0:j+1])
        return memo[j][l]
    
    # Cas où il y a au moins un bloc dans la séquence
    if l >= 1:
        # Cas 2a : la séquence dépasse le nombre de colonnes j, toujous faux
        if j < sequence[l-1] - 1:
            memo[j][l] = False
            return False
        
        # Cas 2b :
        if j == sequence[l-1] - 1 :  
            if(l==1) :              # le nombre de cases correspond a la taille de l'unique bloque (on doit avoir NOIR ou VIDE)
                memo[j][l] = (BLANC not in cases_colorees[0:j+1])
                return memo[j][l]
        
        # Cas 2c : relation de récurrence
        # Ici il faut couvrir tous les cas :
        # 1) la premiere case traitée, aka la derniere, cases_colorées[j] peut être blanche ou vide, on traite récursivement pour verifier si colorable sur les j-1 colonnes 
            # a) si possible, on retour VRAI 
        # 2) si elle est noire, on a deja colorié la derniere case du dernier bloque de la sequénce.
            # a) il faut s'assurer que il ya une suite de cases noires ou vides qui correspondent a s[l-1] 
            # b) il faut verifier qu'au moins la case avant le début de dernier bloque est blanche donc la case j - s[l-1] -1
            # c) si c'est bon, verifier que la sequence est coloriable sur les colonnes entre 0 et j - s[l-1] -1
        else:
            possible = False
            if cases_colorees[j] == BLANC or cases_colorees[j] == VIDE:                   # cas 1
                possible = est_coloriable_rec_2(j-1, l, sequence, memo, cases_colorees)
           
            if possible :
                memo[j][l] = possible
                return memo[j][l]
            else :                                                                                                                            # cas 2 la case j est noire
                if (BLANC not in cases_colorees[j-sequence[l-1]+1:j+1]) :                                                              # cas 2.a)
                    if cases_colorees[j - sequence[l-1]] == BLANC or cases_colorees[j - sequence[l-1]] == VIDE :                               # cas 2.b)
                            possible = est_coloriable_rec_2(j - sequence[l-1]-1, l-1, sequence, memo, cases_colorees)
                            memo[j][l] = possible
                            return memo[j][l]
                else :
                    memo[j][l] = False
                    return False

def colore_ligne_rec(A: list(list()), i: int, index : int, cases_colorees : list(), memoisation):
    """
    Colorie par récurrence un max de cases de la ligne i de A

    Parameters
    ----------
    A : La grille dans son état actuelle. A = grille, sequences_lignes, sequences_colonnes
    i : la ligne a colorié
    index : index de la case avec laquelle on commence
    cases_colorees : liste des indices des cases qu'on colorie

    Returns
    -------
    (Boolean, A, cases_colorees):
        - Boolean : 
            True si la ligne est coloriable, False sinon.
        - A :
            La grille apres coloration de la ligne
        - cases_colorees : 
            Liste des indices des cases que nous avons colorées
    """
    original = copy.deepcopy(A)
    ligne = copy.deepcopy(A[0][i])
    sequence = A[1][i]
    j = len(ligne) - 1    # nb_colonnes de la ligne a coloriée
    l = len(sequence)     # nombre de blocs dans la séquence da la ligne i

    if (tuple(ligne), tuple(cases_colorees)) in memoisation :
        return memoisation[(tuple(ligne), tuple(cases_colorees))]# On connaît déja la valeur grâce a la mémoisation

    # Cas de base : # il ne reste  aucune case vide a coloré
    if  index == j + 1 :
        memoisation[(tuple(ligne), tuple(cases_colorees))] = True, A, cases_colorees
        return True, A, cases_colorees
    
    # La case ne doit pas être encore coloriée
    if ligne[index] == VIDE :
        # Tester si elle peut être coloriée en blanc (la colorier en blanc, et tester si la ligne i a une réponse positive) :
        ligne[index] = BLANC
        memo =  grille_vide(j+1,j+1)
        reponse_b  = est_coloriable_rec_2(j, l, sequence, memo, ligne)

        # Tester de même si elle peut être coloriée en noir :
        ligne[index] = NOIR
        memo =  grille_vide(j+1,j+1)
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
            A[0][i][index] =  VIDE

        if not(reponse_b) and not(reponse_n):   # les 2 tests echouent
            print("Le puzzle n'a pas de solution")
            memoisation[(tuple(ligne), tuple(cases_colorees))] =  False, original,[]
            return False, original,[]
        
        memoisation[(tuple(ligne), tuple(cases_colorees))] = colore_ligne_rec(A, i, index + 1, cases_colorees, memoisation)
        return memoisation[(tuple(ligne), tuple(cases_colorees))]         

    # Cas ou la case est deja colorée
    else :
        memoisation[(tuple(ligne), tuple(cases_colorees))] = colore_ligne_rec(A, i, index+1, cases_colorees, memoisation)
        return memoisation[(tuple(ligne), tuple(cases_colorees))]

def colore_colonne_rec(A: list(list()), j: int, index : int, cases_colorees : list(), memoisation):
    """
    Colorie par récurrence un max de cases de la colonne j de A

    Parameters
    ----------
    A : La grille dans son état actuelle. A = grille, sequences_lignes, sequences_colonnes
    j : la colonne a colorié
    index : index de la case avec laquelle on commence
    cases_colorees : liste des indices des cases qu'on colorie

    Returns
    -------
    (Boolean, A, cases_colorees):
        - Boolean : 
            True si la colonne est coloriable, False sinon.
        - A :
            La grille apres coloration de la colonne.
        - cases_colorees : 
            Liste des indices des cases que nous avons colorées
    """
    original = copy.deepcopy(A)
    colonne = [ligne[j] for ligne in A[0]]
    sequence = A[2][j]
    i = len(colonne) - 1
    l = len(sequence)

    if (tuple(colonne), tuple(cases_colorees)) in memoisation :
        return memoisation[(tuple(colonne), tuple(cases_colorees))]
    
    #case de base : on se trouve à la fin de la colonne et il n'y a plus de cases à colorer
    if index == i + 1:
        return True, A, cases_colorees
    
    #pour les cases qui n'ont pas encore de couleurs
    if colonne[index] == VIDE:
        #Test si elle peut être coloriée en blanc
        colonne[index] = BLANC
        memo = grille_vide(i+1, i+1)
        reponse_b = est_coloriable_rec_2(i, l, sequence, memo, colonne)

        #Test si elle peut être coloriée en noir
        colonne[index] = NOIR
        memo = grille_vide(i+1, i+1)
        reponse_n = est_coloriable_rec_2(i, l, sequence, memo, colonne)
        
        #déductions en fonction des valeurs de reponse_b et reponse_n

        #réussite du test blanc mais pas du test noir
        if reponse_b and not(reponse_n) : 
            colonne[index] = BLANC  
            A[0][index][j] =  BLANC
            cases_colorees.append(index)     
        
        #réussite du test noir mais pas du test blanc
        if reponse_n and not(reponse_b) : 
            colonne[index] = NOIR  
            A[0][index][j]  =  NOIR
            cases_colorees.append(index)

        #réussite des deux tests
        if reponse_b and reponse_n : 
            colonne[index] = VIDE     
            A[0][index][j]  =  VIDE

         #echec des deux tests
        if not(reponse_b) and not(reponse_n):  
            print("Le puzzle n'a pas de solution")
            memoisation[(tuple(colonne), tuple(cases_colorees))] =  False, original,[]
            return False, original, []
        
        memoisation[(tuple(colonne), tuple(cases_colorees))]= colore_colonne_rec(A, j, index + 1, cases_colorees, memoisation)
        return memoisation[(tuple(colonne), tuple(cases_colorees))] 
    
    #pour les cases déjà colorées
    else:
        memoisation[(tuple(colonne), tuple(cases_colorees))] = colore_colonne_rec(A, j, index + 1, cases_colorees, memoisation)
        return memoisation[(tuple(colonne), tuple(cases_colorees))] 
def coloration(A: list(list())):
    """
    Colorie une grille initialement VIDE, en prenant en compte les séquences des lignes, et celles des colonnes.

    Parameters
    ----------
    A : La grille dans son état actuelle. A = grille, sequences_lignes, sequences_colonnes

    Returns
    -------
    (b, A_prime)
    -  b : 
        True si la grille est coloriable, None si nous pouvons rien déduire, False sinon
    - A_prime :
        La grille apres la coloration
    """
    A_prime = copy.deepcopy(A) #O(nm) parce qu'il faut parcourir chaque élément de A pour créer une nouvelle copie
    n = len(A[0])
    m = len(A[0][0])
    lignes_a_voir = [i for i in range(n)]
    colonnes_a_voir = [i for i in range(m)] #en supposant que les lignes ont toutes le même nombre de colonnes

    while len(lignes_a_voir) != 0 and len(colonnes_a_voir) != 0:
        for i in lignes_a_voir:
            possibility, A_prime, new_colonnes = colore_ligne_rec(A_prime, i, 0, [], {})
            if not possibility:
                return False, (grille_vide(n, m), None, None)
            colonnes_a_voir = colonnes_a_voir + new_colonnes
            lignes_a_voir.remove(i)
        
        for j in colonnes_a_voir:
            possibility, A_prime, new_lignes = colore_colonne_rec(A_prime, j, 0, [], {})
            
            #possibility, A_prime, new_lignes = colore_colonne(A_prime, j)
            if not possibility:
                return False, (grille_vide(n, m), None, None)
            lignes_a_voir = lignes_a_voir + new_lignes
            colonnes_a_voir.remove(j)  
    for i in range(n):
        for j in range(m):
            if A_prime[0][i][j] == VIDE:
                return None, A_prime #parce qu'on ne sait pas : None = on ne sait pas
            
    return True, A_prime

def propagation(src) :
    """
    Affiche une visualisation de la grille apres la coloration selon une instance

    Parameters
    ----------
    - src : fichier source de l'instance a représenté
    """
    A =  lire_instance(src)
    (ok,res) = coloration(A)

    if ok :
        print("Voici la solution du puzzle : ")
        affichage(res[0])
    if ok == False :
        print("Le puzzle n'a pas de solution")
    if ok == None :
        print("Nous pouvons rien déduire")
