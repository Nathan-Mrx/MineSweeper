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
    if not isinstance(num_ligne,int) or not isinstance(num_col,int):
        raise TypeError(
            f'construireCoordonnee : Le numéro de ligne {type(num_ligne)} ou le numéro de colonne {type(num_col)} ne '
            f'sont pas des entiers')
    elif 0 > num_ligne or 0 > num_col:
        raise ValueError(
            f'construireCoordonnee : Le numéro de ligne {num_ligne} ou de colonne {num_col} ne sont pas positifs')
    return num_ligne, num_col


def getLigneCoordonnee(coord: tuple) -> int:
    error = 'getLigneCoordonnee : Le paramètre n’est pas une coordonnée'
    if type(coord) != type(tuple()):
        raise TypeError(error)
    elif type(coord[0]) != type(int()) or type(coord[1]) != type(int()) or 0 > coord[0] or 0 > coord[1]:
        raise TypeError(error)
    return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    error = 'getColonneCoordonnee : Le paramètre n’est pas une coordonnée'
    if type(coord) != type(tuple()):
        raise TypeError(error)
    elif type(coord[0]) != type(int()) or type(coord[1]) != type(int()) or 0 > coord[0] or 0 > coord[1]:
        raise TypeError(error)
    return coord[1]
