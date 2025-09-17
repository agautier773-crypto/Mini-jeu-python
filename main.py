from Joueur import Joueur 
from Equipement import Equipement
from Jeu import Jeu
from Menu import Menu 

perso1 = Joueur.creer_perso()
perso2 = Joueur.creer_perso()
print(perso1.presentation())
print(perso2.presentation())

menu = Menu(perso1, perso2)
menu.afficher()

        
        
                    



    