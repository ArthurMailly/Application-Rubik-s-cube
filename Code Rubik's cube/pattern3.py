from cube import *


def create_pattern3(pattern3, scene_handler, rubik_camera):
    def print_pattern():
        # on affiche les lettres du motif
        sol_text.text = "U B2 R2 B2 L2 F2 R2 D' F2 L2 B F' L F2 D U' R2 F' L' R'"

    def open_pattern3():
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
        up(rubik, 0)
        back(rubik, 0)
        back(rubik, 0)
        right(rubik, 0)
        right(rubik, 0)
        back(rubik, 0)
        back(rubik, 0)
        left(rubik, 0)
        left(rubik, 0)
        face(rubik, 0)
        face(rubik, 0)
        right(rubik, 0)
        right(rubik, 0)
        down_p(rubik, 0)
        face(rubik, 0)
        face(rubik, 0)
        left(rubik, 0)
        left(rubik, 0)
        back(rubik, 0)
        face_p(rubik, 0)
        left(rubik, 0)
        face(rubik, 0)
        face(rubik, 0)
        down(rubik, 0)
        up_p(rubik, 0)
        right(rubik, 0)
        right(rubik, 0)
        face_p(rubik, 0)
        left_p(rubik, 0)
        right_p(rubik, 0)

    def close_pattern3():
        # on cache le texte car il doit etre activé que quand on clique sur le bouton
        sol_text.text = ' '
        # on desactive la camera
        rubik_camera.disable()
        # on détruit le cube
        destroy(globals().get('rubik'))

    # texte contenant la solution du mélange
    sol_text = Text(origin=(0, 7), scale=2, parent=pattern3)
    # bouton qui permet de retourner au menu des motifs
    Button(parent=pattern3, text='Retour Motif', scale=(0.2, 0.1), position=(0.7, 0.4),
           on_click=Func(setattr, scene_handler, 'state', 'pattern_menu'))
    # bouton qui permet d'afficher la solution du motif
    Button(parent=pattern3, text='Afficher la solution', scale=(0.3, 0.1), position=(0, 0.39), on_click=print_pattern)

    pattern3.on_enable = open_pattern3
    pattern3.on_disable = close_pattern3
