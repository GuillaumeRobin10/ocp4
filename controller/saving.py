#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller.setting import db


def saving_player(player):
    p_id = len(db.table("players").all()) + 1
    player.edit_identity(p_id)
    player.serialization()
    players_table = db.table("players")
    players_table.insert(player.serialized_player)
    print(player.serialized_player)


def saving_tournament(tournament):
    t_id = len(db.table("tournament").all())+1
    tournament.edit_id(t_id)
    tournament.serialization()
    tournament_table = db.table("tournament")
    tournament_table.insert(tournament.serialized_tournament)
    print(tournament.serialized_tournament)
