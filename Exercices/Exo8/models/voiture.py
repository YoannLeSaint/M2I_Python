"""
Exercice 8 : objet
CREER un petit programme (avec des modules) qui permet de crer des voitures qui ont :
- une couleur
- une marque
- un prix
avec une redefinition (overload) __str__ et __repr__
et une fonction klaxonner qui affiche : la voiture <couleur> de marque <marque> a fait pouet pouet
"""

class Voiture:

    def __init__(self, couleur, marque, prix):
        self.couleur = couleur
        self.marque  = marque
        self.prix    = prix

    def __str__(self):
        return f"la voiture est de couleur {self.couleur} de la marque {self.marque} à {self.prix} €"

    def __repr__(self):
        print(f"Couleur {self.couleur} - Marque {self.marque} - Prix {self.prix}")

    def klaxonner(self):
        print(f"la voiture {self.couleur} de marque {self.marque} a fait pouet pouet")