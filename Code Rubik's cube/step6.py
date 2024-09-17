from cube_template import *


def number_non_yellow_face(p):  # Donne le nombre de coin qui ne sont pas jaune sur la face jaune
    yellow = [0, 2, 6, 8]
    n = 0
    for i in yellow:
        if p[5][i] != 'Y':
            n += 1
    return n


def chair(p):  # Algorithme 1
    move_l(p)
    move_d(p)
    move_d(p)
    move_lp(p)
    move_dp(p)
    move_l(p)
    move_dp(p)
    move_lp(p)
    move_rp(p)
    move_d(p)
    move_d(p)
    move_r(p)
    move_d(p)
    move_rp(p)
    move_d(p)
    move_r(p)
    return ['L', 'D2', "L'", "D'", 'L', "D'", "L'", "R'", 'D2', 'R', "D", "R'", "D", 'R']


def anti_chair(p):  # Algorithme 2
    move_l(p)
    move_d(p)
    move_lp(p)
    move_d(p)
    move_l(p)
    move_d(p)
    move_d(p)
    move_lp(p)
    move_rp(p)
    move_dp(p)
    move_r(p)
    move_dp(p)
    move_rp(p)
    move_d(p)
    move_d(p)
    move_r(p)
    return ['L', 'D', "L'", 'D', 'L', 'D2', "L'", "R'", "D'", 'R', "D'", "R'", 'D2', 'R']


def solve_yellow_face(p):
    move = []
    nonyellow = number_non_yellow_face(p)  # prend le nombre de coin de la jaune qui ne sont pas jaunes
    match nonyellow:  # on fait une distinction des cas
        case 2:  # Si nonyellow==2, on distingue 3 cas
            # print("On est dans le cas 2 !")
            while p[2][6] != 'Y':
                # tourne la face jaune de telle sorte à pouvoir identifier correctement et plus simplement le cas
                move_d(p)
                move += ['D']
            if p[2][8] == 'Y':  # On cherche le cas
                # print("Cas chaise")
                move_dp(p)
                move += ["D'"]
                move += chair(p)
            elif p[3][8] == 'Y':
                # print("Cas autre")
                move_dp(p)
                move += ["D'"]
                move += anti_chair(p)
                move_dp(p)
                move += ["D'"]
                move += anti_chair(p)

            else:
                # print("Cas anti-chaise")
                move += ['D2']
                move_d(p)
                move_d(p)
                move += anti_chair(p)
        case 4:  # si nonyellow == 4, on distingue 2 cas
            while p[1][6] != 'Y' or p[1][8] != 'Y':
                # tourne la face jaune de telle sorte à pouvoir identifier correctement et plus simplement le cas
                move_d(p)
                move += ['D']
            if p[3][6] == 'Y':
                # print("Cas double chaise")
                move += chair(p)
                move_d(p)
                move_d(p)
                move += ['D2']
                move += chair(p)
            else:
                # print("Cas chaise/anti-chaise")
                move += chair(p)
                move += anti_chair(p)

        case 3:  # on distingue 2 cas différents si nonyellow==3
            if p[1][8] == 'Y' or p[2][8] == 'Y':
                # tourne la face jaune de telle sorte à pouvoir identifier correctement et plus simplement le cas
                # print("Ca pointe vers la droite")
                while p[1][8] == 'Y':
                    move_d(p)
                    move += ['D']
                move += anti_chair(p)
                move_d(p)
                move += ['D']
                move += chair(p)
            else:
                # print("Ca pointe vers la gauche")
                while p[1][6] == 'Y':
                    move_d(p)
                    move += ['D']
                move += anti_chair(p)
                move_dp(p)
                move += ["D'"]
                move += chair(p)
    return move
