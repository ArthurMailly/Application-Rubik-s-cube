from shuffle_template import *
from annexes_solve import exchange_corner


def whitecorner(p):  # But: Avoir une liste des coins contenant du blancs et aussi leurs positions
    corner = [[p[5][0], p[1][8], p[2][6], [5, 0], [1, 8], [2, 6]],
              [p[5][2], p[2][8], p[3][6], [5, 2], [2, 8], [3, 6]],
              [p[5][6], p[4][8], p[1][6], [5, 6], [4, 8], [1, 6]],
              [p[5][8], p[3][8], p[4][6], [5, 8], [3, 8], [4, 6]],
              [p[0][6], p[2][0], p[1][2], [0, 6], [2, 0], [1, 2]],
              [p[0][8], p[3][0], p[2][2], [0, 8], [3, 0], [2, 2]],
              [p[0][2], p[4][0], p[3][2], [0, 2], [4, 0], [3, 2]],
              [p[0][0], p[1][0], p[4][2], [0, 0], [1, 0], [4, 2]]]

    cornerwhite = []

    for i in range(len(corner)):
        for j in range(3):
            if corner[i][j] == 'W':
                cornerwhite.append(corner[i])

    finalcornerwhite = []

    for i in range(len(cornerwhite)):  # place tout d'abord les coins qui ont le coté jaune vers le haut
        if cornerwhite[i][0] == 'W' and cornerwhite[i][3][0] == 5:
            finalcornerwhite.append(cornerwhite[i])

    for i in range(len(cornerwhite)):  # on place ensuite les coins contenant du blanc qui sont sur la face jaune mais
        # où le blanc n'est pas sur la face jaune
        if cornerwhite[i][1] == 'W' or cornerwhite[i][2] == 'W':
            finalcornerwhite.append(cornerwhite[i])

    for i in range(len(cornerwhite)):  # on place les coins mal placé qui sont sur la premiere couronne
        if cornerwhite[i][0] == 'W' and cornerwhite[i][3][0] != 5:
            finalcornerwhite.append(cornerwhite[i])

    cornerwhite = []

    for i in range(len(finalcornerwhite)):  # on retire les coins de bien placé
        if good_place_white_corner(finalcornerwhite[i]) == False:
            cornerwhite.append(finalcornerwhite[i])

    return cornerwhite


def good_place_white_corner(corner):  # retourne true si le coin est placé
    ref = [['W', 'G', 'O', [0, 6], [2, 0], [1, 2]], ['W', 'R', 'G', [0, 8], [3, 0], [2, 2]],
           ['W', 'B', 'R', [0, 2], [4, 0], [3, 2]], ['W', 'O', 'B', [0, 0], [1, 0], [4, 2]]]
    ref += exchange_corner(ref)
    if corner in ref:
        return True
    return False


def above_corner(p, corner):  # But détecter le coin dont on parle et le placer
    color1 = corner[0]
    color2 = corner[1]
    color3 = corner[2]
    place = corner[3]
    move = []
    match [color1, color2, color3]:
        case ['W', 'G', 'O']:  # Coin blanc, vert, orange
            goal = [5, 0]
            whiteplace = 0
        case ['G', 'O', 'W']:
            goal = [5, 0]
            whiteplace = 2
        case ['O', 'W', 'G']:
            goal = [5, 0]
            whiteplace = 1
        case ['W', 'R', 'G']:  # Coin Blanc, Rouge, Vert
            goal = [5, 2]
            whiteplace = 0
        case ['R', 'G', 'W']:
            goal = [5, 2]
            whiteplace = 2
        case ['G', 'W', 'R']:
            goal = [5, 2]
            whiteplace = 1
        case ['W', 'B', 'R']:  # Coin Blanc, Bleu, Rouge
            goal = [5, 8]
            whiteplace = 0
        case ['B', 'R', 'W']:
            goal = [5, 8]
            whiteplace = 2
        case ['R', 'W', 'B']:
            goal = [5, 8]
            whiteplace = 1
        case ['W', 'O', 'B']:  # Coin Blanc, Orange, Bleu
            goal = [5, 6]
            whiteplace = 0
        case ['O', 'B', 'W']:
            goal = [5, 6]
            whiteplace = 2
        case ['B', 'W', 'O']:
            goal = [5, 6]
            whiteplace = 1

    if onyellowface(corner) == True:

        while place[1] != goal[1]:  # tant que la piece est mal placé on tourne
            move_d(p)
            move.append('D')
            # print('D')
            match place[1]:  # on change l'emplacement de la piece que l'on vient de bouger
                case 0:
                    place[1] = 2
                case 2:
                    place[1] = 8
                case 8:
                    place[1] = 6
                case 6:
                    place[1] = 0
    return move, whiteplace


def toitsplacecornertop(p, corner):  # on place l'élément de la deuxieme couronne là où il doit se trouver.
    # Cas: blancs vers le haut
    move = []
    match corner[0][3][1]:
        case 0:
            for i in range(3):
                move_l(p)
                move_d(p)
                move_lp(p)
                move_dp(p)
                move += ['L', 'D', "L'", "D'"]
        case 2:
            for i in range(3):
                move_f(p)
                move_d(p)
                move_fp(p)
                move_dp(p)
                move += ['F', 'D', "F'", "D'"]
        case 8:
            for i in range(3):
                move_r(p)
                move_d(p)
                move_rp(p)
                move_dp(p)
                move += ['R', 'D', "R'", "D'"]
        case 6:
            for i in range(3):
                move_b(p)
                move_d(p)
                move_bp(p)
                move_dp(p)
                move += ['B', 'D', "B'", "D'"]
    return move


def leavebottom(p, corner):  # pour les coins qui se trouvent sur la premiere couronne et qui sont mal placé, il faut
    # les enlevé de la premiere couronne avant de les remettre
    place = corner[3][1]
    move = []
    match place:
        case 0:
            for i in range(3):
                move_b(p)
                move_d(p)
                move_bp(p)
                move_dp(p)
                move += ['B', 'D', "B'", "D'"]
        case 6:
            for i in range(3):
                move_l(p)
                move_d(p)
                move_lp(p)
                move_dp(p)
                move += ['L', 'D', "L'", "D'"]
        case 2:
            for i in range(3):
                move_r(p)
                move_d(p)
                move_rp(p)
                move_dp(p)
                move += ['R', 'D', "R'", "D'"]
        case 8:
            for i in range(3):
                move_f(p)
                move_d(p)
                move_fp(p)
                move_dp(p)
                move += ['F', 'D', "F'", "D'"]
    return move


def toitsplacecornerright(p, corner):  # on place l'élément de la deuxieme couronne là où il doit se trouver.
    # Cas: blancs vers la droite
    move = ["D'"]
    move_dp(p)
    match corner[0][5][0]:
        case 1:
            move_b(p)
            move_dp(p)
            move_bp(p)
            move_d(p)
            move_d(p)
            move_b(p)
            move_dp(p)
            move_bp(p)
            move += ['B', "D'", "B'", 'D2', 'B', "D'", "B'"]
        case 4:
            move_r(p)
            move_dp(p)
            move_rp(p)
            move_d(p)
            move_d(p)
            move_r(p)
            move_dp(p)
            move_rp(p)
            move += ['R', "D'", "R'", 'D2', 'R', "D'", "R'"]
        case 2:
            move_l(p)
            move_dp(p)
            move_lp(p)
            move_d(p)
            move_d(p)
            move_l(p)
            move_dp(p)
            move_lp(p)
            move += ['L', "D'", "L'", 'D2', 'L', "D'", "L'"]
        case 3:
            move_f(p)
            move_dp(p)
            move_fp(p)
            move_d(p)
            move_d(p)
            move_f(p)
            move_dp(p)
            move_fp(p)
            move += ['F', "D'", "F'", 'D2', 'F', "D'", "F'"]
    return move


def toitsplacecornerleft(p, corner):  # on place l'élément de la deuxieme couronne là où il doit se trouver.
    # Cas: blancs vers la gauche
    move = ['D']
    move_d(p)
    match corner[0][4][0]:
        case 1:
            move_fp(p)
            move_d(p)
            move_f(p)
            move_d(p)
            move_d(p)
            move_fp(p)
            move_d(p)
            move_f(p)
            move += ["F'", 'D', 'F', 'D2', "F'", 'D', 'F']
        case 2:
            move_rp(p)
            move_d(p)
            move_r(p)
            move_d(p)
            move_d(p)
            move_rp(p)
            move_d(p)
            move_r(p)
            move += ["R'", 'D', 'R', 'D2', "R'", 'D', 'R']
        case 4:
            move_lp(p)
            move_d(p)
            move_l(p)
            move_d(p)
            move_d(p)
            move_lp(p)
            move_d(p)
            move_l(p)
            move += ["L'", 'D', 'L', 'D2', "L'", 'D', 'L']
        case 3:
            move_bp(p)
            move_d(p)
            move_b(p)
            move_d(p)
            move_d(p)
            move_bp(p)
            move_d(p)
            move_b(p)
            move += ["B'", 'D', 'B', 'D2', "B'", 'D', 'B']
    return move


def onyellowface(corner):  # donne un coin, renvoie true s'il se trouve sur la face jaune
    for j in range(3, 6):
        if corner[j][0] == 5:
            return True
    return False


def cornercolor(p, corner, color1, color2, color3):
    # donne les nouvelles coordonnées d'un coin en fonction de ses couleurs
    corner = whitecorner(p)
    for i in range(len(corner)):
        if color1 in corner[i] and color2 in corner[i] and color3 in corner[i]:
            return corner[i]


def solve1stlayer(p):
    corner = whitecorner(p)
    move = []
    i = 0
    n = 0
    while len(corner) != 0 and n < 4:
        # print(corner)
        cornermove, whiteplace = above_corner(p, corner[i])
        color1, color2, color3 = corner[i][0], corner[i][1], corner[i][2]
        corner[i] = cornercolor(p, corner, color1, color2, color3)
        move += cornermove
        if onyellowface(corner[i]) == True:  # si le coin se trouve sur la face jaune
            if whiteplace == 0:  # on regarde en fonction de la place de la face blanche
                move += toitsplacecornertop(p, corner)
            elif whiteplace == 1:
                move += toitsplacecornerleft(p, corner)
            elif whiteplace == 2:
                move += toitsplacecornerright(p, corner)
        else:  # si le coin est mal placé et qu'il se trouve sur la premiere couronne
            move += leavebottom(p, corner[i])  # ce coin va quitter la premiere couronne
            corner = whitecorner(p)
            # print(corner)
            cornermove, whiteplace = above_corner(p, corner[i])
            color1, color2, color3 = corner[i][0], corner[i][1], corner[i][2]
            corner[i] = cornercolor(p, corner, color1, color2, color3)
            move += cornermove
            if onyellowface(corner[i]) == True:  # on insère le coin
                if whiteplace == 0:
                    move += toitsplacecornertop(p, corner)
                elif whiteplace == 1:
                    move += toitsplacecornerleft(p, corner)
                elif whiteplace == 2:
                    move += toitsplacecornerright(p, corner)

        corner = whitecorner(p)
    return move
