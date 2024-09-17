from cube import *


def create_main_menu(main_menu, scene_handler):
    # ce button permet d'aller au mode libre (cube_scene)
    Button(parent=main_menu, text='Mode libre', scale=(0.3, 0.15), position=(0, 0.2),
           on_click=Func(setattr, scene_handler, 'state', 'cube_scene'))
    # ce button permet d'aller au menu des motifs (pattern_menu)
    Button(parent=main_menu, text='Motif', scale=(0.3, 0.15), position=(0, -0.2),
           on_click=Func(setattr, scene_handler, 'state', 'pattern_menu'))
    # ce button permet d'aller au menu de mélange (shuffle_menu)
    Button(parent=main_menu, text='Mélange', scale=(0.3, 0.15), position=(0, 0),
           on_click=Func(setattr, scene_handler, 'state', 'shuffle_menu'))
    # ce button permet d'aller aux règles (rules_scene)
    Button(parent=main_menu, text='?', radius=0.5, scale=(0.1, 0.1), position=(-0.75, -0.4),
           on_click=Func(setattr, scene_handler, 'state', 'rules_scene'))
