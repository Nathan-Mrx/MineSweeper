# Model/Cellule.py
#

from Model.Constantes import *


#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
           and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
           and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(n: int):
    return isinstance(n, int) and 0 <= n <= 8 or n == const.ID_MINE


def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    if contenu != const.ID_MINE and 0 > contenu or 8 < contenu:
        raise ValueError(f'construireCellule : le contenu {contenu} n’est pas correct')
    if not isinstance(visible, bool):
        raise TypeError(f'construireCellule : le second paramètre {type(visible)} n’est pas un booléen')
    dic = {}
    dic['Contenu'] = contenu
    dic['Visible'] = visible
    dic[const.ANNOTATION] = None
    return dic


def getContenuCellule(cell: dict) -> int:
    if not type_cellule(cell):
        raise TypeError('getContenuCellule : Le paramètre n’est pas une cellule.')
    return cell['Contenu']


def isVisibleCellule(cell: dict) -> int:
    if not type_cellule(cell):
        raise TypeError('isVisibleCellule : Le paramètre n’est pas une cellule.')
    return cell['Visible']


def setContenuCellule(cell: dict, c: int) -> None:
    if not type_cellule(cell):
        raise TypeError('setContenuCellule : Le premier paramètre n’est pas une cellule.')
    if not isinstance(c, int) or isinstance(c, bool):
        raise TypeError('setContenuCellule : Le second paramètre n’est pas un entier.')
    if c != const.ID_MINE and 0 > c or 8 < c:
        raise ValueError(f'setContenuCellule : la valeur du contenu {c} n’est pas correcte.')
    cell['Contenu'] = c
    return None


def setVisibleCellule(cell: dict, v: bool) -> None:
    if not type_cellule(cell):
        raise TypeError('setVisibleCellule : Le premier paramètre n’est pas une cellule.')
    if not isinstance(v, bool):
        raise TypeError('setVisibleCellule : Le second paramètre n’est pas un entier.')
    cell['Visible'] = v
    return None


def contientMineCellule(cell: dict) -> bool:
    if not type_cellule(cell):
        raise TypeError('contientMineCellule : Le paramètre n’est pas une cellule.')
    result = False
    if cell['Contenu'] == const.ID_MINE:
        result = True
    return result


def isAnnotationCorrecte(annotation: str) -> bool:
    return annotation in (None, const.FLAG, const.DOUTE)