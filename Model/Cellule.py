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


def isContenuCorrect(n: int) -> bool:
    """
    Détermine si le contenu de la cellule est correct (vaut entre 0 et 8 ou est une mine).

    :param n: Entier représentant le contenu d'une cellule
    :return: True si le contenu est correct, False sinon
    """
    # Revoie True si le contenu est correct, False sinon
    return isinstance(n, int) and 0 <= n <= 8 or n == const.ID_MINE


def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    """
    Construit une cellule à partir d'un contenu et d'un état de visibilité

    :param contenu: contenu de la cellule (nombre de mine dans les voisins ou mine), 0 par défaut
    :param visible: état de visibilité de la cellule (True si visible, False sionn), False par défaut
    :return: Un dictionnaire cellule avec comme clés const.CONTENU
    """
    # Renvoie une erreur si le contenu n'est pas correct
    if not isContenuCorrect(contenu):
        raise ValueError(f'construireCellule : le contenu {contenu} n’est pas correct')
    # Renvoie une erreur si l'état de visibilité n'est pas un booléen
    if not isinstance(visible, bool):
        raise TypeError(f'construireCellule : le second paramètre {type(visible)} n’est pas un booléen')
    # Création du dictionnaire
    dic = {}
    dic[const.CONTENU] = contenu
    dic[const.VISIBLE] = visible
    dic[const.ANNOTATION] = None
    # On renvoie le dictionnaire
    return dic


def getContenuCellule(cell: dict) -> int:
    """
    Renvoie le contenu de la cellule passée en paramètre

    :param cell: objet dont on veut obtenir le contenu
    :return: contenu de l'objet
    """
    # Renvoie une erreur si l'objet n'est pas une cellule
    if not type_cellule(cell):
        raise TypeError('getContenuCellule : Le paramètre n’est pas une cellule.')
    # Renvoie le contenu de l'objet
    return cell[const.CONTENU]


def isVisibleCellule(cell: dict) -> bool:
    """
    Renvoie l'état de visibilité de la cellule passée en paramètre

    :param cell:  objet dont on veut obtenir l'état de visibilité
    :return: état de visibilité de l'objet
    """
    # Renvoie une erreur si l'objet n'est pas une cellule
    if not type_cellule(cell):
        raise TypeError('isVisibleCellule : Le paramètre n’est pas une cellule.')
    # Renvoie le contenu de l'objet
    return cell[const.VISIBLE]


def setContenuCellule(cell: dict, c: int) -> None:
    """
    Change le contenu de la cellule passée en paramètre par un entier passé en paramètre

    :param cell: objet à modifier
    :param c: entier à enregistrer dans le contenu de la cellule
    :return: None
    """
    # Renvoie une erreur si l'objet n'est pas une cellule
    if not type_cellule(cell):
        raise TypeError('setContenuCellule : Le premier paramètre n’est pas une cellule.')
    # Renvoie une erreur si la valeur à enregistrer n'est pas un entier
    if not isinstance(c, int) or isinstance(c, bool):
        raise TypeError('setContenuCellule : Le second paramètre n’est pas un entier.')
    # Renvoie une erreur si la valeur à enregistrer n'est pas correcte
    if not isContenuCorrect(c):
        raise ValueError(f'setContenuCellule : la valeur du contenu {c} n’est pas correcte.')
    # Change la valeur dans l'objet
    cell[const.CONTENU] = c
    return None


def setVisibleCellule(cell: dict, v: bool) -> None:
    """
    Change l'état de visibilité de la cellule passée en paramètre par un booléen passé en paramètre

    :param cell: objet à modifier
    :param v: booléen à enregistrer dans l'état de visibilité de la cellule
    :return: None
    """
    # Renvoie une erreur si cell n'est pas une cellule
    if not type_cellule(cell):
        raise TypeError('setVisibleCellule : Le premier paramètre n’est pas une cellule.')
    # Renvoie une erreur si v n'est pas un booléen
    if not isinstance(v, bool):
        raise TypeError('setVisibleCellule : Le second paramètre n’est pas un entier.')
    # Change la valeur dans l'objet
    cell[const.VISIBLE] = v
    return None


def contientMineCellule(cell: dict) -> bool:
    """
    Verifie si la cellule contient une mine ou non

    :param cell: objet à verifier
    :return: True si l'objet contient une mine, False sinon
    """
    # Renvoie une erreur si l'objet n'est pas une cellule
    if not type_cellule(cell):
        raise TypeError('contientMineCellule : Le paramètre n’est pas une cellule.')
    # verifie si la cellule contient une mine
    result = False
    if cell[const.CONTENU] == const.ID_MINE:
        result = True
        # Renvoie le résultat
    return result


def isAnnotationCorrecte(annotation: str) -> bool:
    """
    Verifie si l'anotation est correcte.

    :param annotation: annotation à verifier
    :return: True si l'annotation est correcte, False sinon
    """
    # renvoie True si l'annotation est correcte, False sinon
    return annotation in (None, const.FLAG, const.DOUTE)


def getAnnotationCellule(cell: dict) -> str:
    """
    Renvoie l'annotation de la cellule

    :param cell: objet où aller chercher l'annotation
    :return: chaîne de caractère d'annotation
    """
    # Renvoie une erreur si l'objet n'set pa une cellule
    if not type_cellule(cell):
        raise TypeError(f'getAnnotationCellule : le paramètre {cell} n’est pas une cellule')
    # Si la cellule n'as pas de clé d'annotation, renvoie None
    if const.ANNOTATION not in cell.keys():
        result = None
    # Sinon, renvoie l'annotation
    else:
        result = cell[const.ANNOTATION]
    return result


def changeAnnotationCellule(cell: dict) -> None:
    """
    Change l'annotation d'une cellule selon le cycle (Rien, drapeau, doute, rien, drapeau, etc.)

    :param cell: objet où enregistrer l'annotation
    :return: None
    """
    # Renvoie une erreur si l'objet n'est pas une cellule
    if not type_cellule(cell):
        raise TypeError('changeAnnotationCellule : le paramètre n’est pas une cellule')
    # Change l'anotation pour l'annotation suivante dans le cycle
    annotations = (None, const.FLAG, const.DOUTE)
    cell[const.ANNOTATION] = annotations[(annotations.index(getAnnotationCellule(cell))+1)%3]
    return None


def reinitialiserCellule(cell: dict) -> None:
    """
    Réinitialise la cellule passée en paramètres

    :param cell: cellule à réinitialiser
    :return: None
    """
    # Réinitialise la cellule
    cell[const.CONTENU] = 0
    cell[const.VISIBLE] = False
    cell[const.ANNOTATION] = None
    return None