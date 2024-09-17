from cube import *

#cette fonction est créé au début et permet de créer la scene cube_scene
def create_cube_scene(cube_scene, scene_handler, rubik_camera):
    #ce button permet de retourner au menu principal
    Button(parent=cube_scene, text='Retour', scale=(0.2, 0.1), position=(0.7, 0.4),
           on_click=Func(setattr, scene_handler, 'state', 'main_menu'))

    def open_cube_scene():
        #le cube est créé
        globals().update({'rubik': create_cube()})
        #on modifie la rotation de la camera pour voir le cube légérement de profil
        rubik_camera.rotation = (10, -10, 0)
        #puis on active la camera du cube
        rubik_camera.enable()

    def close_cube_scene():
        rubik_camera.disable()
        destroy(globals().get('rubik'))

    cube_scene.on_enable = open_cube_scene
    cube_scene.on_disable = close_cube_scene
