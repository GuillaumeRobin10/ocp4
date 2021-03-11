#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.tournament import test_tournois, test_player
from controller.rounding import first_round, other_round, scoring

from view.display_instance_making import display_make_a_tournament, display_make_a_player
from view.tools import choice_menu
from view.setting import MAIN_MENU, T_MENU_STRING, RAPPORT_MENU_STRING, P_MENU_STRING, IN_ROUND_MENU, S_PLAYER, S_C_PLAYER
from view.setting import players
from view.home_menu import main_menu


def r_menu():
    u_choice = choice_menu(RAPPORT_MENU_STRING["string"], RAPPORT_MENU_STRING["cases"], RAPPORT_MENU_STRING["Header"])
    if u_choice == "1":
        print("ordre alpha")
    elif u_choice == "2":
        """
        sorted_player = sorted(players, key=lambda player: player.tournament_point[1], reverse=True)
        for player in sorted_player:
            print(f"prénom : {player.firstname} points {player.tournament_point}")
            """
    elif u_choice == "6":
        main_menu()
    elif u_choice == "9":
        pass
    else:
        print("Houston on as un problème")

