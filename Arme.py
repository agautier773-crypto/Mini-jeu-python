from Equipement import Equipement
import json 
from JsonManager import JsonManager

class Arme (Equipement):

    def __init__(self, nom, bonus_attaque, coef_rarete = "Commun"):
        super().__init__(nom, "Arme")
        self.bonus_attaque = bonus_attaque
        self.coef_rarete = coef_rarete
    
    def presentation (self): 
        return f"{self.nom} (+{self.bonus_attaque} ATK)"
    
    @staticmethod
    def disponibles () :
        armes = JsonManager("C:\\Users\\GAUTIER\\Desktop\\Exercice Python\\Classes\\arme.json").load()
        liste_arme = []
        for arme in armes.values():
            liste_arme.append(Arme(arme["nom"],arme["bonus_attaque"],arme["coef_rarete"]))
        # for potion in liste_potion:
        #     # print (potion.presentation())
        return liste_arme


