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


def construireGrilleDemineur(lin: int, col: int) -> list:
    if lin <= 0 or col <= 0:
        raise ValueError(
            "construireGrilleDemineur : Lenombre de lignes (valeur_du_premier_paramètre) ou de colonnes (valeur_du_second_paramètre) est négatif ou nul. ")
    if type(lin) != int or type(col) != int:
        raise TypeError(
            "construireGrilleDemineur : Le nombre de lignes (type_du_premier_paramètre) ou de colonnes (type_du_second_paramètre) n’est pas un entier. ")
    else:
        l = []
        ll = []
        dico = {}
        for i in range(lin):
            ll.append(l)
            for j in range(col):
                l.append(construireCellule(0, False))
            l = []
    return ll


def getNbLignesGrilleDemineur(tab: list) -> int:
    if not type_grille_demineur(tab):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(tab)


def getNbColonnesGrilleDemineur(tab: list) -> int:
    if not type_grille_demineur(tab):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(tab[0])


def isCoordonneeCorrecte(tab: list, coord: tuple) -> bool:
    if type(coord) != tuple or not type_grille_demineur(tab) or type(coord[0]) != int or type(coord[1]) != int:
        raise TypeError(" isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    if 0 <= coord[0] < getNbLignesGrilleDemineur(tab) and 0 <= coord[1] < getNbColonnesGrilleDemineur(tab):
        res = True
    else:
        res = False
    return res


def getCelluleGrilleDemineur(tab: list, coord: tuple) -> dict:
    if type(coord) != tuple or not type_grille_demineur(tab) or type(coord[0]) != int or type(coord[1]) != int:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if coord[0] > getNbLignesGrilleDemineur(tab) or coord[1] > getNbColonnesGrilleDemineur(tab):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille. ")
    return tab[coord[0]][coord[1]]


def getContenuGrilleDemineur(tab: list, coord: tuple) -> dict:
    if not isCoordonneeCorrecte(tab, coord):
        res = getCelluleGrilleDemineur(tab, coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)

    return res[const.CONTENU]


def setContenuGrilleDemineur(tab: list, coord: tuple, contenu: int) -> None:
    if not isCoordonneeCorrecte(tab, coord):
        res = getContenuGrilleDemineur(tab, coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)
    res[const.CONTENU] = contenu
    return res


def isVisibleGrilleDemineur(tab: list, coord: tuple) -> bool:
    if not isCoordonneeCorrecte(tab, coord):
        res = getCelluleGrilleDemineur(tab, coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)

    return res[const.VISIBLE]


def setVisibleGrilleDemineur(tab: list, coord: tuple, visible: bool) -> bool:
    if not isCoordonneeCorrecte(tab, coord):
        res = getContenuGrilleDemineur(tab, coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)
    res[const.VISIBLE] = visible
    return res[const.VISIBLE]


def contientMineGrilleDemineur(tab: list, coord: tuple) -> bool:
    if not isCoordonneeCorrecte(tab, coord):
        res = getContenuGrilleDemineur(tab, coord)
    else:
        res = getCelluleGrilleDemineur(tab, coord)
    if res[const.CONTENU] == const.ID_MINE:
        res = True
    else:
        res = False
    return res


def getCoordonneeVoisinsGrilleDemineur(tab: list, coord: tuple) -> list:
    if not isCoordonneeCorrecte(tab, coord) or not type_grille_demineur(tab):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if 0 > coord[0] or coord[0] >= getNbLignesGrilleDemineur(tab) or 0 > coord[1] or coord[
        1] >= getNbColonnesGrilleDemineur(tab):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille")
    else:
        res = []
        for i in range(coord[0] - 1, coord[0] + 2, 1):
            for j in range(coord[1] - 1, coord[1] + 2, 1):
                if (i, j) != coord and 0 <= i < getNbLignesGrilleDemineur(tab) and 0 <= j < getNbColonnesGrilleDemineur(
                        tab):
                    res.append((i, j))

        print(res)
    return res


def placerMinesGrilleDemineur(tab: list, nb: int, coord: tuple) -> None:
    if nb<0 or nb>(getNbColonnesGrilleDemineur(tab)*getNbLignesGrilleDemineur(tab))-1:
        raise ValueError(" placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if not isCoordonneeCorrecte(tab,coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")
    k = nb
    while k != 0:
        i=randint(0,getNbLignesGrilleDemineur(tab)-1)
        j=randint(0,getNbColonnesGrilleDemineur(tab)-1)
        if not contientMineGrilleDemineur(tab,(i,j)) and (i,j)!=coord:
            setContenuGrilleDemineur(tab,(i,j),const.ID_MINE)
            k -= 1
    compterMinesVoisinesGrilleDemineur(tab)
    #l'installation de scipy plante sur le venv, j'ai donc du tester avec la version python 3.9 de mon pc mais j'ai tout de meme le doute que la fonction passe le test
    return None

def compterMinesVoisinesGrilleDemineur(tab:list)->None:
    for i in range(getNbLignesGrilleDemineur(tab)):
        for j in range(getNbColonnesGrilleDemineur(tab)):
          if not contientMineGrilleDemineur(tab,(i,j)):
                voisins=getCoordonneeVoisinsGrilleDemineur(tab,(i,j))
                compte=0
                for k in range(len(voisins)):
                    if getContenuGrilleDemineur(tab,voisins[k])==const.ID_MINE:
                        compte+=1
                setContenuGrilleDemineur(tab,(i,j),compte)
    return None

def getNbMinesGrilleDemineur(tab:list)->int:
    if not type_grille_demineur(tab):
        raise ValueError("etNbMinesGrilleDemineur : le paramètre n’est pas une grille")
    res=0
    for i in range(getNbLignesGrilleDemineur(tab)):
        for j in range(getNbColonnesGrilleDemineur(tab)):
            if getContenuGrilleDemineur(tab,(i,j))==const.ID_MINE:
                res+=1
    return res

def getAnnotationGrilleDemineur(tab:list,coord:tuple):
    return getAnnotationCellule(tab[coord[0]][coord[1]])

def getMinesRestantesGrilleDemineur(tab:list)->int:
    nb=getNbMinesGrilleDemineur(tab)
    flag=0
    for i in range(getNbLignesGrilleDemineur(tab)):
        for j in range(getNbColonnesGrilleDemineur(tab)):
            if getAnnotationGrilleDemineur(tab, (i, j)) == const.FLAG:
                flag+=1
    return nb-flag


def gagneGrilleDemineur(tab:list)->bool:
    nb=getNbMinesGrilleDemineur(tab)
    compt=0
    drap=0
    for i in range(getNbLignesGrilleDemineur(tab)):
        for j in range(getNbColonnesGrilleDemineur(tab)):
            if isVisibleGrilleDemineur(tab,(i,j)) and not contientMineGrilleDemineur(tab,(i,j)):
                compt+=1
            if isVisibleGrilleDemineur(tab,(i,j)) and contientMineGrilleDemineur(tab,(i,j)):
                compt-=1
            if not isVisibleGrilleDemineur(tab,(i,j)) and contientMineGrilleDemineur(tab,(i,j)) and getAnnotationGrilleDemineur(tab,(i,j))==const.FLAG:
                drap+=1
    if compt+nb==(getNbLignesGrilleDemineur(tab)*getNbColonnesGrilleDemineur(tab)) and nb==drap:
        return True
    else:
        return False

def perduGrilleDemineur(tab:list)->bool:
    for i in range(getNbLignesGrilleDemineur(tab)):
        for j in range(getNbColonnesGrilleDemineur(tab)):
            if isVisibleGrilleDemineur(tab, (i, j)) and contientMineGrilleDemineur(tab, (i, j)):
                return True
    return False


def reinitialiserGrilleDemineur(tab:list)->None:
    for i in range(getNbLignesGrilleDemineur(tab)):
        for j in range(getNbColonnesGrilleDemineur(tab)):
            reinitialiserCellule(tab[i][j])
    return None

def decouvrirGrilleDemineur(tab:list,coord)->list:
    setVisibleGrilleDemineur(tab,coord,True)
    res=[]
    if getContenuGrilleDemineur(tab,coord)==0:
        pas_mine=True
        while pas_mine:
            for i in range(coord[0] - 1, coord[0] + 2, 1):
                compt=0
                for j in range(coord[1] - 1, coord[1] + 2, 1):
                    if (i, j) != coord and 0 <= i < getNbLignesGrilleDemineur(tab) and 0 <= j < getNbColonnesGrilleDemineur(tab) and getContenuGrilleDemineur(tab,(i,j))!=const.ID_MINE:
                        compt+=1
                    if 8==compt:
                        for i in range(coord[0] - 1, coord[0] + 2, 1):
                            for j in range(coord[1] - 1, coord[1] + 2, 1):
                                if (i,j) not in res and coord!=(i,j):
                                    res.append((i, j))

    for i in range(len(res)):
        setVisibleGrilleDemineur(tab,res[i],True)
    return None