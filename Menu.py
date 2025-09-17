from Joueur import Joueur 
from Jeu import Jeu 


class Menu :
    def __init__(self, perso1, perso2):
        self.perso1 = perso1
        self.perso2 = perso2

    def afficher(self) : 
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
            
            choix_perso = input(f"Quel personnage choisissez vous ? : (1: {self.perso1.nom} 2: {self.perso2.nom}) : ")
            if choix_perso == "1":
                personnage = self.perso1
                print(f"Vous avez choisi le personnage {self.perso1.nom}")
            elif choix_perso == "2" : 
                personnage = self.perso2
                print(f"Vous avez choisi le personnage {self.perso2.nom}")
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
                                
                    Jeu.choix_equipement(self.perso1)
                    Jeu.choix_equipement(self.perso2)
                    
                case "2.b":
                    pass 
                case "2.c":
                    Joueur.retirer(self.perso1, self.perso2)

                case "3.b":
                    combat = Jeu(self.perso1, self.perso2)
                    combat.combattre(self.perso1, self.perso2)