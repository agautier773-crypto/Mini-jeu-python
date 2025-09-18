from Joueur import Joueur 

class Milieu (Joueur) : 
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 30
        self.defense = 20
        self.vie = 120