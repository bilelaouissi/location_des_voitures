from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
from sqlalchemy import asc
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = "71ebf8e13ca209536c29be68d435c00"
app.debug = True
db = SQLAlchemy(app)
from models import Voiture, Locataire


@app.route("/voitures/ajouter", methods=['GET', 'POST'])
def add_voitures():
    if request.method == 'POST':
        data = request.form
        try:
            voiture = Voiture(num_imma=data['num_imma'], marque=data['marque'], modele=data['modele'],
                              kilometrage=data['kilometrage'], prix_location=data['prix_location'])
            db.session.add(voiture)
            db.session.commit()
            success = "Voiture ajouté"
        except Exception as e:
            fail = e
            return render_template('voitures/add.html', result={"fail": fail})
        return render_template('voitures/add.html', result={"success": success})
    else:
        return render_template('voitures/add.html')


@app.route("/voitures/modify/<int:id>/", methods=['GET', 'POST'])
def modify_voitures(id):
    if request.method == 'POST':
        data = request.form
        locataires = Locataire.query.all()
        try:
            voiture = Voiture.query.get(id)
            voiture.num_imma = data['num_imma']
            voiture.marque = data['marque']
            voiture.modele = data['modele']

            locataire = data.get('locataire', None)
            if locataire:
                voiture.locataire = locataire
                voiture.etat = 1
            else:
                voiture.etat = data.get('etat', 0)
            voiture.kilometrage = data['kilometrage']
            voiture.prix_location = data['prix_location']
            db.session.commit()
            success = "Modification enregistrée"
        except Exception as e:
            fail = e
            return render_template('voitures/modify.html', result={"fail": fail})
        result = {"success": success, "voiture": voiture, 'locataires': locataires}
        if locataire:
            locataire = Locataire.query.get(locataire)
            result.update({"locataire": locataire})
        return render_template('voitures/modify.html', result=result)
    else:
        voiture = Voiture.query.get(id)
        locataires = Locataire.query.all()
        result = {"voiture": voiture, 'locataires': locataires}
        if voiture is None:
            result.update({"fail": "Voiture pas trouvé!"})
        else:
            if voiture.etat == 1:
                locataire = Locataire.query.get(voiture.locataire)
                result.update({"locataire": locataire})
        return render_template('voitures/modify.html', result=result)


@app.route("/voitures")
def voitures():
    voiture_list = Voiture.query.all()
    return render_template('voitures/list.html', voitures=voiture_list)


@app.route("/voitures/supprimer/<int:id>/")
def supprimer_voiture(id):
    voiture = Voiture.query.get(id)
    db.session.delete(voiture)
    db.session.commit()
    return redirect('/voitures')


@app.route("/locataires/ajouter", methods=['GET', 'POST'])
def add_locataires():
    if request.method == 'POST':
        data = request.form
        try:
            locataire = Locataire(id_loc=data['id_loc'], nom=data['nom'], prenom=data['prenom'],
                                  adresse=data['adresse'])
            db.session.add(locataire)
            db.session.commit()
            success = "locataire ajouté"
        except Exception as e:
            fail = e
            return render_template('locataires/add.html', result={"fail": fail})
        return render_template('locataires/add.html', result={"success": success})
    else:
        return render_template('locataires/add.html')


@app.route("/locataires", methods=['GET', 'POST'])
def locataires():
    if request.method == 'POST':
        key = request.form['key']
        search = "%{}%".format(key)
        locataire_list = Locataire.query.filter(Locataire.nom.like(search) | Locataire.id_loc.like(search)).order_by(asc(Locataire.nom))
        return render_template('locataires/list.html', locataires=locataire_list)
    else:
        locataire_list = Locataire.query.filter().order_by(asc(Locataire.nom))
        return render_template('locataires/list.html', locataires=locataire_list)


@app.route("/locataires/modify/<int:id>/", methods=['GET', 'POST'])
def modify_locataires(id):
    if request.method == 'POST':
        data = request.form
        try:
            locataire = Locataire.query.get(id)
            locataire.id_loc = data['id_loc']
            locataire.nom = data['nom']
            locataire.prenom = data['prenom']
            locataire.adresse = data['adresse']
            db.session.commit()
            success = "Modification enregistrée"
        except Exception as e:
            fail = e
            return render_template('locataires/modify.html', result={"fail": fail})
        return render_template('locataires/modify.html', result={"success": success, "locataire": locataire})
    else:
        locataire = Locataire.query.get(id)
        result = {"locataire": locataire}
        if locataire is None:
            result.update({"fail": "Locataires pas trouvé ou supprimer!"})
        return render_template('locataires/modify.html', result=result)


@app.route("/locataires/supprimer/<int:id>/")
def supprimer_locataire(id):
    from models import Locataire
    locataire = Locataire.query.get(id)
    db.session.delete(locataire)
    db.session.commit()
    return redirect('/locataires')


@app.route("/")
def index():
    voitures = Voiture.query.all()
    total_km, moyen, total = 0, 0, 0
    total = len(voitures)
    for voiture in voitures:
        total_km += voiture.kilometrage
    if total != 0:
        moyen = total_km / total

    return render_template('index.html', data={"moyen": moyen, "total": total})


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
