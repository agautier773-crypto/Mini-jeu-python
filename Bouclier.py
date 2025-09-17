from Equipement import Equipement

class Bouclier (Equipement):
    liste_bouclier = [
        {"nom": "protège-tibia", "bonus_defense": 8, "coef_rarete": "Legendaire"},
        {"nom": "gants", "bonus_defense" : 6, "coef_rarete": "Rare"}
    ]
    def __init__(self, nom,bonus_defense, coef_rarete = "Commun"):
        super().__init__(nom, "Bouclier")
        self.bonus_defense = bonus_defense
        self.coef_rarete = coef_rarete
    
    def presentation (self): 
        return f"{self.nom} (+{self.bonus_defense} DEF)"
    
    @classmethod
    def disponible(cls):
        objets = []
        for eq in cls.liste_bouclier:
            nom = eq["nom"]
            bonus = eq["bonus_defense"]
            rarete = eq["coef_rarete"] if "coef_rarete" in eq else "Commun"
            objets.append(cls(nom, bonus, rarete))
        return objets
