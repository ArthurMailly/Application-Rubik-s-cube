from cube_template import *


def white_edge(P):
    A = [1, 3, 5, 7]
    white = []
    for i in range(len(P)):
        for j in A:
            if P[i][j] == 'W':
                white.append([i, j])
    return white


def colorofwhitepieces(P):
    white = white_edge(P)
    for i in range(len(white)):
        match white[i][1]:
            case 1:
                match white[i][0]:
                    case 0:
                        white[i].append(P[4][1])
                    case 1:
                        white[i].append(P[0][3])
                    case 2:
                        white[i].append(P[0][7])
                    case 3:
                        white[i].append(P[0][5])
                    case 4:
                        white[i].append(P[0][1])
                    case 5:
                        white[i].append(P[2][7])

            case 3:
                match white[i][0]:
                    case 0:
                        white[i].append(P[1][1])
                    case 1:
                        white[i].append(P[4][5])
                    case 2:
                        white[i].append(P[1][5])
                    case 3:
                        white[i].append(P[2][5])
                    case 4:
                        white[i].append(P[3][5])
                    case 5:
                        white[i].append(P[1][7])

            case 5:
                match white[i][0]:
                    case 0:
                        white[i].append(P[3][1])
                    case 1:
                        white[i].append(P[2][3])
                    case 2:
                        white[i].append(P[3][3])
                    case 3:
                        white[i].append(P[4][3])
                    case 4:
                        white[i].append(P[1][3])
                    case 5:
                        white[i].append(P[3][7])

            case 7:
                match white[i][0]:
                    case 0:
                        white[i].append(P[2][1])
                    case 1:
                        white[i].append(P[5][3])
                    case 2:
                        white[i].append(P[5][1])
                    case 3:
                        white[i].append(P[5][5])
                    case 4:
                        white[i].append(P[5][7])
                    case 5:
                        white[i].append(P[4][7])
    return white


def flower(P):
    move = []
    white = colorofwhitepieces(P)
    yellow = [False, False, False, False]  # arrangement: [1,3,5,7]
    for i in range(len(white)):
        if white[i][0] == 5:
            yellow[(white[i][1]) // 2] = True
    for i in range(4 - sum(yellow)):
        white = colorofwhitepieces(P)
        k = 0  # indice qui n'a pas son blanc vers la face jaune
        while white[k][0] == 5 and k < 3:
            k += 1
        pos = white[k][1]
        match white[k][0]:
            case 0:  # si il est sur la face blanche
                if pos == 1 or pos == 7:
                    if pos == 1 and P[5][7] == "W":
                        while P[5][7] == "W":
                            move_d(P)
                            move.append("D")
                    if pos == 7 and P[5][1] == "W":
                        while P[5][1] == "W":
                            move_d(P)
                            move.append("D")
                elif P[5][pos] == "W":
                    while P[5][pos] == "W":
                        move_d(P)
                        move.append("D")
                match pos:
                    case 1:
                        move_b(P)
                        move_b(P)
                        move.append("B2")
                    case 3:
                        move_l(P)
                        move_l(P)
                        move.append("L2")
                    case 5:
                        move_r(P)
                        move_r(P)
                        move.append("R2")
                    case 7:
                        move_f(P)
                        move_f(P)
                        move.append("F2")

            case 1:  # S'il est sur la face orange
                match pos:
                    case 3:
                        while P[5][7] == "W":
                            move_d(P)
                            move.append("D")
                        move_b(P)
                        move.append("B")
                    case 5:
                        while P[5][1] == "W":
                            move_d(P)
                            move.append("D")
                        move_fp(P)
                        move.append("F'")
                    case 1:
                        while P[5][1] == "W":
                            move_d(P)
                            move.append("D")
                        move_l(P)
                        move_fp(P)
                        move.append("L")
                        move.append("F'")
                        if P[4][5] == "W":  # Si on a déplacé un blanc en voulant insérer celui en cours, on le replace
                            move_lp(P)
                            move.append("L'")
                    case 7:
                        move_lp(P)
                        move.append("L'")
                        while P[5][1] == "W":
                            move_d(P)
                            move.append("D")
                        move_fp(P)
                        move.append("F'")

            case 2:  # S'il est sur la face verte
                match pos:
                    case 3:
                        while P[5][3] == "W":
                            move_d(P)
                            move.append("D")
                        move_l(P)
                        move.append("L")
                    case 5:
                        while P[5][5] == "W":
                            move_d(P)
                            move.append("D")
                        move_rp(P)
                        move.append("R'")
                    case 1:
                        while P[5][5] == "W":
                            move_d(P)
                            move.append("D")
                        move_f(P)
                        move_rp(P)
                        move.append("F")
                        move.append("R'")
                        if P[1][5] == "W":  # Si on a déplacé un blanc en voulant insérer celui en cours, on le replace
                            move_fp(P)
                            move.append("F'")
                    case 7:
                        move_fp(P)
                        move.append("F'")
                        while P[5][5] == "W":
                            move_d(P)
                            move.append("D")
                        move_rp(P)
                        move.append("R'")
            case 3:  # Si le blanc est sur la face rouge
                match pos:
                    case 3:
                        while P[5][1] == "W":
                            move_d(P)
                            move.append("D")
                        move_f(P)
                        move.append("F")
                    case 5:
                        while P[5][7] == "W":
                            move_d(P)
                            move.append("D")
                        move_bp(P)
                        move.append("B'")
                    case 1:
                        while P[5][1] == "W":
                            move_d(P)
                            move.append("D")
                        move_rp(P)
                        move_f(P)
                        move.append("R'")
                        move.append("F")
                        if P[4][3] == "W":  # Si on a déplacé un blanc en voulant insérer celui en cours, on le replace
                            move_r(P)
                            move.append("R")
                    case 7:
                        move_r(P)
                        move.append("R")
                        while P[5][1] == "W":
                            move_d(P)
                            move.append("D")
                        move_f(P)
                        move.append("F")

            case 4:  # Si le blanc est sur la face bleue
                match pos:
                    case 3:
                        while P[5][5] == "W":
                            move_d(P)
                            move.append("D")
                        move_r(P)
                        move.append("R")
                    case 5:
                        while P[5][3] == "W":
                            move_d(P)
                            move.append("D")
                        move_lp(P)
                        move.append("L'")
                    case 1:
                        while P[5][3] == "W":
                            move_d(P)
                            move.append("D")
                        move_b(P)
                        move_lp(P)
                        move.append("B")
                        move.append("L'")
                        if P[3][5] == "W":  # Si on a déplacé un blanc en voulant insérer celui en cours, on le replace
                            move_bp(P)
                            move.append("B'")
                    case 7:
                        move_bp(P)
                        move.append("B'")
                        while P[5][3] == "W":
                            move_d(P)
                            move.append("D")
                        move_lp(P)
                        move.append("L'")

    return move


def solvewhitecross(P):
    move = flower(P)
    whitepos = [False, False, False, False]  # Arrangement [Orange, Green, Red, Blue]
    while whitepos != [True, True, True, True]:
        for i in range(4):
            white = colorofwhitepieces(P)
            if white[i][1] == 3 and white[i][2] == 'O' and whitepos[0] == False:
                move_l(P)
                move_l(P)
                move.append("L2")
                whitepos[0] = True
            elif white[i][1] == 1 and white[i][2] == 'G' and whitepos[1] == False:
                move_f(P)
                move_f(P)
                move.append("F2")
                whitepos[1] = True
            elif white[i][1] == 5 and white[i][2] == 'R' and whitepos[2] == False:
                move_r(P)
                move_r(P)
                move.append("R2")
                whitepos[2] = True
            elif white[i][1] == 7 and white[i][2] == 'B' and whitepos[3] == False:
                move_b(P)
                move_b(P)
                move.append("B2")
                whitepos[3] = True
        if whitepos != [True, True, True, True]:
            move_d(P)
            move.append("D")
    return move
