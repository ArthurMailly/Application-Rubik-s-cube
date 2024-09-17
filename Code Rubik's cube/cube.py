from ursina import *

shift_hold = False


def create_cube():
    # cette liste contient toutes les couleurs des faces du cube
    couleurs_face = [color.red, color.orange, color.white, color.yellow, color.blue, color.green]

    # faire le modele de base (un cube contenant un carré par face)
    cube_de_base = Entity(enabled=False)  # pour ne pas l'afficher
    for i in range(3):
        # "direction" change 3 fois pour faire toutes les directions (1,0,0) , (0,1,0) et (0,0,1)
        direction = Vec3(0, 0, 0)
        direction[i] = 1

        # cube_face permet de créer un plan de couleur couleurs_face[i * 2] qui sera à la position direction/2 et qui
        # aura comme parent cube_de_base
        cube_face = Entity(parent=cube_de_base, model='plane', position=direction / 2, texture='white_cube',
                           color=couleurs_face[i * 2])
        cube_face.look_at(direction, 'up')

        # face_opp permet de créer un plan de couleur couleurs_face[(i * 2)+1] qui sera à la position -direction/2 et
        # qui aura comme parent cube_de_base (il représente la face opposée à cube_face)
        face_opp = Entity(parent=cube_de_base, model='plane', position=-direction / 2, texture='white_cube',
                          color=couleurs_face[(i * 2) + 1])
        face_opp.look_at(-direction, 'up')
    # .combine permet de combiner toutes les faces de façon à avoir une seule entité cube_de_base
    cube_de_base.combine()
    # on créé l'entité rubik
    rubik = Entity()
    for x in range(3):
        for y in range(3):
            for z in range(3):
                # on créé 27 cubes_de_base qui forment un cube de dimension 3x3x3, ces cubes ont pour parent rubik
                Entity(model=copy(cube_de_base.model), parent=rubik, position=Vec3(x - 1, y - 1, z - 1),
                       texture='white_cube')

    # cette fonction permet d'appeler les fonctions de déplacement (left(),right()...
    def input_rubik(key):

        global shift_hold
        match key:
            case 'shift':
                shift_hold = True
            case 'shift up':
                shift_hold = False
            case 'l':
                if shift_hold:
                    left_p(rubik)
                else:
                    left(rubik)
            case 'r':
                if shift_hold:
                    right_p(rubik)
                else:
                    right(rubik)
            case 'f':
                if shift_hold:
                    face_p(rubik)
                else:
                    face(rubik)
            case 'b':
                if shift_hold:
                    back_p(rubik)
                else:
                    back(rubik)
            case 'u':
                if shift_hold:
                    up_p(rubik)
                else:
                    up(rubik)
            case 'd':
                if shift_hold:
                    down_p(rubik)
                else:
                    down(rubik)
            case 'm':
                if shift_hold:
                    middle_p(rubik)
                else:
                    middle(rubik)

    rubik.input = input_rubik

    return rubik


# cette fonction permet que tous les éléments de la face de gauche redeviennent des enfants de rubik
def reset_rubik_world_parent(rubik, moved_cubes, rotation_entity):
    for i in moved_cubes:
        setattr(i, 'world_parent', rubik)
    destroy(rotation_entity)


# cette fonction permet de faire bouger toute la face de gauche de -90 degré (dans le sens trigo)
def left(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.x < 0:  # si le cube appartient à la face de gauche
            setattr(i, 'world_parent', rotation_entity)  # alors i devient un enfant de "world_parent"
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de -90 degré
    rotation_entity.animate('rotation_x', -90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de gauche redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de gauche de 90 degré (dans le sens horaire)
def left_p(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.x < 0:  # si le cube appartient à la face de gauche
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de 90 degré
    rotation_entity.animate('rotation_x', 90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de gauche redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de droite de 90 degré (dans le sens trigo)
def right(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.x > 0:  # si le cube appartient à la face de droite
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de 90 degré
    rotation_entity.animate('rotation_x', 90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de droite redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de droite de -90 degré (dans le sens horaire)
def right_p(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.x > 0:  # si le cube appartient à la face de droite
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de -90 degré
    rotation_entity.animate('rotation_x', -90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de droite redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de devant de 90 degré (dans le sens trigo)
def face(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.z < 0:  # si le cube appartient à la face de devant
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de 90 degré
    rotation_entity.animate('rotation_z', 90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de devant redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de devant de -90 degré (dans le sens horaire)
def face_p(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.z < 0:  # si le cube appartient à la face de devant
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de -90 degré
    rotation_entity.animate('rotation_z', -90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de devant redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de derriere de -90 degré (dans le sens trigo)
def back(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.z > 0:  # si le cube appartient à la face de derriere
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de -90 degré
    rotation_entity.animate('rotation_z', -90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de derriere redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de derriere de 90 degré (dans le sens horaire)
def back_p(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.z > 0:  # si le cube appartient à la face de derriere
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de 90 degré
    rotation_entity.animate('rotation_z', 90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # de derriere redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de derriere de 90 degré (dans le sens trigo)
def up(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.y > 0:  # si le cube appartient à la face d'en haut
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de 90 degré
    rotation_entity.animate('rotation_y', 90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # d'en haut redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de derriere de -90 degré (dans le sens horaire)
def up_p(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.y > 0:  # si le cube appartient à la face d'en haut
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de -90 degré
    rotation_entity.animate('rotation_y', -90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # d'en bas redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de derriere de -90 degré (dans le sens trigo)
def down(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.y < 0:  # si le cube appartient à la face d'en bas
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de -90 degré
    rotation_entity.animate('rotation_y', -90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # d'en bas redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


# cette fonction permet de faire bouger toute la face de derriere de 90 degré (dans le sens horaire)
def down_p(rubik, speed=1):
    # on créé une nouvelle entité et une liste
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:  # les cubes_de_base qui forment le cube rubik
        if i.y < 0:  # si le cube appartient à la face d'en bas
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)  # et on ajoute ce cube à la liste
    # on fait tourner tous les enfants de "rotation entity" de 90 degré
    rotation_entity.animate('rotation_y', 90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    # puis quand le cube a tourné on appelle la fonction reset_rubik_world_parent pour que tous les éléments de la face
    # d'en bas redeviennent des enfants de rubik
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)

#les fonctions suivantes fonctionnent comme les fonctions précédentes (mais nous ne les avons pas utilisées car se sont
# des mouvements utilisés par des experts)
def middle(rubik, speed=1):
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:
        if i.x == 0:
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)
    rotation_entity.animate('rotation_x', -90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)


def middle_p(rubik, speed=1):
    rotation_entity = Entity()
    moved_cubes = []
    for i in rubik.children:
        if i.x == 0:
            setattr(i, 'world_parent', rotation_entity)
            moved_cubes.append(i)
    rotation_entity.animate('rotation_x', 90, duration=speed * 0.15, curve=curve.linear, interrupt='finish')
    invoke(reset_rubik_world_parent, rubik, moved_cubes, rotation_entity, delay=speed * 0.2)
