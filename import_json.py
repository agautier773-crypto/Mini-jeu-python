import json 
import sqlite3 

def importer_items(json_path, type_item) :
    type_item = type_item.capitalize()
    with open(json_path, "r", encoding='utf-8') as f:
        items = json.load(f)
   

    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()

    for item in items.values():
        # Insérer dans Item (table générique)
        cursor.execute("""
            INSERT INTO Item (nom, bonus_ATK, bonus_DEF, bonus_VIE)
            VALUES (?, ?, ?, ?)
        """, (
            item.get('nom', ''),
            item.get('bonus_ATK', 0),
            item.get('bonus_DEF', 0),
            item.get('bonus_VIE', 0)
        ))
        id_item = cursor.lastrowid
        nom_item = item.get('nom', '')
    

        # Insère dans la table pour gérer l’héritage
        cursor.execute(f"INSERT INTO {type_item} (id,nom) VALUES (?,?,?)", (id_item, nom_item,))

    conn.commit()
    conn.close()


importer_items("C:/Users/GAUTIER/Desktop/Exercice Python/Classes/arme.json", "Arme")
importer_items("C:/Users/GAUTIER/Desktop/Exercice Python/Classes/bouclier.json", "bouclier")
importer_items("C:/Users/GAUTIER/Desktop/Exercice Python/Classes/potion.json", "potion")
