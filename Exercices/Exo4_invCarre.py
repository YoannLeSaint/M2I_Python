"""
Ecrire une fonction Python qui calcule la somme des inverses des carrés des n premiers
entiers naturels non nuls.
On pourra ensuite écrire un script plus complet qui, après le calcul précédent, évalue et affiche
l’écart (en %) avec la limite de cette somme qui vaut


π^2/6


π (rappel : le nombre π ne fait pas
partie intégrante du cœur du du langage Python. On importera donc pi via la bibliothèque
math : from math import pi).

Author: Yoann Le Saint
"""



import numpy as np

def som_inv(n):
    if n==1:
        return n
    else:
        return (1/n)**2+som_inv(n-1)
print(som_inv(10))
def conv(n):
    som = som_inv(n)
    return 1-((np.pi**2/6-som)*100)

print(conv(10))
print(conv(50))
print(conv(100))
