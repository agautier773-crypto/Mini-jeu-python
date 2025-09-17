from Joueur import Joueur 

class Milieu (Joueur) : 
    def __init__(self, nom):
        super().__init__(nom)
        self.attaque_base = 20
        self.defense = 30
        self.vie = 100