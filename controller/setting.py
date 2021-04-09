#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinydb import TinyDB

from model.tournament import Tournament


db = TinyDB("data/db.json")

current_tournament = Tournament()
players = []
result_list = []
number_of_player = 8
