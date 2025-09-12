from Equipement import Equipement

class Joueur : 
    nom : str
    vie = 100 
    defense = 25
    attaque_base = 25
    endurance = 100
    sous_boost = False
    endurance_par_coup = 25
    coef_rarete = {"Commun": 1.0 ,
              "Rare" : 1.15,
              "Epique": 1.50,
              "Légendaire":2.0
    }

    
    def __init__(self, nom : str,attaque):
        self.nom = nom 
        self.equipement = []
        self.sous_boost = False
        self.attaque = attaque
        self.attaque_base = attaque
    
    def changer_nom(self) :
        nouveau_nom = input ("Saisissez le nom de votre personnage : ")
        if len(nouveau_nom) > 20 :
            return f"Le nom est trop long (20 caractère max)"
        self.nom = nouveau_nom

    
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
           
        
