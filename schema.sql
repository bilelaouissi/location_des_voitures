DROP TABLE IF EXISTS voiture;
DROP TABLE IF EXISTS locataire;



CREATE TABLE locataire (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_loc INTEGER,
    nom VARCHAR(20),
    prenom VARCHAR(20),
    adresse VARCHAR(20),
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
   

);

CREATE TABLE voiture (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num_imma INTEGER,
    marque VARCHAR(20),
    modele VARCHAR(20),
    kilometrage INTEGER,
    etat INTEGER,
    prix_location FLOAT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_loc INTEGER NULL,
    FOREIGN KEY (id_loc) REFERENCES locataire(id_loc) ON DELETE CASCADE
);
