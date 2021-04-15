# global Const
CASES1 = ["1"]
CASES12 = ["1", "2"]
CASES19 = ["1", "9"]
CASES129 = ["1", "2", "9"]
CASES139 = ["1", "3", "9"]
CASES1239 = ["1", "2", "3", "9"]
CASES123569 = ["1", "2", "3", "4", "5", "6", "9"]
FIRST_MENU = {"string": "Tournois (1)\nQuitter (9)\n",
              "cases": CASES19,
              "Header": "Menu"}
TOURNAMENT_0_LOADED_MENU_STRING = {"string": "Nouveau (1)\nQuitter (9)",
                                   "cases": CASES19,
                                   "Header": "Menu Tournois"}
T_MENU_STRING = {"string": "Nouveau (1)\nCharger (2)\nQuitter (9)",
                 "cases": CASES129,
                 "Header": "Menu Tournois"}
PLAYER_0_LOADED_MENU_STRING = {"string": "Nouveau (1)\nquitter (9)",
                               "cases": CASES19,
                               "Header": "Menu Joueur"}
PLAYER_MENU_STRING = {"string": "Nouveau (1)\nCharger (2)\nquitter (9)",
                      "cases": CASES129,
                      "Header": "Menu Joueur"}
IN_ROUND_MENU = {"string": "Prochaine ronde (1)\nJoueur (2)\nRapport (3)\nQuitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Ronde"}

END_ROUND_MENU = {"string": "Classement (1)\nJoueur (2)\nRapport (3)\nQuitter (9)",
                  "cases": CASES1239,
                  "Header": "Menu Ronde"}
MOD_PLAYER = {"string": "Modifier le classement (1)\nretour (2)",
              "cases": CASES12,
              "Header": "Menu editions"}
RAPPORT_MENU_STRING = {"string": "Liste de tous les acteurs (1)\n"
                                 "Liste de tous les joueurs du tournoi (2)\n"
                                 "Liste de tous les tournois (3)\n"
                                 "Liste de tous les tours du tournoi. (4)\n"
                                 "Liste de tous les matchs du tournoi (5)\n"
                                 "Retour (6)\n"
                                 "Quitter (9)",
                       "cases": CASES123569,
                       "Header": "RAPPORTS"}
RAPPORT_ACTOR = {"string": "Par ordre alphabétique (1)\n"
                           "Par classement (2)\n",
                 "cases": CASES12,
                 "Header": "Liste de tous les acteurs"}
RAPPORT_ACTOR_IN = {"string": "Par ordre alphabétique (1)\n"
                              "Par classement (2)\n",
                    "cases": CASES12,
                    "Header": "Liste de les acteurs du tournois"}
MAIN_MENU = {"string": "Tournois (1)\nJoueurs (2)\nRapport (3)\nquitter (9)\n",
             "cases": CASES1239,
             "Header": "Menu"}
P_MENU_STRING = {"string": "Nouveau (1)\nCharger (2)\nRetour (3)\nquitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Joueur"}
S_PLAYER = {"string": "Sauvegardez (1)\nAjouter au tournois (2)\nQuitter (9)",
            "cases": CASES129,
            "Header": "Ajouter un joueur"}
S_C_PLAYER = {"string": "Revenir au menu (1)\n",
              "cases": CASES1,
              "Header": "Tournois complet"}
# End of global Const
