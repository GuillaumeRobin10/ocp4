#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from controller.Display import display


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


if __name__ == "__main__":
    print("can't be run")
