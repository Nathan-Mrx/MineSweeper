# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nb_lignes: int, nb_colonnes: int) -> list:
    """
        Détermine si le paramètre représente une grille d'un démineur.

        :param nb_lignes: nombre de lignes de la grille à créer
        :param nb_colonnes: nombre de colonnes de la grille à créer
        :return: grille de nb_lignes lignes et nb_colonnes colonnes
        """
    if not isinstance(nb_lignes, int) or not isinstance(nb_colonnes, int):
        raise TypeError(
            f'construireGrilleDemineur : Le nombre de lignes {nb_lignes} ou de colonnes {nb_colonnes} n’est pas '
            f'un entier.')
    if nb_lignes <= 0 or nb_colonnes <= 0:
        raise ValueError(
            f'construireGrilleDemineur : Le nombre de lignes {nb_lignes} ou de colonnes {nb_colonnes} est négatif '
            f'ou nul.')
    grille = []
    for li in range(nb_lignes):
        ligne = []
        for ce in range(nb_colonnes):
            ligne.append(construireCellule())
        grille.append(ligne)
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError('getNbLignesGrilleDemineur : Le paramètre n’est pas une grille')
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError('getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille')
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError('isCoordonneeCorrecte : un des paramètres n’est pas du bon type.')
    return 0 <= coord[0] <= getNbLignesGrilleDemineur(grille) - 1 and 0 <= coord[1] <= getNbColonnesGrilleDemineur(
        grille) - 1


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError('getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.')
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError('getCelluleGrilleDemineur : coordonnée non contenue dans la grille.')
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    return getCelluleGrilleDemineur(grille, coord)['Contenu']


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    return getCelluleGrilleDemineur(grille, coord)['Visible']


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError('getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type')
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError('getCoordonneeVoisinsGrilleDemineur :  la coordonnée n’est pas dans la grille.')
    x = coord[0]
    y = coord[1]
    liste_voisins = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) != coord and 0 <= i <= getNbLignesGrilleDemineur(
                    grille) - 1 and 0 <= j <= getNbColonnesGrilleDemineur(grille) - 1:
                liste_voisins.append(construireCoordonnee(i, j))
    return liste_voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple)->None:
    if nb < 0 or nb > getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille) - 1:
        raise ValueError('placerMinesGrilleDemineur : Nombre de bombes à placer incorrect')
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError('placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.')
    exeptions=[coord]
    i = 0
    while i < nb:
        x = randint(0,getNbLignesGrilleDemineur(grille)-1)
        y = randint(0,getNbColonnesGrilleDemineur(grille)-1)
        if (x, y) not in exeptions:
            setContenuGrilleDemineur(grille, (x, y), const.ID_MINE)
            exeptions.append((x, y))
            i += 1
    return None


