from Joueur import Joueur 

class Milieu (Joueur) : 
    def __init__(self, nom, classe):
        super().__init__(nom, classe)
        self.attaque_base = 20
        self.defense = 30
        self.vie = 100