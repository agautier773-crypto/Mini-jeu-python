from Equipement import Equipement
import json 
import random


class Joueur : 
    nom : str
    vie = 100 
    defense = 25
    classe = str
    endurance = 100
    attaque_base = 25
    sous_boost = False
    endurance_par_coup = 25
    coef_rarete = {"Commun": 1.0 ,
              "Rare" : 1.15,
              "Epique": 1.50,
              "Légendaire":2.0
    }
    
    def __init__(self, nom : str):
        self.nom = nom 
        self.equipement = []
        self.sous_boost = False
        self.attaque = self.attaque_base
        
        # print (f"Création du perso {nom} avec la classe : {classe}")
    
    # def changer_nom(self) :
    #     nouveau_nom = input ("Saisissez le nom de votre personnage : ")
    #     if len(nouveau_nom) > 20 :
    #         return f"Le nom est trop long (20 caractère max)"
    #     self.nom = nouveau_nom

    def creer_perso(): 
        from Gardien import Gardien
        from Defenseur import Defenseur
        from Milieu import Milieu 
        from Attaquant import Attaquant 

        nom = input ("Saisir le nom de votre personnage :")
        print(f"""Choisissez une Classe :
              1 : Attaquant (ATK: 35/ DEF: 12/ VIE: 90)
              2 : Milieu (ATK: 20/ DEF: 30/ VIE: 100)
              3 : Defenseur (ATK: 12/ DEF: 37/ VIE: 110)
              4 : Gardien (ATK: 10/ DEF: 40/ VIE: 120)""")
        choix = input("Votre Choix : ")
        match choix :
            case "1":
                return Attaquant(nom)
            case "2":
                return Milieu(nom)
            case "3":
                return Defenseur(nom)
            case "4":
                return Gardien(nom)
            case _:
                print("Choix invalide ")
                return Joueur(nom)

    def equiper (self, equipement) :
        from Arme import Arme
        from Bouclier import Bouclier
        from Potion import Potion
        if equipement in self.equipement:
            return f"{self.nom} est déja équipé de {equipement.presentation()}"
        if isinstance (equipement, Arme):
            self.attaque_base += equipement.bonus_attaque
            self.attaque = self.attaque_base
            self.equipement.append(equipement)
            print(f"{self.nom} est équipé de l'arme {equipement.presentation()}")
        elif isinstance(equipement, Bouclier):
            self.defense += equipement.bonus_defense
            self.equipement.append(equipement)
            print(f"{self.nom} est équipé du bouclier {equipement.presentation()}")
        elif isinstance(equipement, Potion):
            self.vie += equipement.bonus_vie
            self.equipement.append(equipement)
            print(f"{self.nom} a pris la potion {equipement.presentation}")   
        else :
            print("Aucun equipement trouvé")
    
    def retirer (self, equipement) :
        from Arme import Arme
        from Bouclier import Bouclier
        from Potion import Potion
        print("Retirer Equipement")
        if not equipement in self.equipement:
            return f"Aucun equipement trouvé"
        if isinstance (equipement, Arme):
            self.attaque_base -= equipement.bonus_attaque
            self.attaque = self.attaque_base
            print(f"{self.nom} a retiré l'arme {equipement.presentation()}")
        elif isinstance(equipement, Bouclier):
            self.defense -= equipement.bonus_defense            
            print(f"{self.nom} a retiré le bouclier {equipement.presentation()}")
        elif isinstance(equipement, Potion):
            self.vie -= equipement.bonus_vie            
            print(f"{self.nom} a retiré la potion {equipement.presentation}")   
        else :
            print("Aucun equipement trouvé")
            return 
        self.equipement.remove(equipement)                                                 
    
    def attaquer (self, cible) :
        if cible.vie <= 0 :
            return f"Perso déjà mort"
        degat = self.attaque - cible.defense 
        if degat < 0 :
            degat = 0
        cible.vie -= degat 
        if cible.vie < 0 :
            cible.vie = 0
    
        if self.sous_boost : 
            self.sous_boost = False 
        return f"{self.nom} a attaquer {cible.nom} infligeant {degat}, il reste {cible.vie} Pv a {cible.nom}"
        
    def presentation (self) :
        return f"Je suis {self.nom}, avec {self.attaque_base} d'attaque, {self.defense} de défense et {self.vie} de points de vie"
        
    def soins (self) :
        if self.vie == 100:
            return print("Votre vie est déjà au max !!")
        elif self.vie <= 0:
            return print("Le personnage est déjà mort")
        self.vie = self.vie + self.attaque
        return f"{self.nom} vient de se soigner"
        
    def coup_de_boule(self) : 
        if not self.sous_boost :
           self.attaque = self.attaque_base * 1.2
           self.sous_boost = True 
           return f"{self.nom} a donné un coup de boule il gagne 20% de dommage sur sa prochaine attaque"
        else:
           return f"{self.nom} est déjà sous boost" 
           
        
 

