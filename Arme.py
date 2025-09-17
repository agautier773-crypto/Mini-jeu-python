from Equipement import Equipement

class Arme (Equipement):
    liste_armes = [
        {"nom": "crampons en fer", "bonus_attaque": 6, "coef_rarete": "Epique"},
        {"nom": "crâne chauve", "bonus_attaque" : 8, "coef_rarete": "Legendaire"},
        {"nom": "insultes", "bonus_attaque": 25, "coef_rarete":  "Commun"}
        ]
    def __init__(self, nom, bonus_attaque, coef_rarete = "Commun"):
        super().__init__(nom, "Arme")
        self.bonus_attaque = bonus_attaque
        self.coef_rarete = coef_rarete
    
    def presentation (self): 
        return f"{self.nom} (+{self.bonus_attaque} ATK)"
    
    @classmethod
    def disponible(cls):
        objets = []
        for eq in cls.liste_armes:
            nom = eq["nom"]
            bonus = eq["bonus_attaque"]
            rarete = eq["coef_rarete"] if "coef_rarete" in eq else "Commun"
            objets.append(cls(nom, bonus, rarete))
        return objets



