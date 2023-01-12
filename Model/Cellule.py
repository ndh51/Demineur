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


def isContenuCorrect(contenu: int) -> bool:
    if type(contenu) == int and 0 <= contenu <= 8 or type(contenu) == int and contenu == const.ID_MINE:
        res = True
    else:
        res = False
    return res


def construireCellule(ent:int=0,visible:bool=False) -> dict:
    if not isContenuCorrect(ent) or ent is None or visible is None:
        raise ValueError("construireCellule : le contenu valeur_du_contenu n’est pas correct")
    elif type(visible)!= bool :
        raise TypeError("construireCellule : le second paramètre (type_du_paramètre) n’est pas un booléen")
    else:
        if not isContenuCorrect(ent):
            ent=0

    return {const.CONTENU : ent, const.VISIBLE : visible,const.ANNOTATION: None}

def getContenuCellule(dico:dict)->int:
    if not type_cellule(dico):
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return dico[const.CONTENU]

def isVisibleCellule(dico: dict)->bool:
    if not type_cellule(dico):
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return dico[const.VISIBLE]

def setContenuCellule(dico:dict,contenu:int)->None:
    if type(contenu)!=int:
        raise TypeError(f"setContenuCellule : le type du contenu \"{contenu}\" n’est pas correcte. ")
    if not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : la valeur du contenu \"{contenu}\" n’est pas correcte. ")
    if not type_cellule(dico):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule. ")
    else:
        dico[const.CONTENU]=contenu
    return None

def setVisibleCellule(dico:dict,V:bool)->None:
    if not type_cellule(dico):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule. ")
    if type(V)!=bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen ")
    dico[const.VISIBLE]=V
    return None

def contientMineCellule(dico:dict)->bool:
    if not type_cellule(dico):
        raise TypeError("setContenuCellule : Le paramètre n’est pas une cellule. ")
    if dico[const.CONTENU]==const.ID_MINE:
        res=True
    else:
        res=False
    return res

def isAnnotationCorrecte(anno:str)->bool:
    if anno in[None,const.DOUTE,const.FLAG]:
        res=True
    else:
        res=False
    return res