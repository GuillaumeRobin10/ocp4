#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.tournament_model import Tournament
from model.player_model import Player


def make_a_tournament(tournament_dict):
    tournament = Tournament()
    tournament.edit_name(tournament_dict['name'])
    tournament.edit_place(tournament_dict['place'])
    tournament.edit_kind(tournament_dict['starting_date'])
    tournament.edit_kind(tournament_dict['ending_date'])
    tournament.edit_kind(tournament_dict['kind'])
    tournament.edit_kind(tournament_dict['number_of_round'])
    tournament.edit_kind(tournament_dict['description'])
    return tournament


def make_a_player(player_dict):
    player = Player()
    player.edit_lastname(player_dict['lastname'])
    player.edit_firstname(player_dict['firstname'])
    player.edit_date_of_birth(player_dict['date_of_birth'])
    player.edit_gender(player_dict['gender'])
    player.edit_ranking(player_dict['ranking'])
    return player


if __name__ == "__main__":
    print("can't be run")
