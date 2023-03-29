"""

_*_ coding:Utf8 _*_

Author:         Yoann Le Saint
                E
                Lucie Potiron

Project Name:   Bataille Naval

Last Update:    2023-03-29

Descrition: Player vs player | Player vs IA (random)
            Initionlisation aléatoire
            map 10x10
            0 -> à l'eau
            * -> zone non touchée
            x -> touché

            1 porte avion 4 cases
            2 bateaux 2 cases
            1 intermediaire 3 cases

"""


import numpy as np
import random as rd


def main():
    plateau_1, plateau2 = init()

    print(" ____        _        _ _ _        _   _                  _      \n",
          "|  _ \      | |      (_) | |      | \ | |                | |\n",
          "| |_) | __ _| |_ __ _ _| | | ___  |  \| | __ ___   ____ _| | ___\n",
          "|  _ < / _` | __/ _` | | | |/ _ \ | . ` |/ _` \ \ / / _` | |/ _ \ \n",
          "| |_) | (_| | || (_| | | | |  __/ | |\  | (_| |\ V / (_| | |  __/\n",
          "|____/ \__,_|\__\__,_|_|_|_|\___| |_| \_|\__,_| \_/ \__,_|_|\___|\n",
          "\n")


    print("Bienvenue dans votre jeu de bataille navale \n")
    print("Veuillez choisir votre mode de jeu: \n")

    while(True):
        choix = input("1) Arcade\n",
                      "2) Versus \n",
                      "3) Quitter\n")
            match choix:
                case 1: jouer(joueur(), bot())
                case 2: jouer(joueur(), joueur())
                case 3:
                case _:



def placer_bateau(plateau, taille):
    nonPlacer=True
    while(nonPlacer):
        place = [np.rd.randint(0,9), np.rd.randint(0,9)]
        direction = np.random.randint(0,1)
        match direction:
            case 0:
                # horizontal ()
                rand = np.random.choice([-1,1])

            case 1:
                # vertical



def init():
    # -1 -> eau
    #  0 -> coup pas touche
    #  1 -> bateau
    #  2 -> touche
    plateau_1 = -1 * np.ones((10, 10))
    plateau_2 = -1 * np.ones((10, 10))



    return  plateau_1, plateau_2


def jouer(j1,j2):


def afficher(plateau1,plateau2,joueur):

    plateau_haut = plateau1 if joueur == "B" else plateau2
    plateau_bas = plateau2 if joueur == "B" else plateau1
    2
    print(" ╔═════════════════════╗\n")

    for ligne  in plateau_haut:
        print("║ ")
        for token in ligne:
            match token:
                case 0 : aff = "O",
                case 2 : aff = "X",
                case _: aff = "*"
            print(f"{aff} ")
        print("║\n")
    print("╠═════════════════════╣")
    for ligne  in plateau_haut:
        print("║ ")
        for token in ligne:
            match token:
                case 0 : aff = "O",
                case 1 : aff = "□",
                case 2 : aff = "X",
                case _: aff = "*"
            print(f"{aff} ")
        print("║\n")
    print("╚═════════════════════╝")



def coup(choix):
    #coup_J1
    x=input("J1, préparez votre coup.\n Sélectionnez une ligne :")
    y=input("Sélectionnez une colonne :")
    coup_J1=[x,y]
    #mode versus
    if choix==2:
        x=input("J2, préparez votre coup.\n Sélectionnez une ligne :")
        y=input("Sélectionnez une colonne :")
        coup_J2=[x,y]
    #mode IA
    elif choix==1:
        coup_IA=[rd.randint(0,9),rd.randint(0,9)]

    return coup_J1,coup_J2,coup_IA





def menu()
    pri

    return choix
