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


def isContenuCorrect(ent: int) -> bool:
    if type(ent) == int and (0 <= ent <= 8 or ent == const.ID_MINE):
        res = True
    else:
        res = False
    return res


def construireCellule(ent: int, VF : bool) -> dict:
    if not isContenuCorrect(ent) or ent is None or VF is None:
        raise ValueError("construireCellule : le contenu valeur_du_contenu n’est pas correct")
    elif type(VF)!= bool :
        raise TypeError("construireCellule : le second paramètre (type_du_paramètre) n’est pas un booléen")
    else:
        ent = 0
        VF = False
        res = {}
        res[const.CONTENU] = ent
        res[const.VISIBLE] = VF

    return res

