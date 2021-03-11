#!/usr/bin/env python
# -*- coding: utf-8 -*-

from view.display_instance_making import display_make_a_player
from view.tools import choice_menu
from view.setting import P_MENU_STRING, S_PLAYER, S_C_PLAYER
from view.setting import players
from view.home_menu import main_menu


def players_menu():
    u_choice = choice_menu(P_MENU_STRING["string"], P_MENU_STRING["cases"], P_MENU_STRING["Header"])
    if u_choice == P_MENU_STRING["cases"][0]:
        player = display_make_a_player()
        u_choice = choice_menu(S_PLAYER["string"], S_PLAYER["cases"], S_PLAYER["Header"])
        if u_choice == S_PLAYER["cases"][0]:
            # save_player(player)
            pass
        elif u_choice == S_PLAYER["cases"][1]:
            if len(players) < 8:
                players.append(player)
            else:
                choice_menu(S_C_PLAYER["string"], S_C_PLAYER["cases"], S_C_PLAYER["Header"])
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
        pass

