"""

Exercice 4

Soit une image binaire représentés dans une matrice à 2 dimension.
Les éléments m[i][j] sont dits pixels et sont égaux soit à 0 soit à 1.
Chaque groupement de pixels égaux à 1 et connectés entre eux forment une composante connexe(figure).
L’objectifs est de donner une valeur différente de 1 à chaque composante (2 puis 3 puis 4 etc.)


1. Ecrire une fonction récursive propager permettant de partir d’un point (i,j)
    situé à l’intérieur d’une composante connexe et de propager une étiquette T
    à tous les pixels situés à l’intérieur de la composante.

2. Ecrire une fonction etiqueter permettant d’affecter une étiquette différente à chaque composante connexe

Author:         Yoann Le Saint
                Emmanuel Rochet

Project Name:   Propagation matrice

Last Update:    2023-03-29
"""

import numpy as np
import matplotlib.pyplot as plt

def generation_img_bin(taille_x, taille_y):
    return (np.random.rand(taille_x,taille_y)<0.5).astype(int)

def afficher_img(image_mat):
    plt.imshow(image_mat)
    plt.show()

# def afficher_img(image_mat1, image_mat2):
#     plt.subplot(211)
#     plt.imshow(image_mat1)
#
#     plt.subplot(212)
#     plt.imshow(image_mat2)
#     plt.show()

def recherche(image_mat):
    etiquette = 2
    for i in range(len(image_mat)):
        for j in range(len(image_mat[0])):
            if image_mat[i,j]==1:
                propag(etiquette, image_mat, i,j)
                etiquette+=1
    return image_mat

def propag(etiquette,image, pos_x, pos_y):
    size = image.shape
    image[pos_x, pos_y] = etiquette
    if (pos_x > 0          and image[pos_x-1,pos_y]    == 1):
        propag(etiquette, image, pos_x - 1, pos_y)
    if (pos_x < size[0] -1 and image[pos_x + 1, pos_y] == 1):
        propag(etiquette, image, pos_x + 1, pos_y)
    if (pos_y > 0          and image[pos_x, pos_y - 1] == 1):
        propag(etiquette, image, pos_x, pos_y - 1)
    if (pos_y < size[1] -1 and image[pos_x, pos_y + 1] == 1):
        propag(etiquette, image, pos_x, pos_y + 1)

#test
image_mat = generation_img_bin(10,10)
afficher_img(image_mat)
res = recherche(image_mat)

print(image_mat)
print(res)

afficher_img(res)