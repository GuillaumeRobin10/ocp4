#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.loading import scooting_tournament, loading_tournament
from controller.building import make_a_tournament

from view.tools import choice_menu
from view.setting import T_MENU_STRING, TOURNAMENT_0_LOADED_MENU_STRING
from view.display_instance_making import display_make_a_tournament


def tournament_menu():
    """
    Display tournament menu
    :return: none
    """
    tournament_loaded = scooting_tournament()
    if tournament_loaded == 0:
        u_choice = choice_menu(TOURNAMENT_0_LOADED_MENU_STRING["string"],
                               TOURNAMENT_0_LOADED_MENU_STRING["cases"],
                               TOURNAMENT_0_LOADED_MENU_STRING["Header"])
    else:
        u_choice = choice_menu(T_MENU_STRING["string"],
                               T_MENU_STRING["cases"],
                               T_MENU_STRING["Header"])
    if u_choice == T_MENU_STRING["cases"][0]:
        make_a_tournament(display_make_a_tournament())
    elif u_choice == "2":
        u_choice2 = choice_menu(tournament_loaded["string"], tournament_loaded["cases"], "Chargement de Tournois")
        make_a_tournament(loading_tournament(u_choice2), False)
    elif u_choice == u_choice == T_MENU_STRING["cases"][-1]:
        pass


if __name__ == "__main__":
    print("can't be run")
