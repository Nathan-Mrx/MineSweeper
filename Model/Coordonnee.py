# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(num_ligne: int, num_col: int) -> tuple:
    """
    Construit un tuple coordonnée à partir du numéro de la ligne et du numéro de la colonne passés en paramètres.

    :param num_ligne: numéro de la ligne
    :param num_col: numéro de la colonne
    :return: tuple contenant les coordonnées coordonnées
    """
    # Test verifiant que les paramètres sont bien des entiers, renvoie une erreur sinon.
    if not isinstance(num_ligne,int) or not isinstance(num_col,int):
        raise TypeError(
            f'construireCoordonnee : Le numéro de ligne {type(num_ligne)} ou le numéro de colonne {type(num_col)} ne '
            f'sont pas des entiers')
    # Test verifiant que les paramètres entiers sont biens positifs, renvoie une erreur sinon
    if 0 > num_ligne or 0 > num_col:
        raise ValueError(
            f'construireCoordonnee : Le numéro de ligne {num_ligne} ou de colonne {num_col} ne sont pas positifs')
    # Renvoie le tuple coordonnée
    return num_ligne, num_col


def getLigneCoordonnee(coord: tuple) -> int:
    """
    Renvoie le numéro de ligne de la coordonnée passée en paramètre.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: le numéro de ligne de la coordonnée passée en paramètre
    """
    error = 'getLigneCoordonnee : Le paramètre n’est pas une coordonnée'
    # Renvoie une erreur si coord n'est pas un tuple
    if not isinstance(coord, tuple):
        raise TypeError(error)
    # Renvoie une erreur si coord ne contient pas des entiers positifs
    if not isinstance(coord[0], int) or not isinstance(coord[1], int) or 0 > coord[0] or 0 > coord[1]:
        raise TypeError(error)
    # Renvoie le numéro de ligne
    return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    """
    Renvoie le numéro de colonne de la coordonnée passée en paramètre.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: le numéro de colonne de la coordonnée passée en paramètre
    """
    error = 'getColonneCoordonnee : Le paramètre n’est pas une coordonnée'
    # Renvoie une erreur si coord n'est pas un tuple
    if type(coord) != type(tuple()):
        raise TypeError(error)
    # Renvoie une erreur si coord ne contient pas des entiers positifs
    elif type(coord[0]) != type(int()) or type(coord[1]) != type(int()) or 0 > coord[0] or 0 > coord[1]:
        raise TypeError(error)
    # Renvoie le numéro de colonne
    return coord[1]
