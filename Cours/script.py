print(f'le résultat est => {2 ** 3 >> 1}')

# Prix TTC de 3 article, appliquer la TVA (20%)
# Affichage :
#
#
#

p1, p2, p3 = 5.5, 10, 9.99


def print_ticket(prix):
    print(
        f"Le prix de l'article HT => {prix:.2f} \n ############################### \n Le prix de l'article TTC => {prix * 1.2:.2f}\n")


print_ticket(p1)
print_ticket(p2)
print_ticket(p3)

insertion = input("Indiquer une valeur =>")
print(f"Votre valeur : {insertion}")

# Chhiffre mystere


bas, haut = 0, 9
nb = input("Entrez un chiffre en {bas} et {haut} :")
mystere = 5

if nb == mystere:
    print("bravo c'est le bombre chiffre")
elif (nb < mystere):
    print("c'est au dessus")
else:
    print("c'est en dessous")

mystere = 5
bas, haut = 0, 9
nb = -1

while (nb != mystere):
    nb = int(input(f"Entrez un chiffre en {bas} et {haut} :"))
    if (nb < mystere):
        print("c'est au dessus")
    else:
        print("c'est en dessous")

print("bravo c'est le bon chiffre")

table = int(input("Entrez la table de multiplication"))
max_table = int(input("Entrez le maxmumm multiplicatif"))
pas = int(input("Entrez le pas"))

i = 1
print(" =================")
while (i <= max_table):
    print(f" | {table} x {i} = {table * i} | ")
    i += pas
print(" =================")

#
phrase = input("Donnez une phrase")
lettre = input("Donner une lettre")
new_phrase = ""
for i in range(len(phrase)):
    if phrase[i] == lettre:
        new_phrase = 'X'
    else:
        new_phrase += phrase[i]

print(phrase)
print(new_phrase)

# table de mutiplication
table = int(input("Entrez la table de multiplication"))

print(" =================")
for i in range(1, 11):
    print(f" | {table} x {i} = {table * i} | ")
print(" =================")

# factorel iteratif
fac = int(input("Entrez le nombre"))


def factoriel(fac):
    a = 1
    for i in range(1, fac + 1):
        a *= i
    return a


print(factoriel(fac))

# Nombre magique avec break
mystere = 5
bas, haut = 0, 9
nb = 0

while (nb != mystere):
    nb = int(input(f"Entrez un chiffre en {bas} et {haut} :"))
    if nb < 0:
        print("Vous avez abandonné le jeu")
        break
    elif (nb < mystere):
        print("c'est au dessus")
    elif (nb > mystere):
        print("c'est en dessous")

print("bravo c'est le bon chiffre")

# proposer 4 programmes
# calculer l'air d'un carre
# le volume d'une sphere
# le volume d'un parallépipède
# help (il faut importer math avec l'utilisation de math.pi)

import math
import numpy as np


def entrer_nb(text):
    tmp = int(input(text))
    return tmp


def carre():
    cote = entrer_nb("Cote du carré : ")
    print(f"l'aire du carré est de {cote ** 2}")


def vol_sphere():
    R = entrer_nb("rayon de la shère :")
    print(f"le volume de la shère est : {(4 / 3) * np.pi * (R ** 3)}")


def Vol_parallepipede(a, b, c):
    a = entrer_nb("longueur")
    b = entrer_nb("largeur")
    c = entrer_nb("hauteur")
    print(f"le volume de parallépipiède est : {a * b * c}")


# pour une chaine de caracteres, determine par recursivite sa longueur


# rendre recursif
def somme(L):
    s = 0
    for val in L:
        s += val
    return s


def somme_rec(L):
    # condition d'arret
    if L == "":
        return 0
    else:
        return 1 + somme_rec(L[:-1])


print(somme_rec("a"))


# Ecrire une fonction récursive « Binaire » permettant d’imprimer à l’écran la représentation binaire d’un nombre N.

def rec_bin(bin):
    if bin == 0:
        return '0b'
    else:
        return rec_bin(bin // 2) + str(bin % 2)


rec_bin(3)


# ecrire la suite de Fibonacci en récursif fib(n)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# la factorielle

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)


# donner un nombre et determiner tous les nombres premiers précédents.

def divisible(n, d):
    if (d == 1):
        return False
    if (n % d == 0):
        return True
    return divisible(n, d - 1)


def affiche_premier(n):
    if n == 1:
        return "1"
    else:
        if not (divisible(n, n // 2)):
            return str(n) + " " + str(affiche_premier(n - 1))
        return str(affiche_premier(n - 1))


# ecrire un programme qui determine si un mot est un palindrome.
def palindrome(word):
    if word == "":
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        return False


# Tour d'Hanoi
def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n - 1, A, C, B)
        print(f"Déplacez {A} sur {C}")
        hanoi(n - 1, B, A, C)


hanoi(3, 'a', 'b', 'c')


def hanoi2(n, A, B, C):
    if n == 1:
        C.append(A[-1])
        A.remove(A[-1])
        print('A , B, C :{}\t{}\t{}'.format(A, B, C))
    else:
        hanoi2(n - 1, A, C, B)
        hanoi2(1, A, B, C)
        hanoi2(n - 1, B, A, C)


# it's possible to use any input variable name
n = 4
a = list(range(n, 0, -1))
b, c = [], []
hanoi2(n, a, b, c)

"""Soit un tableau d'entiers contenant des valeurs 0 ou bien 1. On appel composante connexe une suite contigue de nombres égaux à 1. 
On voudrait changer la valeur de chaque composante connexe de telle sorte que la première composante ai la valeur 2 la deuxième ai la 
valeur 3, la 3ème ait la valeur 4 et ainsi de suite. Réaliser deux fonctions :

La première fonction n’est pas récursive et a pour rôle de chercher la position d’un 1 dans un tableau.
La deuxième fonction est récursive. Elle reçoit la position d’un 1 dans une séquence et propage une valeur x à toutes les valeur 1 de la composante connexe."""


def whereOne(list):
    # return the first one in the list
    i = 0
    while (list[i] != 1):
        i += 1
    return i


def connexe(list, pos):
    if pos >= len(list) + 1 or list[pos] == 0:
        return list
    else:
        list[pos] += pos
        return connexe(list, pos + 1)


l = [0, 1, 1, 1, 0, 1, 1, 0, 1]
position = whereOne(l)
print(l)
print(connexe(l, position))


def connexe_complet(list):
    position = whereOne(list)
    while (position != 0):
        position = whereOne(list)
        list = connexe(list, position)
        print(list)
    return list


print(connexe_complet(l))


bonjour = lambda a,b:a*b
print(bonjour(3,4))


# todo list avec un dictionnaire
# vous ajouter