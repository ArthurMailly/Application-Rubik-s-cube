from cube_template import *

def goodwritingscramble(scramble):  # compense les mouvements inutiles dans les solutions

    if len(scramble) >= 4:
        i = 0
        n = len(scramble) - 4
        while i < n:
            if (scramble[i] == scramble[i + 1] and scramble[i + 1] == scramble[i + 2]
                    and scramble[i + 2] == scramble[i + 3]):
                # si on a 4 fois le même mouvement à la suite, on les enlève tous les 4
                scramble.pop(i + 3)
                scramble.pop(i + 2)
                scramble.pop(i + 1)
                scramble.pop(i)
                n = n - 4
            i += 1

    if len(scramble) >= 3:
        i = 0
        n = len(scramble) - 2

        while i < n:
            if scramble[i] == scramble[i + 1] and scramble[i + 1] == scramble[i + 2]:
                # si on a 3 fois le même mouvement à la suite on le retire et on met un '
                scramble[i] += "'"
                scramble.pop(i + 2)
                scramble.pop(i + 1)
                n = n - 2
            i += 1

    if len(scramble) >= 2:

        i = 0
        n = len(scramble) - 1
        while i < n:
            if scramble[i] == scramble[i + 1] and scramble[i][-1] == '2':
                # si on a un cas de type F2 F2 alors ça s'annule
                scramble.pop(i + 1)
                scramble.pop(i)
                n = n - 2
            elif scramble[i] == scramble[i + 1]:
                # si on a deux fois le même mouvement alors on en retire un et on met un 2 à la suite
                scramble[i] = scramble[i][0] + '2'
                scramble.pop(i + 1)
                # print(scramble)
                n = n - 1
            elif scramble[i] == scramble[i + 1] + "'":  # si on a un cas de type F F' alors ça s'annule
                scramble.pop(i + 1)
                scramble.pop(i)
                n = n - 2
            elif scramble[i] + "'" == scramble[i + 1]:  # si on a un cas de type F' F alors ça s'annule
                scramble.pop(i + 1)
                scramble.pop(i)
                n = n - 2
            elif scramble[i][-1] == "2" and scramble[i+1][-1] == "'" and scramble[i][0] == scramble[i+1][0]:
                scramble[i] = scramble[i][0]
                scramble.pop(i+1)
            elif scramble[i][-1] == "'" and scramble[i+1][-1] == "2" and scramble[i][0] == scramble[i+1][0]:
                scramble[i] = scramble[i][0]
                scramble.pop(i+1)
            i += 1


def exchange(li):  # permet de creer les liste référentes
    ex = []
    for i in range(len(li)):
        ex.append([li[i][1], li[i][0], li[i][3], li[i][2]])
    return ex


def on2ndlayer(elem):  # donne les éléments qui se trouvent sur la deuxième couronne
    if elem[2][0] != 5 and elem[3][0] != 5:
        return True
    return False


def above(color, place):  # regarde la piece et là où elle se situe et renvoie si elle est bien placée ou non
    match color:
        case 'B':
            numcolor = 4
        case 'G':
            numcolor = 2
        case 'O':
            numcolor = 1
        case _:
            numcolor = 3
    if place == numcolor:
        return True
    return False


def initsplace(p, above, bellow):  # sert dans la construction de la premiere couronne
    move = []
    match [above, bellow]:  # on regarde la couleur du dessus et la couleur du dessous
        case ['B', 'R']:
            move_r(p)
            move_dp(p)
            move_rp(p)
            move.append('R')
            move.append("D'")
            move.append("R'")
        case ['R', 'B']:
            move_bp(p)
            move_d(p)
            move_b(p)
            move.append("B'")
            move.append('D')
            move.append('B')
        case ['B', 'O']:
            move_lp(p)
            move_d(p)
            move_l(p)
            move.append("L'")
            move.append('D')
            move.append('L')
        case ['O', 'B']:
            move_b(p)
            move_dp(p)
            move_bp(p)
            move.append('B')
            move.append("D'")
            move.append("B'")
        case ['R', 'G']:
            move_f(p)
            move_dp(p)
            move_fp(p)
            move.append('F')
            move.append("D'")
            move.append("F'")
        case ['G', 'R']:
            move_rp(p)
            move_d(p)
            move_r(p)
            move.append("R'")
            move.append('D')
            move.append('R')
        case ['O', 'G']:
            move_fp(p)
            move_d(p)
            move_f(p)
            move.append("F'")
            move.append('D')
            move.append('F')
        case ['G', 'O']:
            move_l(p)
            move_dp(p)
            move_lp(p)
            move.append('L')
            move.append("D'")
            move.append("L'")
    return move


def leave(p, placeleft, placeright):  # sert dans la construction de la premiere couronne

    move = []

    match [placeleft, placeright]:
        case [1, 2]:  # Si la piece est entre les faces orange et verte
            move_l(p)
            move_d(p)
            move_lp(p)
            move.append('L')
            move.append('D')
            move.append("L'")
        case [2, 1]:
            move_l(p)
            move_d(p)
            move_lp(p)
            move.append('L')
            move.append('D')
            move.append("L'")
        case [2, 3]:  # Si la piece est entre les faces verte et rouge
            move_rp(p)
            move_dp(p)
            move_r(p)
            move.append("R'")
            move.append("D'")
            move.append('R')
        case [3, 2]:
            move_rp(p)
            move_dp(p)
            move_r(p)
            move.append("R'")
            move.append("D'")
            move.append('R')
        case [3, 4]:  # Si le piece est entre les faces rouge et bleue
            move_bp(p)
            move_dp(p)
            move_b(p)
            move.append("B'")
            move.append("D'")
            move.append('B')
        case [4, 3]:
            move_bp(p)
            move_dp(p)
            move_b(p)
            move.append("B'")
            move.append("D'")
            move.append('B')
        case [1, 4]:  # Si la piece est entre les faces bleue et orange
            move_b(p)
            move_d(p)
            move_bp(p)
            move.append('B')
            move.append('D')
            move.append("B'")
        case [4, 1]:
            move_b(p)
            move_d(p)
            move_bp(p)
            move.append('B')
            move.append('D')
            move.append("B'")
    return move


def exchange_corner(li):  # Sert à donner toutes les possibilités des coins
    new_l = []
    for i in range(len(li)):
        new_l.append([li[i][2], li[i][0], li[i][1], li[i][5], li[i][3], li[i][4]])
    for i in range(len(li)):
        new_l.append([li[i][1], li[i][2], li[i][0], li[i][4], li[i][5], li[i][3]])
    return new_l


def exchange_yellow_corner(li):  # Sert à donner toutes les possibilités des coins jaunes
    new_l = []
    for i in range(len(li)):
        new_l.append([li[i][2], li[i][0], li[i][1], li[i][5], li[i][3], li[i][4]])
    for i in range(len(li)):
        new_l.append([li[i][1], li[i][2], li[i][0], li[i][4], li[i][5], li[i][3]])
    final = new_l.copy()

    for i in range(len(new_l)):
        final.append([new_l[i][1], new_l[i][2], new_l[i][0], new_l[i][3], new_l[i][4], new_l[i][5]])
        final.append([new_l[i][2], new_l[i][0], new_l[i][1], new_l[i][3], new_l[i][4], new_l[i][5]])
    return final
