import time

BLANC = 1
VIDE = 0
NOIR = -1

def grille_vide(n: int, m: int):
    """
    Créer une matrice nxm initialisée a VIDE

    Parameteres
    -----------
    - n : nombre de lignes
    - m : nombre de colonnes
    
    Returns
    -------
    Une matrice nxm initialisé a VIDE
    """
    return [[VIDE for _ in range(m)] for _ in range(n)]

def lire_instance(src):
    """
    Lecture d'un fichier .txt contenant une instance de sequences de lignes et de colonnes.

    Parameters
    ----------
    - src : fichier source de l'instance a lire

    Returns
    -------
    (grille, sequences_lignes, sequences_colonnes)
        - grille : 
            matrice initialisée a vide de taille nb_lignes x nb_colonnes de l'instance
        - sequences_lignes :
            une liste de liste : contient l'ensemble des sequences de chaque ligne sous forme de liste d'entiers
        - sequences_colonnes :
            une liste de liste : contient l'ensemble des sequences de chaque colonne sous forme de liste d'entiers
    """
    sequences_lignes = []
    sequences_colonnes = []

    with open(src, 'r') as f:
        lignes = f.readlines()

    # Trouver l'index du symbole # pour séparer les lignes et les colonnes
    index_symbole_hashtag = lignes.index('#\n')

    # Traiter les séquences des lignes
    for ligne in lignes[:index_symbole_hashtag]:
        sequence = list(map(int, ligne.split()))
        sequences_lignes.append(sequence)

    # Traiter les séquences des colonnes
    for ligne in lignes[index_symbole_hashtag + 1:]:
        sequence = list(map(int, ligne.split()))
        sequences_colonnes.append(sequence)

    grille = grille_vide(len(sequences_lignes), len(sequences_colonnes))
    return grille, sequences_lignes, sequences_colonnes

def affichage(grille):
    """
    Affiche une représentation visuelle d'une grille.

    Parameters 
    ----------
    grille : grille a 2 dimensions a représenté
    """
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == VIDE:
                print("", end = '')
            if grille[i][j] == BLANC:
                print("⬜", end = '')
            if grille[i][j] == NOIR:
                print("⬛", end = '')
        print()
    print()

def timeFormat(listTemps: list):
    res = []
    for temps in listTemps:
        heure = int(round(temps // 3600))
        minute = int(round((temps % 3600) // 60))
        seconde = int(round(temps % 60))
        formatted_time = "{:02d}:{:02d}:{:02d}".format(heure, minute, seconde)
        res.append(formatted_time)
    return res