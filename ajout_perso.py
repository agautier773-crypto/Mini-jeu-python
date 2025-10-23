import sqlite3

def ajouter_perso():
    conn = sqlite3.connect("game_data.db")
    conn.execute ("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    print("\n === Création d'un personnage ===")
    nom = input("Saisissez le nom de votre personnage : ")
    description = input("Description : (facultatif)")

    cursor.execute ("SELECT id, nom, ATK, DEF, VIE FROM Classes")
    classes = cursor.fetchall()
    if not classes : 
        print("Aucune classe trouvée")
        conn.close()
        return 
    
    print("\n === Classes disponibles ===")
    for c in classes : 
        print(f"{c[0]}. {c[1]} (ATK: {c[2]}, DEF: {c[3]}, VIE: {c[4]})")
    
    id_classe = input("Choisi le numéro de la classe : ")

    cursor.execute ("""
        iNSERT INTO Personnage (nom, description, id_classes)
        VALUES (?,?,?)
    """, (nom, description, id_classe))
    
    conn.commit ()
    conn.close()
    print("Personnage crée avec succès")

ajouter_perso()

