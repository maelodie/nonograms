BLANC = 1
VIDE = 0
NOIR = -1

import numpy as np
def creer_tab(n, m, etat) :
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

def lire_instance(src):
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

    grille = creer_tab(len(sequences_lignes), len(sequences_colonnes), VIDE)
    return grille, sequences_lignes, sequences_colonnes

# Exemple d'utilisation
fichier_instance = "instances//instances//0.txt"
_, sequences_lignes, sequences_colonnes = lire_instance(fichier_instance)

# Affichage des résultats
print("Sequences pour les lignes :", sequences_lignes)
print("Sequences pour les colonnes :", sequences_colonnes)
