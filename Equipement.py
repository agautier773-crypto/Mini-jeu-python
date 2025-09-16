
import json

class Equipement :
    nom : str 
    categorie : str
    bonus_attaque = 0
    bonus_defense = 0
    bonus_vie = 0
    coef_rarete = {"Commun": 1.0 ,
              "Rare" : 1.15,
              "Epique": 1.50,
              "Légendaire":2.0
    }
    default_categorie : list = ["arme", "bouclier","potion"]
    categorie : str   

    def __init__(self, nom :str, categorie : str, bonus_attaque =0, bonus_defense =0, bonus_vie =0, coef_rarete ="commun") :
       
        self.nom = nom 
        if categorie in self.default_categorie :
            self.categorie = categorie
        else: 
            self.categorie = "default"
            f"Les catégories d'objet valides sont : {self.default_categorie}"
        self.bonus_attaque = bonus_attaque 
        self.bonus_defense = bonus_defense
        self.bonus_vie = bonus_vie
        self.rarete = coef_rarete.capitalize()
        self.coef = self.coef_rarete.get(self.rarete, 1.0)
        self.atk = int(self.bonus_attaque * self.coef)
        self.defense = int(self.bonus_defense * self.coef)
        self.vie = int(self.bonus_vie * self.coef)

    def presentation (self) :
 
        return f"{self.nom}, {self.categorie}, {self.rarete}  / +{self.atk} ATK / +{self.defense} DEF / +{self.vie} Pv en plus"
    
    def liste_equipement(listeequipement):
        with open (listeequipement, "r", encoding = "utf-8") as f :
            donnees = json.load(f)
        equipements = [] 
        for item in donnees :
            eq = Equipement(
                nom = item["nom"],
                categorie = item["categorie"],
                bonus_attaque = item["bonus_attaque"],
                bonus_defense = item["bonus_defense"],
                bonus_vie = item ["bonus_vie"],
                coef_rarete = item["coef_rarete"]
            )
            equipements.append(eq)
        return equipements


         
            