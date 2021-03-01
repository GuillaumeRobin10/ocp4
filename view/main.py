#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view.menu import choice_menu,loading_tournament_menu
from view.building import display_make_a_tournament

from controller.instance_making import make_a_tournament
from controller.instance_loading import load_a_json_files
from controller.files_in_database import get_datafiles


def main():
    start_menu_string = "Nouveau tournoi (1)\nCharger un tournoi (2)"
    first_choice = choice_menu(start_menu_string, ["1", "2"], "Start menu")
    if first_choice == "1":
        tournament = make_a_tournament(display_make_a_tournament())
    else:
        tournament = loading_tournament_menu()


if __name__ == "__main__":
    print("can't be run")
