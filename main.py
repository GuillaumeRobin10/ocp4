#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.setting import players, number_of_player

from view.home_menu import first_menu_action
from view.players_menu import players_menu
from view.rounding_menu import in_round_menu

if __name__ == "__main__":
    first_menu_action()
    while len(players) < number_of_player:
        players_menu()
    in_round_menu()

