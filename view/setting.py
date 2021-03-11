
# global Const
CASES1239 = ["1", "2", "3", "9"]
CASES123569 = ["1", "2", "3", "4", "5", "6", "9"]
CASES129 = ["1", "2", "9"]
CASES1 = ["1"]
MAIN_MENU = {"string": "Tournois (1)\nJoueurs (2)\nRapport (3)\nquitter (9)\n",
             "cases": CASES1239,
             "Header": "Menu"}
T_MENU_STRING = {"string": "Nouveau (1)\nCharger (2)\nRetour (3)\nquitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Tournois"}
RAPPORT_MENU_STRING = {"string": "Liste de tous les acteurs (1)"
                              "\nListe de tous les joueurs d'un tournoi (2)"
                              "\nListe de tous les tournois (3)\n"
                              "Liste de tous les matchs d'un tournoi (4)\n"
                              "Liste de tous les tours d'un tournoi. (5)"
                              "\nRetour (6)"
                              "\nQuitter (9)",
                    "cases": CASES123569,
                    "Header": "RAPPORTS"}
P_MENU_STRING = {"string": "Nouveau (1)\nCharger (2)\nRetour (3)\nquitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Joueur"}
IN_ROUND_MENU = {"string": "Prochaine ronde (1)\nJoueur (2)\nRapport (3)\nQuitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Ronde"}
S_PLAYER = {"string": "Sauvegardez (1)\nAjouter au tournois (2)\nQuitter (9)",
                 "cases": CASES129,
                 "Header": "Ajouter un joueur"}

S_C_PLAYER = {"string": "Revenir au menu (1)\n",
                 "cases": CASES1,
                 "Header": "Tournois complet"}

# End of global Const

# Global Variable


players = []

# End of global variable