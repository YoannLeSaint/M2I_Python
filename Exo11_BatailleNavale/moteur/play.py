"""
Author:         Yoann Le Saint

Project Name:   Bataille Navale

Last Update:    2023-04-03

Descrition:     main.py interface for playing battleships
"""

# import plateau as plat # <- test import sur play lui-même
import moteur.plateau as plat
# import .plateau as plat
import os

list_lenght_boat = [2, 2, 3, 4]
path = os.getcwd()
path_save = "\\".join(path.split("\\") + ["save"])
# path_save = "\\".join(path.split("\\")[:-1] + ["save"])  # <- test import sur play lui-même

"""
menu for the battleship
    1 -> Paying IA vs IA
    2 -> Continue a past saved play
    3 -> delete the saved play
    4 -> quit
"""


def menu():
    quit = True
    print(
        " ____        _        _ _ _        _   _                  _      \n",
        "|  _ \      | |      (_) | |      | \ | |                | |\n",
        "| |_) | __ _| |_ __ _ _| | | ___  |  \| | __ ___   ____ _| | ___\n",
        "|  _ < / _` | __/ _` | | | |/ _ \ | . ` |/ _` \ \ / / _` | |/ _ \ \n",
        "| |_) | (_| | || (_| | | | |  __/ | |\  | (_| |\ V / (_| | |  __/\n",
        "|____/ \__,_|\__\__,_|_|_|_|\___| |_| \_|\__,_| \_/ \__,_|_|\___|\n",
        "\n",
    )
    while quit:
        input_user = input(
            "\n ================\n  Menu principal\n ================\n Entrez votre choix :\
                \n 1) IA vs IA\n 2) Continuer une partie\n 3) Supprimer les anciennes parties\n 4) QUITTER\n"
        )
        match input_user:
            case "1":
                play()
            case "2":
                continue_to_play()
            case "3":
                del_previus_play()
            case "4":
                quit = False
            case _:
                print("Entrée incorecte, veuillez entrer l'un des choix proposés")


def initialisation(list_lenght_boat):
    plateau_1 = plat.plateau()
    plateau_2 = plat.plateau()

    for len_boats in list_lenght_boat:
        plateau_1.place_boat(len_boats)
        plateau_2.place_boat(len_boats)

    return plateau_1, plateau_2


"""
delete the past play only if exists
"""
def del_previus_play():
    try:
        os.remove(path_save + "\\" + "plateau_1.npz")
    except:
        pass
    try:
        os.remove(path_save + "\\" + "plateau_2.npz")
        print("Suppression effectuée")
    except:
        print("Vous n'avez pas de partie enregistrée")


"""
init the IA's play
"""
def play():
    plateau_1, plateau_2 = initialisation(list_lenght_boat)
    print("Les bateaux sont placés, le jeu commence ...")
    whileloop_play(plateau_1, plateau_2)


"""
try to continue to play, if not begin a new IA's play
"""
def continue_to_play():
    try:
        plateau_1, plateau_2 = plat.plateau(), plat.plateau()
        plateau_1.load(path_save, "plateau_1")
        plateau_2.load(path_save, "plateau_2")
        whileloop_play(plateau_1, plateau_2)
    except:
        print("Vous n'avez pas de partie enregistrée, voici une nouvelle partie")
        play()


"""
main.py wile loop, continue to play until one of the player had no boat
ask at ony step if you want to stop and save
"""
def whileloop_play(plateau_1, plateau_2):
    proceed = True
    while (plateau_1.in_life() or plateau_2.in_life()) and proceed:
        proceed = True
        while proceed:
            input_user2 = input(
                "Vous voulez \n 1) Continuer\n 2) Enregistrer et quitter\n"
            )
            match input_user2:
                case "1":
                    plateau_1.play_random()
                    plateau_2.play_random()
                    print("Joueur 1 : \n", plateau_1)
                    print("Joueur 2 : \n", plateau_2)
                case "2":
                    # saving ...
                    plateau_1.save(path_save, "plateau_1")
                    plateau_2.save(path_save, "plateau_2")
                    proceed = False
                case _:
                    print("Entrée incorecte, veuillez entrer l'un des choix proposés")




# test
# plateau_1, plateau_2 = initialisation(list_lenght_boat)
# print(plateau_1)
# print(plateau_2)

menu()
