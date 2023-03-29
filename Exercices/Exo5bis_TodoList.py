"""

Author:     Emmanuel Rochet
            Yoann Le Saint
            Lucie Potiron
Project Name:

Last Update: 2023-03-27

Todolist avec un dictionnaire.

Vous rajouter X element todo liste
et ensuite le programme quel todo executer ?
Ca vous enleve le todo dans la todo liste et ca vous affiche la tache.
Votre programme boucle tant que vous n'avez demandé de sortir.

Menu propose :

1) Ajout d'un todo
2) Execution d'un todo
3) Affichage de la todolist
4) Quitter


"""


def main():

    # diconnaire vide
    print(" ╔════════════╗\n",
           "║ TODO Liste ║\n",
           "╚════════════╝\n",
          "\n",
          "\n",
              "Bienvenue dans votre TODO liste\n")
    dico = {}
    while(True):
        # Affichage de notre menu

        print("\n  1) Ajout d'un todo\n",
                " 2) Executer un todo\n",
                " 3) Afficher la todo\n",
                " 4) Quitter")
        entrer = input("Veuillez entrer une commande\n"
                       )
        match entrer:
            case '1':
                ajout_menu(dico)
            case '2':
                executer_menu(dico)
            case '3':
                afficher(dico)
            case '4':
                break
            case _:
                print("Erreur : entrée incorrecte")


def ajout_menu(dico):
    new_key = input("Entrez le nom du projet : ")
    value = input("Entrez votre todo : ")
    ajout(dico, new_key, value)

def ajout(dico, new_key, new_element):
    dico[new_key]=new_element
    return dico

def executer_menu(dico):
    key_exe = input("Entrez le projet exécuté :")
    executer(dico,key_exe)

def executer(dico, key_exe):
    del dico[key_exe]
    return dico

def afficher(dico):
    print("═══════════════════════════════════════════════════════════════════════\n ")
    for clef, valeur in dico.items():
        print(f"• {clef}    =>    {valeur} \n")


main()