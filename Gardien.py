from Joueur import Joueur 

class Gardien (Joueur):
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 8
        self.defense = 37
        self.vie = 120