from Equipement import Equipement

class Joueur : 
    nom : str
    vie = 100 
    defense = 25
    classe = str
    attaque_base = 25
    endurance = 100
    sous_boost = False
    endurance_par_coup = 25
    coef_rarete = {"Commun": 1.0 ,
              "Rare" : 1.15,
              "Epique": 1.50,
              "Légendaire":2.0
    }

    
    def __init__(self, nom : str, classe :str):
        self.nom = nom 
        self.equipement = []
        self.sous_boost = False
        self.attaque = self.attaque_base
        self.classe = classe 
        self.choix_classe(classe)
        # print (f"Création du perso {nom} avec la classe : {classe}")
    
    def changer_nom(self) :
        nouveau_nom = input ("Saisissez le nom de votre personnage : ")
        if len(nouveau_nom) > 20 :
            return f"Le nom est trop long (20 caractère max)"
        self.nom = nouveau_nom

    def choix_classe (self, classe) :
        self.classe = classe
        if classe == "Gardien" :
            self.attaque_base = 8
            self.defense = 33
            self.vie = 120
        elif classe == "Defenseur" :
            self.attaque_base = 12 
            self.defense = 37
            self.vie = 110
        elif classe == "Milieu" : 
            self.attaque_base = 20
            self.defense = 30
            self.vie = 100
        elif classe == "Attaquant" :
            self.attaque_base = 35 
            self.defense = 12
            self.vie = 90
        else : 
            self.attaque_base = 25 
            self.defense = 25 
            self.vie = 100 
   
    def creer_perso():

        nom = input ("Saisissez le nom de votre personnage : ")
        print("Choisissez une classe :")
        print(f""" 1/ Gardien : ATK : 8
                DEF : 33
                Vie : 120
        2/ Defenseur : ATK : 12
                DEF : 37
                Vie : 110
        3/ Milieu : ATK : 20
                DEF : 30
                Vie : 100
        4/ Attaquant : ATK : 35
                DEF : 12
                Vie : 90
          """)
        choix = input("Votre Choix : ")
        classes = {"1" : "Gardien",
               "2" : "Defenseur",
               "3" : "Milieu",
               "4" : "Attaquant"
               }
        classe = classes.get(choix, "Gardien")
        print(f"{nom} sera un {classe}")
        return Joueur(nom, classe)


    def equiper (self, stuff: Equipement) :
            for eq in self.equipement :
                if eq.nom == stuff.nom :
                    return False            
            self.equipement.append(stuff)            
            self.attaque_base += stuff.atk
            self.defense += stuff.defense
            self.vie += stuff.vie
            return True 

               
    def retirer(self, stuff : Equipement):
        if stuff in self.equipement : 
            self.equipement.remove(stuff)
            self.attaque -= stuff.atk
            self.defense -= stuff.defense
            self.vie -= stuff.vie
            print(f"{stuff.nom} a été retiré de {self.nom}")
        else : 
            print(f"{stuff.nom} n'est pas équipé sur {self.nom}")
    
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
            self.attaque = 25
        return f"{self.nom} a attaquer {cible.nom} infligeant {degat}, il reste {cible.vie} Pv a {cible.nom}"
        
    def presentation (self) :
        return f"Je suis {self.nom}, j'ai {self.vie} point de vie, avec {self.attaque} d'attaque, {self.defense} de défense et {self.vie} de points de vie"
        
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
           
        
