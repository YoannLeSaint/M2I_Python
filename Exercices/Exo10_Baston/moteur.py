from Combattant import combattant
import affichage as affiche
import random as rd


def jeu():
    joueur1=choisirPerso()
    joueur2=choisirPerso()
    combat(joueur1,joueur2)
    
    
def choisirPerso():
    classe=rd.randint(1,3)
    match(classe):
        case 1:
            return combattant.Guerrier()
        case 2:
            return combattant.Mage()
        case 3:
            return combattant.Voleur()


def combat(joueur1,joueur2):
    while joueur1.pasMort() and joueur2.pasMort():
        degat_joueur1 = joueur1.attaque(joueur2)
        degat_joueur2 = joueur2.attaque(joueur1)
        affiche.afficher_degats(degat_joueur1, degat_joueur2)
    if not(joueur1.pasMort()) and not(joueur2.pasMort()):
        affiche.fin_de_combat("Personne")
    elif joueur1.pasMort():
        affiche.fin_de_combat("Joueur1")
    else:
        affiche.fin_de_combat("Joueur2")

    

