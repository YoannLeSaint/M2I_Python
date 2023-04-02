
import boat as b

from numpy import ones
from numpy.random import randint

class plateau():

    def __init__(self):
        self.lenght_x = 10
        self.lenght_y = 10
        self.plateau = -1*ones((self.lenght_x,self.lenght_x))

    def start(self):
        return
    def estVide(self, lenght, x,y, direction):
        match direction:
            case 0:
                for i in range(lenght):
                    if self.plateau[x+i, y] == 1:
                        return True
            case 1:
                for i in range(lenght):
                    if self.plateau[x, y+i] == 1:
                        return True
        return False

    def alrady_play(self, x,y):
        return self.plateau[x,y] == 1

    def placer_bateau(self, lenght):
        nonPlacer = True
        direction,x,y = 0,0,0
        while (nonPlacer):
            x, y = randint(0, 10), randint(0, 10)
            direction = randint(0, 2)

            match direction:
                case 0:
                    # horizontal
                    if x + lenght < 10:
                        nonPlacer = self.estVide(lenght, x,y, direction)
                case 1:
                    # vertical
                    if y + lenght < 10:
                        nonPlacer = self.estVide(lenght, x,y, direction)
                # case 2:
                #     # diag
                #

        # placement bateau
        match direction:
            case 0:
                for i in range(lenght):
                    self.plateau[x + i, y] = 1
            case 1:
                for i in range(lenght):
                    self.plateau[x, y + i] = 1

        return x, y, direction

    def __str__(self):
        str = "   ╔═════════════════════╗\n"
        for i, ligne in enumerate(self.plateau):
            if i + 1 != 10:
                str+= f" {i + 1} ║ "
            else:
                str+= f"{i + 1} ║ "
            for token in ligne:
                match token:
                    case 0: aff = "O"
                    case 1: aff = "■"
                    case 2: aff = "X"
                    case _: aff = "*"
                str+= f"{aff} "
            str+= "║\n"
        str+= "   ╚═════════════════════╝\n"
        str+= "     1 2 3 4 5 6 7 8 9 10"
        return str

    def hiden_play(self):
        str = "   ╔═════════════════════╗\n"
        for i, ligne in enumerate(self.plateau):
            if i + 1 != 10:
                str += f" {i + 1} ║ "
            else:
                str += f"{i + 1} ║ "
            for token in ligne:
                match token:
                    case 0: aff = "O"
                    case 2: aff = "X"
                    case _: aff = "*"
                str += f"{aff} "
            str += "║\n"
        str += "   ╚═════════════════════╝\n"
        str += "     1 2 3 4 5 6 7 8 9 10"
        return str

    def play(self, x,y):
        # -1 -> eau
        #  0 -> coup pas touche
        #  1 -> bateau
        #  2 -> touche

        if self.plateau[x,y] == 1:
            print("touché !")
            self.plateau[x,y] = 2
        elif self.plateau[x,y] == -1:
            print("loupé !")
            self.plateau[x,y] = 0

    def IA_random(self):
        x, y = randint(0, 10), randint(0, 10)
        self.play(x,y)

    def play_random(self, display=True):
        possible=True
        while(possible):
            x,y = randint(0, 10), randint(0, 10)
            possible = self.plateau[x,y] == 2 or self.plateau[x,y] == 0
            if not(possible):
                if display:
                    print(f"Coup joué ({x+1},{y+1})")
                self.play(x,y)

    def in_life(self):
        for row in self.plateau:
            for element in row:
                if element == 1:
                    return True
        print("Le jeu est fini")
        return False

# test
# plateau_1 = plateau()
# print(plateau_1)
# plateau_1.placer_bateau(8)
# print(plateau_1)
# plateau_1.play_random(1,1)