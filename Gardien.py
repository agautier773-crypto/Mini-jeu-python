from Joueur import Joueur 

class Gardien (Joueur):
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 35
        self.defense = 15
        self.vie = 100