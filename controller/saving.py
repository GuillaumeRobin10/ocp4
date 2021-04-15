#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.setting import db
from controller.setting import players
from tinydb import Query


def saving_player(player):
    """
    :param player: player instance
    :return: insert this player in database
    """
    player.serialization()
    players_table = db.table("players")
    player_db = Query()
    results = db.table("players").search(player_db.identity == player.identity)
    if not results:
        players_table.insert(player.serialized)
    else:
        db.table("players").update({"ranking": player.serialized["ranking"]},
                                   player_db.identity == player.identity)
        db.table("players").update({"tournament_point": player.serialized["tournament_point"]},
                                   player_db.identity == player.identity)


def saving_tournament(tournament):
    """
    :param tournament: tournament instance
    :return: insert this tournamenent in database
    """
    for ronde in tournament.rounds:
        ronde.serialization()
        tournament.edit_serialized_round(ronde.serialized_round)
    for player in players:
        tournament.edit_players_id_by_one(player.identity)
    tournament.serialization()
    tournament_table = db.table("tournament")
    tournament_db = Query()
    results = db.table("tournament").search(tournament_db.identity == tournament.identity)
    if not results:
        tournament_table.insert(tournament.serialized_tournament)
    else:
        db.table("tournament").update({"serialized_round": tournament.serialized_tournament["serialized_round"]},
                                      tournament_db.identity == tournament.identity)


def edit_ranking(id_player, new_ranking):
    user = Query()
    db.table("players").update({"ranking": new_ranking}, user.identity == int(id_player))
    for player in players:
        if player.identity == id_player:
            player.edit_ranking(new_ranking)


def saving_players():
    for player in players:
        saving_player(player)
