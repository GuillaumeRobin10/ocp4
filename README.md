# ChessTournament
projet 4 openclassroom

Le projet ChessTournament, est une application terminal a exécuter localement réaliser dans le cadre d'une formation.Elle permet de gérer des tournois d'échecs.Elle permets de  sauvegarder des tournois et des joueurs dans la base de données associé.Elle permet également de charger des données se trouvant dans la base de données. Cette application génère les rondes sous un format suisse.

Cette application peut être installée en suivant les étapes décrites ci-dessous. 


### Installation et exécution de l'application

1.  Cloner ce dépôt de code à l'aide de la commande  `$ git clone https://github.com/GuillaumeRobin10/ocp4.git`
2.  Rendez-vous depuis un terminal à la racine du répertoire ocp4 avec la commande  `$ cd ocp4`
3.  Créer un environnement virtuel pour le projet avec  `$ python -m venv env`  sous Windows ou  `$ python3 -m venv env`  sous MacOS ou Linux.
4.  Activez l'environnement virtuel avec  `$ env\Scripts\activate`  sous Windows ou  `$ source env/bin/activate`  sous MacOS ou Linux.
5.  Installez les dépendances du projet avec la commande  `$ pip install -r requirements.txt`
6. Lancer l'application avec la commande `$ python ChessTournament.py`

## Utilisation et documentation

Dans cette application vous ne pouvez pas voir vos entrez clavier tant qu'elle n'ont pas été validée par l'application.
La sauvegarde des joueurs et des tournois est automatique à la fin de chaque ronde.
la sauvegarde d'un joueur est automatique si vous changer sont classement.
