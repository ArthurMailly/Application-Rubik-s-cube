from ursina import *


def create_pattern_menu(pattern_menu, scene_handler):
    # ce bouton permet de retoruner au menu principal (main_menu)
    Button(parent=pattern_menu, text='Retour', scale=(0.2, 0.1), position=(0.7, 0.4),
           on_click=Func(setattr, scene_handler, 'state', 'main_menu'))
    # tous les boutons suivants permettent d'aller aux scenes motif1, motif2...
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif1.png',
           position=(-0.7, 0.15),
           highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern1'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif2.png',
           position=(-0.35, 0.15),
           highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern2'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif3.png',
           position=(0, 0.15),
           highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern3'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif4.png',
           position=(0.35, 0.15),
           highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern4'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif5.png',
           position=(0.7, 0.15),
           highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern5'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif6.png',
           position=(-0.7, -0.2),
           highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern6'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif7.png',
           position=(-0.35, -0.2),
           highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern7'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif8.png',
           position=(0, -0.2), highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern8'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif9.png',
           position=(0.35, -0.2), highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern9'))
    Button(parent=pattern_menu, scale=0.3, color=color.white, texture='motif10.png',
           position=(0.7, -0.2), highlight_color=color.gray, pressed_color=color.dark_gray,
           on_click=Func(setattr, scene_handler, 'state', 'pattern10'))
