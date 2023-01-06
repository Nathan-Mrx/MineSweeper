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


def isContenuCorrect(n:int):
    return isinstance(n, int) and 0 <= n <= 8 or n == const.ID_MINE


def construireCellule(c:int=0, v:bool=False)-> dict:
    if c != const.ID_MINE and 0 > c or 8 < c:
        raise ValueError(f'construireCellule : le contenu {c} n’est pas correct')
    if not isinstance(v, bool):
        raise TypeError(f'construireCellule : le second paramètre {type(v)} n’est pas un booléen')
    dic= {}
    dic['Contenu']=c
    dic['Visible']=v
    return dic