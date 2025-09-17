from Joueur import Joueur

class Defenseur (Joueur) :
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 12
        self.defenseur = 37
        self.vie = 110