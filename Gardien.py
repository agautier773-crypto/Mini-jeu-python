from Joueur import Joueur 

class Gardien (Joueur):
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 10
        self.defense = 40
        self.vie = 120