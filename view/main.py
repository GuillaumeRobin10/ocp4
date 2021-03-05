#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view.tools import choice_menu
from controller.tournament import test_tournois,test_player
from controller.rounding import first_round,other_round,test_point
from view.display_instance_making import display_make_a_tournament, display_make_a_player

# global Const
CASES1239 = ["1", "2", "3", "9"]
CASES129 = ["1", "2", "9"]
CASES1 = ["1"]
MAIN_MENU = {"string": "Tournois (1)\nJoueurs (2)\nliste (3)\nquitter (9)\n",
             "cases": CASES1239,
             "Header": "Menu"}
T_MENU_STRING = {"string": "Nouveau (1)\nCharger (2)\nRetour (3)\nquitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Tournois"}
LIST_MENU_STRING = {"string": "Ordre alphabétique (1)\nClassement (2)\nRetour (3)\nquitter (9)",
                    "cases": CASES1239,
                    "Header": "Liste"}
P_MENU_STRING = {"string": "Nouveau (1)\nCharger (2)\nRetour (3)\nquitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Joueur"}
IN_ROUND_MENU = {"string": "Prochaine ronde (1)\nJoueur (2)\nListe (3)\nQuitter (9)",
                 "cases": CASES1239,
                 "Header": "Menu Ronde"}
S_PLAYER = {"string": "Sauvegardez (1)\nAjouter au tournois (2)\nQuitter (9)",
                 "cases": CASES129,
                 "Header": "Ajouter un joueur"}

S_PLAYER = {"string": "Revenir au menu (1)\n",
                 "cases": CASES1,
                 "Header": "Tournois complet"}
# End of global Const

# Global Variable

players = []

# End of global variable


def in_round_menu(current_tournament):
    u_choice = choice_menu(IN_ROUND_MENU["string"], IN_ROUND_MENU["cases"], IN_ROUND_MENU["Header"])
    if u_choice == "1":
        if len(current_tournament.players_id) == 8:
            if not current_tournament.rounds:
                current_tournament = first_round(players, current_tournament)
                for match in current_tournament.rounds[-1].matches:
                    print(match)
                test_point(players, current_tournament)
                in_round_menu(current_tournament)
            else:
                current_tournament = other_round(players, current_tournament)
                print(current_tournament.rounds[-1].matches)
                test_point(players, current_tournament)
                in_round_menu(current_tournament)

        else:
            p_menu()
    elif u_choice == "2":
        p_menu()
    elif u_choice == "3":
        l_menu()
    elif u_choice == "9":
        pass
    else:
        print("Houston on as un problème")


def main_menu():
    u_choice = choice_menu(MAIN_MENU["string"], MAIN_MENU["cases"], MAIN_MENU["Header"])

    if u_choice == "1":
        t_menu()
    elif u_choice == "2":
        p_menu()
    elif u_choice == "3":
        l_menu()
    elif u_choice == "9":
        print(len(players))
    else:
        print("Houston on as un problème")


def t_menu():
    u_choice = choice_menu(T_MENU_STRING["string"], T_MENU_STRING["cases"], T_MENU_STRING["Header"])
    if u_choice == "1":
        #tournament = display_make_a_tournament()
        current_tournament = test_tournois()#this is the provisoire tournament making
        print(f"{current_tournament.name}")
    elif u_choice == "2":
        print("loading")
        pass
    elif u_choice == "3":
        main_menu()
    elif u_choice == "9":
        return 0
    else:
        print("Houston on as un problème")
    for player in players:
        current_tournament.edit_players_id(player.identity)
    in_round_menu(current_tournament)


def l_menu():
    u_choice = choice_menu(LIST_MENU_STRING["string"], LIST_MENU_STRING["cases"], LIST_MENU_STRING["Header"])
    if u_choice == "1":
        print("ordre alpha")
    elif u_choice == "2":
        sorted_player = sorted(players, key=lambda player: player.tournament_point[1], reverse=True)
        for player in sorted_player:
            print(f"prénom : {player.firstname} points {player.tournament_point}")
    elif u_choice == "3":
        main_menu()
    elif u_choice == "9":
        pass
    else:
        print("Houston on as un problème")


def p_menu():
    u_choice = choice_menu(P_MENU_STRING["string"], P_MENU_STRING["cases"], P_MENU_STRING["Header"])
    if u_choice == P_MENU_STRING["cases"][0]:
        player = display_make_a_player()
        u_choice = choice_menu(S_PLAYER["string"], S_PLAYER["cases"], S_PLAYER["Header"])
        if u_choice == S_PLAYER["cases"][0]:
            # save_player(player)
            pass
        elif u_choice == S_PLAYER["cases"][1]:
            if len(players) >= 8:
                players.append(player)
            else:
                choice_menu(S_PLAYER["string"], S_PLAYER["cases"], S_PLAYER["Header"])
            main_menu()
        elif u_choice == S_PLAYER["cases"][2]:
            pass
    elif u_choice == P_MENU_STRING["cases"][1]:
        # players.append(loadedplayer)
        print("chargement")
    elif u_choice == P_MENU_STRING["cases"][2]:
        main_menu()
    elif u_choice == P_MENU_STRING["cases"][3]:
        pass
    else:
        print("Houston on as un problème")


def main_view():
    for i in range(8):
        a = test_player(i, 1)
        players.append(a)
    main_menu()
