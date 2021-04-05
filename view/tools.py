#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import system

from controller.Display import display


def make_hyphens(name_menu):
    """
    :param name_menu: a string.
    :return: return a string of hyphens equal of the giving string.
    """
    hyphens = ""
    for _ in range(len(name_menu)):
        hyphens += "-"
    return hyphens


def display_head_menu(name):
    """
    :param name: name menu
    :return: header
    """
    system('cls||clear')
    print(make_hyphens(name))
    print(name)
    print(make_hyphens(name))


def choice_menu(menu_string, cases, header_name=""):
    """
    :param menu_string: a string with the text menu
    :param cases: list of user input
    :param header_name: menu's name ( string )
    :return: a choice menu
    """
    """ make a choice menu with a string and different cases"""
    system('cls||clear')
    if not header_name == "":
        display_head_menu(header_name)
    return display(menu_string, "choice", cases)


if __name__ == "__main__":
    print("can't be run")
