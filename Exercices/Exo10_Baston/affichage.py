def afficher_degats(degats1,degats2):
    print(f"Le joueur 1 a infligé {degats1} au joueur 2")
    print(f"Le joueur 2 a infligé {degats2} au joueur 1")

def fin_de_combat(gagnant):
    if(gagnant=="Personne"):
        print("Les deux combattants se sont entretués, quel tragédie! Personne n'as gagné")
    else:
        print(f"Le gagnant est {gagnant}")
        