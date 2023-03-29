import numpy as np
import numpy.random as rd
def isAnuber(number):
    try:
        return int(number)
    except:
        print("Valeur incorect, veuillez recommencer")

def shuifumi():
    # Menu
    while(True):
        tmp = (input("1) Affrontez un joueur\n2) Affrontez IA\n3) Quittez"))
        tmp = isAnuber(tmp)
        if tmp == 3:
            break
        elif tmp == 1:
            combat()
        elif tmp == 2:
            combatIA()
        print("\n")
    print("Vous avez quitté")

def mainTOint(main):
    if main=="pierre":
        return 1
    elif main=="papier":
        return 2
    elif main=="ciseau":
        return 3
    else:
        return 0

def intTOmain(integer):
    if integer==1:
        return "pierre"
    elif integer==2:
        return "papier"
    elif integer==3:
        return "ciseau"
    else:
        return "erreur ce choix n'est pas possible, veuillez choisir une main correct entre\n pierre, papier et ciseau"


def IsOver(gain1,gain2):
    return (gain1 >= 3 or gain2 >= 3) and abs(gain2 - gain1) >=2


def combat():
    main1,main2 = 0,0
    gain1,gain2 = 0,0
    i=1
    while not(IsOver(gain1,gain2)):
        print(f"Tour n°{i}")
        manche()
        print("============\n")

def printScoreJoueur(playerName1, playerName2,score1,score2):
    print(f"Score actuel : {playerName1} - ({score1}) | {playerName2} - ({score2})")

def asking(display):
    print(display)
    main=0
    while(main==0):
        main = mainTOint(input("premier joueur"))
    return main

def manche(IA):
    #Asking main
    main1 = asking("Joueur 1 : ")
    if IA:
        main2 = rd.choice([1,2,3])
    else: main2 = asking("Joueur 2 : ")
    displayGame()
    return main1,main2

def combatIA():
    return 0


shuifumi()