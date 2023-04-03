"""
Author:         Yoann Le Saint

Project Name:   Bataille Navale

Last Update:    2023-04-03

Descrition:     Creation of a boat
                parameters:
                    x,y       -> position on the grid
                    length    -> length of the boat
                    direction -> direction of the boat (verticaly or horizontaly)
"""


class boat:
    def __init__(self, x, y, lenght, direction):
        self.x = x
        self.y = y
        self.lenght = lenght
        self.direction = direction

    """
    position of the boat on the grid
    @output :   x,y (position)
    """

    def position(self):
        return self.x, self.y

    """
    all the arguments of the boat's construtor
    @output :   x,y
                direction
    """

    def where(self):
        return self.x, self.y, self.direction

    """
    lenght of the boat
    @output :   lenght
    """

    def len(self):
        return self.lenght

    """
    display of the parameter's boat
    """

    def __str__(self):
        return f"le bateau est en x:{self.x}-y:{self.y} avec une longueur de {self.lenght} dans la direction {self.direction}"


# b = boat(1,1,3,0)
# print(b)
