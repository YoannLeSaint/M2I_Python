from numpy import random as rd
from numpy import ones

def affichage_menu():
    plateau_1, plateau_2 = init()

    print(" ____        _        _ _ _        _   _                  _      \n",
          "|  _ \      | |      (_) | |      | \ | |                | |\n",
          "| |_) | __ _| |_ __ _ _| | | ___  |  \| | __ ___   ____ _| | ___\n",
          "|  _ < / _` | __/ _` | | | |/ _ \ | . ` |/ _` \ \ / / _` | |/ _ \ \n",
          "| |_) | (_| | || (_| | | | |  __/ | |\  | (_| |\ V / (_| | |  __/\n",
          "|____/ \__,_|\__\__,_|_|_|_|\___| |_| \_|\__,_| \_/ \__,_|_|\___|\n",
          "\n")


    print("Bienvenue dans votre jeu de bataille navale \n")
    print("Veuillez choisir votre mode de jeu: \n")

    quitter = True
    while(quitter):
        choix = input(" 1) Arcade\n 2) Versus \n 3) Quitter\n")
        match choix:
            case '1': jouer(1) # bot
            case '2': jouer(2) # vs
            case '3': quitter=False
            case _: print("Choix incorect, veuillez recommencer")


def placer_bateau(plateau, taille):
    nonPlacer=True
    while(nonPlacer):
        place = [rd.randint(0, 9), rd.randint(0, 9)]
        direction = rd.randint(0,1)

        match direction:
            case 0:
                # horizontal
                if place[0]+taille<10:
                    nonPlacer = estVide(plateau, taille, place, direction)
            case 1:
                # vertical
                if place[1]+taille<10:
                    nonPlacer = estVide(plateau, taille, place, direction)

    # placement bateau
    match direction:
        case 0:
            for i in range(taille):
                plateau[place[0] + i, place[1]] = 1
        case 1:
            for i in range(taille):
                plateau[place[0], place[1] + i] = 1

    return plateau


def estVide(plateau, taille, place, direction):
    match direction:
        case 0:
            for i in range(taille):
                if plateau[place[0]+i,place[1]] == 1:
                    return True
        case 1:
            for i in range(taille):
                if plateau[place[0], place[1]+i] == 1:
                    return True
    return False

def init():
    # -1 -> eau
    #  0 -> coup pas touche
    #  1 -> bateau
    #  2 -> touche
    plateau_1 = -1 * ones((10, 10))
    plateau_2 = -1 * ones((10, 10))
    flotte = [4,3,2,2]

    for bateau in flotte:
        placer_bateau(plateau_1,bateau)
        placer_bateau(plateau_2,bateau)

    return  plateau_1, plateau_2

def maj_plateau(plateau, coup_joueur):
    etat = plateau[coup_joueur[0], coup_joueur[1]]
    if etat==1.:
        print("Touché !")
        plateau[coup_joueur[0], coup_joueur[1]] = 2.
        return plateau, 1
    print("loupé !")
    plateau[coup_joueur[0], coup_joueur[1]] = 0.
    return plateau, 0

def jouer(choix):
    score = [0,0]
    plateau_1, plateau_2 = init()
    while(score[0]<11 or score[1]<11):
        coup_J1,coup_J2 = coup(int(choix), plateau_1, plateau_2)
        plateau_1, score1 = maj_plateau(plateau_1, coup_J2)
        plateau_2, score2 = maj_plateau(plateau_2, coup_J1)
        score[0] += score1
        score[1] += score2

def afficher(plateau_1,plateau_2,joueur):

    plateau_haut = plateau_1 if joueur == "B" else plateau_2
    plateau_bas = plateau_2 if joueur == "B" else plateau_1
    print(f"Au joueur {joueur} de jouer :\nS")
    print("     1 2 3 4 5 6 7 8 9 10 ")
    print("   ╔═════════════════════╗")
    aff = ''
    for i, ligne in enumerate(plateau_haut):
        if i+1!=10:
            print(f"{i+1}  ║ ",end="")
        else:
            print(f"{i + 1} ║ ", end="")
        for token in ligne:
            match token:
                case 0 : aff = "O"
                case 2 : aff = "X"
                case _ : aff = "*"
            print(f"{aff} ",end="")
        print("║")
    print("   ╠═════════════════════╣")
    for i,ligne in enumerate(plateau_bas):
        if i+1 != 10:
            print(f" {i + 1} ║ ", end="")
        else:
            print(f"{i + 1} ║ ", end="")
        for token in ligne:
            match token:
                case 0 : aff = "O"
                case 1 : aff = "■"
                case 2 : aff = "X"
                case _ : aff = "*"
            print(f"{aff} ", end="")
        print("║")
    print("   ╚═════════════════════╝")
    print("     1 2 3 4 5 6 7 8 9 10")

def coup(choix, plateau_1, plateau_2):
    #coup_J1
    afficher(plateau_1, plateau_2, 'A')
    x=input("J1, préparez votre coup.\n Sélectionnez une ligne :\n")
    y=input("Sélectionnez une colonne :")
    coup_J1=[int(x)-1,int(y)-1]
    #mode versus
    if choix==2:
        afficher(plateau_1, plateau_2, 'B')
        x=input("J2, préparez votre coup.\n Sélectionnez une ligne :\n")
        y=input("Sélectionnez une colonne :")
        coup_J2=[int(x)-1,int(y)-1]
    #mode IA
    elif choix==1:
        print("Au tour du joueur 2.\n")
        coup_J2=[rd.randint(0,9),rd.randint(0,9)]
        print("Le joueur 2 a joué :", coup_J2)

    return coup_J1, coup_J2

