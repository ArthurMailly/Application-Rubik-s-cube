from ursina import *


def create_rules_scene(rules_scene, scene_handler):
    # ce bouton permet de retourner au menu principal (main_menu)
    Button(parent=rules_scene, text='Retour', scale=(0.2, 0.1), position=(0.7, 0.4),
           on_click=Func(setattr, scene_handler, 'state', 'main_menu'))

    # cette entité permet d'afficher une photo
    Entity(parent=rules_scene, model='plane', enabled=True, rotation_x=-90, texture='faces.png')

    # ces textes expliques les regles des mouvements du cube
    Text(text='L : face de gauche (Left) sens horaire', color=color.white, position=(-0.8, 0.2), parent=rules_scene)
    Text(text="L' : face de gauche (Left) sens anti_horaire", color=color.white, position=(-0.8, 0.15),
         parent=rules_scene)
    Text(text='F : face de devant (Face) sens horaire', color=color.white, position=(-0.8, 0), parent=rules_scene)
    Text(text="F' : face de devant (Face) sens anti_horaire", color=color.white, position=(-0.8, -0.05),
         parent=rules_scene)
    Text(text='D : face du bas (Down) sens horaire', color=color.white, position=(-0.8, -0.2), parent=rules_scene)
    Text(text="D' : face du bas (Down) sens anti_horaire", color=color.white, position=(-0.8, -0.25),
         parent=rules_scene)
    Text(text='B : face de derriere (Back) sens horaire', color=color.white, position=(0.3, 0.2), parent=rules_scene)
    Text(text="B' : face du derriere (Back) sens anti_horaire", color=color.white, position=(0.3, 0.15),
         parent=rules_scene)
    Text(text='U : face du haut (Up) sens horaire', color=color.white, position=(0.3, 0), parent=rules_scene)
    Text(text="U' : face du haut (Up) sens anti_horaire", color=color.white, position=(0.3, -0.05),
         parent=rules_scene)
    Text(text='R : face de droite (Right) sens horaire', color=color.white, position=(0.3, -0.2), parent=rules_scene)
    Text(text="R' : face de droite (Right) sens anti_horaire", color=color.white, position=(0.3, -0.25),
         parent=rules_scene)
