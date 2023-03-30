"""
le jeu propose à deux joueurs de s'affonter sur un duel Shifumi
le prmier arrivé à trois a gagné la partie
cependant la partie continue tant qu'il n'y a pas 2 points d'écart
"""


gain_1, gain_2 = 0,0
i=1

while (gain_2 != 3 and gain_1 != 3) and abs(gain_2 - gain_1)<3:
    print(f"Tour n°{i}")
    print(f"Score actuel : Joueur 1 - ({gain_1}) | Joueur 2 - ({gain_2})")
    main1 = input("premier joueur")
    main2 = input("deuxième joueur")
    if (main1 == main2):
        print("Vous avez la même main.py")

    elif main1 == "pierre" and main2 == "papier":
        print("le joueur 2 gagne")
        gain_2+=1
    elif main2 == "pierre" and main1 == "papier":
        print("le joueur 1 gagne")
        gain_1+=1

    elif main1 == "pierre" and main2 == "ciseau":
        print("le joueur 1 gagne")
        gain_1+=1
    elif main2 == "pierre" and main1 == "ciseau":
        print("le joueur 2 gagne")
        gain_2+=1

    elif main1 == "ciseau" and main2 == "papier":
        print("le joueur 1 gange")
        gain_1+=1
    elif main2 == "ciseau" and main1 == "papier":
        print("le joueur 2 gange")
        gain_2+=1
    else:
        print("Vous ne pouvez pas jouer ces mains")
    print("====================")
    i+=1

if gain_1>gain_2:
    print(f"le joueur 1 gagne avec un score de {gain_1}")
else:
    print(f"le joueur 2 gagne avec un score de {gain_2}")