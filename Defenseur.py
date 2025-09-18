from Joueur import Joueur

class Defenseur (Joueur) :
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 15
        self.defenseur = 40
        self.vie = 180