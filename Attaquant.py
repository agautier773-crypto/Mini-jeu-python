from Joueur import Joueur

class Attaquant (Joueur) :
    def __init__(self, nom, classe):
        super().__init__(nom, classe)
        self.attaque_base = 35
        self.defense = 12
        self.vie = 90