import sqlite3

def init_db():
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        ATK INTEGER,
        DEF INTEGER,
        VIE INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Personnage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        description TEXT,
        id_classes INTEGER,
        FOREIGN KEY(id_classes) REFERENCES Classes(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Item (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        bonus_ATK INTEGER,
        bonus_DEF INTEGER,
        bonus_VIE INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Arme (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        FOREIGN KEY(id) REFERENCES Item(id_item)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Bouclier (
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        FOREIGN KEY(id) REFERENCES Item(id_item)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Potion (
        id INTEGER PRIMARY KEY,               
        nom TEXT NOT NULL,
        FOREIGN KEY(id) REFERENCES Item(id_item)
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Est_Equipe (
        id_personnage INTEGER,
        id_item INTEGER,
        PRIMARY KEY(id_personnage, id_item),
        FOREIGN KEY(id_personnage) REFERENCES Personnage(id),
        FOREIGN KEY(id_item) REFERENCES Item(id_item)
    )''')

    cursor.execute("SELECT COUNT(*) FROM Classes")
    count = cursor.fetchone()[0]

    if count == 0:
        print("Insertion des classes de base...")
        classes_base = [
            ("Attaquant",50 , 10, 90),
            ("Milieu", 30, 20, 120),
            ("Defenseur", 15, 40, 180),
            ("Gardien", 35, 15, 100)
        ]
        cursor.executemany(
            "INSERT INTO Classes (nom, ATK, DEF, VIE) VALUES (?, ?, ?, ?)",
            classes_base
        )

    conn.commit()
    conn.close()

init_db()