import random


def shuffle(): #A pour but de proposer un mélange
    l = ["F", "B", "U", "D", "L", "R"] #liste des mouvements

    s = [] #liste qui va contenir le mélange

    i = 0 #nombre d'éléments dans la liste, utile car il y a des tours où i ne sera pas incrémenté

    def pass2(s, i): #regarde l'élément de mélange proposé il y a 2 tours et regarde si cela ne se compense pas
        if i > 1 and s[i][0] == s[i - 2][0]:
            match [s[i][0], s[i - 1][0]]:
                case ['L', 'R']:
                    s.pop(i) #supprime l'élément non autorisé
                    return True #renvoie True si ça se compense
                case ['R', 'L']:
                    s.pop(i)
                    return True
                case ['U', 'D']:
                    s.pop(i)
                    return True
                case ['D', 'U']:
                    s.pop(i)
                    return True
                case ['F', 'B']:
                    s.pop(i)
                    return True
                case ['B', 'F']:
                    s.pop(i)
                    return True
        return False #renvoie False si ça ne se compense pas

    while len(s) != 20: #tant que l'on n'a pas 20 éléments dans la liste
        c = random.choice(l) #on tire un élément dans les liste l

        s.append(c) #on ajoute cet élément à s

        if pass2(s, i) == False: #si le mouvement est autorisé
            if len(l) < 6:
                l.append(e) #on ajoute l'élément enlevé s'il y en a un

            if i != 0 and s[i] == s[i - 1]: #si on a eu 2 fois la même lettre sur 2 tours consécutifs
                s[i - 1] += "2" #on fait en sorte d'avoir F2 au lieu de F F
                e = s[i] #on stock à enlever cet élément
                l.remove(s[i]) #on veut enlever le type du mouvement
                s.pop(i) #on supprime l'élément de la liste s
            else:
                i += 1 # si on ne doit pas supprimer un élément, c'est que le précédent et le nouveaux sont différents,  on incrémente i

    for i in range(len(s)): #attribution du ' ou non
        p = random.randint(0, 1)
        if p == 0 and s[i][-1] != "2": 
            s[i] += "'" #ajout du '

    return s


# cette fonction permet de separer tous les termes de s
def display_shuffle(s):
    return " ".join(s)
