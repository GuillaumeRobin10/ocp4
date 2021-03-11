#!/usr/bin/env python
# -*- coding: utf-8 -*-

from view.tools import choice_menu
from view.setting import MAIN_MENU


def main_menu():
    u_choice = choice_menu(MAIN_MENU["string"], MAIN_MENU["cases"], MAIN_MENU["Header"])

    if u_choice == "1":
        t_menu()
    elif u_choice == "2":
        p_menu()
    elif u_choice == "3":
        r_menu()
    elif u_choice == "9":
        pass
    else:
        pass

