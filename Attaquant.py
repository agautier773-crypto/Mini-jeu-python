from Joueur import Joueur

class Attaquant (Joueur) :
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 35
        self.defense = 12
        self.vie = 90