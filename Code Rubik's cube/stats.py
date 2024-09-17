import os

# Obtenez le chemin absolu du répertoire du script en cours d'exécution
script_directory = os.path.dirname(os.path.abspath(__file__))

# Spécifiez le nom du nouveau dossier que vous avez créé
nouveau_dossier = 'timer'

# Obtenez le chemin complet du nouveau dossier
chemin_nouveau_dossier = os.path.join(script_directory, nouveau_dossier)

# Vérifiez si le dossier n'existe pas déjà avant de créer le fichier .txt
if not os.path.exists(chemin_nouveau_dossier):
    os.mkdir(chemin_nouveau_dossier)
    print(f"Dossier '{nouveau_dossier}' créé avec succès dans '{script_directory}'.")
else:
    print(f"Le dossier '{nouveau_dossier}' existe déjà dans '{script_directory}'.")

# Spécifiez le nom du nouveau fichier .txt que vous souhaitez créer
nouveau_fichier_txt = 'timer.txt'

# Obtenez le chemin complet du nouveau fichier .txt
chemin_nouveau_fichier_txt = os.path.join(chemin_nouveau_dossier, nouveau_fichier_txt)

# Vérifiez si le fichier .txt existe déjà
if not os.path.exists(chemin_nouveau_fichier_txt):
    # Créez le fichier .txt s'il n'existe pas
    with open(chemin_nouveau_fichier_txt, 'w') as fichier_txt:
        fichier_txt.write("Contenu initial du fichier .txt\n")
        fichier_txt.write("Vous pouvez ajouter plus de lignes si nécessaire.\n")
    print(f"Fichier '{nouveau_fichier_txt}' créé avec succès dans '{chemin_nouveau_dossier}'.")
else:
    # Ouvrir le fichier en mode 'a' pour l'ajout
    with open(chemin_nouveau_fichier_txt, 'a') as fichier_ecriture:
        # Ajouter du contenu à la fin du fichier
        fichier_ecriture.write("Nouveau contenu ajouté à la fin du fichier.\n")

    with open(chemin_nouveau_fichier_txt, 'r') as fichier_lecture:
        contenu = fichier_lecture.readlines()

    # Utilisez la fonction len() pour obtenir le nombre de lignes
    nombre_de_lignes = len(contenu)
    print(f"Il y a {nombre_de_lignes} lignes dans le fichier précédent.")
    print(f"Le fichier '{nouveau_fichier_txt}' existe déjà dans '{chemin_nouveau_dossier}'.")
    fichier_lecture.close()
    fichier_ecriture.close()
