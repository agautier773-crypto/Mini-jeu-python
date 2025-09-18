from Equipement import Equipement
from JsonManager import JsonManager


class Potion (Equipement):

    def __init__(self, nom, bonus_vie, coef_rarete="commun"):
        super().__init__(nom, "Potion")
        self.bonus_vie = bonus_vie
        self.coef_rarete = coef_rarete

    def presentation (self): 
        return f"{self.nom} (+{self.bonus_vie} VIE)"
    
    @staticmethod
    def disponibles () :
        potions = JsonManager("C:\\Users\\GAUTIER\\Desktop\\Exercice Python\\Classes\\potion.json").load()
        liste_potion = []
        for potion in potions.values():
            liste_potion.append(Potion(potion["nom"],potion["bonus_vie"],potion["coef_rarete"]))
        # for potion in liste_potion:
        #     # print (potion.presentation())
        return liste_potion
        
                                       