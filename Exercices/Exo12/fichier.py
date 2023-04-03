"""

_*_ coding:Utf8 _*_

Author:         Yoann Le Saint
                Emmanuel Rochet
                Lucie Potiron
                Yoan Cottrel

Project Name:   Calculateur via fichiers

Last Update:    2023-04-03

Descrition:

"""


# ------------
# Fichier texte :
# addition 3 4 5 6 34 12
# soustraction 3 4 6 7 8 9
# xxxx

# Faite un programme qui lit le fichier et execute l'operation indique en debut de ligne avec en arguments les éléments du reste de la ligne
# Gerer les exceptions
# ET .... utiliser des lambdas


def read(file_name):
    with open(file_name, 'r') as file:  #ouvre le fichier et l'affecte à la variable file (uniquement durant l'indentation)
        contenu=file.read()             #obtiens le contenu du fichier
        lignes=contenu.split("\n")      #Sépare les lignes et les sauvegarde dans un tableau
        for ligne in lignes:
            operation = ligne.split(' ')[0]        #Stocke le 1er mot afin d'analyser l'opération à effectuer
            try:
                ligne = ligne.split(' ')[1:]        #sépare les mots après l'opération en une liste
                ope = ligne[0]
            except:
                print("you didn't write any number for the operation")     #Verifie s'il y a bien suffisament de valeurs pour effectuer l'opération

            if operation == 'addition':
                print(f"{ope}", end="")
                for i in range (0, len(ligne)):
                    print(f"+{ligne[i]}",end="")
                    try:
                        ope=add(int(ope),int(ligne[i]))
                    except:
                        raise Exception(f"Either {ope} or {i} is not a number")
                print(f"={ope}")
            elif operation == 'soustraction':

                print(f"{ope}", end="")
                for i in range (0, len(ligne)):
                    print(f"-{ligne[i]}",end="")
                    try:
                        ope=sub(int(ope),int(ligne[i]))
                    except:
                        raise Exception(f"Either {ope} or {i} is not a number")
                print(f"={ope}")
            else :
                print(f"The operation {operation} is not supported")



add = lambda x,y : x + y
sub = lambda x,y : x - y


read("operation.txt")