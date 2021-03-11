#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller.tournament import test_player
from view.setting import players
from view.home_menu import main_menu


def main_view():
    for i in range(8):
        a = test_player(i, 1)
        players.append(a)
    main_menu()
