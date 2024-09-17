from shuffle import *
from cube_template import *


def shuffle_template(s): #sert à mélanger un cube
    #s est ici un mélange obtenu grâce à shuffle, il s'agit donc d'une liste
    patron = P.copy() #On prend un patron d'un cube résolu
    for i in range(len(s)): #pour chaque élément de la liste, on va regarder quel est le mouvement indiqué et l'appliquer au patron
        match s[i]:
            case 'L':
                move_l(patron)
            case "L'":
                move_lp(patron)
            case 'L2':
                move_l(patron)
                move_l(patron)
            case 'R':
                move_r(patron)
            case "R'":
                move_rp(patron)
            case 'R2':
                move_r(patron)
                move_r(patron)
            case 'U':
                move_u(patron)
            case "U'":
                move_up(patron)
            case 'U2':
                move_u(patron)
                move_u(patron)
            case 'D':
                move_d(patron)
            case "D'":
                move_dp(patron)
            case 'D2':
                move_d(patron)
                move_d(patron)
            case 'F':
                move_f(patron)
            case "F'":
                move_fp(patron)
            case 'F2':
                move_f(patron)
                move_f(patron)
            case 'B':
                move_b(patron)
            case "B'":
                move_bp(patron)
            case 'B2':
                move_b(patron)
                move_b(patron)
    return patron #patron est le patron d'un Rubik's cube mélangé
