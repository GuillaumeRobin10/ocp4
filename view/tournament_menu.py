#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller.tournament import test_tournois, test_player
from controller.rounding import first_round, other_round, scoring

from view.display_instance_making import display_make_a_tournament, display_make_a_player
from view.tools import choice_menu
from view.setting import MAIN_MENU, T_MENU_STRING, RAPPORT_MENU_STRING, P_MENU_STRING, IN_ROUND_MENU, S_PLAYER, S_C_PLAYER
from view.setting import players
from view.home_menu import main_menu

def t_menu():
    u_choice = choice_menu(T_MENU_STRING["string"], T_MENU_STRING["cases"], T_MENU_STRING["Header"])
    if u_choice == "1":
        #current_tournament = display_make_a_tournament()
        current_tournament = test_tournois()#this is the provisoire tournament making
    elif u_choice == "2":
        print("loading")
        pass
    elif u_choice == "3":
        main_menu()
    elif u_choice == "9":
        return 0
    else:
        return 0
    for player in players:
        current_tournament.edit_players_id(player.identity)
    in_round_menu(current_tournament)
