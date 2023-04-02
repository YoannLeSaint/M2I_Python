import plateau as plat


list_lenght_boat = [2, 2, 3, 4]
def initialisation(list_lenght_boat):
    plateau_1 = plat.plateau()
    plateau_2 = plat.plateau()

    for len_boats in list_lenght_boat:
        plateau_1.placer_bateau(len_boats)
        plateau_2.placer_bateau(len_boats)

    return plateau_1, plateau_2


def play():
    plateau_1, plateau_2 = initialisation(list_lenght_boat)
    print("Les bateaux sont placés, le jeu commence ...")
    while (plateau_1.in_life() or plateau_2.in_life()):
        plateau_1.play_random()
        plateau_2.play_random()
        print("Joueur 1 : \n",plateau_1)
        print("Joueur 2 : \n",plateau_2)




# test
# plateau_1, plateau_2 = initialisation(list_lenght_boat)
# print(plateau_1)
# print(plateau_2)

# play()