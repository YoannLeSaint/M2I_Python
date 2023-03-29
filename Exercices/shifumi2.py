"""
le jeu propose à deux joueurs de s'affonter sur un duel Shifumi
le prmier arrivé à trois a gagné la partie
cependant la partie continue tant qu'il n'y a pas 2 points d'écart

vous proposez un menu :1) Affrontez un joueur 2) Affrontez IA3) Quittez

"""

import numpy as np

def comparaison(main1, main2, gain_1, gain_2):

    if main1 == "pierre" and main2 == "papier":
        gain_2 += 1
    elif main2 == "pierre" and main1 == "papier":
        gain_1 += 1

    elif main1 == "pierre" and main2 == "ciseau":
        gain_1 += 1
    elif main2 == "pierre" and main1 == "ciseau":
        gain_2 += 1

    elif main1 == "ciseau" and main2 == "papier":
        gain_1 += 1
    elif main2 == "ciseau" and main1 == "papier":
        gain_2 += 1

    return gain_1, gain_2

def affichageScore(gain_1,gain_2):
    print(f"Le joueur 1 a {gain_1} et le joueur 2 a {gain_2}")

def choix():
    tmp = int(input("1) Affrontez un joueur 2) Affrontez IA 3) Quittez"))
    return tmp

def combat(gain_2,gain_1, IA):
    i=1
    while (gain_2 != 3 and gain_1 != 3) and abs(gain_2 - gain_1) < 3:
        print(f"Tour n°{i}")
        print(f"Score actuel : Joueur 1 - ({gain_1}) | Joueur 2 - ({gain_2})")
        main1 = input("premier joueur")
        main2 = "pierre"
        if IA:
            np.random.choice(['pierre','papier','ciseau'])
        else:
            main2 = input("deuxième joueur")

        gain_1,gain_2 = comparaison(main1, main2, gain_1, gain_2)
        affichageScore(gain_1,gain_2)
        i += 1

    if gain_1 > gain_2:
        print(f"le joueur 1 gagne avec un score de {gain_1}")
    else:
        print(f"le joueur 2 gagne avec un score de {gain_2}")

def shifumi():
    gain_1, gain_2 = 0, 0
    # Menu
    menu = choix()
    while menu==1 or menu==2:

        if menu == 1:
            IA = False
        elif menu == 2:
            IA = True

        combat(gain_2, gain_1, IA)

    print("Vous quittez le menu")

shifumi()