from cube import *
from step1 import *
from step2 import *
from step3 import *
from step4 import *
from step5 import *
from step6 import *
from step7 import *
from annexes_solve import *


# cette fonction est créé au début et permet de créer la scene scene_beginner
def create_scene_beginner(scene_beginner, scene_handler, rubik_camera):
    def move_rubik(speed, list, rubik, delay_cube):  # permet de déplacer
        j = 0  # on initialise j, cette variable va permettre de modifier le "delay" dans les fonction invoque
        # pour que tous les mouvements ne se fassent pas tous en même temps
        for i in list:
            match i:
                case "L":
                    invoke(left, rubik, speed, delay=delay_cube * j)  # on appelle la fonction "left" avec rubik
                    # en parametre et avec une vitesse "speed" et un delai "delay_cube*j"
                    j += 1  # on ajoute 1 a la variable j pour ajouter 1 au "delay"
                case "L2":
                    invoke(left, rubik, speed, delay=delay_cube * j)
                    j += 1
                    invoke(left, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "L'":
                    invoke(left_p, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "R":
                    invoke(right, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "R2":
                    invoke(right, rubik, speed, delay=delay_cube * j)
                    j += 1
                    invoke(right, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "R'":
                    invoke(right_p, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "U":
                    invoke(up, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "U2":
                    invoke(up, rubik, speed, delay=delay_cube * j)
                    j += 1
                    invoke(up, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "U'":
                    invoke(up_p, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "D":
                    invoke(down, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "D2":
                    invoke(down, rubik, speed, delay=delay_cube * j)
                    j += 1
                    invoke(down, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "D'":
                    invoke(down_p, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "F":
                    invoke(face, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "F2":
                    invoke(face, rubik, speed, delay=delay_cube * j)
                    j += 1
                    invoke(face, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "F'":
                    invoke(face_p, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "B":
                    invoke(back, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "B2":
                    invoke(back, rubik, speed, delay=delay_cube * j)
                    j += 1
                    invoke(back, rubik, speed, delay=delay_cube * j)
                    j += 1
                case "B'":
                    invoke(back_p, rubik, speed, delay=delay_cube * j)
                    j += 1

    # cette fonction permet de résoudre le cube
    def solve_cube():
        # on détruit puis on crée un nouveau cube
        destroy(globals().get('rubik'))
        globals().update({'rubik': create_cube()})
        rubik_camera.rotation = (10, -10, 0)
        rubik = globals().get('rubik')
        # on empeche l'utilisateur de bouger les faces car le cube se résout
        rubik.ignore_input = True
        step = 1  # on initialise step à 1

        # cette fonction permet de calculer quand on pourra à nouveau afficher les boutons et les textes qui ont
        # été caché pendant la résolution (on veut les afficher à la fin de tous les mouvements)
        def delay_reset(step):
            n = len(step)
            for i in step:
                match i:
                    case "L2":
                        n += 1
                    case "R2":
                        n += 1
                    case "U2":
                        n += 1
                    case "D2":
                        n += 1
                    case "F2":
                        n += 1
                    case "B2":
                        n += 1
            return n

        # cette fonction permet d'afficher un nouveau mélange en réinitialisant tous les parametres
        def case_n():
            close_scene_beginner()
            open_scene_beginner()
            scene_beginner.input = input_scene_beginner1

        # cette fonction permet de faire bouger le cube pour le résoudre
        def case_space():
            nonlocal step
            button_back.visible = False
            n_text.visible = False
            n_text2.visible = False
            scene_beginner.ignore_input = True
            space_text.visible = False
            if step == 1:  # dans ce cas on déclenche l'étape 2
                step_text.text = "2ème couronne"
                shuffle_text.text = display_shuffle(step2)  # on affiche les mouvements de l'étape
                shuffle_text.visible = True
                move_rubik(5, step2, rubik, 1.5)  # on fait bouger le cube
                n = delay_reset(step2)
                invoke(active_button, delay=n * 1.5)  # à la fin on réactive ce qui doit être activé
                step += 1
            # pareil pour toutes les autres étapes
            elif step == 2:
                step_text.text = "1ère couronne"
                if len(step3) < 20:  # cette étape est souvent longue alors on l'affiche en 2 fois si c'est le cas
                    shuffle_text.text = display_shuffle(step3)
                else:
                    shuffle_text2.visible = True
                    shuffle_text2.text = display_shuffle(step3[0:len(step3) // 2])
                    shuffle_text.text = display_shuffle(step3[len(step3) // 2:])
                shuffle_text.visible = True
                move_rubik(5, step3, rubik, 1.5)
                n = delay_reset(step3)
                invoke(active_button, delay=n * 1.5)
                step += 1
            elif step == 3:
                step_text.text = "croix jaune"
                shuffle_text.text = display_shuffle(step4)
                shuffle_text.visible = True
                move_rubik(5, step4, rubik, 1.5)
                n = delay_reset(step4)
                invoke(active_button, delay=n * 1.5)
                step += 1
            elif step == 4:
                step_text.text = "placement des coins"
                shuffle_text.text = display_shuffle(step5)
                shuffle_text.visible = True
                move_rubik(5, step5, rubik, 1.5)
                n = delay_reset(step5)
                invoke(active_button, delay=n * 1.5)
                step += 1
            elif step == 5:
                step_text.text = "face jaune"
                shuffle_text.text = display_shuffle(step6)
                shuffle_text.visible = True
                move_rubik(5, step6, rubik, 1.5)
                n = delay_reset(step6)
                invoke(active_button, delay=n * 1.5)
                step += 1
            elif step == 6:
                step_text.text = "3ème couronne"
                shuffle_text.text = display_shuffle(step7)
                shuffle_text.visible = True
                move_rubik(5, step7, rubik, 1.5)
                n = delay_reset(step7)
                invoke(active_button, delay=n * 1.5)
                step += 1

        # cette fonction permet de changer l'input car on à besoin d'utiliser la touche espace pendant la résolution
        def input_scene_beginner2(key):
            if key == 'space':
                case_space()
            elif key == 'n':
                case_n()

        # cette fonction permet des désactiver et réactiver ce qui doit l'être à la fin de chaque étape
        def active_button():
            scene_beginner.ignore_input = False
            if step != 7:  # step=7 quand le cube est résolu
                space_text.visible = True
                scene_beginner.input = input_scene_beginner2
            else:
                scene_beginner.input = input_scene_beginner1
                step_text.text = "cube terminé !"
            button_back.visible = True
            n_text.visible = True
            n_text2.visible = True
            shuffle_text.visible = False
            shuffle_text2.visible = False

        button_back.visible = False
        button_solve.visible = False
        n_text.visible = False
        n_text2.visible = False
        space_text.visible = False
        scene_beginner.ignore_input = True
        shuffle_button.visible = False
        reset_button.visible = False
        step_text.visible = True

        step_text.text = "croix blanche"
        move_rubik(0, shuffle_list, rubik, 0)  # affiche le mélange en 0 seconde
        shuffle_text.text = display_shuffle(step1)
        move_rubik(5, step1, rubik, 1.5)  # fait la premiere étape avec une vitesse "5"

        n1 = delay_reset(step1)
        invoke(active_button, delay=n1 * 1.5)  # appelle active_button quand l'etape est finie

    # cette fontion permet d'afficher le cube mélangé
    def switch_cube():
        # réinitialisation du cube:
        rubik_camera.disable()
        destroy(globals().get('rubik'))
        globals().update({'rubik': create_cube()})
        rubik_camera.rotation = (10, -10, 0)
        rubik_camera.enable()
        rubik = globals().get('rubik')
        rubik.ignore_input = True
        # affiche le mélange en 0 seconde
        move_rubik(0, shuffle_list, rubik, 0)
        shuffle_button.visible = False

    # cette fontion permet de réinitialiser le cube
    def reset_cube():
        rubik_camera.disable()
        destroy(globals().get('rubik'))
        globals().update({'rubik': create_cube()})
        rubik_camera.rotation = (10, -10, 0)
        rubik_camera.enable()
        shuffle_button.visible = True

    # création de tous les textes et les boutons :
    shuffle_text: Text = Text(origin=(0, -6), scale=2, parent=scene_beginner)
    shuffle_text2: Text = Text(origin=(0, -7), scale=2, parent=scene_beginner)
    step_text: Text = Text(position=(-0.8, 0.45), scale=2, parent=scene_beginner)
    button_back = Button(parent=scene_beginner, text='Retour', scale=(0.2, 0.1), position=(0.7, 0.4),
                         on_click=Func(setattr, scene_handler, 'state', 'shuffle_menu'))
    shuffle_button = Button(parent=scene_beginner, text='Appliquer \nle mélange', scale=(0.2, 0.1),
                            position=(-0.6, 0.1),
                            on_click=switch_cube)
    reset_button = Button(parent=scene_beginner, text='Réinitialiser \nle cube', scale=(0.2, 0.1),
                          position=(-0.6, -0.3), on_click=reset_cube)
    button_solve = Button(parent=scene_beginner, text='Résoudre le cube', scale=(0.2, 0.1), position=(0.6, -0.3),
                          on_click=solve_cube)
    n_text = Text(text='N', origin=(0, 0), color=color.white, x=0.65, y=0.1, scale=1.5, parent=scene_beginner)
    n_text2 = Text(text='changer le mélange', origin=(0, 0), color=color.white, x=0.65, y=0.05, scale=1.2,
                   parent=scene_beginner)

    space_text = Text(text="Appuie sur la barre espace pour passer à l'étape suivante", position=(-0.45, -0.3),
                      color=color.white, scale=1.5, parent=scene_beginner, visible=False)

    # tout ce qui est dans la fonction se déclenchera à l'ouverture de la scene
    def open_scene_beginner():
        global shuffle_list
        shuffle_list = shuffle()  # shuffle_list possède le mélange
        template = shuffle_template(shuffle_list)  # template est le patron mélangé
        shuffle_text.visible = True
        reset_button.visible = True
        # on crée step1,step2... qui contiennent les mouvements de chaque étape pour résoudre le cube
        global step1
        step1 = solvewhitecross(template)
        goodwritingscramble(step1)
        global step2
        step2 = solve2ndlayer(template)
        goodwritingscramble(step2)
        global step3
        step3 = solve1stlayer(template)
        goodwritingscramble(step3)
        global step4
        step4 = solveyellowcross(template)
        goodwritingscramble(step4)
        global step5
        step5 = solve_arrangement_yellow_corner(template)
        goodwritingscramble(step5)
        global step6
        step6 = solve_yellow_face(template)
        goodwritingscramble(step6)
        global step7
        step7 = solve_last_layer(template)
        goodwritingscramble(step7)

        shuffle_text.text = display_shuffle(shuffle_list)
        # on initialise le cube et les textes et boutons:
        globals().update({'rubik': create_cube()})
        rubik_camera.rotation = (10, -10, 0)
        rubik_camera.enable()
        button_solve.visible = True
        space_text.visible = False
        shuffle_button.visible = True
        shuffle_text2.visible = False
        step_text.visible = False

    # tout ce qui est dans la fonction se déclenchera à la fermeture de la scene
    def close_scene_beginner():
        # on détruit le cube
        rubik_camera.disable()
        destroy(globals().get('rubik'))

    scene_beginner.on_enable = open_scene_beginner
    scene_beginner.on_disable = close_scene_beginner

    # cette fonction permet de proposer en nouveau mélange quand on appuie sur "n" en fermant et réouvrant la scene
    def input_scene_beginner1(key):
        if key == 'n':
            close_scene_beginner()
            open_scene_beginner()

    scene_beginner.input = input_scene_beginner1
