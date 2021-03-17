#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.loading import get_identity
from controller.setting import current_tournament, players, current_player


def make_a_tournament(tournament_dict):
    current_tournament.edit_name(tournament_dict['name'])
    current_tournament.edit_place(tournament_dict['place'])
    current_tournament.edit_starting_date(tournament_dict['starting_date'])
    current_tournament.edit_ending_date(tournament_dict['ending_date'])
    current_tournament.edit_kind(tournament_dict['kind'])
    current_tournament.edit_number_of_round(tournament_dict['number_of_round'])
    current_tournament.edit_description(tournament_dict['description'])
    current_tournament.edit_id(get_identity("tournament"))


def make_a_player(player_dict):
    if len(players) < 8:
        current_player.edit_lastname(player_dict["lastname"])
        current_player.edit_firstname(player_dict["firstname"])
        current_player.edit_date_of_birth(player_dict["date_of_birth"])
        current_player.edit_gender(player_dict["gender"])
        current_player.edit_ranking(player_dict["ranking"])
        current_player.edit_identity(get_identity("players"))
        players.append(current_player)
        return True
    else:
        return False


if __name__ == "__main__":
    print("can't be run")
