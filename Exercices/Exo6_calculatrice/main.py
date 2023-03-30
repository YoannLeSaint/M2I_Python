"""
une application

avec un main qui propose un menu : add sous div fact quitter

quand l'utilisateur un choix il effectue l'action en fonction des parametres

proposer un programme modulaire (par exemple : utils.math.<function>())

vous rajoutez un main a votre fichier principal :)
"""


import os
import utils.math.functions as mat

def menu():
    quit = True
    while(quit):
        print("### Menu ###")
        tmp = input(" 1) addition\n 2) soustraction\n 3) division\n 4) factoriel\n 5)quitter")
        match tmp:
            case '1':
                print("\n-- Addition --")
                a,b = action()
                res = mat.add(a,b)
                affiche(res)
            case '2':
                print("\n-- Soustraction --")
                a, b = action()
                res = mat.sous(a, b)
                affiche(res)
            case '3':
                print("\n-- Division --")
                a, b = action()
                res = mat.div(a, b)
                affiche(res)
            case '4':
                print("\n-- Factoriel --")
                a = input("Entez n :")
                res = mat.fac(a)
                affiche(res)
            case '5':
                quit = False
            case _:
                print("Valeur incorecte\n ")


def action():

    a = int(input("Entrez a :"))
    b = int(input("Entrez b : "))
    return a,b

def affiche(res):
    print(f"le résultat est {res}\n")


if __name__ == "__main__":
    menu()
    #os.system("pause")