


class boat():


    def __init__(self, x, y, lenght, direction):
        self.x = x
        self.y = y
        self.lenght = lenght
        self.direction = direction


    def position(self):
        return self.x, self.y

    def where(self):
        return self.x, self.y, self.direction

    def len(self):
        return self.lenght

    def __str__(self):
        return f"le bateau est en x:{self.x}-y:{self.y} avec une longueur de {self.lenght} dans la direction {self.direction}"



# b = boat(1,1,3,0)
# print(b)