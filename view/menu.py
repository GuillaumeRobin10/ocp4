#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from controller.display_function import display
from controller.instance_loading import load_a_json_files
from controller.files_in_database import get_datafiles
from controller.instance_making import make_a_tournament

def make_hyphens(name_menu):
    """Give it a string and return a string of hyphens equal of the giving string."""
    hyphens = ""
    for _ in range(len(name_menu)):
        hyphens += "-"
    return hyphens


def display_head_menu(name):
    """Give it a name and make a header to your menu"""
    print(make_hyphens(name))
    print(name)
    print(make_hyphens(name))


def choice_menu(menu_string, cases, header_name=""):
    """ make a choice menu with a string and different cases"""
    os.system('cls||clear')
    if not header_name == "":
        display_head_menu(header_name)
    return display(menu_string, "choice", cases)


def loading_tournament_menu():
    files = get_datafiles("databases/tournaments/*.json")
    if files == {}:
        print("pas de fichier disponible en base de donnée")
    else:
        keys = []
        for key in files:
            menu_string = f"Nom : {files[key]} ({key})\n"
            keys.append(key)
        uchoice = choice_menu(menu_string, keys, "Chargement d'un tournois")
        tournament_file = f"databases/tournaments/{uchoice}_{files[uchoice]}.json"
        tournament = make_a_tournament(load_a_json_files(tournament_file))
        return tournament


if __name__ == "__main__":
    print("can't be run")
