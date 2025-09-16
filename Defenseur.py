from Joueur import Joueur

class Defenseur (Joueur) :
    def __init__(self, nom, classe):
        super().__init__(nom, classe)
        self.attaque_base = 12
        self.defenseur = 37
        self.vie = 110