from Equipement import Equipement

class Potion (Equipement):
    liste_potion = [
        {"nom": "powerade", "bonus_vie": 6, "rarete": "Epique"},
        {"nom": "gourde", "bonus_vie": 12, "rarete": "Commun"}
    ]
    def __init__(self, nom, bonus_vie, coef_rarete="commun"):
        super().__init__(nom, "Potion")
        self.bonus_vie = bonus_vie
        self.coef_rarete = coef_rarete

    def presentation (self): 
        return f"{self.nom} (+{self.bonus_vie} VIE)"
    
    @classmethod
    def disponible(cls):
        objets = []
        for eq in cls.liste_potion:
            nom = eq["nom"]
            bonus = eq["bonus_vie"]
            rarete = eq["coef_rarete"] if "coef_rarete" in eq else "Commun"
            objets.append(cls(nom, bonus, rarete))
        return objets
