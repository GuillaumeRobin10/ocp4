#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.loading import scooting_player, loading_player
from controller.building import make_a_player
from controller.Display import display
from model.saving import edit_ranking

from view.display_instance_making import display_make_a_player
from view.tools import choice_menu, display_head_menu
from view.setting import P_MENU_STRING, S_C_PLAYER, MOD_PLAYER
from view.setting import PLAYER_0_LOADED_MENU_STRING


def players_menu():
    """
    Display player's menu
    :return: none
    """
    players_loaded = scooting_player()
    if players_loaded == 0:
        u_choice = choice_menu(PLAYER_0_LOADED_MENU_STRING["string"],
                               PLAYER_0_LOADED_MENU_STRING["cases"],
                               PLAYER_0_LOADED_MENU_STRING["Header"])
    else:
        u_choice = choice_menu(P_MENU_STRING["string"],
                               P_MENU_STRING["cases"],
                               P_MENU_STRING["Header"])

    if u_choice == P_MENU_STRING["cases"][0]:
        if not make_a_player(display_make_a_player()):
            choice_menu(S_C_PLAYER["string"],
                        S_C_PLAYER["cases"],
                        S_C_PLAYER["Header"])

    elif u_choice == "2":
        u_choice2 = choice_menu(players_loaded["string"], players_loaded["cases"], "Chargement de Joueur")
        if not make_a_player(loading_player(u_choice2), False):
            choice_menu(S_C_PLAYER["string"],
                        S_C_PLAYER["cases"],
                        S_C_PLAYER["Header"])

    elif u_choice == P_MENU_STRING["cases"][-1]:
        quit()


def player_menu_2():
    """
    Display edition menu
    allow edit player ronk
    :return: none
    """
    u_choice2 = choice_menu(MOD_PLAYER["string"], MOD_PLAYER["cases"], "Chargement de Joueur")
    if u_choice2 == "1":
        players_loaded = scooting_player()
        u_choice2 = choice_menu(players_loaded["string"], players_loaded["cases"], "Editions des joueurs")
        display_head_menu("edition")
        edit_ranking(u_choice2, display("Entrez le nouveau classement : ", "natural"))
        return 1
    else:
        return 1


if __name__ == "__main__":
    print("can't be run")
