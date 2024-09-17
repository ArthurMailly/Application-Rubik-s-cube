import os
import locale

from ursina import *
from shuffle_template import *
from annexes import *
from shuffle import *
from datetime import datetime

# Set the locale to French
locale.setlocale(locale.LC_TIME, 'fr_FR')

def create_scene_expert(scene_expert, scene_handler):
    # on créé le bouton retour qui permet de retourner au menu melange (shuffle_menu)
    Button(parent=scene_expert, text='Retour', scale=(0.2, 0.1), position=(0.7, 0.4),
           on_click=Func(setattr, scene_handler, 'state', 'shuffle_menu'))

    def open_scene_expert():
        # on créé un parent pour tous les objets de cette scene
        globals().update({'parent_template': game()})

    def close_scene_expert():
        # on detruit ce parent
        destroy(globals().get('parent_template'))

    scene_expert.on_enable = open_scene_expert
    scene_expert.on_disable = close_scene_expert

    couleurs_face = [color.white, color.orange, color.green, color.red, color.blue, color.yellow]
    faces_list = []
    t_color = 54 * [0]

    def color_case(cas):
        match cas:
            case 'W':
                return faces_list[0]
            case 'O':
                return faces_list[1]
            case 'G':
                return faces_list[2]
            case 'R':
                return faces_list[3]
            case 'B':
                return faces_list[4]
            case _:
                return faces_list[5]

    for couleur in range(len(couleurs_face)):
        # Faire un carre blanc

        face = Entity(model='plane', position=-Vec3(0, 0, 1) / 2, texture='white_cube', color=couleurs_face[couleur],
                      scale=0.5, enabled=False)
        face.look_at(-Vec3(0, 0, 1), 'up')

        faces_list.append(face)

    def game():
        s = shuffle()
        template = shuffle_template(s)

        s = display_shuffle(s)

        comp = 0
        parent_template = Entity()
        text_scramble.text = s
        for i in range(3):
            for j in range(3):
                cube = Entity(parent=parent_template, model=copy(color_case(template[0][3 * j + i])),
                              position=((i - 0.3) * 0.5 - 1.5, -(j * 0.5) + 2),
                              texture='white_cube')
                t_color[comp] = cube
                comp += 1

        for k in range(4):
            for i in range(3):
                for j in range(3):
                    cube = Entity(parent=parent_template, model=copy(color_case(template[k + 1][3 * j + i])),
                                  position=(k * 1.5 + (i - 0.3) * 0.5 - 3, -j * 0.5 + 0.5), texture='white_cube')
                    t_color[comp] = cube
                    comp += 1

        for i in range(3):
            for j in range(3):
                cube = Entity(parent=parent_template, model=copy(color_case(template[5][3 * j + i])),
                              position=((i - 0.3) * 0.5 - 1.5, -(j * 0.5) - 1), texture='white_cube')
                t_color[comp] = cube
                comp += 1
        return parent_template

    timer_running = False
    timer_value = 0

    #timer_comp = 0
    
    timer_mean = 0
    text_stat=""

    timer_text = Text(parent=scene_expert, text=f'Temps: {timer_value:.3f}', y=.9, scale=2, origin=(0, 0),
                      color=color.white)
    text_timer = Text(parent=scene_expert, text='Barre espace pour commencer', origin=(0, 0),
                      color=color.white, x=0, y=-.4, scale=2)
    Text(parent=scene_expert, text='Mes statistiques :', origin=(0, 0), color=color.white, x=-0.7, y=0.25, scale=1.3)
    Text(parent=scene_expert, text='Appuie sur :', origin=(0, 0), color=color.white, x=0.6, y=0.25, scale=1.3)
    Text(parent=scene_expert, text='N', origin=(0, 0), color=color.white, x=0.6, y=0.1, scale=1.5)
    Text(parent=scene_expert, text='changer le mélange', origin=(0, 0), color=color.white, x=0.6, y=0.05, scale=1.2)
    #Text(parent=scene_expert, text='R', origin=(0, 0), color=color.white, x=0.6, y=-0.2, scale=1.5)
    #Text(parent=scene_expert, text='réinitialiser les statistiques', origin=(0, 0), color=color.white, x=0.6, y=-0.25,scale=1.2)
    Text(parent=scene_expert, text='D', origin=(0, 0), color=color.white, x=0.6, y=-0.05, scale=1.5)
    Text(parent=scene_expert, text='supprimer le dernier mélange', origin=(0, 0), color=color.white, x=0.6, y=-0.1,scale=1.2)
    text_scramble = Text(parent=scene_expert, text='', origin=(0.1, 0), color=color.white, y=.4, scale=2)

    text_pb = Text(parent=scene_expert, text='Meilleur: None', origin=(0, 0), color=color.white, x=-.7, y=.10,
                   scale=1.2)
    text_previous = Text(parent=scene_expert, text='Dernier mélange: None', origin=(0, 0), color=color.white, x=-.7,
                         y=.7, scale=1.2)
    text_worst = Text(parent=scene_expert, text='Pire: None', origin=(0, 0), color=color.white, x=-.7, y=.06,
                      scale=1.2)
    text_mean = Text(parent=scene_expert, text='Moyenne: None', origin=(0, 0), color=color.white, x=-.7, y=0,
                     scale=1.2)
    text_std = Text(parent=scene_expert, text='Ecart-type: None', origin=(0, 0), color=color.white, x=-.7, y=0.03,
                    scale=1.2)
    text_ao5 = Text(parent=scene_expert, text='Ao5: None', origin=(0, 0), color=color.white, x=-.7, y=-.09, scale=1.2)
    text_ao12 = Text(parent=scene_expert, text='Ao12: None', origin=(0, 0), color=color.white, x=-.7, y=-.12, scale=1.2)
    text_ao50 = Text(parent=scene_expert, text='Ao50: None', origin=(0, 0), color=color.white, x=-.7, y=-.15, scale=1.2)
    text_ao100 = Text(parent=scene_expert, text='Ao100: None', origin=(0, 0), color=color.white, x=-.7, y=-.18,
                      scale=1.2)
    textcomp = Text(parent=scene_expert, text="Résolution: 0", origin=(0, 0), color=color.white, x=-.7, y=-.24,
                    scale=1.2)

    #Times = []

    def search_stats():
        current_date = datetime.now().date()

        month = current_date.strftime("%B")
        year = current_date.strftime("%Y")
        folder_name = f'Temps {year}'
        file_name = f'{month}.txt'
        file_path = os.path.join(folder_name, file_name)

        try:
            # Create the folder if it doesn't exist
            os.mkdir(folder_name)

            # Create and write to the text file
            with open(file_path, 'w') as fichier_txt:
                fichier_txt.write("Voici vos statistiques:\n")

            print(f"File '{file_name}' created successfully in folder '{folder_name}'.")
        except OSError as error:
            print(f"Failed to create file '{file_name}': {error}")

        # Vérifiez si le fichier .txt existe déjà
        if not os.path.exists(file_path):
            # Créez le fichier .txt s'il n'existe pas
            with open(file_path, 'w') as fichier_txt:
                fichier_txt.write("Voici vos statistiques:\n")

            with open(file_path, 'r') as fichier_txt:
                contenu = fichier_txt.readlines()
        else:
            with open(file_path, 'r') as fichier_txt:
                contenu = fichier_txt.readlines()

        
        #print(len(contenu))
        compteur = len(contenu)

        contenu2=contenu[1:]

        T=[]

        if len(contenu2)>0:
            for i in range(len(contenu2)):
                contenu2[i]=contenu2[i].split("  ")
                T.append(float(contenu2[i][1]))

        fichier_txt.close()
        return compteur,T

    timer_comp,Times = search_stats()
    timer_comp -=1
    if timer_comp-1>=0:
        textcomp.text = f'Résolution: {timer_comp}'

        text_mean.text = f'Moyenne: {mean(Times):.3f}'
        if timer_comp >= 2:
            text_std.text = f'Ecart-type: {std(Times):.3f}'
            text_previous.text = f'Dernier mélange: {Times[-2]:.3f}'

        text_pb.text = f'Meilleur: {pbest(Times):.3f}'
        text_worst.text = f'Pire: {pworst(Times):.3f}'

        if timer_comp >= 5:
            text_ao5.text = f'Ao5: {ao(5, Times):.3f}'
        if timer_comp >= 12:
            text_ao12.text = f'Ao12: {ao(12, Times):.3f}'
        if timer_comp >= 50:
            text_ao50.text = f'Ao50: {ao(50, Times):.3f}'
        if timer_comp >= 100:
            text_ao100.text = f'Ao100: {ao(100, Times):.3f}'

    def update_stats(time):
        current_date = datetime.now().date()

        month = current_date.strftime("%B")
        year = current_date.strftime("%Y")
        folder_name = f'Temps {year}'
        file_name = f'{month}.txt'
        file_path = os.path.join(folder_name, file_name)

        try:
            # Create the folder if it doesn't exist
            os.mkdir(folder_name)

            # Create and write to the text file
            with open(file_path, 'w') as fichier_txt:
                fichier_txt.write("Voici vos statistiques:\n")

            print(f"File '{file_name}' created successfully in folder '{folder_name}'.")
        except OSError as error:
            print(f"Failed to create file '{file_name}': {error}")

        # Vérifiez si le fichier .txt existe déjà
        if not os.path.exists(file_path):
            # Créez le fichier .txt s'il n'existe pas
            with open(file_path, 'w') as fichier_txt:
                fichier_txt.write(f"{time}\n")
                print("Coucou")
        else:
            # Ouvrir le fichier en mode 'a' pour l'ajout
            with open(file_path, 'a') as fichier_ecriture:
                # Ajouter du contenu à la fin du fichier
                fichier_ecriture.write(f"{time}\n")
                print("Tamanoir")

            with open(file_path, 'r') as fichier_lecture:
                contenu = fichier_lecture.readlines()
            print(f'contenu = {contenu}')
            # Utilisez la fonction len() pour obtenir le nombre de lignes
            timer_comp = len(contenu)-1
            print(f"Il y a {timer_comp} lignes dans le fichier précédent.")
            fichier_lecture.close()
            fichier_ecriture.close()

    def delete_last_line():

        current_date = datetime.now().date()

        month = current_date.strftime("%B")
        year = current_date.strftime("%Y")
        folder_name = f'Temps {year}'
        file_name = f'{month}.txt'
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            if len(lines)>1:

                # Remove the last line
                if lines:
                    lines.pop()

                with open(file_path, 'w') as file:
                    file.writelines(lines)
        file.close()

    def change_first_line():

        current_date = datetime.now().date()

        month = current_date.strftime("%B")
        year = current_date.strftime("%Y")
        folder_name = f'Temps {year}'
        file_name = f'{month}.txt'
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        T=[]

        lines=lines[1:]

        for i in range(len(lines)):
            lines[i]=lines[i].split("  ")
            T.append(float(lines[i][1]))

        print(T)

        if len(T)==0:
            with open(file_path,'w') as file:
                file.writelines(f"Vous verrez bientôt ici vos statistiques pour {month} {year}!\n")
        elif len(T)==1:
            moy = mean(T)
            pb=pbest(T)
            pw=pworst(T)

            with open(file_path, 'r') as file:
                lines = file.readlines()
                lines[0] = f"Voici vos statistiques pour {month} {year}: Moyenne: {moy:.3f}  Meilleur temps: {pb}  Pire temps: {pw}\n"
            with open(file_path,'w') as file:
                file.writelines(lines)

        elif len(T)>=2 and len(T)<5:
            moy = mean(T)
            pb=pbest(T)
            pw=pworst(T)
            et=std(T)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()
                lines[0] = f"Voici vos statistiques pour {month} {year}: Moyenne: {moy:.3f}  Meilleur temps: {pb}  Pire temps: {pw}  Écart-type: {et:.3f}\n"
            with open(file_path,'w') as file:
                file.writelines(lines)

        elif len(T)>=5 and len(T)<12:
            moy = mean(T)
            pb=pbest(T)
            pw=pworst(T)
            et=std(T)
            a5=ao(5,T)
        
            with open(file_path, 'r') as file:
                lines = file.readlines()
                lines[0] = f"Voici vos statistiques pour {month} {year}: Moyenne: {moy:.3f}  Meilleur temps: {pb}  Pire temps: {pw}  Écart-type: {et:.3f}  ao5: {a5:.3f}\n"
            with open(file_path,'w') as file:
                file.writelines(lines)

        elif len(T)>=12 and len(T)<50:
            moy = mean(T)
            pb=pbest(T)
            pw=pworst(T)
            et=std(T)
            a5=ao(5,T)
            a12=ao(12,T)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()
                lines[0] = f"Voici vos statistiques pour {month} {year}: Moyenne: {moy:.3f}  Meilleur temps: {pb}  Pire temps: {pw}  Écart-type: {et:.3f}  ao5: {a5:.3f}  ao12: {a12:.3f}\n"
            with open(file_path,'w') as file:
                file.writelines(lines)

        elif len(T)>=50 and len(T)<100:
            moy = mean(T)
            pb=pbest(T)
            pw=pworst(T)
            et=std(T)
            a5=ao(5,T)
            a12=ao(12,T)
            a50=ao(50,T)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()
                lines[0] = f"Voici vos statistiques pour {month} {year}: Moyenne: {moy:.3f}  Meilleur temps: {pb}  Pire temps: {pw}  Écart-type: {et:.3f}  ao5: {a5:.3f}  ao12: {a12:.3f}  ao50: {a50:.3f}\n"
            with open(file_path,'w') as file:
                file.writelines(lines)

        elif len(T)>=100:
            moy = mean(T)
            pb=pbest(T)
            pw=pworst(T)
            et=std(T)
            a5=ao(5,T)
            a12=ao(12,T)
            a50=ao(50,T)
            a100=ao(100,T)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()
                lines[0] = f"Voici vos statistiques pour {month} {year}: Moyenne: {moy:.3f}  Meilleur temps: {pb}  Pire temps: {pw}  Écart-type: {et:.3f}  ao5: {a5:.3f}  ao12: {a12:.3f}  ao50: {a50:.3f}  ao100: {a100:.3f}\n"
            with open(file_path,'w') as file:
                file.writelines(lines)


    def update_template():
        nonlocal timer_running, timer_value, text_scramble, text_stat

        if timer_running:
            timer_value += time.dt
            text_stat=timer_value
            timer_text.text = f'Temps: {timer_value:.3f}'
            text_timer.text = " "
            text_timer.text = "Prêt ? ... c'est parti !"

        if held_keys['space']:
            timer_value = 0

    def input_template(key):
        nonlocal timer_running, timer_value, text_scramble, timer_comp, text_stat, Times

        if key == 'space':
            if not timer_running:
                timer_running = True

            else:
                timer_running = False
                timer_text.text = f'Temps: {timer_value:.3f}'
                text_timer.text = timer_text.text
                #Times.append(float(f'{timer_value:.3f}'))
                #timer_value = 0
                #timer_comp += 1
                timer_comp,Times = search_stats()
                Times.append(float(f'{timer_value:.3f}')) 
                print(f'Times = {Times}')
                print(f'timer_comp = {timer_comp}')
                #print(f"search_stats= {compteur}")
                textcomp.text = f'Résolution: {timer_comp}'
                current_date = datetime.now().date()

                minute = datetime.now().minute
                hour = datetime.now().hour
                day = current_date.strftime("%d")
                month = current_date.strftime("%B")
                year = current_date.strftime("%Y")

                update_stats(f'Temps {timer_comp}:  {text_stat:.3f}  Mélange:  {text_scramble.text}  Date: {day} {month} {year}  Heure: {hour}:{minute}')

                change_first_line()

                text_mean.text = f'Moyenne: {mean(Times):.3f}'
                if timer_comp >= 2:
                    text_std.text = f'Ecart-type: {std(Times):.3f}'
                    text_previous.text = f'Dernier mélange: {Times[-2]:.3f}'

                text_pb.text = f'Meilleur: {pbest(Times):.3f}'
                text_worst.text = f'Pire: {pworst(Times):.3f}'

                if timer_comp >= 5:
                    text_ao5.text = f'Ao5: {ao(5, Times):.3f}'
                if timer_comp >= 12:
                    text_ao12.text = f'Ao12: {ao(12, Times):.3f}'
                if timer_comp >= 50:
                    text_ao50.text = f'Ao50: {ao(50, Times):.3f}'
                if timer_comp >= 100:
                    text_ao100.text = f'Ao100: {ao(100, Times):.3f}'

        elif key == 'n' and timer_running == False:
            for i in range(len(t_color)):
                t_color[i].enabled = not t_color[i].enabled
            text_timer.text = 'Barre espace pour commencer'
            close_scene_expert()
            open_scene_expert()

#        elif key == 'r':
#            text_pb.text = 'Meilleur: None'
#            text_previous.text = 'Dernier mélange: None'
#            text_worst.text = 'Pire: None'
#            text_mean.text = 'Moyenne: None'
#            text_std.text = 'Ecart-type: None'

#            Times.clear()
#            timer_comp = 0

#            textcomp.text = "Résolution: 0"
#            text_timer.text = 'Barre espace pour commencer'
#            text_ao5.text = 'Ao5: None'
#            text_ao12.text = 'Ao12: None'
#            text_ao50.text = 'Ao50: None'
#            text_ao100.text = 'Ao100: None'

        elif key == 'd':
            if timer_comp >= 1:
                #del (Times[-1])
                delete_last_line()
                timer_comp, Times = search_stats()
                timer_comp -=1
                print(f"timer_comp = {timer_comp}")
                print(f"Times = {Times}")

                change_first_line()

                textcomp.text = f'Résolution: {timer_comp}'
                text_timer.text = 'Barre espace pour commencer'

                if timer_comp == 0:
                    text_mean.text = 'Moyenne: None'
                    text_pb.text = 'Meilleur: None'
                    text_worst.text = 'Pire: None'

                if timer_comp >= 1:
                    text_mean.text = f'Moyenne: {mean(Times):.3f}'
                    text_pb.text = f'Meilleur: {pbest(Times):.3f}'
                    text_worst.text = f'Pire: {pworst(Times):.3f}'

                if timer_comp == 1:
                    text_std.text = f'Ecart-type: None'
                    text_previous.text = 'Dernier mélange: None'

                if timer_comp >= 2:
                    text_std.text = f'Ecart-type: {std(Times):.3f}'
                    text_previous.text = f'Dernier mélange: {Times[-2]:.3f}'

                if timer_comp == 4:
                    text_ao5.text = f'Ao5: None'
                if timer_comp >= 5:
                    text_ao5.text = f'Ao5: {ao(5, Times):.3f}'

                if timer_comp == 11:
                    text_ao12.text = f'Ao12: None'
                if timer_comp >= 12:
                    text_ao12.text = f'Ao12: {ao(12, Times):.3f}'

                if timer_comp == 49:
                    text_ao50.text = f'Ao50: None'
                if timer_comp >= 50:
                    text_ao50.text = f'Ao50: {ao(50, Times):.3f}'

                if timer_comp == 99:
                    text_ao100.text = f'Ao100: None'
                if timer_comp >= 100:
                    text_ao100.text = f'Ao100: {ao(100, Times):.3f}'

    scene_expert.input = input_template
    scene_expert.update = update_template
