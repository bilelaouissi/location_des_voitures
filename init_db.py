import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO locataire (id_loc, nom, prenom, adresse) VALUES (?, ?, ?, ?)",
            ('1', 'Atef', 'Zoiaidi', 'Tunis')
            )

cur.execute("INSERT INTO voiture (num_imma, marque, modele, kilometrage, etat, prix_location) VALUES (?, ?, ?, ?, ?, ?)",
            ('111111', 'Peugeot', 'Peugeot 308', '150000', '0', '50')
            )
cur.execute("INSERT INTO voiture (num_imma, marque, modele, kilometrage, etat, prix_location) VALUES (?, ?, ?, ?, ?, ?)",
            ('111111', 'Peugeot', 'Peugeot 208', '50000', '0', '60')
            )
connection.commit()
connection.close()