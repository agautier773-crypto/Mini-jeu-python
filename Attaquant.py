from Joueur import Joueur

class Attaquant (Joueur) :
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 50
        self.defense = 10
        self.vie = 90