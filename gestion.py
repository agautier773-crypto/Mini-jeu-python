import sqlite3


def supprimer():

    conn = sqlite3.connect ("game_data.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Arme (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        bonus_ATK INT,
        FOREIGN KEY(id) REFERENCES Item(id_item)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Bouclier (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        bonus_DEF INT,
        FOREIGN KEY(id) REFERENCES Item(id_item)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Potion (
        id INTEGER PRIMARY KEY,               
        nom TEXT NOT NULL,
        bonus_VIE INT,
        FOREIGN KEY(id) REFERENCES Item(id_item)
    )''')
supprimer()