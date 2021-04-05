#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view.tools import choice_menu
from view.setting import FIRST_MENU
from view.tournament_menu import tournament_menu


def first_menu_action():
    u_choice = choice_menu(FIRST_MENU["string"], FIRST_MENU["cases"], FIRST_MENU["Header"])
    if u_choice == FIRST_MENU["cases"][0]:
        tournament_menu()
    else:
        quit()
