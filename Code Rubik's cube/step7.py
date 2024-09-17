from cube_template import *


def number_to_place_last_layer(p):  # On regarde le nombre de piece qui sont mal placées sur la derniere couronne
    last_layer = [1, 2, 3, 4]
    number = 0
    for i in last_layer:
        if p[i][7] != p[i][8]:
            number += 1
    return number


def algo_last_layer_right(p):  # Algorithme à droite
    move_lp(p)
    move_d(p)
    move_lp(p)
    move_dp(p)
    move_lp(p)
    move_dp(p)
    move_lp(p)
    move_d(p)
    move_l(p)
    move_d(p)
    move_l(p)
    move_l(p)
    return ["L'", 'D', "L'", "D'", "L'", "D'", "L'", 'D', 'L', 'D', 'L2']


def algo_last_layer_left(p):  # Algorithme à gauche
    move_r(p)
    move_dp(p)
    move_r(p)
    move_d(p)
    move_r(p)
    move_d(p)
    move_r(p)
    move_dp(p)
    move_rp(p)
    move_dp(p)
    move_r(p)
    move_r(p)
    return ['R', "D'", 'R', 'D', 'R', 'D', 'R', "D'", "R'", "D'", 'R2']


def solve_last_layer(p):
    move = []
    if number_to_place_last_layer(
            p) == 4:  # S'il y a 4 pieces de mal placées alors il faut effectué l'algorithme une fois
        # de telle sorte à retomber dans le cas où il n'y en ait que 3
        move += algo_last_layer_right(p)
        # print("Il y a 4 !")
    if number_to_place_last_layer(p) == 3:  # S'il n'y a que trois pieces de mal placées
        while p[2][6] != p[2][7]:
            # alors on tourne la face jaune de telle sorte à ce que l'on ait la face à modifiée en face de nous
            move_d(p)
            move += ['D']
        condition_right = ([p[1][6], p[1][7]] == ['O', 'R'] or [p[1][6], p[1][7]] == ['R', 'O']
                           or [p[1][6], p[1][7]] == ['B', 'G'] or [p[1][6], p[1][7]] == ['G', 'B'])
        match [p[1][6], p[1][7]]:
            # on regarde les couleurs de la face de droite pour savoir si l'on effectue l'algorithme à droite
            case _ if condition_right:
                move += algo_last_layer_right(p)
            case _:
                # si on ne se trouve pas dans l'un des cas précédents c'est qu'il faut effectuer l'algorithme à gauche
                move += algo_last_layer_left(p)

    while p[2][7] != p[2][4]:  # On tourne la derniere couronne de telle sorte à ce que le cube soit terminé
        move_d(p)
        move += ['D']

    return move
