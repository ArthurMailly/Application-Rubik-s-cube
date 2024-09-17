from shuffle_template import *
from annexes_solve import exchange, on2ndlayer, above, initsplace, leave


def elem2ndlayer(p):  # But: avoir une liste des éléments qui vont sur la seconde ligne avec l'emplacement de leur
    # couleur qui sont mal place
    elem = [[p[1][5], p[2][3], [1, 5], [2, 3]], [p[2][5], p[3][3], [2, 5], [3, 3]], [p[3][5], p[4][3], [3, 5], [4, 3]],
            [p[4][5], p[1][3], [4, 5], [1, 3]],
            [p[1][7], p[5][3], [1, 7], [5, 3]], [p[2][7], p[5][1], [2, 7], [5, 1]], [p[3][7], p[5][5], [3, 7], [5, 5]],
            [p[4][7], p[5][7], [4, 7], [5, 7]]]
    toput = []
    for i in range(len(elem)):
        v = 0
        for j in range(2):
            if elem[i][j] == 'Y':
                v = 1
        if v == 0 and good_place(elem[i]) == False:
            toput.append(elem[i])
    finaltoput = []  # Une liste qui contiendra les arretes de la deuxieme couronne. Les premiers elements de la liste
    # seront ceux coté face jaune
    for i in range(len(toput)):
        if toput[i][2][0] == 5 or toput[i][3][0] == 5:
            finaltoput.append(toput[i])
    for i in range(len(toput)):
        if toput[i][2][0] != 5 and toput[i][3][0] != 5:
            finaltoput.append(toput[i])
    return finaltoput


def good_place(elem):  # renvoie True si l'element donne est a la bonne place
    ref = [['O', 'G', [1, 5], [2, 3]], ['G', 'R', [2, 5], [3, 3]], ['R', 'B', [3, 5], [4, 3]],
           ['B', 'O', [4, 5], [1, 3]]]
    ref += exchange(ref)  # ref est la liste referente qui contient tous les cas possibles indiquant qu'un élément de
    # la deuxieme couronne est bien placé.

    if elem in ref:
        return True
    return False


def solve2ndlayer(p):
    toplace = elem2ndlayer(p)
    i = 0
    n = 0
    move = []
    while len(toplace) != 0 and n < 4:  # Placer les pieces de la 2eme couronne qui touche la face jaune
        if on2ndlayer(toplace[i]) == False:
            if toplace[i][2][0] == 5:
                coloab = toplace[i][0]
                colobe = toplace[i][1]
                place = toplace[i][3][0]
            else:
                coloab = toplace[i][1]  # On récupère la couleur qui se situe du cote de la face jaune
                colobe = toplace[i][0]
                place = toplace[i][2][0]  # On retient le numero de la face sur laquelle est la deuxieme couleur
            while above(coloab,
                        place) == False:  # tant que la piece n'est pas au dessus de la bonne case à placer, on tourne
                move_d(p)
                move.append('D')
                place += 1
                if place == 5:
                    place = 1
            move += initsplace(p, coloab, colobe)
            # print(f"{coloab} est bien placé, {colobe} est la deuxieme couleur")

        else:
            n += 1
        toplace = elem2ndlayer(p)

    if len(toplace) != 0:
        while len(toplace) != 0:
            move += leave(p, toplace[0][2][0], toplace[0][3][0])
            toplace = elem2ndlayer(p)
            if toplace[i][2][0] == 5:
                coloab = toplace[i][0]
                colobe = toplace[i][1]
                place = toplace[i][3][0]
            else:
                coloab = toplace[i][1]  # On récupère la couleur qui se situe du cote de la face jaune
                colobe = toplace[i][0]
                place = toplace[i][2][0]  # On retient le numero de la face sur laquelle est la deuxieme couleur
            while above(coloab, place) == False:
                move_d(p)
                move.append('D')
                place += 1
                if place == 5:
                    place = 1
            move += initsplace(p, coloab, colobe)
            # print(f"{coloab} est bien placé, {colobe} est la deuxieme couleur")
            toplace = elem2ndlayer(p)
    return move
