"""
Author:         Yoann Le Saint

Project Name:   Bataille Navale

Last Update:    2023-04-03

Descrition:     Creation of a game board
                parameters:
                    x,y     -> lenghts of the grid
                    plateau -> numpy array of the boat grid
                            # -1 -> water
                            #  0 -> non touched
                            #  1 -> boat
                            #  2 -> touched
"""

from numpy import ones
from numpy.random import randint
from numpy import save, load


class plateau:
    def __init__(self):
        self.lenght_x = 10
        self.lenght_y = 10
        self.plateau = -1 * ones((self.lenght_x, self.lenght_x))

    """
    look if they are any boat in the trajectory and didn't overflowed above the band
    With a (x,y) position, return true if the method find a boat ([x,y]==1)
    in the trajectory (lenght)
    @input:     lenght
                x,y
                direction
    @output:    Boolean
    """

    def isEmpty(self, lenght, x, y, direction):
        match direction:
            case 0:
                for i in range(lenght):
                    if self.plateau[x + i, y] == 1:
                        return True
            case 1:
                for i in range(lenght):
                    if self.plateau[x, y + i] == 1:
                        return True
        return False

    """
    find if a pisition in the grid is 1, so if a boat is here
    @input:     x,y
    @output:    Boolean
    """

    def alrady_play(self, x, y):
        return self.plateau[x, y] == 1

    """
    place one boat on the grid only if the boat is not out of range
    and if there is no boat in the trajectory
    @input:     lenght
    @output:    x,y
                direction
    (change the grid itself)
    """

    def place_boat(self, lenght):
        nonPlacer = True
        direction, x, y = 0, 0, 0
        while nonPlacer:
            x, y = randint(0, 10), randint(0, 10)
            direction = randint(0, 2)

            match direction:
                case 0:
                    # horizontal
                    if x + lenght < 10:
                        nonPlacer = self.isEmpty(lenght, x, y, direction)
                case 1:
                    # vertical
                    if y + lenght < 10:
                        nonPlacer = self.isEmpty(lenght, x, y, direction)
                # case 2:
                #     # diag

        # placement bateau
        match direction:
            case 0:
                for i in range(lenght):
                    self.plateau[x + i, y] = 1
            case 1:
                for i in range(lenght):
                    self.plateau[x, y + i] = 1

        return x, y, direction

    """
    display the battle ship in the grid form
    @input:     *
    @output     grid
    """

    def __str__(self):
        str = "   ╔═════════════════════╗\n"
        for i, ligne in enumerate(self.plateau):
            if i + 1 != 10:
                str += f" {i + 1} ║ "
            else:
                str += f"{i + 1} ║ "
            for token in ligne:
                match token:
                    case 0:
                        aff = "O"
                    case 1:
                        aff = "■"
                    case 2:
                        aff = "X"
                    case _:
                        aff = "*"
                str += f"{aff} "
            str += "║\n"
        str += "   ╚═════════════════════╝\n"
        str += "     1 2 3 4 5 6 7 8 9 10"
        return str

    """
        display the battle ship in the grid form for the other player
        He/She can't see where the boat's opponent are
        @input:     *
        @output     grid
        """

    def hiden_play(self):
        str = "  ╔═════════════════════╗\n"
        for i, ligne in enumerate(self.plateau):
            if i + 1 != 10:
                str += f" {i + 1} ║ "
            else:
                str += f"{i + 1} ║ "
            for token in ligne:
                match token:
                    case 0:
                        aff = "O"
                    case 2:
                        aff = "X"
                    case _:
                        aff = "*"
                str += f"{aff} "
            str += "║\n"
        str += "   ╚═════════════════════╝\n"
        str += "     1 2 3 4 5 6 7 8 9 10"
        return str

    """
    try to play and shote in (x,y) and change it status (2 or 0)
    @input:     x,y
    @output:    *
    """

    def play(self, x, y):
        # -1 -> eau
        #  0 -> coup pas touche
        #  1 -> bateau
        #  2 -> touche

        if self.plateau[x, y] == 1:
            print("touché !")
            self.plateau[x, y] = 2
        elif self.plateau[x, y] == -1:
            print("loupé !")
            self.plateau[x, y] = 0

    """
    play a in random place of the grid
    """

    def IA_random(self):
        x, y = randint(0, 10), randint(0, 10)
        self.play(x, y)

    """
    play in a random place but only if it isn't alrady play (status = 2 or 0)
    @input:     display (display in command prompt)
    """

    def play_random(self, display=True):
        possible = True
        while possible:
            x, y = randint(0, 10), randint(0, 10)
            possible = self.plateau[x, y] == 2 or self.plateau[x, y] == 0
            if not (possible):
                if display:
                    print(f"Coup joué ({x+1},{y+1})")
                self.play(x, y)

    """
    check if there are any boat in the grid
    @output:    boolean
    """

    def in_life(self):
        for row in self.plateau:
            for element in row:
                if element == 1:
                    return True
        print("Le jeu est fini")
        return False

    """
    save the grid in npz format
    @input:     path (saving path)
                name (plateau name)
                display
    """

    def save(self, path, name, display=True):
        if display:
            print(f"Saving {name} ...")
        with open(path + "\\" + name + ".npz", "wb") as f:
            save(f, self.plateau)

    """
        load the grid in npz format
        @input:     path (saving path)
                    name (plateau name)
        """

    def load(self, path, name):
        name = path + "\\" + name + ".npz"
        tmp = load(name)
        self.plateau = tmp


# test
# plateau_1 = plateau()
# print(plateau_1)
# plateau_1.place_boat(8)
# print(plateau_1)
# plateau_1.play_random(1,1)
