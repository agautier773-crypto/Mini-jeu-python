from Equipement import Equipement
import json 
from JsonManager import JsonManager

class Bouclier (Equipement):
  
    def __init__(self, nom,bonus_defense, coef_rarete = "Commun"):
        super().__init__(nom, "Bouclier")
        self.bonus_defense = bonus_defense
        self.coef_rarete = coef_rarete
    
    def presentation (self): 
        return f"{self.nom} (+{self.bonus_defense} DEF)"
    
    @staticmethod
    def disponibles () :
        boucliers = JsonManager("C:\\Users\\GAUTIER\\Desktop\\Exercice Python\\Classes\\bouclier.json").load()
        liste_bouclier = []
        for bouclier in boucliers.values():
            liste_bouclier.append(Bouclier(bouclier["nom"],bouclier["bonus_defense"],bouclier["coef_rarete"]))
        # for potion in liste_potion:
        #     # print (potion.presentation())
        return liste_bouclier