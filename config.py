import time

BLANC = 1
VIDE = 0
NOIR = -1

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
    return [[etat for _ in range(m)] for _ in range(n)]

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

def empty_grille(n: int, m: int):
    """
        Cette fonction renvoie une grille vide de taille n x m
    """
    return [[VIDE for _ in range(m)] for _ in range(n)]


# # Exemple d'utilisation
# fichier_instance = "instances/0.txt"
# _, sequences_lignes, sequences_colonnes = lire_instance(fichier_instance)

# # Affichage des résultats
# print("Sequences pour les lignes :", sequences_lignes)
# print("Sequences pour les colonnes :", sequences_colonnes)

def time_resolution(instance, function):
    debut = time.time
    function(instance)
    fin = time.time
    return fin - debut

def tab_times(list_instance):
    total_temps = 0
    tab_temps = []
    for instance in list_instance:
        t = time_resolution(instance)
        tab_temps.append([instance, t])
        total_temps += t
    return tab_temps

def affichage(grille):
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