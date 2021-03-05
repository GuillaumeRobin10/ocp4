#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.tournament import Tournament
from model.player import Player
from model.round import Round

def test_tournois():
    current_tournament = Tournament(identity=1, name="challenger",place="moscou",starting_date="10/10/2020",ending_date="10/10/2020",kind='bullet', description="test")
    return current_tournament


def test_player(i, tid):
    player = Player(lastname=f"lastname{i}", firstname=f"firstname{i}", date_of_birth="10/10/10", gender="homme", ranking=i, identity=i, tournament_point= 0, tournament_id=tid)
    return player


def make_a_tournament(tournament_dict):
    tournament = Tournament()
    tournament.edit_name(tournament_dict['name'])
    tournament.edit_place(tournament_dict['place'])
    tournament.edit_starting_date(tournament_dict['starting_date'])
    tournament.edit_ending_date(tournament_dict['ending_date'])
    tournament.edit_kind(tournament_dict['kind'])
    tournament.edit_number_of_round(tournament_dict['number_of_round'])
    tournament.edit_description(tournament_dict['description'])
    return tournament


def make_a_player(player_dict, loading=False, identity=0):
    player = Player()
    player.edit_lastname(player_dict['lastname'])
    player.edit_firstname(player_dict['firstname'])
    player.edit_date_of_birth(player_dict['date_of_birth'])
    player.edit_gender(player_dict['gender'])
    player.edit_ranking(player_dict['ranking'])
    return player
"""
    if loading:
        player.edit_id(identity)
    else:
        player.edit_id(what_is_the_id("player"))
        player.save()
        """




