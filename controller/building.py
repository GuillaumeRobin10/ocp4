#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.player import Player
from controller.loading import get_identity, scooting_player_id
from controller.setting import current_tournament, players, db
from controller.saving import saving_player
from tinydb import Query


def make_a_tournament(tournament_dict):
    current_tournament.edit_name(tournament_dict['name'])
    current_tournament.edit_place(tournament_dict['place'])
    current_tournament.edit_starting_date(tournament_dict['starting_date'])
    current_tournament.edit_ending_date(tournament_dict['ending_date'])
    current_tournament.edit_kind(tournament_dict['kind'])
    current_tournament.edit_number_of_round(tournament_dict['number_of_round'])
    current_tournament.edit_description(tournament_dict['description'])
    current_tournament.edit_id(get_identity("tournament"))


def make_a_player(player_dict, new=True):
    if len(players) < 8:
        current_player = Player()
        current_player.edit_lastname(player_dict["lastname"])
        current_player.edit_firstname(player_dict["firstname"])
        current_player.edit_date_of_birth(player_dict["date_of_birth"])
        current_player.edit_gender(player_dict["gender"])
        current_player.edit_ranking(player_dict["ranking"])
        if new:
            current_player.edit_identity(get_identity("players"))
            saving_player(current_player)
        else:
            current_player.edit_identity(scooting_player_id(current_player))
        players.append(current_player)
        return True
    else:
        return False


def edit_ranking(id_player, new_ranking):
    user = Query()
    db.table("players").update({"ranking": new_ranking}, user.identity == int(id_player))
    for player in players:
        if player.identity == id_player:
            player.edit_ranking(new_ranking)


if __name__ == "__main__":
    print("can't be run")
