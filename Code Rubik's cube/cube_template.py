import numpy as np

#P est représente un Rubik's cube résolu

P = np.array([['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], #face blanche
              ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], #face orange
              ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'], #face verte
              ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'], #face rouge
              ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], #face bleue
              ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]) #face jaune


def display_cube(c): #Afficher le patron du cube pour aider au développement 
    for k in range(3):
        print("\t\t\t\t||\t", end="")
        for j in range(3 * k, 3 * k + 3):
            print(c[0, j], end='\t') #affichage de la face blanche, qui sera tout en haut
        print('||\n')

    for k in range(3):
        print("||", end="\t")
        for i in range(1, 5):
            for j in range(3 * k, 3 * k + 3):
                print(c[i, j], end='\t') #affichage des faces orange, verte, rouge et bleue, qui se situeront en dessous de la blanche
            print('||', end='\t')
        print("\n")

    for k in range(3):
        print("\t\t\t\t||\t", end="")
        for j in range(3 * k, 3 * k + 3):
            print(c[5, j], end='\t') #affichage de la face jaune qui sera en bas
        print('||\n')

#clockwise et anticlockwise servent à permuter les éléments d'une même face lors d'un mouvement

def clockwise(c, i): #sert pour les mouvements sans ' tel que F
    c[i, 0], c[i, 2], c[i, 6], c[i, 8] = c[i, 6], c[i, 0], c[i, 8], c[i, 2]

    c[i, 1], c[i, 3], c[i, 5], c[i, 7] = c[i, 3], c[i, 7], c[i, 1], c[i, 5]


def anticlockwise(c, i): #sert pour les mouvements avec un ' tel que F'
    c[i, 6], c[i, 8], c[i, 2], c[i, 0] = c[i, 0], c[i, 6], c[i, 8], c[i, 2]

    c[i, 3], c[i, 7], c[i, 1], c[i, 5] = c[i, 1], c[i, 3], c[i, 5], c[i, 7]


def move_r(c): #R

    #permutation des couleurs qui n'appartiennent pas à la face rouge mais qui subissent tout de même des conséquences due au mouvement R
    c[0, 2], c[0, 5], c[0, 8], c[2, 2], c[2, 5], c[2, 8], c[4, 0], c[4, 3], c[4, 6], c[5, 2], c[5, 5], c[5, 8] = c[
        2, 2], c[2, 5], c[2, 8], c[5, 2], c[5, 5], c[5, 8], c[0, 8], c[0, 5], c[0, 2], c[4, 6], c[4, 3], c[4, 0]

    clockwise(c, 3) #permutations des couleurs de la face rouge


def move_rp(c): #R'
    c[2, 2], c[2, 5], c[2, 8], c[5, 2], c[5, 5], c[5, 8], c[0, 8], c[0, 5], c[0, 2], c[4, 6], c[4, 3], c[4, 0] = c[
        0, 2], c[0, 5], c[0, 8], c[2, 2], c[2, 5], c[2, 8], c[4, 0], c[4, 3], c[4, 6], c[5, 2], c[5, 5], c[5, 8]

    anticlockwise(c, 3)


def move_l(c): #L
    c[0, 0], c[0, 3], c[0, 6], c[2, 0], c[2, 3], c[2, 6], c[5, 0], c[5, 3], c[5, 6], c[4, 2], c[4, 5], c[4, 8] = c[
        4, 8], c[4, 5], c[4, 2], c[0, 0], c[0, 3], c[0, 6], c[2, 0], c[2, 3], c[2, 6], c[5, 6], c[5, 3], c[5, 0]

    clockwise(c, 1)


def move_lp(c): #L'
    c[4, 8], c[4, 5], c[4, 2], c[0, 0], c[0, 3], c[0, 6], c[2, 0], c[2, 3], c[2, 6], c[5, 6], c[5, 3], c[5, 0] = c[
        0, 0], c[0, 3], c[0, 6], c[2, 0], c[2, 3], c[2, 6], c[5, 0], c[5, 3], c[5, 6], c[4, 2], c[4, 5], c[4, 8]

    anticlockwise(c, 1)


def move_f(c): #F
    c[0, 6], c[0, 7], c[0, 8], c[1, 2], c[1, 5], c[1, 8], c[3, 0], c[3, 3], c[3, 6], c[5, 0], c[5, 1], c[5, 2] = c[
        1, 8], c[1, 5], c[1, 2], c[5, 0], c[5, 1], c[5, 2], c[0, 6], c[0, 7], c[0, 8], c[3, 6], c[3, 3], c[3, 0]

    clockwise(c, 2)


def move_fp(c): #F'
    c[1, 8], c[1, 5], c[1, 2], c[5, 0], c[5, 1], c[5, 2], c[0, 6], c[0, 7], c[0, 8], c[3, 6], c[3, 3], c[3, 0] = c[
        0, 6], c[0, 7], c[0, 8], c[1, 2], c[1, 5], c[1, 8], c[3, 0], c[3, 3], c[3, 6], c[5, 0], c[5, 1], c[5, 2]

    anticlockwise(c, 2)


def move_b(c): #B
    c[0, 0], c[0, 1], c[0, 2], c[1, 0], c[1, 3], c[1, 6], c[3, 2], c[3, 5], c[3, 8], c[5, 6], c[5, 7], c[5, 8] = c[
        3, 2], c[3, 5], c[3, 8], c[0, 2], c[0, 1], c[0, 0], c[5, 8], c[5, 7], c[5, 6], c[1, 0], c[1, 3], c[1, 6]

    clockwise(c, 4)


def move_bp(c): #B'
    c[3, 2], c[3, 5], c[3, 8], c[0, 2], c[0, 1], c[0, 0], c[5, 8], c[5, 7], c[5, 6], c[1, 0], c[1, 3], c[1, 6] = c[
        0, 0], c[0, 1], c[0, 2], c[1, 0], c[1, 3], c[1, 6], c[3, 2], c[3, 5], c[3, 8], c[5, 6], c[5, 7], c[5, 8]

    anticlockwise(c, 4)


def move_u(c): #U
    c[1, 0], c[1, 1], c[1, 2], c[2, 0], c[2, 1], c[2, 2], c[3, 0], c[3, 1], c[3, 2], c[4, 0], c[4, 1], c[4, 2] = c[
        2, 0], c[2, 1], c[2, 2], c[3, 0], c[3, 1], c[3, 2], c[4, 0], c[4, 1], c[4, 2], c[1, 0], c[1, 1], c[1, 2]

    clockwise(c, 0)


def move_up(c): #U'
    c[2, 0], c[2, 1], c[2, 2], c[3, 0], c[3, 1], c[3, 2], c[4, 0], c[4, 1], c[4, 2], c[1, 0], c[1, 1], c[1, 2] = c[
        1, 0], c[1, 1], c[1, 2], c[2, 0], c[2, 1], c[2, 2], c[3, 0], c[3, 1], c[3, 2], c[4, 0], c[4, 1], c[4, 2]

    anticlockwise(c, 0)


def move_d(c): #D
    c[1, 6], c[1, 7], c[1, 8], c[2, 6], c[2, 7], c[2, 8], c[3, 6], c[3, 7], c[3, 8], c[4, 6], c[4, 7], c[4, 8] = c[
        4, 6], c[4, 7], c[4, 8], c[1, 6], c[1, 7], c[1, 8], c[2, 6], c[2, 7], c[2, 8], c[3, 6], c[3, 7], c[3, 8]

    clockwise(c, 5)


def move_dp(c): #D'
    c[4, 6], c[4, 7], c[4, 8], c[1, 6], c[1, 7], c[1, 8], c[2, 6], c[2, 7], c[2, 8], c[3, 6], c[3, 7], c[3, 8] = c[
        1, 6], c[1, 7], c[1, 8], c[2, 6], c[2, 7], c[2, 8], c[3, 6], c[3, 7], c[3, 8], c[4, 6], c[4, 7], c[4, 8]

    anticlockwise(c, 5)
