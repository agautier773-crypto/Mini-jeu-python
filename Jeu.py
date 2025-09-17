import random 
from Joueur import Joueur
from Arme import Arme
from Bouclier import Bouclier
from Potion import Potion

class Jeu :

    def __init__(self, perso1, perso2):
        self.perso1 = perso1
        self.perso2 = perso2

    def combattre (self, p1, p2):
        p1 = self.perso1
        p2 = self.perso2
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

    def choix_equipement (self):
        print("Quel type d'équipement voulez-vous ? :")
        print("1 : Arme")
        print("2 : Bouclier")
        print("3 : Potion")
        choix = input ("Votre Choix : ")
        match choix:
            case "1":
                liste = Arme.disponible()
            case "2":
                liste = Bouclier.disponible()
            case "3": 
                liste = Potion.disponible()
            case _: 
                print("Choix invalide")
                return 
        print("Liste des Equipements disponibles : ")
        for i, eq in enumerate(liste, 1):
            print(f"{i}.{eq.presentation()}")
        choix_eq = input("Choisissez un equipement : ")
        if choix_eq.isdigit():
            index = int(choix_eq) - 1
            if 0 <= index < len(liste):
                equipement_choisi = liste[index]
                
                self.equiper(equipement_choisi)
            else :
                print("Choix invalide")
        else:
            print("Choix invalide")
            
                

