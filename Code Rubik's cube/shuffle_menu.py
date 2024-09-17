from ursina import *


def create_shuffle_menu(shuffle_menu, scene_handler):
    # ce bouton permet de retourner au menu principal
    Button(parent=shuffle_menu, text='Retour', scale=(0.2, 0.1), position=(0.7, 0.4),
           on_click=Func(setattr, scene_handler, 'state', 'main_menu'))
    # ce bouton permet d'aller à la scene mélange debutant
    Button(parent=shuffle_menu, text='Mélange débutant', scale=(0.3, 0.15), position=(0, 0.15),
           on_click=Func(setattr, scene_handler, 'state', 'scene_beginner'))
    # ce bouton permet d'aller à la scene mélange expert
    Button(parent=shuffle_menu, text='Mélange expert', scale=(0.3, 0.15), position=(0, -0.15),
           on_click=Func(setattr, scene_handler, 'state', 'scene_expert'))
