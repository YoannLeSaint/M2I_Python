import random as rd

class combattant(object):

    def __init__(self,pv,pa):
        self.pv = pv
        self.pa = pa

    def attaque(self,ennemi):
        jet = rd.randint(0,20)/10
        ennemi.degats(self.pa*jet)
        return self.pa*jet

    def degats(self, coup):
        pv -= coup     

    def pasMort(self):
        return self.pv > 0

    def vie(self):
        return self.pv
    
