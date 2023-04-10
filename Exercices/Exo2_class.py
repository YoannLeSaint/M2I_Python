# Exercice 2 - Classe
# creer un programme qui rentre un nombre d'élèves, un nombre de matières
# pour chaque élève et matière : demander à l'utilisateur de rentrer les notes (nombre aléatoire de note)
# une fois terminer : vous faites par élève : moyenne dans la matière, note la plus haute dans la matière, note la plus basse dans la matière
# moyenne générale
# global (tout les élèves confondus) moyenne générale de la classe, note la plus haute, la plus basse


#@Author :  Yoann Le Saint
#           Emmanuel Rochet
#           Lucie Potiron

import random as rd


""""
main.py.py : initialisation main.py.py du programme - cf. entête
"""
def main():

    print("#################################\n",
          "# Programme de calcul des notes #\n",
          "#################################\n",
          "#\n" )

    #on demande notre nombre d'élève et de matières
    nb_eleve = input("Nombre d'élèves")
    nb_eleve = isAnuber(nb_eleve)

    nb_matiere = input("Nombre de matière")
    nb_matiere = isAnuber(nb_matiere)

    notes = remplissage(nb_eleve,nb_matiere)
    stat_note_eleve = stat_eleve(notes)
    stat_note_global = stat_classe(stat_note_eleve)

    print(f" Statistique par élève :\n")
    affichage(stat_note_eleve)
    print(f"\n",
          f"_______________________________________\n",)
    print(f"Statistique pour la classe : \n",
        f"{stat_note_global['moyennes']} \n",
        f"{stat_note_global['max']} \n",
        f"{stat_note_global['min']}"
    )

    return stat_note_eleve, stat_note_global

def isAnuber(number):
    try:
        return int(number)
    except:
        print("Valeur incorect")
        return 0

def affichage(eleves):
    for i in range(len(eleves)):
        print(f"__________________________\n",
              f"Eleve numéro {i+1}\n",
              f"Moyenne : {eleves['moyennes'][i]} \n",
              f"Maximum : {eleves['max'][i]} \n",
              f"Minimum : {eleves['min'][i]} \n")


"""
Matrice des notes
@input : 
* nb_eleve :  le nombre d'élèves dans la classe
* nb_matiere : le nombre de matière dans la classe

@output : la matrice des notes, les élèves en dimention 1 et les matières en dim 2
"""
def remplissage(nb_eleve, nb_matiere):
    notes = []
    for i in range(nb_eleve):
        eleve = []
        for j in range(nb_matiere):
            # remplissage aléatoire des notes de chaques élèves
            eleve.append(rd.randint(0,20))
        notes.append(eleve)
    return notes

"""
Statiques des notes des élèves (aléatoire)
@input :
* note : matrice contruite dans remplissage - 
         matrice des notes des élèves dans chaques matière

@output : ret - dictionnaire des moyennes, notes la plus haute, note la plus basse
          de chaque élèves
"""
def stat_eleve(notes):
    #initialisation
    moyenne = []
    bas, haute = [], []

    #on parcour nos élèves
    for eleve in notes:
        #on initialise les calculs par élève
        somme = 0
        max_note = 0
        min_note = 20

        #on parcours nos notes
        for note_eleve in eleve :
            somme += note_eleve
            max_note = max(max_note,note_eleve)
            min_note = min(min_note,note_eleve)

        #on rajoute nos calculs dans nos listes de retour
        moyenne.append(somme / len(eleve))
        haute.append(max_note)
        bas.append(min_note)

    #On formate notre retour
    ret = {
        "moyennes" : moyenne,
        "max" : haute,
        "min" : bas
    }

    return ret

"""
stat_classe : renvoie les statiques globales des élèves

@input : stat_eleve - dictionnaire construit par la fonction stat_eleve
         stat_eleve : moyenne-max-min
@output : ret - dictionnaire des moyennes, notes max et notes min global des élèves
          ret : moyenne, max, min
"""
def stat_classe(stat_eleve):
    #initialisation
    somme = 0
    min_note, max_note = 0,20

    #calcul des moyennes de élèves de al classe
    for note in stat_eleve["moyennes"]:
        somme += note
    moyenne = somme / len(stat_eleve["moyennes"])

    #calcul de al note la plus basse
    for note in stat_eleve["min"]:
        min_note = min(note,min_note)

    #calcul de la note la plus haute
    for note in stat_eleve["max"]:
        max_note = max(note, max_note)

    # On formate notre retour
    ret = {
        "moyennes": moyenne,
        "max": max_note,
        "min": min_note
    }

    return ret


stat_note_eleve, stat_note_global = main()