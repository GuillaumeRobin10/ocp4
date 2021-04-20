# ChessTournament
Projet 4 openclassroom

Le projet ChessTournament, est une application terminal à exécuter localement réalisée dans le cadre d'une formation. Elle permet de gérer des tournois d'échecs. Elle permet de sauvegarder des tournois et des joueurs dans la base de données associée. Elle permet également de charger des données se trouvant dans la base de données. Cette application génère les rondes sous un format suisse.

Cette application peut être installée en suivant les étapes décrites ci-dessous. 


### Installation et exécution de l'application

1.  Cloner ce dépôt de code à l'aide de la commande  `$ git clone https://github.com/GuillaumeRobin10/ocp4.git`
2.  Rendez-vous depuis un terminal à la racine du répertoire ocp4 avec la commande  `$ cd ocp4`
3.  Créer un environnement virtuel pour le projet avec  `$ python -m venv env`  sous Windows ou  `$ python3 -m venv env`  sous MacOS ou Linux.
4.  Activez l'environnement virtuel avec  `$ env\Scripts\activate`  sous Windows ou  `$ source env/bin/activate`  sous MacOS ou Linux.
5.  Installez les dépendances du projet avec la commande  `$ pip install -r requirements.txt`
6. Lancer l'application avec la commande `$ python ChessTournament.py`

## Utilisation et documentation

Dans cette application vous ne pouvez pas voir vos entrées clavier tant qu'elles n'ont pas été validées par l'application.
La sauvegarde des joueurs et des tournois est automatique à la fin de chaque ronde.
La sauvegarde d'un joueur est automatique si vous change son classement.

## Flake8

Afin de pouvez générer un rapport flake8 html vous devez suivre les instructions suivantes:
1. Ouvrez un terminal dans le dossier ocp4.
2. Activez l'environnement virtuel avec  `$ env\Scripts\activate`  sous Windows ou  `$ source env/bin/activate`  sous MacOS ou Linux.
3. Lancer le rapport du projet avec la commande  `flake8 --format=html --htmldir=flake-report --exclude env --max-line-length 11`
