from Combattant import combattant

class Mage(combattant):
    def __init__(self):
        combattant.__init__(80,15)

    def __str__(self):
        return f'Mage;{self.pv};{self.pa}'

    def __repr__(self):
        return f"objet = Mage(pv='{self.pv}',pa='{self.pa}')"