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


def construireGrilleDemineur(lin:int, col:int)->list:
    if lin<=0 or col<=0:
        raise ValueError("construireGrilleDemineur : Lenombre de lignes (valeur_du_premier_paramètre) ou de colonnes (valeur_du_second_paramètre) est négatif ou nul. ")
    if type(lin)!=int or type(col)!=int:
        raise TypeError("construireGrilleDemineur : Le nombre de lignes (type_du_premier_paramètre) ou de colonnes (type_du_second_paramètre) n’est pas un entier. ")
    else :
        l=[]
        ll=[]
        dico={}
        for i in range(lin):
            ll.append(l)
            for j in range(col):
                l.append(construireCellule(0, False))
            l=[]
    return ll

def getNbLignesGrilleDemineur(tab:list)->int:
    if not type_grille_demineur(tab):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(tab)

def getNbColonnesGrilleDemineur(tab:list)->int:
    if not type_grille_demineur(tab):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(tab[0])

def isCoordonneeCorrecte(tab:list,coord:tuple)->bool:
    if type(coord)!=tuple or not type_grille_demineur(tab) or type(coord[0])!=int or type(coord[1])!=int :
        raise TypeError(" isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    if 0<=coord[0]<getNbLignesGrilleDemineur(tab) and 0<=coord[1]<getNbColonnesGrilleDemineur(tab):
        res = True
    else :
        res = False
    return res

def getCelluleGrilleDemineur(tab:list,coord:tuple)->dict:
    if type(coord)!=tuple or not type_grille_demineur(tab) or type(coord[0])!=int or type(coord[1])!=int:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if coord[0]>getNbLignesGrilleDemineur(tab) or coord[1]>getNbColonnesGrilleDemineur(tab):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille. ")
    return tab[coord[0]][coord[1]]

def getContenuGrilleDemineur(tab:list,coord:tuple)->dict:
    if not isCoordonneeCorrecte(tab,coord):
        res = getCelluleGrilleDemineur(tab, coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)

    return res[const.CONTENU]

def setContenuGrilleDemineur(tab:list,coord:tuple,contenu:int)->None:
    if not isCoordonneeCorrecte(tab,coord):
        res = getContenuGrilleDemineur(tab,coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)
    res[const.CONTENU]=contenu
    return res

def isVisibleGrilleDemineur(tab:list,coord:tuple)->bool:
    if not isCoordonneeCorrecte(tab,coord):
        res = getCelluleGrilleDemineur(tab, coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)

    return res[const.VISIBLE]

def setVisibleGrilleDemineur(tab:list,coord:tuple,visible:int)->bool:
    if not isCoordonneeCorrecte(tab,coord):
        res = getContenuGrilleDemineur(tab,coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)
    res[const.VISIBLE]=visible
    return res[const.VISIBLE]

def contientMineGrilleDemineur(tab:list,coord:tuple):
    if not isCoordonneeCorrecte(tab,coord):
        res = getContenuGrilleDemineur(tab,coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)
    if res[const.CONTENU]==const.ID_MINE:
        res=True
    else:
        res=False
    return res