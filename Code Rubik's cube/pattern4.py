from cube import *


def create_pattern4(pattern4, scene_handler, rubik_camera):
    def print_pattern():
        # on affiche les lettres du motif
        sol_text.text = "U' L' U' F' R2 B' R F U B2 U B' L U' F U R F'"

    def open_pattern4():
        # on modifie la rotation du cube
        rubik_camera.rotation = (10, -10, 0)
        # puis on active la camera du cube
        rubik_camera.enable()
        # on créé le cube
        globals().update({'rubik': create_cube()})
        rubik = globals().get('rubik')
        # on ignore l'input car l'utilisateur ne doit plus pouvoir utiliser les fonctions left...
        rubik.ignore_input = True
        # les mouvements suivants forment le motif
        up_p(rubik, 0)
        left_p(rubik, 0)
        up_p(rubik, 0)
        face_p(rubik, 0)
        right(rubik, 0)
        right(rubik, 0)
        back_p(rubik, 0)
        right(rubik, 0)
        face(rubik, 0)
        up(rubik, 0)
        back(rubik, 0)
        back(rubik, 0)
        up(rubik, 0)
        back_p(rubik, 0)
        left(rubik, 0)
        up_p(rubik, 0)
        face(rubik, 0)
        up(rubik, 0)
        right(rubik, 0)
        face_p(rubik, 0)

    def close_pattern4():
        # on cache le texte car il doit etre activé que quand on clique sur le bouton
        sol_text.text = ' '
        # on desactive la camera
        rubik_camera.disable()
        # on détruit le cube
        destroy(globals().get('rubik'))

    # texte contenant la solution du mélange
    sol_text = Text(origin=(0, 7), scale=2, parent=pattern4)
    # bouton qui permet de retourner au menu des motifs
    Button(parent=pattern4, text='Retour Motif', scale=(0.2, 0.1), position=(0.7, 0.4),
           on_click=Func(setattr, scene_handler, 'state', 'pattern_menu'))
    # bouton qui permet d'afficher la solution du motif
    Button(parent=pattern4, text='Afficher la solution', scale=(0.3, 0.1), position=(0, 0.39), on_click=print_pattern)

    pattern4.on_enable = open_pattern4
    pattern4.on_disable = close_pattern4
