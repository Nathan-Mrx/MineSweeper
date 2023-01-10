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
    # Renvoie une erreur si les paramètres ne sont pas des entiers
    if not isinstance(nb_lignes, int) or not isinstance(nb_colonnes, int):
        raise TypeError(
            f'construireGrilleDemineur : Le nombre de lignes {nb_lignes} ou de colonnes {nb_colonnes} n’est pas '
            f'un entier.')
    # Renvoie une erreur si les paramètres sont négatifs
    if nb_lignes <= 0 or nb_colonnes <= 0:
        raise ValueError(
            f'construireGrilleDemineur : Le nombre de lignes {nb_lignes} ou de colonnes {nb_colonnes} est négatif '
            f'ou nul.')
    # Construit la grille
    grille = []
    for li in range(nb_lignes):
        ligne = []
        for ce in range(nb_colonnes):
            ligne.append(construireCellule())
        grille.append(ligne)
    # Renvoie la grille
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    Renvoie le nombre de lignes de la grille

    :param grille: grille de démineur
    :return: nombre de lignes de la grille
    """
    # Renvoie une erreur si grille n'est pas une grille
    if not type_grille_demineur(grille):
        raise TypeError('getNbLignesGrilleDemineur : Le paramètre n’est pas une grille')
    # Renvoie le nombre de lignes de la grille
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    Renvoie le nombre de colonnes de la grille

    :param grille: grille de démineur
    :return: nombre de colonnes de la grille
    """
    # Renvoie une erreur si grille n'est pas une grille

    if not type_grille_demineur(grille):
        raise TypeError('getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille')
    # Renvoie le nombre de colonnes de la grille
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """
    Verifie si la coordonnée passée en paramètre est contenue dans la grille passée en paramètre.

    :param grille: grille de démineur
    :param coord: coordonnée à verifier
    :return: True si la coordonnée est contenue dans la grille, False sinon
    """
    # Renvoie une erreur si un des deux paramètres n'est pas du bon type
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError('isCoordonneeCorrecte : un des paramètres n’est pas du bon type.')
    # Renvoie True si la coordonnée est contenue dans la grille, False sinon
    return 0 <= coord[0] <= getNbLignesGrilleDemineur(grille) - 1 and 0 <= coord[1] <= getNbColonnesGrilleDemineur(
        grille) - 1


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """
    Renvoie la cellule contenue à la coordonnée passée en paramètre dans la grille passée enn paramètre.

    :param grille: grille de démineur
    :param coord: coordonnée où aller chercher la cellule
    :return: cellule
    """
    # Renvoie une erreur si un des deux paramètres n'est pas du bon type
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError('getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.')
    # Renvoie une erreur si la coordonnée est hors de la grille
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError('getCelluleGrilleDemineur : coordonnée non contenue dans la grille.')
    # Renvoie la cellule
    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    """
    Renvoie le contenu de la cellule à la coordonnée coord dans la grille grille.

    :param grille: grille de démineur
    :param coord: coordonnée où aller chercher la cellule
    :return: entier contenu de la cellule
    """
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """
    Change le contenu de la cellule à la coordonnée coord dans la grille grille.

    :param grille: grille de démineur
    :param coord: coordonnée où aller chercher la cellule
    :contenu: contenu à enregistrer dans le contenu de la cellule
    :return: None
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Renvoie l'état de visibilité de la cellule à la coordonnée coord dans la grille grille.

    :param grille: grille de démineur
    :param coord: coordonnée où aller chercher la cellule
    :return: booléen représentant l'état de visibilité de la cellule
    """
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    """
    Change l'état de visibilité de la cellule à la coordonnée coord dans la grille grille.

    :param grille: grille de démineur
    :param coord: coordonnée où aller chercher la cellule
    :visible: état de visibilité à enregistrer dans l'état de visibilité de la cellule
    :return: None
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)
    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Verifie si la cellule à la coordonnée coord dans la grille grille contient une mine ou non.

    :param grille: grille de démineur
    :param coord: coordonnée où aller chercher la cellule
    :return: True si la cellule contient une mine, False sinon
    """
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """
    Renvoie la liste de voisins de la cellule à la coordonnée coord dans la grille grille

    :param grille: grille de démineur
    :param coord: coordonnée de la cellule
    :return: liste des voisins de la cellule
    """
    # Renvoie une erreur si l'un des paramètres n'est pas du bon type
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError('getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type')
    # Renvoie une erreur si la coordonnée est hors de la grille
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError('getCoordonneeVoisinsGrilleDemineur :  la coordonnée n’est pas dans la grille.')
    x = coord[0]
    y = coord[1]
    liste_voisins = []
    # On entre dans une bouble allant de la case de cauche à la case de droite
    for i in range(x - 1, x + 2):
        # On entre dans une bouble allant de la case du haut à la case du bas
        for j in range(y - 1, y + 2):
            # Si on ne regarde pas la cellule de départ et qu'on n'as pas dépassé les limites de la grille,
            if (i, j) != coord and 0 <= i <= getNbLignesGrilleDemineur(
                    grille) - 1 and 0 <= j <= getNbColonnesGrilleDemineur(grille) - 1:
                # alors on enregistre le voisin
                liste_voisins.append(construireCoordonnee(i, j))
    # On renvoie la liste de tous les voisins
    return liste_voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    """
    Place un nombre nb de mines aléatoirement dans la grille, la case coord exclue

    :param grille: grille de démineur
    :param nb: Nombre entier de mine à placer
    :param coord: Coordonnéede la cellule à exclure
    :return: None
    """
    # Renvoie une erreur si le nombre est négatif ou supérieur au nombre de cases possibles dans la grille
    if nb < 0 or nb > getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille) - 1:
        raise ValueError('placerMinesGrilleDemineur : Nombre de bombes à placer incorrect')
    # renvoie une erreur si la coordonnée exclue est hors de la grille
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError('placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.')
    # création d'une liste d'exclusions
    exclusions = [coord]
    i = 0
    # Tant qu'on a pas le bon nombre de mine dans la grille
    while i < nb:
        # On génère aléatoirement des coordonnées
        x = randint(0, getNbLignesGrilleDemineur(grille) - 1)
        y = randint(0, getNbColonnesGrilleDemineur(grille) - 1)
        # Si ces coordonnées ne sont pas exclues, on y place une mine et on les ajoutes aux exclusions
        if (x, y) not in exclusions:
            setContenuGrilleDemineur(grille, (x, y), const.ID_MINE)
            exclusions.append((x, y))
            i += 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """
    Change le contenu de toutes les cellules de la grille ne  contenant pas de mines par le nombre de mines parmis
    ses voisins

    :param grille: grille de démineur
    :return: None
    """
    # Pour chaque ligne et pour chaque cellule de la grille
    for li in range(getNbLignesGrilleDemineur(grille)):
        for ce in range(getNbColonnesGrilleDemineur(grille)):
            # On verifie si elle ne contient pas de mine
            if getContenuGrilleDemineur(grille, (li, ce)) != const.ID_MINE:
                nbMines = 0
                # On regarde combien de ses voisins sont des mines
                voisins = getCoordonneeVoisinsGrilleDemineur(grille, (li, ce))
                for v in voisins:
                    if getContenuGrilleDemineur(grille, v) == const.ID_MINE:
                        nbMines += 1
                # On stocke le résultat dans le contenu de la cellule
                setContenuGrilleDemineur(grille, (li, ce), nbMines)
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    Renvoie le nombre de mines dans la grille

    :param grille: grille de démineur
    :return: entier nombre de mines dans la grille
    """
    # Renvoie une erreur si grille n'est pas une grille
    if not type_grille_demineur(grille):
        raise ValueError('getNbMinesGrilleDemineur : le paramètre n’est pas une grille.')
    nbMines = 0
    # Pour chaque ligne et pour chaque cellule de la grille on regarde si elle contient une mine
    for li in range(getNbLignesGrilleDemineur(grille)):
        for ce in range(getNbColonnesGrilleDemineur(grille)):
            if getContenuGrilleDemineur(grille, (li, ce)) == const.ID_MINE:
                # On rajoute la mine à notre décompte
                nbMines += 1
    # Renvoie le nombre total de mines dans la grille
    return nbMines


def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    """
    Renvoie l'annotation de la cellule à la coordonnée coord dans la grille grille.

    :param grille: grille de démineur
    :param coord: coordonnée où aller chercher la cellule
    :return: annotation de la cellule
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    Renvoie le nombre de mines moins le nombre de drapeaux

    :param grille: grille de démineur
    :return: entier nombre de mines moins nombre de drapeaux
    """
    nbFlag = 0
    # Pour chaque ligne et pour chaque cellule on regarde si elle est annotée d'un drapeau
    for li in range(getNbLignesGrilleDemineur(grille)):
        for ce in range(getNbColonnesGrilleDemineur(grille)):
            if getAnnotationGrilleDemineur(grille, (li, ce)) == const.FLAG:
                # On rajoute le drapeau au décompte
                nbFlag += 1
    # On renvoie le nombre de mines moins le nombre de drapeaux placés
    return getNbMinesGrilleDemineur(grille) - nbFlag


def gagneGrilleDemineur(grille: list) -> bool:
    """
    Renvoie si la partie est gagnée ou non (si toutes les cases non mines ont été découvertes et aucunes mines
    n'ont été découvertes)

    :param grille: grille de démineur
    :return: True si la partie est gagnée, false sinon
    """
    cpt = 0
    nbFlag = 0
    minesDecouvertes = False
    # On parcourt chaque cellules de la grille
    # Si aucunes mines n'est découvertes, qu'il y a autant de mines que de drapeaux placés et si toutes les cases ne
    # contenant pas de mines ont étées découvertes, on renvoie True, False sinon
    for li in range(getNbLignesGrilleDemineur(grille)):
        for ce in range(getNbColonnesGrilleDemineur(grille)):
            if not contientMineGrilleDemineur(grille, (li, ce)) and isVisibleGrilleDemineur(grille, (li, ce)):
                cpt += 1
            if contientMineGrilleDemineur(grille, (li, ce)) and isVisibleGrilleDemineur(grille, (li, ce)):
                minesDecouvertes = True
            if contientMineGrilleDemineur(grille, (li, ce)) and \
                    getAnnotationGrilleDemineur(grille, (li, ce)) == const.FLAG:
                nbFlag += 1
    return getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille) - getNbMinesGrilleDemineur(
        grille) == cpt and not minesDecouvertes and getNbMinesGrilleDemineur(grille) == nbFlag


def perduGrilleDemineur(grille: list) -> bool:
    """
    Renvoie si la partie est perdue ou non

    :param grille: grille de démineur
    :return: True si la partie est perdue, False sinon
    """
    perdu = False
    # On parcourt chaque cellules de la grille
    for li in range(getNbLignesGrilleDemineur(grille)):
        for ce in range(getNbColonnesGrilleDemineur(grille)):
            # Si on trouve au moins une mine visible, on renvoie True
            if contientMineGrilleDemineur(grille, (li, ce)) and isVisibleGrilleDemineur(grille, (li, ce)):
                perdu = True
    return perdu


def reinitialiserGrilleDemineur(grille: list) -> None:
    """
    Réinitialise chaque cellule de la grille

    :param grille: grille de démineur
    :return: None
    """
    for li in range(getNbLignesGrilleDemineur(grille)):
        for ce in range(getNbColonnesGrilleDemineur(grille)):
            reinitialiserCellule(getCelluleGrilleDemineur(grille, (li, ce)))
    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    ensemble = set()
    pile = [coord]
    while pile:
        current = pile.pop()
        ensemble.add(current)
        if getContenuGrilleDemineur(grille, current) == 0:
            voisins = getCoordonneeVoisinsGrilleDemineur(grille, current)
            for v in voisins:
                if not contientMineGrilleDemineur(grille, v) and v not in ensemble:
                    pile.append(v)
                    ensemble.add(v)
    for elt in ensemble:
        setVisibleGrilleDemineur(grille, elt, True)
    return ensemble
