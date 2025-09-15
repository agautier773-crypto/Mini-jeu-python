from Joueur import Joueur 
from Equipement import Equipement
import random


# def creer_perso():
#     nom = input ("Saisissez le nom de votre personnage : ")
#     print("Choisissez une classe :")
#     print(f""" 1/ Gardien : ATK : 8
#                 DEF : 33
#                 Vie : 120
#         2/ Defenseur : ATK : 12
#                 DEF : 37
#                 Vie : 110
#         3/ Milieu : ATK : 20
#                 DEF : 30
#                 Vie : 100
#         4/ Attaquant : ATK : 35
#                 DEF : 12
#                 Vie : 90
#           """)
#     choix = input("Votre Choix : ")
#     classes = {"1" : "Gardien",
#                "2" : "Defenseur",
#                "3" : "Milieu",
#                "4" : "Attaquant"
#                }
#     classe = classes.get(choix, "Gardien")
#     print(f"{nom} sera un {classe}")
#     return Joueur(nom, classe)

perso1 = Joueur.creer_perso()
perso2 = Joueur.creer_perso()

def combattre (p1 : Joueur, p2 : Joueur):
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
        
        degat2 = max(0, p2.attaque_base - p1.defense)
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

    if vie1 <= 0 and vie2 <= 0 :
        print("Match nul les deux sont deads")
    elif vie1 <= 0 : 
        print(f"{p1.nom} est mort ce soir (comme le roi Lion)")
    else: 
        print(f"{p2.nom} est mort ce soir (comme le roi Lion)")

def menu() : 
    while True : 
        print(f"""

*** MENU MINI JEU ***
      
1 : Gestion personnage
        1.a : Renommer le personnage
        1.b : Gestion des caractéristique (+1 points par niveau)
        1.c : Equipements du perso
2 : Gestion Equipements
        2.a : Ajouter un équipement
        2.b : Modifier un équipement
        2.c : Supprimer un équipement
3 : Gestion du jeu
        3.a : Regles du jeu
        3.b : Combat
0 : Quitter le jeu
""")
            
        choix_perso = input(f"Quel personnage choisissez vous ? : (1: {perso1.nom} 2: {perso2.nom}) : ")
        if choix_perso == "1":
            personnage = perso1
            print(f"Vous avez choisi le personnage {perso1.nom}")
        elif choix_perso == "2" : 
            personnage = perso2
            print(f"Vous avez choisi le personnage {perso2.nom}")
        else: 
            print("Choix invalide")
            continue
        choix = input("Votre choix : ")
        match (choix) :
        
            case "0" :
                print("Vous avez quitter le Mini Jeu")
                break 
            case "1.a":
                personnage.changer_nom()
                print(f"Le nouveau nom est :{personnage.nom}") 
            case "1.b":
                pass 
            case "1.c":
                if personnage.equipement:                    
                    print(f"\n Votre personnage est équipé de :")
                    for i, eq in enumerate(personnage.equipement) :
                        print(f"  {i + 1}. {eq.presentation()}")
                    print(f"Stat du personnage {personnage.nom}: Vie {personnage.vie}, ATK {personnage.attaque_base}, DEF {personnage.defense}")            
                else :
                    print("Aucun Equipement trouvé !")
            case "2.a":                
                print("\n Ajout d'un nouvel Equipement :")
                equipements_disponibles = Equipement.liste_equipement("listeequipement.json")
                if not equipements_disponibles :
                    print("Aucun equipement trouvé")
                    break 
                print("Voici les equipements disponibles : ")
                for i, eq in enumerate(equipements_disponibles):
                    print(f" {i +1}.{eq.presentation()}")

                choix_eq = input("Choisissez un equipement à ajouter (numéros) : ")

                if choix_eq.isdigit() : 
                    numero = int(choix_eq) - 1
                    if 0 <= numero < len(equipements_disponibles): 
                        equipement_choisi = equipements_disponibles[numero]
                        if personnage.equiper(equipement_choisi):
                            print(f" \n {personnage.nom} a choisi l'équipement {equipement_choisi.nom}"
                            f"(+ATK {equipement_choisi.atk}, DEF {equipement_choisi.defense}, PV {equipement_choisi.vie})")                   
                        else : 
                            print(f"le personnage est déjà équipé de {equipement_choisi.nom}")                        
                    else : 
                        print("Numéro invalide")
                else :
                    print("Numero invalide")

            case "2.b":
                pass 
            case "2.c":
                 
                print("\n Retirer un équipement")
                if not personnage.equipement :
                    print("Aucun equipement trouvé")
                else:
                    for i, eq in enumerate(personnage.equipement):
                        
                        print(f" {i +1}.{eq.presentation()}")
                    choix_eq = input("Choisissez un equipement à retirer (numéros) : ")
                    if choix_eq.isdigit() : 
                        numero = int(choix_eq) - 1
                        if 0 <= numero < len(personnage.equipement) : 
                            stuff_a_retirer = personnage.equipement[numero]
                            personnage.retirer(stuff_a_retirer)   
                            print(f"Equipement {stuff_a_retirer.presentation()} a été retiré de votre personnage")    
                                                 
                        else : 
                            print("Numéro invalide")
                    else : 
                        print("Numéro invalide")
            case "3.b":
                combattre(perso1, perso2)
          
               
menu()

        
        
                    



    