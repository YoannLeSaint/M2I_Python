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
                param = action2()
                res = mat.add2(*param)
                affiche(res)
            case '2':
                print("\n-- Soustraction --")
                param = action()
                res = mat.sous2(*param)
                affiche(res)
            case '3':
                print("\n-- Division --")
                param = action()
                res = mat.div2(*param)
                affiche(res)
            case '4':
                print("\n-- Factoriel --")
                a = input("Entez n :")
                res = mat.fac2(a)
                affiche(res)
            case '5':
                quit = False
            case _:
                print("Valeur incorecte\n ")


def action():
    a = int(input("Entrez a :"))
    b = int(input("Entrez b : "))
    return a,b

def strTOint(strint):
    try:
        return int(strint)
    except:
        return strint
def action2():
    quit = True
    res = []
    i, tmp = 0, 0
    while(quit):
        if tmp!='&':
            tmp = strTOint(input(f"Entrer la valeur {i+1}, tapper '&' pour quitter"))
            res+=[tmp]
            i+=1
        else:
            quit=False
            res.pop()
    print(res)
    return tuple(res)

def affiche(res):
    print(f"le résultat est {res}\n")


if __name__ == "__main__":
    menu()
    #os.system("pause")