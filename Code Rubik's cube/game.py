from ursina import *
# on importe toutes les scenes
from main_menu import create_main_menu
from cube_scene import create_cube_scene
from pattern_menu import create_pattern_menu
from pattern1 import create_pattern1
from pattern2 import create_pattern2
from pattern3 import create_pattern3
from pattern4 import create_pattern4
from pattern5 import create_pattern5
from pattern6 import create_pattern6
from pattern7 import create_pattern7
from pattern8 import create_pattern8
from pattern9 import create_pattern9
from pattern10 import create_pattern10
from shuffle_menu import create_shuffle_menu
from scene_beginner import create_scene_beginner
from rules_scene import create_rules_scene
from scene_expert import create_scene_expert

app = Ursina()
application.hot_reloader.disable()
window.input_entity.disable()
window.collider_counter.disable()
window.entity_counter.disable()
window.fps_counter.disable()
window.cog_button.disable()




# on initialise la camera à false (car dans le menu principal on ne dot pas pouvoir modifier la camera)
rubik_camera = EditorCamera(enabled=False)
# on a desactivé les parametres suivants car certains (comme focus) avait pour raccourcis des lettres comme (f) qui sont
# utilisées pour les fonctions (comme face)
rubik_camera.hotkeys = {'toggle_orthographic': '', 'focus': '', 'reset_center': ''}

# on créé des entités qui permettront de passer d'une scene à une autre
main_menu = Entity(parent=camera.ui, enabled=True)
cube_scene = Entity(parent=camera.ui, enabled=False)
pattern_menu = Entity(parent=camera.ui, enabled=False)
pattern1 = Entity(parent=camera.ui, enabled=False)
pattern2 = Entity(parent=camera.ui, enabled=False)
pattern3 = Entity(parent=camera.ui, enabled=False)
pattern4 = Entity(parent=camera.ui, enabled=False)
pattern5 = Entity(parent=camera.ui, enabled=False)
pattern6 = Entity(parent=camera.ui, enabled=False)
pattern7 = Entity(parent=camera.ui, enabled=False)
pattern8 = Entity(parent=camera.ui, enabled=False)
pattern9 = Entity(parent=camera.ui, enabled=False)
pattern10 = Entity(parent=camera.ui, enabled=False)
shuffle_menu = Entity(parent=camera.ui, enabled=False)
scene_beginner = Entity(parent=camera.ui, enabled=False)
scene_expert = Entity(parent=camera.ui, enabled=False)
rules_scene = Entity(parent=camera.ui, enabled=False)

# on met toutes les entités dans scene_handler qui permet de changer de scenes 
scene_handler = Animator(
    {'main_menu': main_menu, 'cube_scene': cube_scene, 'pattern_menu': pattern_menu, 'pattern1': pattern1,
     'pattern2': pattern2, 'pattern3': pattern3, 'pattern4': pattern4, 'pattern5': pattern5, 'pattern6': pattern6,
     'pattern7': pattern7, 'pattern8': pattern8, 'pattern9': pattern9, 'pattern10': pattern10,
     'shuffle_menu': shuffle_menu, 'scene_beginner': scene_beginner, 'scene_expert': scene_expert,
     'rules_scene': rules_scene})

# on créé toutes les scenes
create_main_menu(main_menu, scene_handler)
create_pattern_menu(pattern_menu, scene_handler)
create_pattern1(pattern1, scene_handler, rubik_camera)
create_pattern2(pattern2, scene_handler, rubik_camera)
create_pattern3(pattern3, scene_handler, rubik_camera)
create_pattern4(pattern4, scene_handler, rubik_camera)
create_pattern5(pattern5, scene_handler, rubik_camera)
create_pattern6(pattern6, scene_handler, rubik_camera)
create_pattern7(pattern7, scene_handler, rubik_camera)
create_pattern8(pattern8, scene_handler, rubik_camera)
create_pattern9(pattern9, scene_handler, rubik_camera)
create_pattern10(pattern10, scene_handler, rubik_camera)
create_cube_scene(cube_scene, scene_handler, rubik_camera)
create_scene_beginner(scene_beginner, scene_handler, rubik_camera)
create_shuffle_menu(shuffle_menu, scene_handler)
create_rules_scene(rules_scene, scene_handler)
create_scene_expert(scene_expert, scene_handler)

app.run()
