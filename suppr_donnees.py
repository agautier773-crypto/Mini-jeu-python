import sqlite3 

conn = sqlite3.connect("game_data.db")
cursor = conn.cursor()

def suppr ():
    cursor.execute("""DELETE FROM Item""")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Item'")

    conn.commit()
    

suppr()

def drop():
    cursor.executescript("""DROP TABLE Arme;
                   DROP TABLE Bouclier;
                   DROP TABLE Potion;""")
    conn.commit()


drop()
conn.close()