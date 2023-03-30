"""

Author:         Yoann Le Saint

Project Name:   Bataille Naval

Last Update:    2023-03-30

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

import os
import utils.bataille.functions as bat



def menu():
    bat.affichage_menu()



if __name__ == "__main__":
    menu()
    #os.system("pause")