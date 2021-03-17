#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinydb import TinyDB

from model.tournament import Tournament
from model.player import Player
db = TinyDB("data/db.json")

current_tournament = Tournament()
current_player = Player()
players = []
result_list = []
