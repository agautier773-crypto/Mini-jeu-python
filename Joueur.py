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

    def equiper (self) :
            
        print("\n Ajout d'un nouvel Equipement :")
        liste = Equipement.liste_equipement("listeequipement.json")            
        if not liste :
            print("Aucun equipement trouvé")
            return
        else : 
            print("Voici les equipements disponibles : ")           
        for i, eq in enumerate(liste):
            print(f" {i +1}.{eq.presentation()}")
        choix_eq = input("Choisissez un equipement à ajouter (numéros) : ")
        if choix_eq.isdigit() : 
            numero = int(choix_eq) - 1
            if 0 <= numero < len(liste): 
                equipement_choisi = liste[numero]
                self.equipement.append(equipement_choisi)            
                self.attaque_base += equipement_choisi.atk
                self.defense += equipement_choisi.defense
                self.vie += equipement_choisi.vie                        
                print(f" \n {self.nom} a choisi l'équipement {equipement_choisi.nom}"
            f"(+ATK {equipement_choisi.atk}, DEF {equipement_choisi.defense}, PV {equipement_choisi.vie})")     
                return
            else : 
                print("Numéro invalide")
        else : 
            print("Numéro invalide")              
    
                                                       
    def retirer(self):
            print("\n Retirer un équipement")
            if not self.equipement :
                print("Aucun equipement trouvé")
            else:
                for i, eq in enumerate(self.equipement):                        
                    print(f" {i +1}.{eq.presentation()}")
                    choix_eq = input("Choisissez un equipement à retirer (numéros) : ")
                    if choix_eq.isdigit() : 
                        numero = int(choix_eq) - 1
                        if 0 <= numero < len(self.equipement) : 
                            stuff_a_retirer = self.equipement[numero]                             
                            self.equipement.remove(stuff_a_retirer)
                            self.attaque -= stuff_a_retirer.atk
                            self.defense -= stuff_a_retirer.defense
                            self.vie -= stuff_a_retirer.vie  
                            print(f"Equipement {stuff_a_retirer.presentation()} a été retiré de votre personnage")    
    
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
           
        
    def combattre (self, p1, p2):
        print(f" \n --- Combat entre {p1.nom} VS {p2.nom} --- ")
        vie1 = p1.vie 
        vie2 = p2.vie
        tour = 1

        while vie1 > 0 and vie2 > 0 :
            print(f" \n --- Tour {tour} ---")    
            if not p1.sous_boost and random.randint(1,10) == 1:
                print(p1.coup_de_boule())
            degat1 = max(0, p1.attaque - p2.defense)
            vie2 -= degat1
            print(f"{p1.nom} attaque {p2.nom} et inflige {degat1:.2f} de dégâts \n", 
              f"Vie restante de {p2.nom} : {max(0, vie2):.2f})")
            
            if p1.sous_boost :
                p1.attaque = p1.attaque_base
                p1.sous_boost = False

            if vie2 <= 0 :
                print(f"{p2.nom} est mort sous les coups de {p1.nom}")
                break 

            if not p2.sous_boost and random.randint(1,10) == 1 : 
                print(p2.coup_de_boule())        
            degat2 = max(0, p2.attaque - p1.defense)
            vie1 -= degat2
            print(f"{p2.nom} attaque {p1.nom} et inflige {degat2:.2f} de dégâts \n"
              f"Vie restante de {p1.nom}: {max(0, vie1):.2f})")
            
            if p2.sous_boost : 
                p2.attaque = p2.attaque_base
                p2.sous_boost = False
            if vie1 <= 0 :
                print(f"{p1.nom} est mort sous les coups de {p2.nom}")
                break 
            tour += 1

