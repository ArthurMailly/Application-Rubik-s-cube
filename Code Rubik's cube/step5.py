from cube_template import *
from annexes_solve import exchange_yellow_corner


def yellowcorner(p):  # But: Avoir une liste des coins jaunes
    corner = [[p[5][0], p[1][8], p[2][6], [5, 0], [1, 8], [2, 6]],
              [p[5][2], p[2][8], p[3][6], [5, 2], [2, 8], [3, 6]],
              [p[5][6], p[4][8], p[1][6], [5, 6], [4, 8], [1, 6]],
              [p[5][8], p[3][8], p[4][6], [5, 8], [3, 8], [4, 6]]]

    return corner


def algoyellowcorner(p):  # Algorithme qui ordonne les coins
    move_rp(p)
    move_d(p)
    move_l(p)
    move_dp(p)
    move_r(p)
    move_d(p)
    move_lp(p)
    move_dp(p)
    return ["R'", 'D', 'L', "D'", 'R', 'D', "L'", "D'"]


def good_place_yellow_corner(p):
    # But: retourne le nombre de coin bien placé, la liste des mouvements effectués et le coin qui est bien placé
    # s'il n'y en a qu'un
    ref = [['G', 'Y', 'O', [2, 6], [5, 0], [1, 8]], ['G', 'R', 'Y', [2, 8], [3, 6], [5, 2]],
           ['Y', 'B', 'O', [5, 6], [4, 8], [1, 6]], ['B', 'Y', 'R', [4, 6], [5, 8], [3, 8]]]
    # Liste référente qui sert à s'appercevoir lorsqu'un coin est bien placé, l'ordre de la liste est très importante
    turn = 0
    numgoodplace = 0
    move = []
    while turn != 4 and numgoodplace != 1 and numgoodplace != 4:
        # Tant que l'on ne trouve pas un seul de bien placé on continue à moins que tout soit déjà fait
        # print(f"On a tourné {turn} fois !")
        corner = yellowcorner(p)
        numgoodplace = 0
        for i in range(len(ref)):
            if corner[i][0] in ref[i] and corner[i][1] in ref[i] and corner[i][2] in ref[i]:
                # si le coin a les bonnes couleurs:
                # print(f"Le coin {corner[i]} est bien placé !")
                numgoodplace += 1  # un de plus est bien placé
                good_corner = corner[i]
                # est le dernier a être bien placé, good_corner ne sert que dans le cas où il n'y a qu'un seul coin
                # de bien placé
        if numgoodplace != 1 and numgoodplace != 4:
            # l'inverse de "si un seul coin est placé ou que les 4 le sont déjà"
            move_d(p)
            move += ['D']
            # print("D")
            turn += 1

    match numgoodplace:
        case 1:
            # print("Cas avec 1 seul de bien placé")
            return numgoodplace, move, good_corner
        case 4:
            # print("Tout est déjà fait")
            return numgoodplace, move, -1  # -1 pour signifier qu'il n'y a pas seul coin de bien placé mais au moins 2
        case _:
            # print("Cas embêtant avec 2 de bien placés!")
            return 2, move, -1  # idem pour le -1


def solve_arrangement_yellow_corner(p):  # Algorithme qui résout l'ordre des coins
    numgoodplace, move, goodcorner = good_place_yellow_corner(p)  # on récupère le coin de bien placé

    if numgoodplace == 2:
        move += algoyellowcorner(p)
        # on effectue l'algorithme pour retomber dans le cas où il n'y a qu'un seul de bien placé
        numgoodplace, movecase2, goodcorner = good_place_yellow_corner(p)
        move += movecase2

    if numgoodplace == 1:
        for i in range(3, 6):
            if goodcorner[i][0] == 5:  # on récupère la place du coin qui est bien placé sur la face jaune
                place = goodcorner[i][1]
        match place:  # on place ce coin en 0
            case 2:
                move_dp(p)
                move += ["D'"]
            case 8:
                move_d(p)
                move_d(p)
                move += ['D2']
            case 6:
                move_d(p)
                move += ['D']

        move += algoyellowcorner(p)  # on effectue l'algorithme

        match place:  # on regarde la place du bien placé
            case 2:
                move_d(p)
                numgoodplace, _, _ = good_place_yellow_corner(p)
                if numgoodplace == 4:
                    move += ['D']
                else:
                    move_dp(p)
                    move += algoyellowcorner(p)
                    move_d(p)
                    move += ['D']
            case 8:
                move_d(p)
                move_d(p)
                numgoodplace, _, _ = good_place_yellow_corner(p)
                if numgoodplace == 4:
                    move += ['D2']
                else:
                    move_d(p)
                    move_d(p)
                    move += algoyellowcorner(p)
                    move_d(p)
                    move_d(p)
                    move += ['D2']

            case 6:
                move_dp(p)
                numgoodplace, _, _ = good_place_yellow_corner(p)
                if numgoodplace == 4:
                    move += ["D'"]
                else:
                    move_d(p)
                    move += algoyellowcorner(p)
                    move_dp(p)
                    move += ["D'"]

            case 0:
                numgoodplace, _, _ = good_place_yellow_corner(p)
                if numgoodplace != 4:
                    move += algoyellowcorner(p)

    return move
