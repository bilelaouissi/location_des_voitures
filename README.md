# location-des-voitures
Mini projet location des voitures

## Comment l'installez-vous?
- utiliser git pour cloner.
```bash
git clone https://github.com/bilelaouissi/location-des-voitures.git
```
- Création d'environnements virtuels.
```bash
python -m venv location-voiture/venv
```
- Installation de virtualenv
```bash
pip install virtualenv
```
- Activer l'environnement virtuel
```bash
location-voiture\venv\Scripts\activate
```
- Installer des packages avec pip
```bash
 pip install -r requirement.txt
 ```
- Exécuter l'application
```bash
pip install flask
pip install flask_sqlalchemy
pip install sqlalchemy
flask run
 ```
 
## Gestion des voitures :
- Ajouter, modifier et supprimer une voiture 
![1](https://user-images.githubusercontent.com/24235276/147363439-2bb286c4-94dd-40f6-baa9-d4707262067d.png)
![2](https://user-images.githubusercontent.com/24235276/147363467-d6d56b1b-54ac-493b-a333-5e6261b2e1d2.png)
- Afficher l’état d’une voiture (disponible ou en cours de location)
![3](https://user-images.githubusercontent.com/24235276/147363478-c6621ba4-6fbb-4feb-8e10-f2f9d1da7d78.png)

2) Gestion des locataires :
- Ajouter, modifier et supprimer un locataire
![5](https://user-images.githubusercontent.com/24235276/147363916-889a8a4f-ba7c-4628-a993-1b0a04ae91ee.png)

- Rechercher un locataire par son identifiant et par son nom
- Afficher la liste des locataires par ordre alphabétique
![7](https://user-images.githubusercontent.com/24235276/147363623-48bf2b02-01ad-455f-953b-4063000fca63.png)

## Gestion des locations :
- Louer une voiture
![2](https://user-images.githubusercontent.com/24235276/147364030-ec2d3ff6-946c-46b6-abdf-f973a5d3a9be.png)
- Afficher un état résumé de l’ensemble du parc de voitures (Le nombre total de voitures , Le kilométrage moyen de l’ensemble des voitures )
![6](https://user-images.githubusercontent.com/24235276/147364087-f458e4af-1e8b-41be-a818-d899f6fb5bb7.png)
