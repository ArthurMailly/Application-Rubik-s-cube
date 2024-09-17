from cube_template import *


def countyellowcross(p):  # Compte les arrêtes jaunes qui sont tournées vers la face jaune
    yellow = [1, 3, 5, 7]
    c = 0
    for i in yellow:
        if p[5][i] == 'Y':  # Si l'arrête est jaune, on incrémente le compteur
            c += 1
    return c


def algoyellowcross(p):  # Algorithme de la croix jaune
    move_f(p)
    move_l(p)
    move_d(p)
    move_lp(p)
    move_dp(p)
    move_fp(p)
    return ['F', 'L', 'D', "L'", "D'", "F'"]


def solveyellowcross(p):  # Sert à reconnaître le cas
    count = countyellowcross(p)
    # print(count)
    move = []
    while count != 4:  # Tant que la croix jaune n'est pas faite, on recommence
        match count:
            case 0:  # cas où il n'y a qu'un point jaune: peut importe dans quel sens on fait l'algo, c'est équivalent
                move += algoyellowcross(p)
            case 2:  # cas où y a 2 arrêtes jaunes
                if p[5][1] == 'Y' and p[5][7] == 'Y':  # cas ligne verticale
                    move_d(p)
                    move += ['D']
                    move += algoyellowcross(p)
                elif p[5][3] == 'Y' and p[5][5] == 'Y':  # cas ligne horizontale
                    move += algoyellowcross(p)
                else:  # le seul cas qu'il reste avec count==2: le neuf heure
                    while p[5][5] != 'Y' or p[5][7] != 'Y':
                        move_d(p)
                        move += ['D']
                        # print('D')
                    # print("Sortie !")
                    move += algoyellowcross(p)
        count = countyellowcross(p)
        # print(count)
    return move
