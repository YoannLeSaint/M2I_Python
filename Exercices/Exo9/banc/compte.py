
"""
Programme qui va gerer un compte

.solde() permet de connaitre l'état du compte
compte + xxxx permet de rajouter de l'argent et informer l'utilisateur
compte - xxxx permet de sous de l'argent et en informe l'utilisateur

et on oublie pas __repr__ / __str__

un compte s'initialise avec une valeur de départ.
"""



class Compte(object):

    def __init__(self, solde):
        self.solde = solde

    def __repr__(self):
        print(f" solde {self.solde}")

    def __str__(self):
        return f"Votre solde : {self.solde}€"

    def __add__(self, argent):
        self.solde += argent
        print(f"Ajout de {argent}€ sur votre compte")

    def __sub__(self, argent):
        self.solde -= argent
        print(f"Vous avez retirez {argent} de votre compte")

    def __iadd__(self, other):
        self.solde+= other
        return self



