from Equipement import Equipement

class Potion (Equipement):
    liste_potion = [
        {"nom": "powerade", "bonus_vie": 6, "rarete": "Epique"},
        {"nom": "gourde", "bonus_vie": 12, "rarete": "Commun"}
    ]
    def __init__(self, nom, bonus_vie, coef_rarete="commun"):
        super().__init__(nom)
        self.bonus_vie = bonus_vie
        self.coef_rarete = coef_rarete