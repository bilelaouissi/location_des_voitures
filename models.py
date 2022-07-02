from app import db
import datetime


class Locataire(db.Model):
    __tablename__ = 'locataire'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_loc = db.Column(db.Integer, nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Voiture(db.Model):
    __tablename__ = 'voiture'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_imma = db.Column(db.Integer)
    marque = db.Column(db.String(250), nullable=False)
    modele = db.Column(db.String(250), nullable=False)
    kilometrage = db.Column(db.Integer)
    etat = db.Column(db.Integer, default=0)
    prix_location = db.Column(db.Float, default=0)
    locataire = db.Column(db.Integer, db.ForeignKey('locataire.id'), nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)