from Equipement import Equipement

class Bouclier (Equipement):
    liste_bouclier = [
        {"nom": "protège-tibia", "bonus_defense": 8, "coef_rarete": "Legendaire"},
        {"nom": "gants", "bonus_defense" : 6, "coef_rarete": "Rare"}
    ]
    def __init__(self, nom,bonus_defense, coef_rarete = "Commun"):
        super().__init__(nom)
        self.bonus_defense = bonus_defense
        self.coef_rarete = coef_rarete